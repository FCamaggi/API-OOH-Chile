-- =============================================================================
-- MIGRACIÓN 001: ESQUEMA CORE POSTGIS PARA INVENTARIO Y AUDITORÍA OOH/DOOH RM
-- Cobertura: 52 Comunas de la Región Metropolitana (EPSG:4326 y EPSG:32719)
-- =============================================================================

CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Catálogo Oficial de las 52 Comunas de la Región Metropolitana
CREATE TABLE IF NOT EXISTS communes_rm (
    commune_code VARCHAR(5) PRIMARY KEY,
    commune_name VARCHAR(100) NOT NULL,
    province_name VARCHAR(100) NOT NULL,
    ring_tier SMALLINT NOT NULL CHECK (ring_tier BETWEEN 1 AND 4),
    utm_tax_rate_standard NUMERIC(6,2) NOT NULL DEFAULT 0.50,
    utm_tax_rate_led NUMERIC(6,2) NOT NULL DEFAULT 2.00,
    gis_rest_endpoint TEXT,
    geom_wgs84 GEOMETRY(MultiPolygon, 4326),
    geom_utm19s GEOMETRY(MultiPolygon, 32719)
);

-- 2. Operadores Comerciales (Media Owners) y Registro MOP (RNAVC)
CREATE TABLE IF NOT EXISTS media_owners (
    owner_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    rut VARCHAR(15) UNIQUE,
    legal_name VARCHAR(200) NOT NULL,
    commercial_brand VARCHAR(150),
    tier_category VARCHAR(50),
    mop_rnavc_number VARCHAR(50),
    mop_rnavc_status VARCHAR(30) DEFAULT 'ACTIVE',
    commercial_contact_email VARCHAR(150),
    website_url TEXT,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Contratos de Concesión en BNUP y Transporte (Mercado Público / DTPM / Metro / EFE)
CREATE TABLE IF NOT EXISTS concessions_contracts (
    concession_id VARCHAR(60) PRIMARY KEY,
    commune_code VARCHAR(5) REFERENCES communes_rm(commune_code),
    granting_entity VARCHAR(150) NOT NULL,
    owner_id UUID REFERENCES media_owners(owner_id),
    title TEXT NOT NULL,
    award_decree_number VARCHAR(100),
    start_date DATE,
    expiration_date DATE,
    annual_canon_clp BIGINT,
    total_authorized_assets INT,
    source_document_url TEXT
);

-- 4. Estructuras Físicas (ASSETS)
CREATE TABLE IF NOT EXISTS assets (
    asset_id VARCHAR(40) PRIMARY KEY,
    commune_code VARCHAR(5) NOT NULL REFERENCES communes_rm(commune_code),
    owner_id UUID REFERENCES media_owners(owner_id),
    concession_id VARCHAR(60) REFERENCES concessions_contracts(concession_id),
    dtpm_stop_code VARCHAR(30),
    sii_parcel_rol VARCHAR(30),
    address_raw TEXT NOT NULL,
    address_normalized TEXT NOT NULL,
    intersection_street TEXT,
    road_name VARCHAR(150),
    road_type VARCHAR(40) NOT NULL,
    highway_kilometer NUMERIC(6,2),
    speed_limit_kmh SMALLINT DEFAULT 50,
    structure_category VARCHAR(40) NOT NULL,
    structure_sub_type VARCHAR(50) NOT NULL,
    land_regime VARCHAR(20) NOT NULL,
    total_height_m NUMERIC(5,2),
    installation_date DATE,
    geom_wgs84 GEOMETRY(Point, 4326) NOT NULL,
    geom_utm19s GEOMETRY(Point, 32719) NOT NULL,
    location_confidence NUMERIC(3,2) NOT NULL DEFAULT 0.85,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Caras Publicitarias (FACES - Relación 1:N con Assets)
CREATE TABLE IF NOT EXISTS faces (
    face_id VARCHAR(50) PRIMARY KEY,
    asset_id VARCHAR(40) NOT NULL REFERENCES assets(asset_id) ON DELETE CASCADE,
    face_label VARCHAR(100) NOT NULL,
    azimuth_degrees SMALLINT CHECK (azimuth_degrees BETWEEN 0 AND 360),
    orientation_cardinal VARCHAR(5),
    traffic_flow_direction VARCHAR(10),
    width_m NUMERIC(5,2) NOT NULL,
    height_m NUMERIC(5,2) NOT NULL,
    area_m2 NUMERIC(6,2) GENERATED ALWAYS AS (ROUND(width_m * height_m, 2)) STORED,
    tech_type VARCHAR(30) NOT NULL,
    illumination_type VARCHAR(30),
    resolution_px VARCHAR(30),
    pixel_pitch_mm NUMERIC(4,2),
    slot_duration_sec SMALLINT,
    loop_slots_total SMALLINT,
    photo_day_url TEXT,
    photo_night_url TEXT,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 6. Auditoría Normativa y Cumplimiento Legal (COMPLIANCE - Ley N° 21.473)
CREATE TABLE IF NOT EXISTS compliance_records (
    compliance_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    asset_id VARCHAR(40) UNIQUE NOT NULL REFERENCES assets(asset_id) ON DELETE CASCADE,
    status VARCHAR(40) NOT NULL,
    ley_21473_class VARCHAR(30) NOT NULL,
    dom_permit_number VARCHAR(80),
    dom_permit_date DATE,
    dom_authorized_area_m2 NUMERIC(6,2),
    municipal_patent_rol VARCHAR(60),
    patent_last_paid_semester VARCHAR(15),
    patent_taxed_area_m2 NUMERIC(6,2),
    mop_itf_resolution VARCHAR(80),
    mma_ds1_lum_certified BOOLEAN DEFAULT FALSE,
    prc_zone_code VARCHAR(50),
    is_exclusive_residential BOOLEAN DEFAULT FALSE,
    distance_to_nearest_hazard_m NUMERIC(6,1),
    distance_to_nearest_sign_m NUMERIC(6,1),
    permit_expiration_date DATE,
    risk_flags JSONB DEFAULT '[]'::jsonb,
    last_audited_at TIMESTAMPTZ DEFAULT NOW()
);

-- 7. Métricas de Audiencia Abierta y Precios por Cara
CREATE TABLE IF NOT EXISTS face_metrics_pricing (
    face_id VARCHAR(50) PRIMARY KEY REFERENCES faces(face_id) ON DELETE CASCADE,
    uoct_hourly_vehicles_avg INT,
    mop_tmda_daily_vehicles INT,
    dtpm_bip_daily_validations INT,
    sectra_occupancy_factor NUMERIC(3,2) DEFAULT 1.45,
    weekly_ots_gross BIGINT,
    visibility_index_weight NUMERIC(4,3),
    weekly_vac_impacts BIGINT,
    scopesi_reference_vac BIGINT,
    list_price_clp_monthly BIGINT,
    production_cost_clp BIGINT DEFAULT 0,
    billing_periodicity VARCHAR(20) DEFAULT 'MONTHLY',
    estimated_net_discount_pct NUMERIC(4,2) DEFAULT 0.42,
    estimated_net_price_clp BIGINT,
    estimated_annual_municipal_tax_clp BIGINT,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_assets_geom_wgs84 ON assets USING GIST (geom_wgs84);
CREATE INDEX IF NOT EXISTS idx_assets_geom_utm19s ON assets USING GIST (geom_utm19s);
CREATE INDEX IF NOT EXISTS idx_assets_address_trgm ON assets USING GIN (address_normalized gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_assets_commune_category ON assets (commune_code, structure_category, is_active);
CREATE INDEX IF NOT EXISTS idx_compliance_status ON compliance_records (status, ley_21473_class);
