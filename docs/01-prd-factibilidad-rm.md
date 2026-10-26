# DOCUMENTO 1: PRD Y ESTUDIO DE FACTIBILIDAD — PLATAFORMA API-FIRST DE INVENTARIO Y AUDITORÍA OOH / DOOH (REGIÓN METROPOLITANA)

- **Arquitectura de Producto:** API-First (Core Data Engine & REST/GeoJSON API, desacoplado para consumo posterior por visores propios y clientes B2B/B2G).
- **Alcance Territorial:** Las **52 comunas de la Región Metropolitana de Santiago** (34 comunas urbanas del Gran Santiago + 18 comunas rurales/periféricas y corredores interurbanos Ruta 5, Ruta 68, Ruta 78, Ruta 57 Los Libertadores y Camino a Melipilla).

## 1. Estrategia API-First y Propuesta de Valor Dual

1. **Desacoplamiento Total ("API First, Consumo Después"):** Toda la lógica geoespacial, reconciliación de entidades, auditoría de la Ley N° 21.473, cálculo de impactos abiertos y simulación presupuestaria se expone vía endpoints RESTful y GeoJSON (RFC 7946).
2. **Responsabilidad Solidaria (Art. 31 Ley N° 21.473):** La normativa vigente hace solidariamente responsable al anunciante por exhibir publicidad en soportes sin permiso DOM o sin inscripción vigente en el Registro Nacional de Avisadores Viales y Camineros (RNAVC) del MOP. La API integra el semáforo de cumplimiento normativo directamente en el flujo de planificación de medios.

## 2. Segmentación de las 52 Comunas de la RM en 4 Anillos Operativos

| Anillo | N° Comunas | Comunas Incluidas | Foco Primario de Datos |
| :--- | :--- | :--- | :--- |
| **Anillo 1: Eje Prime y Cono Oriente** | 6 | Santiago, Providencia, Las Condes, Vitacura, Lo Barnechea, Ñuñoa | Pantallas LED prime, mobiliario digital, visores ArcGIS REST comunales (GeoProvidencia, Catastro DOM Las Condes/Vitacura) y altas tasas de derechos municipales (1,5 a 4,5 UTM/m2 semestral). |
| **Anillo 2: Polos Comerciales y Autopistas** | 12 | Huechuraba, Quilicura, Pudahuel, Estación Central, Maipú, La Florida, Puente Alto, San Bernardo, Recoleta, Independencia, Macul, Peñalolén | Letreros monumentales y unipoles en predios privados colindantes a Costanera Norte, Vespucio Norte/Sur, Autopista Central, Aeropuerto AMB (SCL) y grandes centros comerciales. |
| **Anillo 3: Gran Santiago Urbano** | 18 | Cerrillos, Cerro Navia, Conchalí, El Bosque, La Cisterna, La Granja, La Pintana, La Reina, Lo Espejo, Lo Prado, Pedro Aguirre Cerda, Quinta Normal, Renca, San Joaquín, San Miguel, San Ramón, Padre Hurtado, Pirque | Red de +11.000 paraderos Red Movilidad (DTPM Shapefile/GTFS) y licitaciones municipales de mobiliario urbano en Mercado Público. |
| **Anillo 4: Comunas Periféricas y Rutas RM** | 16 | Colina, Lampa, Tiltil, Buin, Paine, Calera de Tango, Melipilla, Curacaví, María Pinto, Alhué, San Pedro, Talagante, Peñaflor, Isla de Maipo, El Monte, San José de Maipo | Letreros camineros e interurbanos en Ruta 5 Norte/Sur, Ruta 68, Ruta 78 y Los Libertadores bajo fiscalización de Vialidad MOP (RNAVC y censos TMDA). |

## 3. Requerimientos Funcionales (RF) y No Funcionales (RNF)

- **RF-01 (Modelo Tricapa):** Separar `Asset` (estructura física), `Face` (1:N caras publicitarias) y `ComplianceAudit` (expediente normativo Ley N° 21.473).
- **RF-02 (Consultas Espaciales):** Soportar filtrado por `commune_code` (52 comunas RM), `bbox`, radio en metros (`near=lat,lng,radius_m`), tecnología y estado legal, entregando `JSON` o `GeoJSON` (`FeatureCollection`).
- **RF-03 (Semáforo de Cumplimiento Ley N° 21.473):** Clasificar cada estructura en `VERIFIED_LEGAL`, `PARTIAL_COMPLIANCE` (ej. subdeclaración >15% de m² entre oferta comercial y Rol de Rentas), `UNREGISTERED_CLANDESTINE` o `ZONING_VIOLATION_RISK` (pantalla LED en zona residencial exclusiva según Art. 28 Ley N° 21.473).
- **RF-04 (Motor Abierto de Audiencia):** Calcular `weekly_ots_gross` y `weekly_vac_impacts` combinando Traffic UOCT, validaciones bip! ADATRAP, TMDA MOP y tasa de ocupación EOD SECTRA ponderados por superficie, azimut, iluminación y ciclo de loop digital.
- **RF-05 (Inteligencia de Precios Netos):** Estimar el precio neto de negociación aplicando el descuento real (30%–55%) observado en Órdenes de Compra de campañas estatales en Mercado Público, además de calcular el derecho municipal anual estimado en UTM/m².
