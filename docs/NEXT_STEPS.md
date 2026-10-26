# NEXT STEPS: Implementación PostGIS (Sesiones Futuras)

Este documento resume las tareas pendientes para completar la transición completa de la base de datos en memoria a la base de datos relacional y geoespacial (PostgreSQL + PostGIS).

## 1. Mapeo de Modelos (ORM)
*   **Crear `app/models.py`:** Utilizando SQLAlchemy 2.0 (o SQLModel) y GeoAlchemy2, mapear las tablas definidas en `migrations/001_init_postgis_rm.sql` a clases de Python (ej: `CommuneRMModel`, `MediaOwnerModel`, `AssetModel`, etc.).
*   **Implementar `PostgresOOHRepository`:** Crear una clase en `app/data/postgres_repo.py` que cumpla la misma firma o interfaz implícita que el repositorio actual `InMemoryOOHRepository`, pero ejecutando consultas contra SQLAlchemy y PostGIS.
*   **Actualizar inyección de dependencias:** Reemplazar el "dummy" actual en `app/dependencies.py` para devolver instancias de `PostgresOOHRepository` cuando `USE_IN_MEMORY_DB` sea falso.

## 2. Bases de Datos Efímeras para Testing
*   **Integrar Testcontainers o pytest-postgresql:** Configurar Pytest para levantar un contenedor efímero de PostGIS durante las pruebas (en `conftest.py`).
*   **Fixtures SQL:** Convertir la data semilla o `new_assets.json` en scripts SQL que puedan poblar esta base de datos antes de cada test.
*   Con esto, el pipeline CI/CD validará el código contra la base de datos real.

## 3. Conexión de ETL a Base de Datos
*   **Actualizar Conectores ETL (`etl/connectors/`):** Hacer que los conectores como `dtpm_ingestor.py` y `municipal_parser.py` inyecten directamente los datos parseados a las tablas PostGIS utilizando la capa de modelos ORM.
*   **Pipelines Automatizados:** Habilitar cronjobs o endpoints administrativos que gatillen la ingesta de manera periódica.

## 4. Evolución de Lógica Geoespacial y Simulaciones
*   **Cálculos de Audiencia y Precios:** Mover parte del cálculo que actualmente sucede en memoria en `app/routers/campaigns.py` o `app/services/audience_engine.py` a consultas SQL optimizadas aprovechando PG_TRGM y funciones como `ST_DWithin` de PostGIS para los filtrados geoespaciales rápidos.
