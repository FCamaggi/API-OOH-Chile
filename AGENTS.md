# AGENTS.md — Guía Operativa para Agentes de Código (Google Jules / Gemini)

Este archivo es leído automáticamente por **Google Jules** (`jules.google.com`) y otros agentes autónomos al clonar `FCamaggi/API-OOH-Chile`. Sigue estas reglas estrictamente para evitar bloqueos de entorno, timeouts de red o fallos de base de datos.

## 1. Resumen del Proyecto y Arquitectura
- **Objetivo:** Plataforma **API-First** de inventario geoespacial, planificación comercial (OOH/DOOH) y auditoría normativa (Ley N° 21.473, Decreto MOP N° 24/2023 y Ley N° 21.770) para las **52 comunas de la Región Metropolitana de Santiago**.
- **Paradigma:** Backend desacoplado (`FastAPI` + `Pydantic v2` + `PostgreSQL 16 / PostGIS 3.4`). El modelo separa estrictamente:
  1. `Asset` (Estructura física georreferenciada en `EPSG:4326` WGS84 y `EPSG:32719` UTM Huso 19S).
  2. `Face` (Cara publicitaria 1:N con tecnología, medidas, métricas abiertas de audiencia OTS/VAC y tarifas de lista vs. netas).
  3. `ComplianceAudit` (Estado legal Ley N° 21.473: Permiso Obra Menor DOM, Rol de Patente Municipal en Rentas, Registro MOP RNAVC y alertas de riesgo).

## 2. Reglas Críticas para NO Quedarse Pegado en la VM de Jules
1. **NUNCA intentes levantar Docker ni conectarte a un servidor PostgreSQL/PostGIS externo durante `pytest`:**
   - Por defecto, la aplicación y los tests operan con `USE_IN_MEMORY_DB=true` (definido en `app/config.py` y `app/data/seed_rm.py`), que provee el catálogo de las 52 comunas de la RM y activos de prueba en memoria con soporte completo de proyecciones, búsqueda por `bbox`/radio, GeoJSON RFC 7946 y *Spatial Entity Resolution*.
   - Para validar cualquier cambio, ejecuta únicamente:
     ```bash
     pytest -q
     ```
2. **NUNCA ejecutes scraping real ni peticiones HTTP hacia sitios externos en los tests:**
   - Todos los conectores en `/etl/connectors/` (DTPM, Mercado Público, Agregadores OOH, Visores ArcGIS Municipales) deben probarse usando fixtures locales en `tests/fixtures/` o `httpx.MockTransport`.
3. **Un cambio acotado por tarea (Micro-PRs):**
   - Mantén los cambios focalizados en el módulo solicitado en el prompt. Antes de modificar contratos JSON/GeoJSON, revisa `docs/03-openapi-geojson-spec.md` y `openapi/openapi.yaml`.

## 3. Comandos de Entorno y Verificación Rápida
```bash
# 1. Instalar dependencias ligeras (sin compilar GDAL/C++ pesados en la VM)
pip install -r requirements.txt

# 2. Ejecutar suite completa de pruebas (debe tardar menos de 2 segundos)
pytest -v

# 3. Verificar que el contrato OpenAPI 3.1 se exporta sin errores
python3 scripts/export_openapi.py
```

## 4. Mapa de Documentación de Ingeniería (`/docs`)
Antes de implementar nuevas funciones, consulta siempre la fuente de verdad en `/docs`:
- `docs/01-prd-factibilidad-rm.md`: Requerimientos funcionales (RF-01 a RF-06), no funcionales y segmentación de las 52 comunas RM en 4 anillos.
- `docs/02-sdd-arquitectura-postgis-etl.md`: Esquema SQL/PostGIS (`migrations/001_init_postgis_rm.sql`), fórmula de *Spatial Entity Resolution* y cálculo abierto de impactos (Traffic UOCT + bip! ADATRAP + TMDA MOP + EOD SECTRA).
- `docs/03-openapi-geojson-spec.md`: Contratos exactos de endpoints (`/v1/assets`, `/v1/faces/search`, `/v1/compliance/discrepancies`, `/v1/campaigns/simulate`, `/v1/ingestion/municipal-batch`, `/v1/tiles/{z}/{x}/{y}.mvt`).
- `docs/04-plan-implementacion-qa-jules-playbook.md`: Sprints de implementación, plantillas jurídicas de Transparencia Pasiva (DOM Art. 16 y Rentas), reglas de QA espacial y lista de micro-prompts para Jules.
