# DOCUMENTO 3: ESPECIFICACIÓN TÉCNICA DE LA API (OPENAPI 3.1, GEOJSON & VECTOR TILES)

El contrato formal OpenAPI 3.1.0 se encuentra en `openapi/openapi.yaml` y se autogenera mediante `python3 scripts/export_openapi.py`.

## Catálogo de Endpoints Implementados en `/app/routers`

| Método | Ruta | Descripción | Parámetros Clave / Cuerpo |
| :--- | :--- | :--- | :--- |
| `GET` | `/health` | Estado de salud del motor API-First y conteo de comunas/activos cargados. | Ninguno |
| `GET` | `/v1/territories/communes` | Lista las **52 comunas de la Región Metropolitana** con su código CUT, provincia, anillo operativo (1 a 4) y tasas de derechos de propaganda en UTM/m². | `ring_tier` (1..4), `province_name` |
| `GET` | `/v1/assets` | Búsqueda geoespacial y multicriterio de estructuras físicas. Soporta salida tabular (`format=json`) o `FeatureCollection` estándar RFC 7946 (`format=geojson`). | `commune_code`, `bbox`, `near` (`lat,lng,radius_m`), `structure_category`, `tech_type`, `compliance_status`, `format` |
| `GET` | `/v1/assets/{asset_id}` | Ficha canónica completa de una estructura física (`location`, `structure`, `ownership`, `faces`, `compliance_audit`, `metadata`). | `asset_id` (ej. `CL-RM-PROV-00482`) |
| `GET` | `/v1/faces/search` | Buscador de caras publicitarias para planificación de medios con métricas OTS/VAC y precios netos estimados. | `commune_code`, `tech_type`, `min_area_m2`, `max_net_price_clp`, `min_weekly_vac` |
| `GET` | `/v1/compliance/discrepancies` | Fiscalización Ley N° 21.473: lista soportes clandestinos, sin permiso DOM o con subdeclaración de m² y calcula la evasión estimada en UTM/CLP. | `commune_code`, `status`, `ley_21473_class` |
| `GET` | `/v1/compliance/communes/{commune_code}/summary` | Resumen ejecutivo de auditoría municipal para una comuna específica de la RM. | `commune_code` (ej. `13107` Huechuraba) |
| `POST` | `/v1/campaigns/simulate` | Simula una campaña sobre una lista de `face_ids`, filtrando activos con riesgo de responsabilidad solidaria (Art. 31 Ley 21.473) y proyectando inversión neta (descuento 30%–55%). | JSON con `campaign_name`, `duration_weeks`, `exclude_non_compliant_assets`, `face_ids` |
| `POST` | `/v1/ingestion/municipal-batch` | Recibe registros administrativos de DOM o Rentas Municipales y ejecuta en vivo el motor de *Spatial Entity Resolution* contra el inventario comercial. | JSON con `commune_code`, `source_type` (`DOM_ART16` o `RENTAS_PATENTES`) y lista `records` |
| `GET` | `/v1/tiles/{z}/{x}/{y}.json` | Descriptor de capa vectorial ligero para previsualización rápida en el futuro visor frontend (y conector PostGIS `ST_AsMVT` en producción). | `z`, `x`, `y` |
