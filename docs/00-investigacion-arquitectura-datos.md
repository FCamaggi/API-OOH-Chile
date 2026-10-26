# Informe Estratégico y Arquitectura de Datos: Publicidad Exterior (OOH / DOOH) en Chile

- **Enfoque Territorial:** Región Metropolitana (52 comunas, escalable a nivel nacional)
- **Objetivo del Sistema:** Construcción de API de inventario para Planificación/Compra de Medios y Auditoría/Fiscalización Normativa (Ley N° 21.473)

## 1. Resumen Ejecutivo y Diagnóstico del Mercado OOH

El mercado chileno de publicidad exterior carece de un repositorio o API unificada. La información sobre soportes (paletas publicitarias, paraderos, pantallas LED monumentales, tótems y muros) se encuentra dispersa entre operadores privados y entidades públicas.

El valor central de la API consiste en el cruce entre dos fuentes primarias:
- **Inventario Comercial (Oferta Privada):** Qué soportes existen, sus dimensiones, orientación, fotos, flujo estimado y titularidad comercial.
- **Catastro Regulatorio y Fiscal (Cumplimiento Legal):** Permisos de edificación menor de la DOM, pago de derechos de propaganda comunal y autorizaciones de Vialidad MOP. Permite identificar elementos sin patente o instalados fuera de norma.

## 2. Mapa de Fuentes y Mecanismos de Extracción (Sin Terceros)

| Operador / Portal | Formatos Principales | Datos Disponibles | Estrategia de Extracción |
| :--- | :--- | :--- | :--- |
| **Grandes Concesionarios** (JCDecaux, Clear Channel, Global Vía Pública) | Mobiliario urbano (Mupis, paraderos Red Movilidad, relojes), Metro de Santiago, pantallas LED prime. | Georreferenciación (coordenadas / intersecciones), formatos estáticos vs. digitales, dimensiones de cara visible, loops y resolución. | Inspección de peticiones de red en visores web/mapas interactivos y cruce con anexos de licitaciones municipales. |
| **Operadores Gran Formato y Digital** (Massiva, Grupo Clan, Publivía, Bigmedia, Bboard) | Pantallas LED monumentales, unipoles y tótems en autopistas (Costanera Norte, Vespucio, Autopista Central), muros medianeros. | Medidas en metros, orientación cardinal/flujo vehicular, visualizaciones diurnas/nocturnas, estimaciones de impacto. | Scraping de fichas de inventario, capas KML/KMZ y parsing de Media Kits y tarifarios técnicos en PDF. |
| **Directorios y Agregadores** (oohpublicidad.cl, dondepauto.cl) | Multi-operador y formatos mixtos (+15.000 soportes). | Coordenadas, caras (A/B), dimensiones exactas, comuna, audiencias en +3.600 puntos y fotografías de referencia. | Extracción estructurada de catálogos web paginados por comuna, proveedor y formato. |

## 3. Matriz Maestra de Atributos vs. Fuentes

| Atributo | Fuente Primaria (Oficial / Legal) | Fuente Secundaria (Comercial / Web) | Dificultad | Actualización |
| :--- | :--- | :--- | :--- | :--- |
| **Coordenadas (Lat/Lng y UTM 19S)** | Anexos Técnicos de Licitaciones / DTPM Shapefile | APIs/Mapas web de operadores OOH | Fácil | Trimestral |
| **Dimensiones (m2, Al x An)** | Bases Técnicas Municipales / Permiso DOM | Catálogos web y Media Kits PDF | Fácil | Semestral |
| **Titular / Operador (RUT)** | Decretos de Adjudicación / Rol Rentas / RNAVC MOP | Sitio web del comercializador | Fácil | Semestral |
| **Tecnología (LED / Estático)** | Permiso de instalación DOM / Informe Vialidad | Catálogo comercial / Web del operador | Fácil | Mensual |
| **Orientación y Flujo** | Informes Viales / Sentido en Shapefile DTPM | Fichas comerciales de agencias | Media | Semestral |
| **Tarifa de Lista vs. Neta** | Órdenes de compra Mercado Público (Campañas Estado) | Tarifarios PDF / Cotizadores web | Media | Bimestral |
| **Permiso DOM / Rol Patente** | Transparencia Pasiva (Art. 16 Ley 21.473 y Rentas) | No disponible públicamente | Media | Semestral |
| **Métricas de Audiencia / Flujo** | Conteos UOCT / Validaciones bip! DTPM / TMDA MOP | Estudios SCOPESI / Estimaciones en agregadores | Media | Semestral |
