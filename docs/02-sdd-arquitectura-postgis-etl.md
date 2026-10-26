# DOCUMENTO 2: SDD ARQUITECTURA DE SOFTWARE, MODELO POSTGIS Y PIPELINES ETL (REGIÓN METROPOLITANA)

## 1. Arquitectura de Datos y Doble Proyección Geodésica
- Todas las estructuras físicas (`assets`) y límites comunales (`communes_rm`) almacenan geometrías en dos sistemas de referencia espacial:
  - `EPSG:4326` (WGS84 Latitud/Longitud) para serialización directa en GeoJSON y consumo en mapas web.
  - `EPSG:32719` (UTM Datum WGS84 Huso 19 Sur en metros) para cruces exactos con el Shapefile oficial del DTPM, kilometrajes de Vialidad MOP y verificación de distancias normativas en metros (Decreto MOP N° 24/2023).
- El DDL completo de producción se encuentra en `migrations/001_init_postgis_rm.sql`.

## 2. Algoritmo de Reconciliación Espacial (Spatial Entity Resolution)
Implementado en `app/services/entity_resolution.py`. Para vincular un registro administrativo municipal (Permiso DOM o Rol de Patente de Propaganda en Rentas) con un activo comercial existente dentro de la misma comuna, se calcula un puntaje compuesto entre `0.00` y `1.00`:

```text
Match_Score = (0.40 * S_espacial) + (0.25 * S_direccion) + (0.20 * S_estructural) + (0.15 * S_titular)
```

1. **`S_espacial` (40%):** Si hay coincidencia exacta de Rol SII predial (`sii_parcel_rol`) o distancia euclidiana <= 10 metros en UTM 19S, `S_espacial = 1.0`. Entre 10 m y 35 m decae linealmente hasta `0.40`. Mayor a 35 m es `0.0`.
2. **`S_direccion` (25%):** Normalización de direcciones chilenas (`AVDA.` -> `AVENIDA`, `ESQ.` -> `ESQUINA`, eliminación de tildes y signos) y cálculo de similitud de tokens/trigramas.
3. **`S_estructural` (20%):** Compara categoría (`ELEMENTO_MAYOR` vs `ELEMENTO_MENOR`) y superficie (`area_m2`). Si las demás dimensiones coinciden pero la superficie comercial supera en más de un 15% la superficie declarada en Rentas o DOM, vincula el registro y agrega automáticamente la bandera `"AREA_SUBDECLARATION_GT_15PCT"`.
4. **`S_titular` (15%):** Coincidencia por RUT societario normalizado o razón social del operador.

Umbrales:
- `Match_Score >= 0.82`: Fusión automática (`AUTO_MERGED`).
- `0.60 <= Match_Score < 0.82`: Cola de revisión (`PENDING_MANUAL_REVIEW`).
- `Match_Score < 0.60`: Sin coincidencia (registro nuevo o activo comercial clandestino `UNREGISTERED_CLANDESTINE`).

## 3. Motor Abierto de Audiencia e Impactos (OTS / VAC Sintético)
Implementado en `app/services/audience_engine.py`:
- Calcula el flujo base diario combinando conteos horarios **Traffic UOCT** (`uoct_hourly_vehicles_avg * 18 horas activas * sectra_occupancy_factor`), validaciones diarias **bip! ADATRAP** (`dtpm_bip_daily_validations`) o **TMDA MOP** en autopistas y rutas interurbanas.
- Pondera el `visibility_index_weight` (entre `0.100` y `1.000`) según el área en m², el ángulo de orientación respecto al eje vial (`azimuth_degrees`), el tipo de iluminación y la cuota de pantalla en loops `DOOH_LED` (`slot_duration_sec / (slot_duration_sec * loop_slots_total)`).
