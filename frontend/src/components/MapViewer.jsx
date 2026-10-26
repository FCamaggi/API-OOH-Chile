import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, GeoJSON, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';
import Sidebar from './Sidebar';

export default function MapViewer() {
  const [geoData, setGeoData] = useState(null);
  const [selectedAsset, setSelectedAsset] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Filter states
  const [communes, setCommunes] = useState([]);
  const [filters, setFilters] = useState({
    commune_code: '',
    structure_category: '',
    tech_type: '',
    compliance_status: ''
  });

  useEffect(() => {
    // Fetch communes for the filter dropdown
    axios.get('/v1/territories/communes')
      .then(res => setCommunes(res.data))
      .catch(err => console.error("Error fetching communes:", err));
  }, []);

  useEffect(() => {
    setLoading(true);
    // Build query params
    const params = new URLSearchParams();
    params.append('format', 'geojson');
    if (filters.commune_code) params.append('commune_code', filters.commune_code);
    if (filters.structure_category) params.append('structure_category', filters.structure_category);
    if (filters.tech_type) params.append('tech_type', filters.tech_type);
    if (filters.compliance_status) params.append('compliance_status', filters.compliance_status);

    axios.get(`/v1/assets?${params.toString()}`)
      .then(res => {
        setGeoData(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching assets:", err);
        setError("Error loading assets.");
        setLoading(false);
      });
  }, [filters]);

  const onEachFeature = (feature, layer) => {
    if (feature.properties) {
      layer.on({
        click: () => {
          axios.get(`/v1/assets/${feature.properties.asset_id}`)
            .then(res => setSelectedAsset(res.data))
            .catch(err => setSelectedAsset(feature.properties));
        }
      });
    }
  };

  return (
    <div style={{ display: 'flex', width: '100%', height: '100%' }}>
      {/* Filters Panel */}
      <div style={{ width: '250px', background: '#f8f9fa', padding: '15px', borderRight: '1px solid #dee2e6', overflowY: 'auto' }}>
        <h3>Filtros de Búsqueda</h3>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontSize: '0.9rem', fontWeight: 'bold' }}>Comuna</label>
          <select
            style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
            value={filters.commune_code}
            onChange={(e) => setFilters(prev => ({ ...prev, commune_code: e.target.value }))}
          >
            <option value="">Todas las comunas</option>
            {communes.map(c => (
              <option key={c.commune_code} value={c.commune_code}>{c.commune_name}</option>
            ))}
          </select>
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontSize: '0.9rem', fontWeight: 'bold' }}>Categoría de Estructura</label>
          <select
            style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
            value={filters.structure_category}
            onChange={(e) => setFilters(prev => ({ ...prev, structure_category: e.target.value }))}
          >
            <option value="">Todas</option>
            <option value="STREET_FURNITURE">Mobiliario Urbano</option>
            <option value="LARGE_FORMAT_ROADSIDE">Gran Formato en Ruta</option>
            <option value="TRANSPORT_NETWORK">Red de Transporte</option>
            <option value="BUILDING_FACADE">Fachada de Edificio</option>
          </select>
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontSize: '0.9rem', fontWeight: 'bold' }}>Tecnología</label>
          <select
            style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
            value={filters.tech_type}
            onChange={(e) => setFilters(prev => ({ ...prev, tech_type: e.target.value }))}
          >
            <option value="">Todas</option>
            <option value="DOOH_LED">LED / Digital</option>
            <option value="STATIC_BACKLIGHT">Estático Iluminado (Backlight)</option>
            <option value="STATIC_PAPER">Estático (Papel/Tela)</option>
            <option value="TRIVISION">Trivisión</option>
          </select>
        </div>

        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px', fontSize: '0.9rem', fontWeight: 'bold' }}>Estado Legal (Compliance)</label>
          <select
            style={{ width: '100%', padding: '8px', borderRadius: '4px', border: '1px solid #ccc' }}
            value={filters.compliance_status}
            onChange={(e) => setFilters(prev => ({ ...prev, compliance_status: e.target.value }))}
          >
            <option value="">Todos</option>
            <option value="VERIFIED_LEGAL">Verificado (Legal)</option>
            <option value="PARTIAL_COMPLIANCE">Cumplimiento Parcial</option>
            <option value="UNREGISTERED_CLANDESTINE">No Registrado / Clandestino</option>
            <option value="ZONING_VIOLATION_RISK">Riesgo de Violación de Zona</option>
            <option value="EXPIRED_PERMIT">Permiso Expirado</option>
          </select>
        </div>

        <div style={{ fontSize: '0.85rem', color: '#666', marginTop: '20px' }}>
          Mostrando {geoData?.total_features || 0} activos.
        </div>
      </div>

      {/* Map Area */}
      <div style={{ flex: 1, position: 'relative' }}>
        {loading && <div style={{ position: 'absolute', top: 10, left: '50%', transform: 'translateX(-50%)', zIndex: 1000, background: 'rgba(255,255,255,0.9)', padding: '5px 15px', borderRadius: '20px', boxShadow: '0 2px 5px rgba(0,0,0,0.2)' }}>Cargando datos del mapa...</div>}
        {error && <div style={{ position: 'absolute', top: 10, left: 10, zIndex: 1000, background: '#ffcccc', padding: '10px', borderRadius: '5px' }}>{error}</div>}
        <MapContainer center={[-33.4489, -70.6693]} zoom={11} style={{ height: '100%', width: '100%' }}>
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {geoData && geoData.features && geoData.features.length > 0 && (
            <GeoJSON
              key={JSON.stringify(filters)} // Force re-render of GeoJSON when filters change
              data={geoData}
              onEachFeature={onEachFeature}
              pointToLayer={(feature, latlng) => {
                let color = '#f39c12';
                if (feature.properties.compliance_status === 'VERIFIED_LEGAL') color = '#2ecc71';
                else if (feature.properties.compliance_status === 'ZONING_VIOLATION_RISK' || feature.properties.compliance_status === 'UNREGISTERED_CLANDESTINE') color = '#e74c3c';

                return L.circleMarker(latlng, {
                  radius: 6,
                  fillColor: color,
                  color: '#000',
                  weight: 1,
                  opacity: 1,
                  fillOpacity: 0.8
                });
              }}
            />
          )}
        </MapContainer>
      </div>
      <Sidebar asset={selectedAsset} onClose={() => setSelectedAsset(null)} />
    </div>
  );
}
