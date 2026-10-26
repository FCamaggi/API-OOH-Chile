# DOCUMENTO 5: REVISIÓN DE IMPLEMENTACIÓN Y GUÍA DE DESPLIEGUE

## 1. Análisis de Brechas: Documentación vs. Implementación

Tras una revisión exhaustiva del código fuente comparado con los requerimientos establecidos en los documentos de arquitectura y factibilidad (`docs/`), se ha constatado que **todos los requerimientos principales (RF-01 a RF-06) y las tareas del Playbook de Jules (Documento 4) ya se encuentran implementados y operativos.**

### Funcionalidades Implementadas y Verificadas:
*   **Exportador de Reportes de Fiscalización (Tarea 1):** El endpoint `GET /v1/compliance/discrepancies/export` está implementado en `app/routers/compliance.py` y permite exportar en formato CSV el cruce entre la oferta comercial y el estatus legal según la Ley N° 21.473.
*   **Parser de Planillas Municipales (Tarea 2):** El script `etl/connectors/municipal_parser.py` incluye las funciones `standardize_municipal_record` y `normalize_municipal_rows`, capaces de mapear nombres de columnas variables (ej. "ROL PATENTE", "SUPERFICIE") al esquema estándar `MunicipalInboundRecord`, unificando datos provenientes de Transparencia.
*   **Validador de Seguridad Vial y Zonas Residenciales (Tarea 3):** Se encuentra en `app/services/regulatory_validator.py`. Verifica dinámicamente si una pantalla LED se encuentra en zona residencial (`PROHIBITED_LED_IN_RESIDENTIAL_ZONE_ART28`) o a menos de 40 metros de una ruta (`HAZARD_PROXIMITY_LT_40M_DECRETO24`).
*   **Conector de Paraderos DTPM (Tarea 4):** En `etl/connectors/dtpm_ingestor.py` la función `parse_dtpm_gtfs_stops` mapea coordenadas WGS84 a UTM Huso 19S en memoria y convierte los registros en `Asset` tipo `BUS_SHELTER`.
*   **Simulador de Precios y Campañas (Tarea 5):** En `app/routers/campaigns.py`, el endpoint `/v1/campaigns/simulate` procesa el `pricing_strategy` con los descuentos de mercado configurados (ej. `STATE_TENDER_55PCT`, `MARKET_AVERAGE_42PCT`), ajustando la tarifa real.
*   **Modelo de Datos en Memoria:** Tal y como se exige en `AGENTS.md`, la aplicación es capaz de correr en modo desacoplado `USE_IN_MEMORY_DB=true` cargando la semilla `seed_rm.py`, sin bloquearse por Docker.

**Conclusión del Análisis de Brechas:** No existen funcionalidades críticas pendientes de implementación para la versión base. El backend responde íntegramente bajo la arquitectura *API-First*.

## 2. Resultados de las Pruebas Unitarias

La suite de `pytest` corrió 30 pruebas (`tests/test_api.py`, `tests/test_dtpm_ingestor.py`, `tests/test_municipal_parser.py`, `tests/test_regulatory_validator.py`) de manera 100% exitosa en **~0.8 segundos**.

### ¿Qué demuestran estas pruebas en lenguaje natural?
1.  **API y Rutas (routers):** El servidor es capaz de levantar el servicio y exponer correctamente el catálogo de las 52 comunas, devolver estructuras físicas en formato JSON y GeoJSON, realizar las conciliaciones espaciales para reportar evasión tributaria, y calcular la rentabilidad de las campañas. Todo esto sin colapsar el sistema.
2.  **Validación Normativa:** Demuestran que si el sistema detecta que un letrero digital está ubicado donde no corresponde según la Ley N° 21.473 o muy cerca de una autopista según el Decreto MOP N° 24/2023, la bandera de riesgo se activa automáticamente en el expediente de cumplimiento.
3.  **Procesamiento de Archivos e Ingesta:** Aseguran que cuando el municipio sube una planilla Excel/CSV mal formateada, el sistema es capaz de limpiar los nombres de las columnas, extraer los números, y normalizar las direcciones para procesarlos. Igualmente con el listado de los paraderos del Transantiago (DTPM).
4.  **Cero Dependencias Externas:** Reafirman que el sistema es resiliente, autoconntenido y determinista. No necesita que la base de datos externa de PostgreSQL/PostGIS esté levantada para que el equipo (y los agentes IA) verifiquen que la lógica de negocio esté correcta.

## 3. Guía de Despliegue en Fly.io (Free Tier)

Fly.io es ideal para este tipo de aplicación gracias a su compatibilidad nativa con Docker y su capa de alojamiento gratuito para proyectos personales o demostraciones.

### 3.1 Prerrequisitos
1. Tener instalado [flyctl](https://fly.io/docs/hands-on/install-flyctl/) (la CLI de Fly.io).
2. Estar autenticado ejecutando:
   ```bash
   fly auth login
   ```

### 3.2 El Archivo `fly.toml`
Se ha creado un archivo `fly.toml` en la raíz del repositorio. Este archivo instruye a Fly.io a construir la aplicación a partir del `Dockerfile` existente y a usar el modo `in-memory` (ideal para *free tier*, sin necesidad de pagar por una base de datos manejada).

### 3.3 Pasos para Desplegar

**Paso 1: Lanzar la aplicación inicial (pero no la despliegues aún)**
Ejecuta el siguiente comando en la raíz del proyecto para crear la app en Fly. Cuando pregunte si deseas ajustar la configuración (tweak settings) o desplegar ahora, dile que **No**.
```bash
fly launch --no-deploy --copy-config --name "api-ooh-chile"
```
*(Nota: Si el nombre "api-ooh-chile" ya está en uso a nivel global en Fly, elige otro o deja que asigne uno aleatoriamente).*

**Paso 2: Desplegar**
Una vez registrada la app en tu cuenta de Fly, lanza el despliegue con:
```bash
fly deploy
```

Fly.io leerá el `Dockerfile`, instalará las dependencias en una máquina virtual de 256MB de RAM (suficiente para la API sin PostGIS), y dejará el servicio expuesto públicamente en `https://[tu-nombre-de-app].fly.dev`.

**Paso 3: Verificar el servicio**
Puedes abrir el navegador o ejecutar:
```bash
curl https://[tu-nombre-de-app].fly.dev/health
```
También podrás ver la documentación Swagger interactiva en:
`https://[tu-nombre-de-app].fly.dev/docs`
