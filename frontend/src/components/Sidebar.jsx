import React from 'react';

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
        <h2 style={{ margin: 0, fontSize: '1.2rem' }}>Asset Details</h2>
        <button onClick={onClose} style={{ cursor: 'pointer', border: 'none', background: 'none', fontSize: '1.2rem' }}>&times;</button>
      </div>

      <div style={{ marginBottom: '15px' }}>
        <strong>ID:</strong> {asset.asset_id}
      </div>

      {asset.location && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Location</h3>
          <div><strong>Address:</strong> {asset.location.address_normalized || asset.location.address_raw}</div>
          <div><strong>Commune:</strong> {asset.location.commune_name} ({asset.location.commune_code})</div>
        </div>
      )}

      {asset.structure && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Structure</h3>
          <div><strong>Category:</strong> {asset.structure.category}</div>
          <div><strong>Sub Type:</strong> {asset.structure.sub_type}</div>
        </div>
      )}

      {asset.compliance_audit && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Compliance</h3>
          <div style={{
            padding: '5px 10px',
            borderRadius: '4px',
            background: asset.compliance_audit.status === 'VERIFIED_LEGAL' ? '#d4edda' :
                        asset.compliance_audit.status === 'ZONING_VIOLATION_RISK' ? '#f8d7da' : '#fff3cd',
            color: asset.compliance_audit.status === 'VERIFIED_LEGAL' ? '#155724' :
                   asset.compliance_audit.status === 'ZONING_VIOLATION_RISK' ? '#721c24' : '#856404',
            display: 'inline-block',
            marginBottom: '10px'
          }}>
            <strong>{asset.compliance_audit.status}</strong>
          </div>
          {asset.compliance_audit.risk_flags && asset.compliance_audit.risk_flags.length > 0 && (
            <div>
              <strong>Risk Flags:</strong>
              <ul style={{ margin: '5px 0', paddingLeft: '20px' }}>
                {asset.compliance_audit.risk_flags.map((flag, i) => <li key={i}>{flag}</li>)}
              </ul>
            </div>
          )}
        </div>
      )}

      {asset.ownership && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Ownership</h3>
          <div><strong>Owner:</strong> {asset.ownership.media_owner_name}</div>
        </div>
      )}

      {asset.faces && asset.faces.length > 0 && (
        <div style={{ marginBottom: '15px' }}>
          <h3>Faces ({asset.faces.length})</h3>
          {asset.faces.map(face => (
            <div key={face.face_id} style={{ border: '1px solid #ccc', padding: '10px', marginBottom: '10px', borderRadius: '4px', background: 'white' }}>
              <div><strong>Label:</strong> {face.face_label}</div>
              <div><strong>Tech:</strong> {face.technology.type} ({face.technology.illumination})</div>
              <div><strong>Dimensions:</strong> {face.dimensions.width_m}m x {face.dimensions.height_m}m ({face.dimensions.area_m2} m²)</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
