# Planificación de Frontend: Vista Simple y Consumo de API (API OOH Chile)

Este documento detalla la planificación arquitectónica y técnica para la creación de una vista frontend ligera (Single Page Application o SPA) destinada a consumir la API geoespacial del proyecto "API OOH Chile".

## 1. Stack Tecnológico Recomendado
Para asegurar agilidad, un desarrollo simple pero robusto y un bajo costo de mantenimiento (acorde al enfoque *API-First* del proyecto), se propone el siguiente stack:
- **Framework Core:** React.js con Vite (por su rapidez de compilación y facilidad para desplegar en servicios gratuitos como Vercel o el mismo Render).
- **Enrutamiento:** React Router (para manejar la navegación entre los módulos).
- **Peticiones HTTP:** Axios o la API Fetch nativa.
- **Mapas y Geoespacial (Módulo Core):** React Leaflet (integración de la librería Leaflet en React), consumiendo teselas base de OpenStreetMap o Mapbox, y añadiendo las capas de GeoJSON generadas por el backend.

## 2. Arquitectura de Módulos
La aplicación constará de dos módulos principales altamente diferenciados por su objetivo.

### Módulo 1: Documentación Interactiva de la API
Dado que el proyecto enfatiza un enfoque *API-First*, el desarrollador o consumidor de la plataforma necesita un punto centralizado para entender los contratos de integración.
- **Implementación:**
  - La opción más limpia y que sigue la convención actual es usar un `<iframe src="/docs" />` o `<iframe src="/redoc" />` apuntando directamente a la documentación autogenerada (Swagger UI o ReDoc) expuesta por el servidor FastAPI.
  - Alternativamente, si ambos sistemas conviven en el mismo dominio, la barra de navegación del Frontend SPA puede tener un enlace simple que redirija a `/docs` (ruta administrada por el Backend).
- **Objetivo:** Exploración de endpoints (`/v1/assets`, `/v1/faces/search`, etc.), visualización de esquemas Pydantic y pruebas *en vivo* de las rutas de la API.

### Módulo 2: Visualización Geoespacial (Caso de Uso Core)
Este módulo abordará el caso de uso central: Planificación Comercial OOH/DOOH e Inventario Geoespacial en la Región Metropolitana de Santiago.
- **Implementación:**
  - **Mapa Interactivo:** Una vista a pantalla completa (o dominante en el layout) renderizando un mapa base centrado en Santiago (EPSG:4326).
  - **Carga de Activos (Assets):** El frontend hará un request `GET /v1/assets` o usará una ruta de búsqueda con Bounding Box (`bbox`) a medida que el usuario arrastre el mapa.
  - **Renderizado de Puntos:** Los activos se pintarán como marcadores o clústeres. Dado que FastAPI puede retornar `FeatureCollection` (GeoJSON), Leaflet puede parsear e ingerir estos datos directamente usando el componente `<GeoJSON data={data} />`.
  - **Interactividad (Popups y Sidebar):** Al hacer clic en un soporte publicitario (Asset):
    - Se despliega un *Popup* sobre el mapa con información básica (tipo de elemento, ubicación).
    - Un panel lateral (*Sidebar*) se actualiza consumiendo el detalle (Faces, tecnología, medidas y métricas como OTS).
    - En ese mismo panel se mostrará visualmente el semáforo del estado del `ComplianceAudit` (ej. verde si tiene permiso de DOM al día, rojo si no).

## 3. Flujo de Trabajo y Próximos Pasos para Desarrollo
1. **Inicialización:** `npm create vite@latest api-ooh-frontend -- --template react` (o integrar los estáticos al servidor de FastAPI usando `StaticFiles` si se requiere un único despliegue).
2. **Componentes Base:** Crear un layout que cuente con una *Sidebar* para navegación y un área principal dinámica.
3. **Integración Mapas:** Instalar dependencias (`leaflet`, `react-leaflet`) y configurar el componente principal `MapViewer`.
4. **Conexión de API:** Configurar el cliente HTTP apuntando al dominio configurado en Render (o `localhost:8080` para desarrollo) y armar el hook de estado (ej. `useAssets()`) para fetchear los datos.

Este documento sienta las bases para comenzar la implementación visual de forma clara, priorizando el valor del negocio geolocalizado.
