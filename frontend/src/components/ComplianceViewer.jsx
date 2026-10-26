import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { formatComplianceStatus, formatRiskFlag } from '../utils/formatters';

export default function ComplianceViewer() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [communes, setCommunes] = useState([]);
  const [selectedCommune, setSelectedCommune] = useState('');

  useEffect(() => {
    axios.get('/v1/territories/communes')
      .then(res => setCommunes(res.data))
      .catch(err => console.error("Error fetching communes:", err));
  }, []);

  useEffect(() => {
    fetchDiscrepancies();
  }, [selectedCommune]);

  const fetchDiscrepancies = () => {
    setLoading(true);
    const params = selectedCommune ? `?commune_code=${selectedCommune}` : '';
    axios.get(`/v1/compliance/discrepancies${params}`)
      .then(res => {
        setData(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching compliance data:", err);
        setError("Error al cargar los datos de auditoría.");
        setLoading(false);
      });
  };

  const handleExport = () => {
    const params = selectedCommune ? `?commune_code=${selectedCommune}` : '';
    window.open(`/v1/compliance/discrepancies/export${params}`, '_blank');
  };

  return (
    <div style={{ padding: '30px', width: '100%', height: '100%', overflowY: 'auto', boxSizing: 'border-box', background: '#f4f6f8' }}>
      <div style={{ maxWidth: '1200px', margin: '0 auto' }}>

        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
          <div>
            <h1 style={{ margin: '0 0 10px 0', color: '#2c3e50' }}>Auditoría y Cumplimiento Legal (Ley N° 21.473)</h1>
            <p style={{ margin: 0, color: '#555' }}>
              Detecta soportes clandestinos, sin permiso DOM o con subdeclaración de m² afectos a impuestos.
            </p>
          </div>
          <button
            onClick={handleExport}
            style={{ padding: '10px 20px', background: '#27ae60', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}
          >
            Exportar CSV
          </button>
        </div>

        <div style={{ marginBottom: '20px', background: 'white', padding: '15px', borderRadius: '8px', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' }}>
          <label style={{ fontWeight: 'bold', marginRight: '10px' }}>Filtrar por Comuna:</label>
          <select
            value={selectedCommune}
            onChange={(e) => setSelectedCommune(e.target.value)}
            style={{ padding: '8px', borderRadius: '4px', border: '1px solid #ccc', minWidth: '200px' }}
          >
            <option value="">Toda la Región Metropolitana</option>
            {communes.map(c => (
              <option key={c.commune_code} value={c.commune_code}>{c.commune_name}</option>
            ))}
          </select>
        </div>

        {loading && <div style={{ textAlign: 'center', padding: '50px', fontSize: '1.2rem', color: '#666' }}>Analizando registros...</div>}
        {error && <div style={{ color: 'red', marginBottom: '15px' }}>{error}</div>}

        {data && !loading && (
          <>
            {/* Dashboard Summary */}
            <div style={{ display: 'flex', gap: '20px', marginBottom: '30px' }}>
              <div style={{ flex: 1, background: 'white', padding: '20px', borderRadius: '8px', borderLeft: '5px solid #e74c3c', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' }}>
                <h4 style={{ margin: '0 0 10px 0', color: '#6c757d' }}>Total Discrepancias</h4>
                <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#2c3e50' }}>
                  {data.query_context.total_discrepancies_found}
                </div>
              </div>
              <div style={{ flex: 1, background: 'white', padding: '20px', borderRadius: '8px', borderLeft: '5px solid #f39c12', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' }}>
                <h4 style={{ margin: '0 0 10px 0', color: '#6c757d' }}>Evasión Estimada Anual (CLP)</h4>
                <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#2c3e50' }}>
                  ${data.query_context.estimated_annual_uncollected_tax_clp.toLocaleString('es-CL')}
                </div>
              </div>
              <div style={{ flex: 1, background: 'white', padding: '20px', borderRadius: '8px', borderLeft: '5px solid #3498db', boxShadow: '0 1px 3px rgba(0,0,0,0.1)' }}>
                <h4 style={{ margin: '0 0 10px 0', color: '#6c757d' }}>Evasión Estimada Anual (UTM)</h4>
                <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#2c3e50' }}>
                  {data.query_context.estimated_annual_uncollected_tax_utm.toLocaleString('es-CL')} UTM
                </div>
              </div>
            </div>

            {/* Table */}
            <div style={{ background: 'white', borderRadius: '8px', boxShadow: '0 1px 3px rgba(0,0,0,0.1)', overflow: 'hidden' }}>
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                  <thead style={{ background: '#f8f9fa', borderBottom: '2px solid #dee2e6' }}>
                    <tr>
                      <th style={{ padding: '12px 15px', color: '#495057' }}>ID Soporte</th>
                      <th style={{ padding: '12px 15px', color: '#495057' }}>Comuna</th>
                      <th style={{ padding: '12px 15px', color: '#495057' }}>Exhibidor</th>
                      <th style={{ padding: '12px 15px', color: '#495057' }}>Estado Legal</th>
                      <th style={{ padding: '12px 15px', color: '#495057' }}>Área (m²) / Subdeclarada</th>
                      <th style={{ padding: '12px 15px', color: '#495057' }}>Riesgos Principales</th>
                    </tr>
                  </thead>
                  <tbody>
                    {data.items.length === 0 ? (
                      <tr>
                        <td colSpan="6" style={{ padding: '20px', textAlign: 'center', color: '#777' }}>
                          No se encontraron discrepancias para los filtros seleccionados.
                        </td>
                      </tr>
                    ) : (
                      data.items.map(item => (
                        <tr key={item.asset_id} style={{ borderBottom: '1px solid #eee' }}>
                          <td style={{ padding: '12px 15px', fontFamily: 'monospace', fontSize: '0.85rem' }}>{item.asset_id}</td>
                          <td style={{ padding: '12px 15px' }}>{item.commune_name}</td>
                          <td style={{ padding: '12px 15px' }}>{item.media_owner_name}</td>
                          <td style={{ padding: '12px 15px' }}>
                            <span style={{
                              background: (item.compliance_status === 'ZONING_VIOLATION_RISK' || item.compliance_status === 'UNREGISTERED_CLANDESTINE') ? '#f8d7da' : '#fff3cd',
                              color: (item.compliance_status === 'ZONING_VIOLATION_RISK' || item.compliance_status === 'UNREGISTERED_CLANDESTINE') ? '#721c24' : '#856404',
                              padding: '3px 8px',
                              borderRadius: '12px',
                              fontSize: '0.8rem',
                              fontWeight: 'bold'
                            }}>
                              {formatComplianceStatus(item.compliance_status)}
                            </span>
                          </td>
                          <td style={{ padding: '12px 15px' }}>
                            {item.commercial_area_m2} m²
                            {item.discrepancy_details.undeclared_area_m2 > 0 && (
                              <span style={{ color: '#e74c3c', marginLeft: '5px', fontWeight: 'bold' }}>
                                (+{item.discrepancy_details.undeclared_area_m2} m² no declarados)
                              </span>
                            )}
                          </td>
                          <td style={{ padding: '12px 15px', fontSize: '0.85rem', color: '#c0392b' }}>
                            <ul style={{ margin: 0, paddingLeft: '15px' }}>
                              {item.discrepancy_details.risk_flags.map((flag, i) => (
                                <li key={i}>{formatRiskFlag(flag)}</li>
                              ))}
                            </ul>
                          </td>
                        </tr>
                      ))
                    )}
                  </tbody>
                </table>
              </div>
            </div>
          </>
        )}

      </div>
    </div>
  );
}
