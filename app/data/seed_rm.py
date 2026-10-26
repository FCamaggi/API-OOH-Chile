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
        "asset_id": "CL-RM-LAS -1000",
        "location": {
            "lat": -33.36972893702244,
            "lng": -70.62277061604019,
            "utm_x": 346234.0,
            "utm_y": 6309995.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13114",
            "commune_name": "Las Condes",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "LOCAL",
            "address_raw": "Avenida Principal 115, Las Condes",
            "address_normalized": "AV PRINCIPAL 1721",
            "sii_parcel_rol": "3138-80",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "STREET_FURNITURE",
            "sub_type": "BUS_STOP_SHELTER",
            "land_regime": "BNUP",
            "total_height_m": 6.061848981957727,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "acb2e422-163e-4b7c-a505-b67a99e4356c",
            "media_owner_rut": "77987654-3",
            "media_owner_name": "Clear Channel",
            "mop_rnavc_status": "NOT_REGISTERED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-LAS -1000-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "UNILLUMINATED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 941,
                    "mop_tmda_daily_vehicles": 41372,
                    "dtpm_bip_daily_validations": 14450,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 435222,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 179931,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 517441,
                    "production_cost_clp": 167753,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 300115,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "ZONING_VIOLATION_RISK",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 153.07015879321227,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "HIGH",
            "risk_flags": [
                "MISSING_DOM_OBRA_MENOR_PERMIT",
                "AREA_SUBDECLARATION_GT_15PCT",
                "UNREGISTERED_IN_DOM_AND_RENTAS"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-SANT-1001",
        "location": {
            "lat": -33.31515460520987,
            "lng": -70.76776761094662,
            "utm_x": 353184.0,
            "utm_y": 6309766.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13101",
            "commune_name": "Santiago",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "ARTERIAL",
            "address_raw": "Avenida Principal 6675, Santiago",
            "address_normalized": "AV PRINCIPAL 6688",
            "sii_parcel_rol": "7556-10",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "STREET_FURNITURE",
            "sub_type": "BUS_STOP_SHELTER",
            "land_regime": "BNUP",
            "total_height_m": 13.3018963916766,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "b225dae4-4c81-49c3-a51f-27f0ddf1546b",
            "media_owner_rut": "96432123-5",
            "media_owner_name": "Massiva",
            "mop_rnavc_status": "EXPIRED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-SANT-1001-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "UNILLUMINATED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 438,
                    "mop_tmda_daily_vehicles": 2649,
                    "dtpm_bip_daily_validations": 5055,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 400061,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 96686,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 2525161,
                    "production_cost_clp": 98922,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 1464593,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "PARTIAL_COMPLIANCE",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 130.88311166439155,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "HIGH",
            "risk_flags": [
                "MISSING_MUNICIPAL_PATENT_PAYMENT",
                "UNREGISTERED_IN_DOM_AND_RENTAS"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-MAIP-1002",
        "location": {
            "lat": -33.34607867050154,
            "lng": -70.63631076315883,
            "utm_x": 340567.0,
            "utm_y": 6293692.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13119",
            "commune_name": "Maip\u00fa",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "HIGHWAY",
            "address_raw": "Avenida Principal 7816, Maip\u00fa",
            "address_normalized": "AV PRINCIPAL 3052",
            "sii_parcel_rol": "9895-67",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "WALL_MURAL",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 8.665768604860123,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "931b1878-91a9-4f2e-85f6-7bc7e5ffb267",
            "media_owner_rut": "96432123-5",
            "media_owner_name": "Massiva",
            "mop_rnavc_status": "NOT_REGISTERED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-MAIP-1002-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "UNILLUMINATED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 860,
                    "mop_tmda_daily_vehicles": 47742,
                    "dtpm_bip_daily_validations": 14128,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 236490,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 141767,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 2710682,
                    "production_cost_clp": 80528,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 1572195,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "ZONING_VIOLATION_RISK",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 57.11447152665315,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "CRITICAL",
            "risk_flags": [
                "HAZARD_PROXIMITY_LT_40M_DECRETO24",
                "MISSING_DOM_OBRA_MENOR_PERMIT",
                "AREA_SUBDECLARATION_GT_15PCT"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-MAIP-1003",
        "location": {
            "lat": -33.46486251247197,
            "lng": -70.58614863530195,
            "utm_x": 341338.0,
            "utm_y": 6291622.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13119",
            "commune_name": "Maip\u00fa",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "LOCAL",
            "address_raw": "Avenida Principal 5347, Maip\u00fa",
            "address_normalized": "AV PRINCIPAL 8587",
            "sii_parcel_rol": "4764-64",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "LARGE_FORMAT_ROADSIDE",
            "sub_type": "STATIC_BILLBOARD",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 7.180653366922978,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "480323da-7924-401c-8053-111748abe6ad",
            "media_owner_rut": "78543210-9",
            "media_owner_name": "Global",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-MAIP-1003-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "EXTERNAL_SPOTLIGHT",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 1872,
                    "mop_tmda_daily_vehicles": 37876,
                    "dtpm_bip_daily_validations": 10467,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 118068,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 34315,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 4294219,
                    "production_cost_clp": 55316,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 2490647,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "VERIFIED_LEGAL",
            "ley_21473_class": "ELEMENTO_MAYOR",
            "dom_permit_number": "123/2020",
            "dom_authorized_area_m2": 6.0,
            "municipal_patent_rol": "456-789",
            "patent_last_paid_semester": "2026-S1",
            "patent_taxed_area_m2": 6.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": True,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 134.7372939046134,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "LOW",
            "risk_flags": []
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-SAN -1004",
        "location": {
            "lat": -33.32134868546958,
            "lng": -70.50430719098078,
            "utm_x": 342128.0,
            "utm_y": 6298785.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13130",
            "commune_name": "San Miguel",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "ARTERIAL",
            "address_raw": "Avenida Principal 3813, San Miguel",
            "address_normalized": "AV PRINCIPAL 2241",
            "sii_parcel_rol": "3121-31",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "STREET_FURNITURE",
            "sub_type": "DIGITAL_MUPI",
            "land_regime": "BNUP",
            "total_height_m": 8.416839034364298,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "2674413c-9610-493c-9785-66aa1e4ffbf5",
            "media_owner_rut": "96432123-5",
            "media_owner_name": "Massiva",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-SAN -1004-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 176,
                    "mop_tmda_daily_vehicles": 1978,
                    "dtpm_bip_daily_validations": 13631,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 240554,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 198997,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 781794,
                    "production_cost_clp": 65852,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 453440,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "PARTIAL_COMPLIANCE",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 119.01228785375366,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "CRITICAL",
            "risk_flags": [
                "UNREGISTERED_IN_DOM_AND_RENTAS",
                "AREA_SUBDECLARATION_GT_15PCT",
                "MISSING_MOP_ITF_RUTA_68"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-MAIP-1005",
        "location": {
            "lat": -33.36160044815573,
            "lng": -70.70965628978017,
            "utm_x": 353336.0,
            "utm_y": 6296337.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13119",
            "commune_name": "Maip\u00fa",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "HIGHWAY",
            "address_raw": "Avenida Principal 946, Maip\u00fa",
            "address_normalized": "AV PRINCIPAL 1844",
            "sii_parcel_rol": "9005-93",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "WALL_MURAL",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 3.3584582345585634,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "3ffe2695-dbe0-4104-b776-a5f2b50d08fa",
            "media_owner_rut": "78543210-9",
            "media_owner_name": "Global",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-MAIP-1005-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "UNILLUMINATED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 1806,
                    "mop_tmda_daily_vehicles": 18935,
                    "dtpm_bip_daily_validations": 11883,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 162867,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 56108,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 2147982,
                    "production_cost_clp": 83473,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 1245829,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "VERIFIED_LEGAL",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": "123/2020",
            "dom_authorized_area_m2": 6.0,
            "municipal_patent_rol": "456-789",
            "patent_last_paid_semester": "2026-S1",
            "patent_taxed_area_m2": 6.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": True,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 56.8917242937587,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "LOW",
            "risk_flags": []
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-LA F-1006",
        "location": {
            "lat": -33.49733193345172,
            "lng": -70.52559136986655,
            "utm_x": 351458.0,
            "utm_y": 6306323.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13110",
            "commune_name": "La Florida",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "ARTERIAL",
            "address_raw": "Avenida Principal 223, La Florida",
            "address_normalized": "AV PRINCIPAL 8288",
            "sii_parcel_rol": "5162-30",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "WALL_MURAL",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 5.8309290129345,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "0bf7c43e-68cd-4829-a477-5533416ff9c7",
            "media_owner_rut": "78543210-9",
            "media_owner_name": "Global",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-LA F-1006-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "UNILLUMINATED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 1464,
                    "mop_tmda_daily_vehicles": 44064,
                    "dtpm_bip_daily_validations": 1331,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 167307,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 138864,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 3771075,
                    "production_cost_clp": 145740,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 2187223,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "VERIFIED_LEGAL",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": "123/2020",
            "dom_authorized_area_m2": 6.0,
            "municipal_patent_rol": "456-789",
            "patent_last_paid_semester": "2026-S1",
            "patent_taxed_area_m2": 6.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": True,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 93.41675830345565,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "LOW",
            "risk_flags": []
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-RECO-1007",
        "location": {
            "lat": -33.34144896174905,
            "lng": -70.58463692768676,
            "utm_x": 352085.0,
            "utm_y": 6300375.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13127",
            "commune_name": "Recoleta",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "HIGHWAY",
            "address_raw": "Avenida Principal 1021, Recoleta",
            "address_normalized": "AV PRINCIPAL 9555",
            "sii_parcel_rol": "4024-93",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "STREET_FURNITURE",
            "sub_type": "DIGITAL_MUPI",
            "land_regime": "BNUP",
            "total_height_m": 4.699339517505351,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "469d6e17-eba3-4ef7-906a-8790e223a488",
            "media_owner_rut": "79876543-2",
            "media_owner_name": "Vallas y Soportes",
            "mop_rnavc_status": "NOT_REGISTERED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-RECO-1007-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 908,
                    "mop_tmda_daily_vehicles": 42628,
                    "dtpm_bip_daily_validations": 8576,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 431206,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 95930,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 4171478,
                    "production_cost_clp": 182889,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 2419457,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "ZONING_VIOLATION_RISK",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 55.22410826984011,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "HIGH",
            "risk_flags": [
                "MISSING_MOP_ITF_RUTA_68"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-SAN -1008",
        "location": {
            "lat": -33.31071157586568,
            "lng": -70.5961334909422,
            "utm_x": 347024.0,
            "utm_y": 6296978.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13130",
            "commune_name": "San Miguel",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "LOCAL",
            "address_raw": "Avenida Principal 3766, San Miguel",
            "address_normalized": "AV PRINCIPAL 2050",
            "sii_parcel_rol": "9210-80",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "LED_SCREEN",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 7.14327389921303,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "8c0e37e2-f7ff-49fc-90c9-daa3054939fb",
            "media_owner_rut": "79876543-2",
            "media_owner_name": "Vallas y Soportes",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-SAN -1008-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": "1920x1080",
                    "pixel_pitch_mm": 6.0,
                    "slot_duration_sec": 10,
                    "loop_slots_total": 6
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 146,
                    "mop_tmda_daily_vehicles": 43251,
                    "dtpm_bip_daily_validations": 6687,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 399489,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 220375,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 2968137,
                    "production_cost_clp": 64243,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 1721519,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "VERIFIED_LEGAL",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": "123/2020",
            "dom_authorized_area_m2": 6.0,
            "municipal_patent_rol": "456-789",
            "patent_last_paid_semester": "2026-S1",
            "patent_taxed_area_m2": 6.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": True,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 144.87161467862097,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "LOW",
            "risk_flags": []
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-PROV-1009",
        "location": {
            "lat": -33.417368798988576,
            "lng": -70.57823911196002,
            "utm_x": 348598.0,
            "utm_y": 6292122.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13123",
            "commune_name": "Providencia",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "LOCAL",
            "address_raw": "Avenida Principal 9577, Providencia",
            "address_normalized": "AV PRINCIPAL 5340",
            "sii_parcel_rol": "6339-88",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "LED_SCREEN",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 8.953363732195239,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "58eca44c-9735-46e5-8bd4-bac144ed5c8a",
            "media_owner_rut": "96432123-5",
            "media_owner_name": "Massiva",
            "mop_rnavc_status": "NOT_REGISTERED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-PROV-1009-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": "1920x1080",
                    "pixel_pitch_mm": 6.0,
                    "slot_duration_sec": 10,
                    "loop_slots_total": 6
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 1568,
                    "mop_tmda_daily_vehicles": 3834,
                    "dtpm_bip_daily_validations": 5020,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 236883,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 203593,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 4436429,
                    "production_cost_clp": 113327,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 2573128,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "UNREGISTERED_CLANDESTINE",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 143.90159120130528,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "HIGH",
            "risk_flags": [
                "HAZARD_PROXIMITY_LT_40M_DECRETO24"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-RECO-1010",
        "location": {
            "lat": -33.498274867366,
            "lng": -70.68450695897899,
            "utm_x": 350605.0,
            "utm_y": 6298136.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13127",
            "commune_name": "Recoleta",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "ARTERIAL",
            "address_raw": "Avenida Principal 1547, Recoleta",
            "address_normalized": "AV PRINCIPAL 3634",
            "sii_parcel_rol": "3297-47",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "STREET_FURNITURE",
            "sub_type": "DIGITAL_MUPI",
            "land_regime": "BNUP",
            "total_height_m": 11.764936843928325,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "ecac5dd0-10e9-452c-99c6-a6f130d64a6d",
            "media_owner_rut": "78543210-9",
            "media_owner_name": "Global",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-RECO-1010-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 1699,
                    "mop_tmda_daily_vehicles": 42733,
                    "dtpm_bip_daily_validations": 4943,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 130304,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 117955,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 3612116,
                    "production_cost_clp": 193851,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 2095027,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "VERIFIED_LEGAL",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": "123/2020",
            "dom_authorized_area_m2": 6.0,
            "municipal_patent_rol": "456-789",
            "patent_last_paid_semester": "2026-S1",
            "patent_taxed_area_m2": 6.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": True,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 132.43573092913797,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "LOW",
            "risk_flags": []
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-COLI-1011",
        "location": {
            "lat": -33.487010079455985,
            "lng": -70.77839855970551,
            "utm_x": 342516.0,
            "utm_y": 6304841.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13301",
            "commune_name": "Colina",
            "province_name": "Chacabuco",
            "region_code": "RM",
            "road_type": "HIGHWAY",
            "address_raw": "Avenida Principal 3480, Colina",
            "address_normalized": "AV PRINCIPAL 4937",
            "sii_parcel_rol": "6794-57",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "LED_SCREEN",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 10.958599355086864,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "719ee3c1-a661-4845-b073-d0f34fcc4b9f",
            "media_owner_rut": "96432123-5",
            "media_owner_name": "Massiva",
            "mop_rnavc_status": "NOT_REGISTERED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-COLI-1011-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": "1920x1080",
                    "pixel_pitch_mm": 6.0,
                    "slot_duration_sec": 10,
                    "loop_slots_total": 6
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 1210,
                    "mop_tmda_daily_vehicles": 13979,
                    "dtpm_bip_daily_validations": 6181,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 470864,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 72615,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 567516,
                    "production_cost_clp": 154920,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 329159,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "UNREGISTERED_CLANDESTINE",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 94.86094443748787,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "CRITICAL",
            "risk_flags": [
                "MISSING_MUNICIPAL_PATENT_PAYMENT",
                "AREA_SUBDECLARATION_GT_15PCT",
                "UNREGISTERED_IN_DOM_AND_RENTAS"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-LA F-1012",
        "location": {
            "lat": -33.36386601575287,
            "lng": -70.78702594348323,
            "utm_x": 352829.0,
            "utm_y": 6299569.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13110",
            "commune_name": "La Florida",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "ARTERIAL",
            "address_raw": "Avenida Principal 4030, La Florida",
            "address_normalized": "AV PRINCIPAL 9692",
            "sii_parcel_rol": "6861-14",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "WALL_MURAL",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 10.105238943922203,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "3d0edb9c-5b77-44e8-bb23-0b3b7c48ca19",
            "media_owner_rut": "77987654-3",
            "media_owner_name": "Clear Channel",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-LA F-1012-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "EXTERNAL_SPOTLIGHT",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 188,
                    "mop_tmda_daily_vehicles": 13364,
                    "dtpm_bip_daily_validations": 12500,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 435308,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 141134,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 2299741,
                    "production_cost_clp": 68677,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 1333849,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "VERIFIED_LEGAL",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": "123/2020",
            "dom_authorized_area_m2": 6.0,
            "municipal_patent_rol": "456-789",
            "patent_last_paid_semester": "2026-S1",
            "patent_taxed_area_m2": 6.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": True,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 112.42383522129529,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "LOW",
            "risk_flags": []
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-MAIP-1013",
        "location": {
            "lat": -33.467655115210704,
            "lng": -70.77425741961052,
            "utm_x": 348176.0,
            "utm_y": 6292186.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13119",
            "commune_name": "Maip\u00fa",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "HIGHWAY",
            "address_raw": "Avenida Principal 9768, Maip\u00fa",
            "address_normalized": "AV PRINCIPAL 2039",
            "sii_parcel_rol": "9937-60",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "STREET_FURNITURE",
            "sub_type": "BUS_STOP_SHELTER",
            "land_regime": "BNUP",
            "total_height_m": 13.747854837235066,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "e0d793a1-d7f7-49b7-b52c-dad7cc4c2a4b",
            "media_owner_rut": "77987654-3",
            "media_owner_name": "Clear Channel",
            "mop_rnavc_status": "NOT_REGISTERED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-MAIP-1013-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "EXTERNAL_SPOTLIGHT",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 1822,
                    "mop_tmda_daily_vehicles": 27862,
                    "dtpm_bip_daily_validations": 12605,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 48196,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 27539,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 3036084,
                    "production_cost_clp": 59749,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 1760928,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "UNREGISTERED_CLANDESTINE",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 162.74658697697322,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "HIGH",
            "risk_flags": [
                "UNREGISTERED_IN_DOM_AND_RENTAS"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-MAIP-1014",
        "location": {
            "lat": -33.39768831418826,
            "lng": -70.7579356109217,
            "utm_x": 350716.0,
            "utm_y": 6299987.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13119",
            "commune_name": "Maip\u00fa",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "HIGHWAY",
            "address_raw": "Avenida Principal 5804, Maip\u00fa",
            "address_normalized": "AV PRINCIPAL 2232",
            "sii_parcel_rol": "8232-60",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "LED_SCREEN",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 9.076511020997641,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "8e8a9a19-65a9-44bd-b142-a976503d7660",
            "media_owner_rut": "76123456-K",
            "media_owner_name": "JCDecaux",
            "mop_rnavc_status": "EXPIRED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-MAIP-1014-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": "1920x1080",
                    "pixel_pitch_mm": 6.0,
                    "slot_duration_sec": 10,
                    "loop_slots_total": 6
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 1373,
                    "mop_tmda_daily_vehicles": 24377,
                    "dtpm_bip_daily_validations": 8001,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 261740,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 117532,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 1544595,
                    "production_cost_clp": 152525,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 895865,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "ZONING_VIOLATION_RISK",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 70.74382864058552,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "CRITICAL",
            "risk_flags": [
                "MISSING_MOP_ITF_RUTA_68",
                "UNREGISTERED_IN_DOM_AND_RENTAS"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-SAN -1015",
        "location": {
            "lat": -33.46875167131505,
            "lng": -70.74526398474089,
            "utm_x": 346032.0,
            "utm_y": 6297862.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13130",
            "commune_name": "San Miguel",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "ARTERIAL",
            "address_raw": "Avenida Principal 7384, San Miguel",
            "address_normalized": "AV PRINCIPAL 1417",
            "sii_parcel_rol": "7080-15",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "LARGE_FORMAT_ROADSIDE",
            "sub_type": "STATIC_BILLBOARD",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 10.791312263102096,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "11ea9c63-93fa-427b-b019-dcce122fa85a",
            "media_owner_rut": "96432123-5",
            "media_owner_name": "Massiva",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-SAN -1015-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "UNILLUMINATED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 337,
                    "mop_tmda_daily_vehicles": 4230,
                    "dtpm_bip_daily_validations": 8815,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 278450,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 67670,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 3636226,
                    "production_cost_clp": 66923,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 2109011,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "UNREGISTERED_CLANDESTINE",
            "ley_21473_class": "ELEMENTO_MAYOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 70.3288508538732,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "CRITICAL",
            "risk_flags": [
                "MISSING_MOP_ITF_RUTA_68",
                "MISSING_MUNICIPAL_PATENT_PAYMENT",
                "MISSING_DOM_OBRA_MENOR_PERMIT"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-SAN -1016",
        "location": {
            "lat": -33.37418901348232,
            "lng": -70.76148777842235,
            "utm_x": 343736.0,
            "utm_y": 6294404.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13130",
            "commune_name": "San Miguel",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "LOCAL",
            "address_raw": "Avenida Principal 6483, San Miguel",
            "address_normalized": "AV PRINCIPAL 3231",
            "sii_parcel_rol": "7169-13",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "LED_SCREEN",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 11.710637128616924,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "e77757d3-daff-4736-b95a-72a294d30435",
            "media_owner_rut": "77987654-3",
            "media_owner_name": "Clear Channel",
            "mop_rnavc_status": "NOT_REGISTERED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-SAN -1016-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": "1920x1080",
                    "pixel_pitch_mm": 6.0,
                    "slot_duration_sec": 10,
                    "loop_slots_total": 6
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 963,
                    "mop_tmda_daily_vehicles": 45774,
                    "dtpm_bip_daily_validations": 6337,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 298468,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 238345,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 3527951,
                    "production_cost_clp": 67167,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 2046211,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "ZONING_VIOLATION_RISK",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 112.52923985002457,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "HIGH",
            "risk_flags": [
                "MISSING_DOM_OBRA_MENOR_PERMIT",
                "AREA_SUBDECLARATION_GT_15PCT",
                "MISSING_MOP_ITF_RUTA_68"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-SAN -1017",
        "location": {
            "lat": -33.46687463219706,
            "lng": -70.6869899169506,
            "utm_x": 351815.0,
            "utm_y": 6306813.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13401",
            "commune_name": "San Bernardo",
            "province_name": "Maipo",
            "region_code": "RM",
            "road_type": "HIGHWAY",
            "address_raw": "Avenida Principal 1468, San Bernardo",
            "address_normalized": "AV PRINCIPAL 2280",
            "sii_parcel_rol": "1064-86",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "STREET_FURNITURE",
            "sub_type": "BUS_STOP_SHELTER",
            "land_regime": "BNUP",
            "total_height_m": 4.654308027236593,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "054129c8-a6bc-419f-a37d-7ffd795663f0",
            "media_owner_rut": "77987654-3",
            "media_owner_name": "Clear Channel",
            "mop_rnavc_status": "NOT_REGISTERED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-SAN -1017-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "UNILLUMINATED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 536,
                    "mop_tmda_daily_vehicles": 8644,
                    "dtpm_bip_daily_validations": 8389,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 357614,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 122574,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 1101738,
                    "production_cost_clp": 111977,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 639008,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "UNREGISTERED_CLANDESTINE",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 157.54161501243294,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "CRITICAL",
            "risk_flags": [
                "MISSING_MOP_ITF_RUTA_68"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-SAN -1018",
        "location": {
            "lat": -33.47661123737469,
            "lng": -70.56736398910742,
            "utm_x": 356479.0,
            "utm_y": 6293037.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13130",
            "commune_name": "San Miguel",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "ARTERIAL",
            "address_raw": "Avenida Principal 7907, San Miguel",
            "address_normalized": "AV PRINCIPAL 6421",
            "sii_parcel_rol": "2256-81",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "STREET_FURNITURE",
            "sub_type": "BUS_STOP_SHELTER",
            "land_regime": "BNUP",
            "total_height_m": 9.377634958535396,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "53c4ba7e-df66-493a-bf6c-7abefbeceece",
            "media_owner_rut": "79876543-2",
            "media_owner_name": "Vallas y Soportes",
            "mop_rnavc_status": "NOT_REGISTERED",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-SAN -1018-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "STATIC_PAPER",
                    "illumination": "UNILLUMINATED",
                    "resolution_px": None,
                    "pixel_pitch_mm": None,
                    "slot_duration_sec": None,
                    "loop_slots_total": None
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 914,
                    "mop_tmda_daily_vehicles": 33650,
                    "dtpm_bip_daily_validations": 12432,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 378934,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 11098,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 2604548,
                    "production_cost_clp": 54905,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 1510637,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "ZONING_VIOLATION_RISK",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": None,
            "dom_authorized_area_m2": None,
            "municipal_patent_rol": None,
            "patent_last_paid_semester": None,
            "patent_taxed_area_m2": 0.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": False,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 81.09332494190687,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "HIGH",
            "risk_flags": [
                "UNREGISTERED_IN_DOM_AND_RENTAS",
                "MISSING_MUNICIPAL_PATENT_PAYMENT"
            ]
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    },
    {
        "asset_id": "CL-RM-LA F-1019",
        "location": {
            "lat": -33.40497919708617,
            "lng": -70.77131207159634,
            "utm_x": 350920.0,
            "utm_y": 6293005.0,
            "srid_geographic": 4326,
            "srid_projected": 32719,
            "commune_code": "13110",
            "commune_name": "La Florida",
            "province_name": "Santiago",
            "region_code": "RM",
            "road_type": "ARTERIAL",
            "address_raw": "Avenida Principal 6379, La Florida",
            "address_normalized": "AV PRINCIPAL 8140",
            "sii_parcel_rol": "4564-55",
            "dtpm_stop_code": None,
            "highway_kilometer": None,
            "speed_limit_kmh": 50
        },
        "structure": {
            "category": "BUILDING_FACADE",
            "sub_type": "LED_SCREEN",
            "land_regime": "PRIVATE_LOT",
            "total_height_m": 9.665944341642415,
            "installation_date": "2020-01-01"
        },
        "ownership": {
            "owner_id": "f287ca99-8412-4fd6-8514-d1804ed7e8a6",
            "media_owner_rut": "76123456-K",
            "media_owner_name": "JCDecaux",
            "mop_rnavc_status": "ACTIVE",
            "commercial_contact": None,
            "concession_id": None,
            "concession_expiration_date": None
        },
        "faces": [
            {
                "face_id": "CL-RM-LA F-1019-F1",
                "face_label": "Norte",
                "azimuth_degrees": 0,
                "orientation_cardinal": "N",
                "traffic_flow_direction": "S-N",
                "dimensions": {
                    "width_m": 3.0,
                    "height_m": 2.0,
                    "area_m2": 6.0
                },
                "technology": {
                    "type": "DOOH_LED",
                    "illumination": "SELF_EMISSIVE_LED",
                    "resolution_px": "1920x1080",
                    "pixel_pitch_mm": 6.0,
                    "slot_duration_sec": 10,
                    "loop_slots_total": 6
                },
                "audience_metrics": {
                    "uoct_hourly_vehicles_avg": 398,
                    "mop_tmda_daily_vehicles": 36213,
                    "dtpm_bip_daily_validations": 3448,
                    "sectra_occupancy_factor": 1.42,
                    "weekly_ots_gross": 138287,
                    "visibility_index_weight": 0.8,
                    "weekly_vac_impacts": 148590,
                    "methodology": "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"
                },
                "commercial_pricing": {
                    "billing_periodicity": "MONTHLY",
                    "list_price_clp_monthly": 3885990,
                    "production_cost_clp": 104856,
                    "estimated_net_discount_pct": 0.42,
                    "estimated_net_price_clp": 2253874,
                    "estimated_annual_municipal_tax_clp": 780000
                }
            }
        ],
        "compliance_audit": {
            "status": "VERIFIED_LEGAL",
            "ley_21473_class": "ELEMENTO_MENOR",
            "dom_permit_number": "123/2020",
            "dom_authorized_area_m2": 6.0,
            "municipal_patent_rol": "456-789",
            "patent_last_paid_semester": "2026-S1",
            "patent_taxed_area_m2": 6.0,
            "mop_vialidad_itf_resolution": None,
            "mma_ds1_lum_certified": True,
            "prc_zone_code": "Z-COM",
            "is_exclusive_residential": False,
            "distance_to_nearest_hazard_m": 135.15633701142792,
            "permit_expiration_date": None,
            "solidary_liability_risk_level": "LOW",
            "risk_flags": []
        },
        "metadata": {
            "entity_resolution_confidence": 0.95,
            "last_scraped_at": "2026-10-25T19:00:00Z",
            "last_audited_at": "2026-10-26T08:00:00Z",
            "sources": []
        }
    }
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
