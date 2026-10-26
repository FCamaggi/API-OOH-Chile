"""
Catálogo oficial de las 52 comunas de la Región Metropolitana de Santiago
organizadas en los 4 anillos operativos (PRD sección 2.2) + inventario semilla
auditado para ejecución inmediata y pruebas deterministas en memoria.
"""
from app.schemas import AssetRecord, CommuneRM

# Las 52 comunas de la Región Metropolitana de Santiago (Provincias: Santiago, Cordillera, Chacabuco, Maipo, Melipilla, Talagante)
RM_COMMUNES_DATA: list[dict] = [
    # ANILLO 1: Eje Prime y Cono de Alta Renta (6 comunas)
    {"commune_code": "13101", "commune_name": "Santiago", "province_name": "Santiago", "ring_tier": 1, "utm_tax_rate_standard": 1.2, "utm_tax_rate_led": 3.5, "gis_rest_endpoint": "https://sig.munistgo.cl/arcgis/rest/services"},
    {"commune_code": "13123", "commune_name": "Providencia", "province_name": "Santiago", "ring_tier": 1, "utm_tax_rate_standard": 1.5, "utm_tax_rate_led": 4.0, "gis_rest_endpoint": "https://geoprovidencia.providencia.cl/arcgis/rest/services"},
    {"commune_code": "13114", "commune_name": "Las Condes", "province_name": "Santiago", "ring_tier": 1, "utm_tax_rate_standard": 1.8, "utm_tax_rate_led": 4.5, "gis_rest_endpoint": "https://catastro.lascondes.cl/arcgis/rest/services"},
    {"commune_code": "13132", "commune_name": "Vitacura", "province_name": "Santiago", "ring_tier": 1, "utm_tax_rate_standard": 1.8, "utm_tax_rate_led": 4.5, "gis_rest_endpoint": "https://visor.vitacura.cl/arcgis/rest/services"},
    {"commune_code": "13115", "commune_name": "Lo Barnechea", "province_name": "Santiago", "ring_tier": 1, "utm_tax_rate_standard": 1.5, "utm_tax_rate_led": 4.0, "gis_rest_endpoint": None},
    {"commune_code": "13120", "commune_name": "Ñuñoa", "province_name": "Santiago", "ring_tier": 1, "utm_tax_rate_standard": 1.2, "utm_tax_rate_led": 3.0, "gis_rest_endpoint": "https://visor.nunoa.cl/arcgis/rest/services"},
    # ANILLO 2: Polos Comerciales Masivos e Industriales / Autopistas (12 comunas)
    {"commune_code": "13107", "commune_name": "Huechuraba", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 1.0, "utm_tax_rate_led": 2.8, "gis_rest_endpoint": None},
    {"commune_code": "13125", "commune_name": "Quilicura", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 0.9, "utm_tax_rate_led": 2.5, "gis_rest_endpoint": None},
    {"commune_code": "13124", "commune_name": "Pudahuel", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 1.0, "utm_tax_rate_led": 2.8, "gis_rest_endpoint": None},
    {"commune_code": "13106", "commune_name": "Estación Central", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 1.0, "utm_tax_rate_led": 2.5, "gis_rest_endpoint": None},
    {"commune_code": "13119", "commune_name": "Maipú", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 0.8, "utm_tax_rate_led": 2.2, "gis_rest_endpoint": None},
    {"commune_code": "13110", "commune_name": "La Florida", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 0.9, "utm_tax_rate_led": 2.4, "gis_rest_endpoint": None},
    {"commune_code": "13201", "commune_name": "Puente Alto", "province_name": "Cordillera", "ring_tier": 2, "utm_tax_rate_standard": 0.8, "utm_tax_rate_led": 2.0, "gis_rest_endpoint": None},
    {"commune_code": "13401", "commune_name": "San Bernardo", "province_name": "Maipo", "ring_tier": 2, "utm_tax_rate_standard": 0.8, "utm_tax_rate_led": 2.2, "gis_rest_endpoint": None},
    {"commune_code": "13127", "commune_name": "Recoleta", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 0.8, "utm_tax_rate_led": 2.0, "gis_rest_endpoint": None},
    {"commune_code": "13108", "commune_name": "Independencia", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 0.8, "utm_tax_rate_led": 2.0, "gis_rest_endpoint": None},
    {"commune_code": "13118", "commune_name": "Macul", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 0.8, "utm_tax_rate_led": 2.2, "gis_rest_endpoint": None},
    {"commune_code": "13122", "commune_name": "Peñalolén", "province_name": "Santiago", "ring_tier": 2, "utm_tax_rate_standard": 0.9, "utm_tax_rate_led": 2.5, "gis_rest_endpoint": None},
    # ANILLO 3: Resto del Gran Santiago Urbano (18 comunas)
    {"commune_code": "13102", "commune_name": "Cerrillos", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.8, "gis_rest_endpoint": None},
    {"commune_code": "13103", "commune_name": "Cerro Navia", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.5, "utm_tax_rate_led": 1.5, "gis_rest_endpoint": None},
    {"commune_code": "13104", "commune_name": "Conchalí", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.8, "gis_rest_endpoint": None},
    {"commune_code": "13105", "commune_name": "El Bosque", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.6, "gis_rest_endpoint": None},
    {"commune_code": "13109", "commune_name": "La Cisterna", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.9, "gis_rest_endpoint": None},
    {"commune_code": "13111", "commune_name": "La Granja", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.5, "gis_rest_endpoint": None},
    {"commune_code": "13112", "commune_name": "La Pintana", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.5, "utm_tax_rate_led": 1.4, "gis_rest_endpoint": None},
    {"commune_code": "13113", "commune_name": "La Reina", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 1.0, "utm_tax_rate_led": 2.6, "gis_rest_endpoint": None},
    {"commune_code": "13116", "commune_name": "Lo Espejo", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.5, "utm_tax_rate_led": 1.5, "gis_rest_endpoint": None},
    {"commune_code": "13117", "commune_name": "Lo Prado", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.5, "gis_rest_endpoint": None},
    {"commune_code": "13121", "commune_name": "Pedro Aguirre Cerda", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.6, "gis_rest_endpoint": None},
    {"commune_code": "13126", "commune_name": "Quinta Normal", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.8, "gis_rest_endpoint": None},
    {"commune_code": "13128", "commune_name": "Renca", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.8, "utm_tax_rate_led": 2.0, "gis_rest_endpoint": None},
    {"commune_code": "13129", "commune_name": "San Joaquín", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.8, "gis_rest_endpoint": None},
    {"commune_code": "13130", "commune_name": "San Miguel", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.8, "utm_tax_rate_led": 2.1, "gis_rest_endpoint": None},
    {"commune_code": "13131", "commune_name": "San Ramón", "province_name": "Santiago", "ring_tier": 3, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.5, "gis_rest_endpoint": None},
    {"commune_code": "13604", "commune_name": "Padre Hurtado", "province_name": "Talagante", "ring_tier": 3, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.6, "gis_rest_endpoint": None},
    {"commune_code": "13202", "commune_name": "Pirque", "province_name": "Cordillera", "ring_tier": 3, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.6, "gis_rest_endpoint": None},
    # ANILLO 4: Comunas Periféricas y Corredores Interurbanos RM (16 comunas)
    {"commune_code": "13301", "commune_name": "Colina", "province_name": "Chacabuco", "ring_tier": 4, "utm_tax_rate_standard": 1.0, "utm_tax_rate_led": 2.8, "gis_rest_endpoint": None},
    {"commune_code": "13302", "commune_name": "Lampa", "province_name": "Chacabuco", "ring_tier": 4, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.9, "gis_rest_endpoint": None},
    {"commune_code": "13303", "commune_name": "Tiltil", "province_name": "Chacabuco", "ring_tier": 4, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.6, "gis_rest_endpoint": None},
    {"commune_code": "13402", "commune_name": "Buin", "province_name": "Maipo", "ring_tier": 4, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.9, "gis_rest_endpoint": None},
    {"commune_code": "13403", "commune_name": "Calera de Tango", "province_name": "Maipo", "ring_tier": 4, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.8, "gis_rest_endpoint": None},
    {"commune_code": "13404", "commune_name": "Paine", "province_name": "Maipo", "ring_tier": 4, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.7, "gis_rest_endpoint": None},
    {"commune_code": "13501", "commune_name": "Melipilla", "province_name": "Melipilla", "ring_tier": 4, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.8, "gis_rest_endpoint": None},
    {"commune_code": "13502", "commune_name": "Alhué", "province_name": "Melipilla", "ring_tier": 4, "utm_tax_rate_standard": 0.5, "utm_tax_rate_led": 1.2, "gis_rest_endpoint": None},
    {"commune_code": "13503", "commune_name": "Curacaví", "province_name": "Melipilla", "ring_tier": 4, "utm_tax_rate_standard": 0.7, "utm_tax_rate_led": 1.8, "gis_rest_endpoint": None},
    {"commune_code": "13504", "commune_name": "María Pinto", "province_name": "Melipilla", "ring_tier": 4, "utm_tax_rate_standard": 0.5, "utm_tax_rate_led": 1.3, "gis_rest_endpoint": None},
    {"commune_code": "13505", "commune_name": "San Pedro", "province_name": "Melipilla", "ring_tier": 4, "utm_tax_rate_standard": 0.5, "utm_tax_rate_led": 1.3, "gis_rest_endpoint": None},
    {"commune_code": "13601", "commune_name": "Talagante", "province_name": "Talagante", "ring_tier": 4, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.6, "gis_rest_endpoint": None},
    {"commune_code": "13602", "commune_name": "El Monte", "province_name": "Talagante", "ring_tier": 4, "utm_tax_rate_standard": 0.5, "utm_tax_rate_led": 1.4, "gis_rest_endpoint": None},
    {"commune_code": "13603", "commune_name": "Isla de Maipo", "province_name": "Talagante", "ring_tier": 4, "utm_tax_rate_standard": 0.5, "utm_tax_rate_led": 1.4, "gis_rest_endpoint": None},
    {"commune_code": "13605", "commune_name": "Peñaflor", "province_name": "Talagante", "ring_tier": 4, "utm_tax_rate_standard": 0.6, "utm_tax_rate_led": 1.5, "gis_rest_endpoint": None},
    {"commune_code": "13203", "commune_name": "San José de Maipo", "province_name": "Cordillera", "ring_tier": 4, "utm_tax_rate_standard": 0.5, "utm_tax_rate_led": 1.4, "gis_rest_endpoint": None},
]

