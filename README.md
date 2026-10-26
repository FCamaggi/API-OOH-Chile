# API-OOH-Chile — Plataforma API-First de Inventario y Auditoría OOH / DOOH (Región Metropolitana)

Motor geoespacial, comercial y de fiscalización normativa (**Ley N° 21.473**, **Decreto MOP N° 24/2023** y **Ley N° 21.770**) diseñado bajo arquitectura **API-First** para consolidar el inventario de publicidad exterior (*Out-of-Home* y *Digital Out-of-Home*) en las **52 comunas de la Región Metropolitana de Santiago**.

## Propósito Dual de la Plataforma

1. **Planificación y Compra de Medios (AdTech / Media Buying):**
   - Catálogo unificado de estructuras físicas (`Asset`) y caras publicitarias (`Face`, relación 1:N) en formato JSON y **GeoJSON (RFC 7946)**.
   - Motor abierto de estimación de audiencias (**OTS / VAC sintético**) basado en conteos horarios **Traffic UOCT**, validaciones **bip! (ADATRAP DTPM/Metro)**, censos **TMDA del MOP** y tasas de ocupación vehicular **EOD SECTRA**.
   - Benchmark financiero entre tarifas de lista y **precios netos reales** (descuentos de 30% a 55% auditados en Órdenes de Compra de Mercado Público).
2. **Auditoría Urbana y Cumplimiento Legal (GovTech / RegTech):**
   - Conciliación espacial automatizada (*Spatial Entity Resolution*) entre la oferta comercial y los registros oficiales: **Permisos de Obra Menor DOM (Art. 16 Ley N° 21.473)**, **Roles de Patentes de Propaganda en Rentas Municipales** y el **Registro Nacional de Avisadores Viales y Camineros (RNAVC del MOP)**.
   - Detección automática de soportes clandestinos (`UNREGISTERED_CLANDESTINE`), subdeclaración de superficie afecta a impuestos (`AREA_SUBDECLARATION_GT_15PCT`) y prohibiciones de emplazamiento en zonas residenciales exclusivas (Art. 28 Ley N° 21.473) para mitigar la **responsabilidad solidaria del anunciante (Art. 31)**.

## Estructura del Repositorio

```text
API-OOH-Chile/
├── AGENTS.md                        # Instrucciones automáticas para Google Jules (evita bloqueos en VM)
├── README.md                        # Guía general del proyecto
├── docker-compose.yml               # Stack local: PostgreSQL 16 + PostGIS 3.4, Redis 7 y API FastAPI
├── Dockerfile                       # Imagen de producción del servidor API-First
├── pyproject.toml                   # Configuración de proyecto Python, pytest y ruff
├── requirements.txt                 # Dependencias rápidas y compatibles con entornos de agentes
├── docs/                            # Suite completa de documentos de Diseño, Producto y Datos
│   ├── 00-inteligencia-datos-regulacion-rm.md
│   ├── 00-investigacion-arquitectura-datos.md
│   ├── 01-prd-factibilidad-rm.md
│   ├── 02-sdd-arquitectura-postgis-etl.md
│   ├── 03-openapi-geojson-spec.md
│   └── 04-plan-implementacion-qa-jules-playbook.md
├── migrations/
│   └── 001_init_postgis_rm.sql      # Esquema físico PostgreSQL 16 + PostGIS 3.4 + Índices GIST
├── openapi/
│   └── openapi.yaml                 # Especificación OpenAPI 3.1.0 autogenerada
├── app/                             # Aplicación Core API-First (FastAPI)
│   ├── main.py                      # Punto de entrada y registro de routers
│   ├── config.py                    # Variables de entorno y modo in-memory/PostGIS
│   ├── schemas.py                   # Contratos Pydantic v2 (Asset, Face, Compliance, GeoJSON)
│   ├── data/
│   │   └── seed_rm.py               # Catálogo de las 52 comunas RM (4 anillos) y activos semilla
│   ├── services/
│   │   ├── entity_resolution.py     # Algoritmo híbrido de Spatial Entity Resolution (DOM/Rentas vs Comercial)
│   │   └── audience_engine.py       # Cálculo abierto de OTS y VAC (UOCT + bip! + TMDA + SECTRA)
│   └── routers/
│       ├── assets.py                # GET /v1/assets (JSON & GeoJSON RFC 7946) y GET /v1/assets/{id}
│       ├── faces.py                 # GET /v1/faces/search (planificación multicriterio)
│       ├── compliance.py            # GET /v1/compliance/discrepancies y resumen comunal Ley 21.473
│       ├── campaigns.py             # POST /v1/campaigns/simulate (presupuesto neto y filtro legal)
│       ├── territories.py           # GET /v1/territories/communes (52 comunas RM) y Vector Tiles MVT stub
│       └── ingestion.py             # POST /v1/ingestion/municipal-batch (conciliación de planillas DOM/Rentas)
├── etl/
│   └── connectors/                  # Conectores base (DTPM, Agregadores, Mercado Público, Padrones DOM/Rentas)
├── scripts/
│   ├── jules_setup.sh               # Script de configuración de entorno para Google Jules
│   └── export_openapi.py            # Exportador del contrato OpenAPI 3.1 a openapi/openapi.yaml
└── tests/                           # Suite pytest 100% determinista y sin dependencias externas
```

## Inicio Rápido

### Opción A: Ejecución inmediata y Tests (Modo ligero / Google Jules)
```bash
pip install -r requirements.txt
pytest -v
uvicorn app.main:app --reload --port 8000
```
- Documentación interactiva Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

### Opción B: Stack Completo con PostGIS (`docker-compose`)
```bash
docker compose up --build -d
```
Levanta `PostgreSQL 16 + PostGIS 3.4` (ejecutando automáticamente `migrations/001_init_postgis_rm.sql`), `Redis 7` y el servicio `FastAPI`.
