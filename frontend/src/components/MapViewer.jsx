import React, { useState, useEffect } from 'react';
import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';
import Sidebar from './Sidebar';

export default function MapViewer() {
  const [geoData, setGeoData] = useState(null);
  const [selectedAsset, setSelectedAsset] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch assets as GeoJSON
    axios.get('/v1/assets?format=geojson')
      .then(res => {
        setGeoData(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching assets:", err);
        setError("Error loading assets.");
        setLoading(false);
      });
  }, []);

  const onEachFeature = (feature, layer) => {
    if (feature.properties) {
      layer.on({
        click: () => {
          // When an asset is clicked on the map, fetch full details
          axios.get(`/v1/assets/${feature.properties.asset_id}`)
            .then(res => {
              setSelectedAsset(res.data);
            })
            .catch(err => {
              console.error("Error fetching asset details:", err);
              // Fallback to basic info from properties if full fetch fails
              setSelectedAsset(feature.properties);
            });
        }
      });
    }
  };

  return (
    <div style={{ display: 'flex', width: '100%', height: '100%' }}>
      <div style={{ flex: 1, position: 'relative' }}>
        {loading && <div style={{ position: 'absolute', top: 10, left: 10, zIndex: 1000, background: 'white', padding: '10px', borderRadius: '5px' }}>Loading map data...</div>}
        {error && <div style={{ position: 'absolute', top: 10, left: 10, zIndex: 1000, background: '#ffcccc', padding: '10px', borderRadius: '5px' }}>{error}</div>}
        <MapContainer center={[-33.4489, -70.6693]} zoom={11} style={{ height: '100%', width: '100%' }}>
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          {geoData && (
            <GeoJSON
              data={geoData}
              onEachFeature={onEachFeature}
              pointToLayer={(feature, latlng) => {
                // Return a simple circle marker
                return L.circleMarker(latlng, {
                  radius: 6,
                  fillColor: feature.properties.compliance_status === 'VERIFIED_LEGAL' ? '#2ecc71' :
                             feature.properties.compliance_status === 'ZONING_VIOLATION_RISK' ? '#e74c3c' : '#f39c12',
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