SEED_ASSETS_DATA: list[dict] = [
    {
        "asset_id": "CL-RM-PROV-00482",
        "location": {
            "lat": -33.42628,
            "lng": -70.61094,
            "utm_x": 350214.5,
            "utm_y": 6299812.1,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "address_raw": "Av. Providencia esq. Ricardo Lyon",
            "address_normalized": "AVENIDA PROVIDENCIA ESQUINA RICARDO LYON",
            "sii_parcel_rol": None,
            "dtpm_stop_code": "PC182",
            "commune_code": "13123",
            "commune_name": "Providencia",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "URBAN_ARTERIAL",
            "highway_kilometer": None,
            "speed_limit_kmh": 50,
        },
        "structure": {
            "category": "STREET_FURNITURE",
            "sub_type": "MUPI",
            "land_regime": "BNUP",
            "total_height_m": 2.40,
            "installation_date": "2023-05-12",
        },
        "ownership": {
            "owner_id": "8f14e45f-ceea-467f-a814-2b4d9001c112",
            "media_owner_name": "JCDecaux Chile S.A.",
            "media_owner_rut": "96.682.110-4",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": "comercial@jcdecaux.com",
            "concession_id": "2455-88-LP22",
            "concession_expiration_date": "2033-05-12",
        },
        "faces": [
            {
                "face_id": "CL-RM-PROV-00482-A",
                "face_label": "Cara A (Flujo Oriente-Poniente)",
                "azimuth_degrees": 75,
                "orientation_cardinal": "E",
                "traffic_flow_direction": "O-P",
                "dimensions": {"width_m": 1.20, "height_m": 1.75, "area_m2": 2.10},
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": "1080x1920",
                    "pixel_pitch_mm": 4.0,
                    "slot_duration_sec": 10,
                    "loop_slots_total": 6,
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 2140,
                    "mop_tmda_daily_vehicles": None,
                    "dtpm_bip_daily_validations": 4850,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 428600,
                    "visibility_index_weight": 0.34,
                    "weekly_vac_impacts": 145724,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1",
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 2400000,
                    "production_cost_clp": 0,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 1392000,
                    "estimated_annual_municipal_tax_clp": 1122240,
                },
            }
        ],
        "compliance_audit": {
            "status": "VERIFIED_LEGAL",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": "PE-2023-114",
            "dom_authorized_area_m2": 2.10,
            "municipal_patent_rol": "400921-K",
            "patent_last_paid_semester": "2026-S2",
            "patent_taxed_area_m2": 2.10,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": True,
            "prc_zone_code": "Z-COM-1",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 120.0,
            "permit_expiration_date": "2033-05-12",
            "solidary_liability_risk_level": "LOW",
            "risk_flags": [],
        },
        "metadata": {
            "entity_resolution_confidence": 0.96,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": [
                {"source_type": "DTPM_SHAPEFILE", "reference_id": "STOP_PC182", "verified_at": "2026-10-01T00:00:00Z"},
                {"source_type": "DOM_ART16_TRANSPARENCIA", "reference_id": "OFICIO-DOM-PROV-2026-08", "verified_at": "2026-10-10T00:00:00Z"},
            ],
        },
    },
    {
        "asset_id": "CL-RM-LCON-01120",
        "location": {
            "lat": -33.40891,
            "lng": -70.56721,
            "utm_x": 354276.8,
            "utm_y": 6301738.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "address_raw": "Av. Apoquindo 5400 esq. Rosario Norte",
            "address_normalized": "AVENIDA APOQUINDO 5400 ESQUINA ROSARIO NORTE",
            "sii_parcel_rol": "01140-00018",
            "dtpm_stop_code": None,
            "commune_code": "13114",
            "commune_name": "Las Condes",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "URBAN_ARTERIAL",
            "highway_kilometer": None,
            "speed_limit_kmh": 50,
        },
        "structure": {
            "category": "LARGE_FORMAT_ROADSIDE",
            "sub_type": "MONUMENTAL_LED",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 12.0,
            "installation_date": "2024-02-15",
        },
        "ownership": {
            "owner_id": "3c91a442-1122-4a91-8899-abc123456789",
            "media_owner_name": "Clear Channel Chile Publicidad Ltda.",
            "media_owner_rut": "76.192.410-8",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": "contacto@clearchannel.cl",
            "concession_id": None,
            "concession_expiration_date": None,
        },
        "faces": [
            {
                "face_id": "CL-RM-LCON-01120-A",
                "face_label": "Pantalla Digital Monumental Poniente-Oriente",
                "azimuth_degrees": 255,
                "orientation_cardinal": "W",
                "traffic_flow_direction": "P-O",
                "dimensions": {"width_m": 8.0, "height_m": 4.0, "area_m2": 32.0},
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": "1920x960",
                    "pixel_pitch_mm": 8.0,
                    "slot_duration_sec": 10,
                    "loop_slots_total": 6,
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 3420,
                    "mop_tmda_daily_vehicles": None,
                    "dtpm_bip_daily_validations": 6120,
                    "sectra_occupancy_factor": 1.48,
                    "weekly_ots_gross": 694800,
                    "visibility_index_weight": 0.52,
                    "weekly_vac_impacts": 361296,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1",
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 6800000,
                    "production_cost_clp": 0,
                    "estimated_net_discount_pct": 0.40,
                    "estimated_net_price_clp": 4080000,
                    "estimated_annual_municipal_tax_clp": 19238400,
                },
            }
        ],
        "compliance_audit": {
            "status": "VERIFIED_LEGAL",
            "ley_21473_class": "ELEMENTO_MAYOR",
            "dom_permit_number": "OM-LC-2024-089",
            "dom_authorized_area_m2": 32.0,
            "municipal_patent_rol": "801442-1",
            "patent_last_paid_semester": "2026-S2",
            "patent_taxed_area_m2": 32.0,
            "mop_vialidad_itf_resolution": "ITF-RM-2024-031",
            "mma_ds1_lum_certified": True,
            "prc_zone_code": "UC-1",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 95.0,
            "permit_expiration_date": "2029-02-15",
            "solidary_liability_risk_level": "LOW",
            "risk_flags": [],
        },
        "metadata": {
            "entity_resolution_confidence": 0.98,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": [
                {"source_type": "AGGREGATOR_WEB_CATALOG", "reference_id": "OOHPUB_CC_1120", "verified_at": "2026-10-24T00:00:00Z"},
                {"source_type": "DOM_CATASTRO_DIGITAL", "reference_id": "OM-LC-2024-089", "verified_at": "2026-10-15T00:00:00Z"},
            ],
        },
    },
    {
        "asset_id": "CL-RM-HUEC-00109",
        "location": {
            "lat": -33.37912,
            "lng": -70.64108,
            "utm_x": 347414.5,
            "utm_y": 6305042.1,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "address_raw": "Américo Vespucio Norte 1450",
            "address_normalized": "AMERICO VESPUCIO NORTE 1450",
            "sii_parcel_rol": "02410-00082",
            "dtpm_stop_code": None,
            "commune_code": "13107",
            "commune_name": "Huechuraba",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "HIGHWAY_CONCESSION",
            "highway_kilometer": 9.4,
            "speed_limit_kmh": 100,
        },
        "structure": {
            "category": "LARGE_FORMAT_ROADSIDE",
            "sub_type": "MONUMENTAL_LED",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 18.0,
            "installation_date": "2025-01-20",
        },
        "ownership": {
            "owner_id": "7a88b991-0011-4c22-9911-ff0011223344",
            "media_owner_name": "Operador Gran Formato Vial SpA",
            "media_owner_rut": "77.410.892-1",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": "ventas@granformatovial.cl",
            "concession_id": None,
            "concession_expiration_date": None,
        },
        "faces": [
            {
                "face_id": "CL-RM-HUEC-00109-A",
                "face_label": "Cara A Oriente-Poniente (Vespucio Norte)",
                "azimuth_degrees": 85,
                "orientation_cardinal": "E",
                "traffic_flow_direction": "O-P",
                "dimensions": {"width_m": 12.0, "height_m": 4.0, "area_m2": 48.0},
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": "2400x800",
                    "pixel_pitch_mm": 10.0,
                    "slot_duration_sec": 10,
                    "loop_slots_total": 8,
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": None,
                    "mop_tmda_daily_vehicles": 98500,
                    "dtpm_bip_daily_validations": None,
                    "sectra_occupancy_factor": 1.45,
                    "weekly_ots_gross": 999775,
                    "visibility_index_weight": 0.44,
                    "weekly_vac_impacts": 439901,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1",
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 7500000,
                    "production_cost_clp": 0,
                    "estimated_net_discount_pct": 0.45,
                    "estimated_net_price_clp": 4125000,
                    "estimated_annual_municipal_tax_clp": 17955840,
                },
            }
        ],
        "compliance_audit": {
            "status": "PARTIAL_COMPLIANCE",
            "ley_21473_class": "ELEMENTO_MAYOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": "700192-4",
            "patent_last_paid_semester": "2026-S1",
            "patent_taxed_area_m2": 24.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-IND-2",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 55.0,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "HIGH",
            "risk_flags": [
                "MISSING_DOM_OBRA_MENOR_PERMIT",
                "AREA_SUBDECLARATION_GT_15PCT",
                "MISSING_MOP_CONCESSION_INSPECTION_CERT",
            ],
        },
        "metadata": {
            "entity_resolution_confidence": 0.89,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": [
                {"source_type": "AGGREGATOR_WEB_CATALOG", "reference_id": "OOHPUB_GF_109", "verified_at": "2026-10-24T00:00:00Z"},
                {"source_type": "RENTAS_PADRON_TRANSPARENCIA", "reference_id": "ROL-700192-4", "verified_at": "2026-10-12T00:00:00Z"},
            ],
        },
    },
    {
        "asset_id": "CL-RM-PUDA-00304",
        "location": {
            "lat": -33.44102,
            "lng": -70.79120,
            "utm_x": 333468.2,
            "utm_y": 6298177.5,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "address_raw": "Ruta 68 Km 11.2 Acceso Oriente",
            "address_normalized": "RUTA 68 KM 11.2 ACCESO ORIENTE",
            "sii_parcel_rol": "04102-00012",
            "dtpm_stop_code": None,
            "commune_code": "13124",
            "commune_name": "Pudahuel",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "INTERURBAN_ROUTE",
            "highway_kilometer": 11.2,
            "speed_limit_kmh": 120,
        },
        "structure": {
            "category": "LARGE_FORMAT_ROADSIDE",
            "sub_type": "UNIPOLE",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 16.0,
            "installation_date": "2024-08-10",
        },
        "ownership": {
            "owner_id": "9900aabb-ccdd-4455-8899-112233445566",
            "media_owner_name": "Publivía S.A.",
            "media_owner_rut": "96.510.220-K",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": "comercial@publivia.cl",
            "concession_id": None,
            "concession_expiration_date": None,
        },
        "faces": [
            {
                "face_id": "CL-RM-PUDA-00304-A",
                "face_label": "Cara A Poniente-Oriente (Hacia Santiago)",
                "azimuth_degrees": 95,
                "orientation_cardinal": "E",
                "traffic_flow_direction": "P-O",
                "dimensions": {"width_m": 12.0, "height_m": 5.0, "area_m2": 60.0},
                "technology": {
                    "type": "STATIC_BACKLIGHT",
                    "illumination": "EXTERNAL_SPOTLIGHT",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None,
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": None,
                    "mop_tmda_daily_vehicles": 74200,
                    "dtpm_bip_daily_validations": None,
                    "sectra_occupancy_factor": 1.52,
                    "weekly_ots_gross": 789488,
                    "visibility_index_weight": 0.81,
                    "weekly_vac_impacts": 639485,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1",
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 3900000,
                    "production_cost_clp": 650000,
                    "estimated_net_discount_pct": 0.38,
                    "estimated_net_price_clp": 2418000,
                    "estimated_annual_municipal_tax_clp": 8016000,
                },
            }
        ],
        "compliance_audit": {
            "status": "UNREGISTERED_CLANDESTINE",
            "ley_21473_class": "ELEMENTO_MAYOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": None,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-IND-R68",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 32.0,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "CRITICAL",
            "risk_flags": [
                "UNREGISTERED_IN_DOM_AND_RENTAS",
                "MISSING_MOP_ITF_RUTA_68",
                "HAZARD_PROXIMITY_LT_40M_DECRETO24",
            ],
        },
        "metadata": {
            "entity_resolution_confidence": 0.92,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": [
                {"source_type": "OWNER_KML_LAYER", "reference_id": "R68_KM11_2", "verified_at": "2026-10-20T00:00:00Z"},
            ],
        },
    },
]


class InMemoryOOHRepository:
    """
    Repositorio en memoria determinista para desarrollo API-First y ejecución
    instantánea de tests en Google Jules sin requerir PostGIS levantado.
    """

    def __init__(self) -> None:
        self.communes: dict[str, CommuneRM] = {
            c["commune_code"]: CommuneRM(**c) for c in RM_COMMUNES_DATA
        }
        self.assets: dict[str, AssetRecord] = {
            a["asset_id"]: AssetRecord(**a) for a in SEED_ASSETS_DATA
        }

    def list_communes(self, ring_tier: int | None = None, province_name: str | None = None) -> list[CommuneRM]:
        items = list(self.communes.values())
        if ring_tier is not None:
            items = [c for c in items if c.ring_tier == ring_tier]
        if province_name:
            items = [c for c in items if c.province_name.lower() == province_name.lower()]
        return sorted(items, key=lambda x: (x.ring_tier, x.commune_code))

    def list_assets(self) -> list[AssetRecord]:
        return list(self.assets.values())

    def get_asset(self, asset_id: str) -> AssetRecord | None:
        return self.assets.get(asset_id)


repo = InMemoryOOHRepository()
