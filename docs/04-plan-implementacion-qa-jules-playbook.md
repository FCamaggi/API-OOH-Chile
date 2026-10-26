# DOCUMENTO 4: PLAN DE IMPLEMENTACIÓN, QA ESPACIAL Y PLAYBOOK PARA GOOGLE JULES

## 1. Por Qué Jules No Se Quedará Pegado en Este Repositorio

1. **Archivo `AGENTS.md` en la raíz:** Jules lo detecta automáticamente al clonar `FCamaggi/API-OOH-Chile` y aprende que debe correr `pytest -q` en modo in-memory sin bloquearse intentando levantar contenedores Docker ni instancias externas de PostgreSQL.
2. **Script de configuración de entorno (`scripts/jules_setup.sh`):** En la interfaz web de Jules (`jules.google.com`), en la sección opcional **Environment setup**, pega únicamente:
   ```bash
   bash scripts/jules_setup.sh
   ```
3. **Regla de Oro para Prompts en Jules:** Nunca le pidas más de **1 archivo o 1 funcionalidad concreta por tarea**. Usa la lista de micro-prompts de abajo en orden secuencial.

## 2. Secuencia de Micro-Prompts Quirúrgicos para Google Jules

Copia y pega **uno a la vez** en Jules una vez que hayas subido este repositorio base a `FCamaggi/API-OOH-Chile`:

### Tarea Jules #1: Exportador de Reportes de Fiscalización Municipal en CSV/Excel
> **Prompt para Jules:**
> "Lee `AGENTS.md` y `app/routers/compliance.py`. Agrega un nuevo endpoint `GET /v1/compliance/discrepancies/export` en `app/routers/compliance.py` que reciba `commune_code` (opcional) y devuelva un archivo CSV descargable (`text/csv`) con todas las discrepancias detectadas (columnas: `asset_id`, `commune_name`, `address_normalized`, `media_owner_name`, `compliance_status`, `commercial_area_m2`, `patent_taxed_area_m2`, `undeclared_area_m2`, `risk_flags`). Agrega su test correspondiente en `tests/test_api.py` y verifica ejecutando `pytest -q`."

### Tarea Jules #2: Parser de Planillas Excel/CSV de Transparencia Pasiva (DOM y Rentas)
> **Prompt para Jules:**
> "Lee `AGENTS.md` y `etl/connectors/municipal_parser.py`. Implementa la función `normalize_municipal_rows(raw_rows: list[dict], commune_code: str)` en `etl/connectors/municipal_parser.py` para mapear nombres de columnas variables provenientes de municipalidades chilenas (ej. 'ROL PATENTE' o 'N_ROL' -> `municipal_patent_rol`, 'DIRECCION' o 'UBICACION' -> `address`, 'M2' o 'SUPERFICIE' -> `area_m2`, 'RUT' -> `owner_rut`) al esquema `MunicipalInboundRecord` de `app/schemas.py`. Crea pruebas unitarias en `tests/test_municipal_parser.py` sin llamadas de red y corre `pytest -q`."

### Tarea Jules #3: Validador de Seguridad Vial y Zonas Residenciales (Ley N° 21.473 Arts. 5 y 28)
> **Prompt para Jules:**
> "Lee `AGENTS.md` y `docs/02-sdd-arquitectura-postgis-etl.md`. Crea un servicio `app/services/regulatory_validator.py` con una función pura `evaluate_ley_21473_restrictions(asset, faces)` que verifique: 1) Si alguna cara es `DOOH_LED` y `is_exclusive_residential` es `True`, agregue la bandera `PROHIBITED_LED_IN_RESIDENTIAL_ZONE_ART28` y cambie el estado a `ZONING_VIOLATION_RISK`; 2) Si `distance_to_nearest_hazard_m` es menor a 40.0 metros en `HIGHWAY_CONCESSION` o `INTERURBAN_ROUTE`, agregue `HAZARD_PROXIMITY_LT_40M_DECRETO24`. Añade tests unitarios en `tests/test_regulatory_validator.py` y ejecuta `pytest -q`."

### Tarea Jules #4: Conector de Paraderos DTPM (`stops.txt` GTFS y Shapefile)
> **Prompt para Jules:**
> "Lee `AGENTS.md` y `etl/connectors/dtpm_ingestor.py`. Implementa la función `parse_dtpm_gtfs_stops(csv_content: str, default_commune_code: str)` que lea filas en formato GTFS `stops.txt` (`stop_id`, `stop_code`, `stop_name`, `stop_lat`, `stop_lon`), convierta las coordenadas WGS84 a UTM Huso 19S aproximado usando el helper de `app/services/entity_resolution.py` y construya objetos `Asset` de categoría `STREET_FURNITURE` y subtipo `BUS_SHELTER`. Agrega tests con un CSV en memoria en `tests/test_dtpm_ingestor.py` y corre `pytest -q`."

### Tarea Jules #5: Simulador de Descuentos Reales de Mercado Público por Formato
> **Prompt para Jules:**
> "Lee `AGENTS.md` y `app/routers/campaigns.py`. Mejora el cálculo financiero en `POST /v1/campaigns/simulate` para que, cuando se envíe el parámetro opcional `pricing_strategy` (`LIST_PRICE`, `CONSERVATIVE_30PCT`, `MARKET_AVERAGE_42PCT`, `STATE_TENDER_55PCT`), ajuste dinámicamente los costos netos y devuelva también el desglose por comuna (`breakdown_by_commune`) y por operador (`breakdown_by_owner`). Agrega tests en `tests/test_api.py` y verifica con `pytest -q`."
