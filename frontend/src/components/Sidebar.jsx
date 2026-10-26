import React from 'react';
import {
  formatComplianceStatus,
  formatStructureCategory,
  formatStructureSubType,
  formatTechType,
  formatIllumination,
  formatRiskFlag
} from '../utils/formatters';

export default function Sidebar({ asset, onClose }) {
  if (!asset) return null;

  return (
    <div style={{
      width: '350px',
      background: '#f8f9fa',
      borderLeft: '1px solid #dee2e6',
      padding: '20px',
      overflowY: 'auto',
      boxShadow: '-2px 0 5px rgba(0,0,0,0.1)'
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <h2 style={{ margin: 0, fontSize: '1.2rem' }}>Detalles del Soporte</h2>
        <button onClick={onClose} style={{ cursor: 'pointer', border: 'none', background: 'none', fontSize: '1.2rem' }}>&times;</button>
      </div>

      <div style={{ marginBottom: '15px' }}>
        <strong>ID:</strong> <span style={{ fontSize: '0.85em', fontFamily: 'monospace' }}>{asset.asset_id}</span>
      </div>

      {asset.location && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Ubicación</h3>
          <div><strong>Dirección:</strong> {asset.location.address_normalized || asset.location.address_raw}</div>
          <div><strong>Comuna:</strong> {asset.location.commune_name}</div>
        </div>
      )}

      {asset.structure && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Estructura</h3>
          <div><strong>Categoría:</strong> {formatStructureCategory(asset.structure.category || asset.structure_category)}</div>
          <div><strong>Subtipo:</strong> {formatStructureSubType(asset.structure.sub_type || asset.sub_type)}</div>
        </div>
      )}

      {asset.compliance_audit && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Estado Legal (Compliance)</h3>
          <div style={{
            padding: '5px 10px',
            borderRadius: '4px',
            background: asset.compliance_audit.status === 'VERIFIED_LEGAL' ? '#d4edda' :
                        (asset.compliance_audit.status === 'ZONING_VIOLATION_RISK' || asset.compliance_audit.status === 'UNREGISTERED_CLANDESTINE') ? '#f8d7da' : '#fff3cd',
            color: asset.compliance_audit.status === 'VERIFIED_LEGAL' ? '#155724' :
                   (asset.compliance_audit.status === 'ZONING_VIOLATION_RISK' || asset.compliance_audit.status === 'UNREGISTERED_CLANDESTINE') ? '#721c24' : '#856404',
            display: 'inline-block',
            marginBottom: '10px'
          }}>
            <strong>{formatComplianceStatus(asset.compliance_audit.status)}</strong>
          </div>
          {asset.compliance_audit.risk_flags && asset.compliance_audit.risk_flags.length > 0 && (
            <div>
              <strong>Riesgos detectados:</strong>
              <ul style={{ margin: '5px 0', paddingLeft: '20px', color: '#c0392b' }}>
                {asset.compliance_audit.risk_flags.map((flag, i) => <li key={i}>{formatRiskFlag(flag)}</li>)}
              </ul>
            </div>
          )}
        </div>
      )}

      {/* Fallback properties when viewing GeoJSON properties directly (if full fetch failed or hasn't loaded) */}
      {!asset.compliance_audit && asset.compliance_status && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Estado Legal (Compliance)</h3>
          <div style={{
            padding: '5px 10px',
            borderRadius: '4px',
            background: asset.compliance_status === 'VERIFIED_LEGAL' ? '#d4edda' :
                        (asset.compliance_status === 'ZONING_VIOLATION_RISK' || asset.compliance_status === 'UNREGISTERED_CLANDESTINE') ? '#f8d7da' : '#fff3cd',
            color: asset.compliance_status === 'VERIFIED_LEGAL' ? '#155724' :
                   (asset.compliance_status === 'ZONING_VIOLATION_RISK' || asset.compliance_status === 'UNREGISTERED_CLANDESTINE') ? '#721c24' : '#856404',
            display: 'inline-block',
            marginBottom: '10px'
          }}>
            <strong>{formatComplianceStatus(asset.compliance_status)}</strong>
          </div>
        </div>
      )}

      {asset.ownership && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Propiedad</h3>
          <div><strong>Exhibidor (Dueño):</strong> {asset.ownership.media_owner_name}</div>
        </div>
      )}

      {asset.faces && asset.faces.length > 0 && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Caras Publicitarias ({asset.faces.length})</h3>
          {asset.faces.map(face => (
            <div key={face.face_id} style={{ border: '1px solid #ddd', padding: '10px', marginBottom: '10px', borderRadius: '6px', background: 'white' }}>
              <div><strong>Orientación:</strong> {face.face_label}</div>
              <div><strong>Tecnología:</strong> {formatTechType(face.technology.type)} ({formatIllumination(face.technology.illumination)})</div>
              <div><strong>Dimensiones:</strong> {face.dimensions.width_m}m x {face.dimensions.height_m}m ({face.dimensions.area_m2} m²)</div>
              {face.commercial_pricing && (
                <div style={{ marginTop: '5px', fontSize: '0.9em', color: '#555' }}>
                  <strong>Precio Lista Mensual:</strong> ${face.commercial_pricing.list_price_clp_monthly.toLocaleString('es-CL')}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
