# DOCUMENTO 06: Plan para Implementar Funcionalidad Real de Datos (Base de Datos / PostGIS)

Este documento detalla el plan paso a paso para reemplazar la base de datos simulada en memoria (`InMemoryOOHRepository` alojada en `app/data/seed_rm.py`) con la base de datos real utilizando **PostgreSQL** y su extensión geoespacial **PostGIS**.

## 1. Configuración de la Base de Datos Relacional y Extensiones Geoespaciales
La API está estructurada para depender de una base de datos que ya ha sido modelada.
*   **Aprovisionamiento:** Instanciar la base de datos PostgreSQL en el entorno local (utilizando `docker-compose.yml`) y en producción (con un proveedor administrado como AWS RDS, Supabase, Neon o Render) que soporte **PostGIS 3.4+**.
*   **Migraciones:** Ejecutar el archivo de esquema inicial `migrations/001_init_postgis_rm.sql`. Este archivo contiene las tablas de estructura base, en donde se contemplan geometrías tanto en `EPSG:4326` (para UI y APIs GeoJSON) como en `EPSG:32719` (para reconciliación espacial exacta).

## 2. Abstracción del Repositorio de Datos
Actualmente, los enrutadores (routers) importan directamente la instancia de pruebas `repo = InMemoryOOHRepository()` desde `app/data/seed_rm.py`. Se requiere migrar a un patrón de diseño dependencias más robusto.
*   **ORM e Integración:** Seleccionar e incorporar un ORM (como `SQLAlchemy 2.0` o `SQLModel` que incluyen soporte para `GeoAlchemy2` en el caso de bases geoespaciales), o bien, utilizar consultas asíncronas directas usando bibliotecas como `asyncpg`.
*   **Actualizar Routers y Dependencias:** Implementar la inyección de dependencias nativa de FastAPI (ej: `Depends(get_db_session)`) en todos los endpoints (`app/routers/assets.py`, `app/routers/campaigns.py`, `app/routers/compliance.py`, `app/routers/ingestion.py`, `app/routers/territories.py`).

## 3. Implementación de los Conectores Base (ETL y Pipelines de Ingestión)
Para poblar y mantener actualizada la base de datos real con las diversas fuentes:
*   **DTPM, UOCT y MOP:** Configurar scripts en `etl/connectors/` (como el archivo propuesto `dtpm_ingestor.py`) para ingestar periódicamente las cargas de datos reales (rutas, paraderos, flujos de tráfico vehicular, etc.).
*   **Planillas Municipales:** Integrar de forma programática las cargas de los padrones municipales DOM (Permisos Art. 16 de la Ley N° 21.473) y Rentas utilizando el script `municipal_parser.py`, que ejecutará el servicio de `entity_resolution.py` contra los datos guardados en PostGIS.

## 4. Evolución del Simulador de Precios y Audiencias
Para el Endpoint de simulación de campañas `POST /v1/campaigns/simulate`:
*   Sustituir los cálculos de iteración en memoria (ciclos `for` que buscan IDs a nivel código) por consultas SQL/ORM optimizadas.
*   Conectar el motor abierto de audiencias y proyecciones (`app/services/audience_engine.py`) con las tablas reales pobladas desde la UOCT y validaciones de DTPM/Metro.

## 5. Pruebas y Validación (CI/CD)
Una vez conectados a PostGIS, el comportamiento de los endpoints cambiará de determinista predecible en memoria a dinámico:
*   **Testcontainers / Base de Datos Efímera:** Integrar en Pytest una configuración con `pytest-postgresql` o `testcontainers` que levante una base PostgreSQL con PostGIS temporal.
*   **Fixtures de Semilla:** Convertir los 25 activos falsos usados anteriormente (`new_assets.json` o `seed_rm.py`) en scripts SQL o de carga (`Fixtures`) para poblar la DB efímera de pruebas antes de cada ciclo de validación.

## Conclusión
Al completar estos hitos, la API pasará de ser un entorno demostrativo "API-First / Mocked" a un entorno de producción totalmente transaccional e indexado geoespacialmente para la Región Metropolitana, respaldado por datos continuos desde municipalidades, ministerios y operadores DOOH.
