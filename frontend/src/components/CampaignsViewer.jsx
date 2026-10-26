import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { formatPricingStrategy } from '../utils/formatters';

export default function CampaignsViewer() {
  const [faces, setFaces] = useState([]);
  const [loadingFaces, setLoadingFaces] = useState(true);

  const [formData, setFormData] = useState({
    campaign_name: 'Mi Primera Campaña',
    duration_weeks: 4,
    exclude_non_compliant_assets: true,
    pricing_strategy: 'MARKET_AVERAGE_42PCT',
    face_ids: []
  });

  const [simulationResult, setSimulationResult] = useState(null);
  const [loadingSim, setLoadingSim] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // We need some face IDs to select from. We'll fetch all assets and extract faces.
    // In a real large-scale app, we might use a dedicated search faces endpoint.
    axios.get('/v1/assets')
      .then(res => {
        const allFaces = [];
        res.data.forEach(asset => {
          asset.faces.forEach(face => {
            allFaces.push({
              face_id: face.face_id,
              asset_id: asset.asset_id,
              commune_name: asset.location.commune_name,
              media_owner_name: asset.ownership.media_owner_name,
              label: face.face_label,
              tech: face.technology.type
            });
          });
        });
        setFaces(allFaces);
        setLoadingFaces(false);
      })
      .catch(err => {
        console.error("Error fetching faces for campaign:", err);
        setLoadingFaces(false);
      });
  }, []);

  const handleToggleFace = (face_id) => {
    setFormData(prev => {
      const selected = prev.face_ids.includes(face_id)
        ? prev.face_ids.filter(id => id !== face_id)
        : [...prev.face_ids, face_id];
      return { ...prev, face_ids: selected };
    });
  };

  const handleSimulate = (e) => {
    e.preventDefault();
    if (formData.face_ids.length === 0) {
      setError("Debes seleccionar al menos una cara publicitaria.");
      return;
    }

    setError(null);
    setLoadingSim(true);
    setSimulationResult(null);

    axios.post('/v1/campaigns/simulate', formData)
      .then(res => {
        setSimulationResult(res.data);
        setLoadingSim(false);
      })
      .catch(err => {
        console.error("Error simulating campaign:", err);
        setError("Error al simular la campaña. Revisa la consola.");
        setLoadingSim(false);
      });
  };

  return (
    <div style={{ display: 'flex', width: '100%', height: '100%', overflow: 'hidden' }}>

      {/* Left Panel: Form */}
      <div style={{ width: '400px', background: '#f8f9fa', padding: '20px', borderRight: '1px solid #dee2e6', overflowY: 'auto' }}>
        <h2>Simulador de Campañas</h2>
        <p style={{ fontSize: '0.9rem', color: '#555' }}>
          Configura y simula el alcance, costos y cumplimiento legal de tu campaña publicitaria.
        </p>

        <form onSubmit={handleSimulate}>
          <div style={{ marginBottom: '15px' }}>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Nombre de Campaña</label>
            <input
              type="text"
              style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              value={formData.campaign_name}
              onChange={e => setFormData({...formData, campaign_name: e.target.value})}
              required
            />
          </div>

          <div style={{ marginBottom: '15px' }}>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Duración (Semanas)</label>
            <input
              type="number"
              min="1" max="52"
              style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              value={formData.duration_weeks}
              onChange={e => setFormData({...formData, duration_weeks: parseInt(e.target.value)})}
              required
            />
          </div>

          <div style={{ marginBottom: '15px' }}>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Estrategia de Precios (Descuento)</label>
            <select
              style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              value={formData.pricing_strategy}
              onChange={e => setFormData({...formData, pricing_strategy: e.target.value})}
            >
              <option value="LIST_PRICE">{formatPricingStrategy("LIST_PRICE")}</option>
              <option value="CONSERVATIVE_30PCT">{formatPricingStrategy("CONSERVATIVE_30PCT")}</option>
              <option value="MARKET_AVERAGE_42PCT">{formatPricingStrategy("MARKET_AVERAGE_42PCT")}</option>
              <option value="STATE_TENDER_55PCT">{formatPricingStrategy("STATE_TENDER_55PCT")}</option>
            </select>
          </div>

          <div style={{ marginBottom: '20px' }}>
            <label style={{ display: 'flex', alignItems: 'center', fontWeight: 'bold' }}>
              <input
                type="checkbox"
                checked={formData.exclude_non_compliant_assets}
                onChange={e => setFormData({...formData, exclude_non_compliant_assets: e.target.checked})}
                style={{ marginRight: '10px' }}
              />
              Excluir Soportes Ilegales / Clandestinos
            </label>
            <div style={{ fontSize: '0.8rem', color: '#777', marginLeft: '25px', marginTop: '5px' }}>
              Protégete de la responsabilidad solidaria (Ley N° 21.473).
            </div>
          </div>

          <div style={{ marginBottom: '20px' }}>
            <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>
              Seleccionar Caras ({formData.face_ids.length} seleccionadas)
            </label>
            <div style={{ border: '1px solid #ccc', height: '250px', overflowY: 'auto', background: 'white', padding: '10px' }}>
              {loadingFaces ? <p>Cargando inventario...</p> : faces.map(f => (
                <div key={f.face_id} style={{ marginBottom: '5px', display: 'flex', alignItems: 'center', fontSize: '0.85rem' }}>
                  <input
                    type="checkbox"
                    checked={formData.face_ids.includes(f.face_id)}
                    onChange={() => handleToggleFace(f.face_id)}
                    style={{ marginRight: '8px' }}
                  />
                  <span>
                    {f.commune_name} - {f.media_owner_name} ({f.tech}) <br/>
                    <span style={{ color: '#888', fontSize: '0.8rem' }}>{f.face_id}</span>
                  </span>
                </div>
              ))}
            </div>
          </div>

          {error && <div style={{ color: 'red', marginBottom: '15px', fontSize: '0.9rem' }}>{error}</div>}

          <button
            type="submit"
            style={{ width: '100%', padding: '10px', background: '#2c3e50', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer', fontWeight: 'bold' }}
            disabled={loadingSim}
          >
            {loadingSim ? 'Simulando...' : 'Simular Campaña'}
          </button>
        </form>
      </div>

      {/* Right Panel: Results */}
      <div style={{ flex: 1, padding: '30px', overflowY: 'auto', background: '#fff' }}>
        {!simulationResult && !loadingSim && (
          <div style={{ display: 'flex', height: '100%', alignItems: 'center', justifyContent: 'center', color: '#aaa', fontSize: '1.2rem' }}>
            Configura y simula una campaña para ver los resultados aquí.
          </div>
        )}

        {loadingSim && (
          <div style={{ display: 'flex', height: '100%', alignItems: 'center', justifyContent: 'center', color: '#666', fontSize: '1.2rem' }}>
            Procesando simulación...
          </div>
        )}

        {simulationResult && (
          <div>
            <h1 style={{ marginTop: 0, color: '#2c3e50' }}>Resultados: {simulationResult.campaign_name}</h1>

            <div style={{ display: 'flex', gap: '20px', marginBottom: '30px', flexWrap: 'wrap' }}>
              {/* Summary Cards */}
              <div style={{ flex: '1 1 200px', background: '#f8f9fa', padding: '15px', borderRadius: '8px', border: '1px solid #e9ecef' }}>
                <h4 style={{ margin: '0 0 10px 0', color: '#6c757d' }}>Alcance (OTS Bruto)</h4>
                <div style={{ fontSize: '1.8rem', fontWeight: 'bold' }}>{simulationResult.total_ots_gross.toLocaleString('es-CL')}</div>
              </div>
              <div style={{ flex: '1 1 200px', background: '#f8f9fa', padding: '15px', borderRadius: '8px', border: '1px solid #e9ecef' }}>
                <h4 style={{ margin: '0 0 10px 0', color: '#6c757d' }}>Impactos Efectivos (VAC)</h4>
                <div style={{ fontSize: '1.8rem', fontWeight: 'bold', color: '#2980b9' }}>{simulationResult.total_vac_impacts.toLocaleString('es-CL')}</div>
              </div>
              <div style={{ flex: '1 1 200px', background: '#f8f9fa', padding: '15px', borderRadius: '8px', border: '1px solid #e9ecef' }}>
                <h4 style={{ margin: '0 0 10px 0', color: '#6c757d' }}>Inversión Neta (CLP)</h4>
                <div style={{ fontSize: '1.8rem', fontWeight: 'bold', color: '#27ae60' }}>
                  ${simulationResult.financial_projection_clp.total_estimated_net_investment_clp.toLocaleString('es-CL')}
                </div>
              </div>
              <div style={{ flex: '1 1 200px', background: '#f8f9fa', padding: '15px', borderRadius: '8px', border: '1px solid #e9ecef' }}>
                <h4 style={{ margin: '0 0 10px 0', color: '#6c757d' }}>Caras Aprobadas</h4>
                <div style={{ fontSize: '1.8rem', fontWeight: 'bold' }}>
                  {simulationResult.compliant_faces_approved} / {simulationResult.total_faces_evaluated}
                </div>
                {simulationResult.rejected_by_ley_21473_risk > 0 && (
                  <div style={{ color: '#e74c3c', fontSize: '0.85rem', marginTop: '5px' }}>
                    {simulationResult.rejected_by_ley_21473_risk} caras rechazadas por riesgo legal.
                  </div>
                )}
              </div>
            </div>

            <div style={{ display: 'flex', gap: '30px', flexWrap: 'wrap' }}>

              <div style={{ flex: '1 1 400px' }}>
                <h3 style={{ borderBottom: '2px solid #2c3e50', paddingBottom: '5px' }}>Proyección Financiera</h3>
                <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                  <tbody>
                    <tr>
                      <td style={{ padding: '8px 0', borderBottom: '1px solid #eee' }}>Total Precio Lista (Mensualizado):</td>
                      <td style={{ padding: '8px 0', borderBottom: '1px solid #eee', textAlign: 'right', fontWeight: 'bold' }}>
                        ${simulationResult.financial_projection_clp.total_list_price_clp.toLocaleString('es-CL')}
                      </td>
                    </tr>
                    <tr>
                      <td style={{ padding: '8px 0', borderBottom: '1px solid #eee' }}>Descuento Promedio Aplicado:</td>
                      <td style={{ padding: '8px 0', borderBottom: '1px solid #eee', textAlign: 'right', fontWeight: 'bold' }}>
                        {(simulationResult.financial_projection_clp.estimated_negotiated_discount_pct * 100).toFixed(0)}%
                      </td>
                    </tr>
                    <tr>
                      <td style={{ padding: '8px 0', borderBottom: '1px solid #eee' }}>Total Costo Medio Neto:</td>
                      <td style={{ padding: '8px 0', borderBottom: '1px solid #eee', textAlign: 'right', fontWeight: 'bold' }}>
                        ${simulationResult.financial_projection_clp.estimated_net_media_cost_clp.toLocaleString('es-CL')}
                      </td>
                    </tr>
                    <tr>
                      <td style={{ padding: '8px 0', borderBottom: '1px solid #eee' }}>Total Producción:</td>
                      <td style={{ padding: '8px 0', borderBottom: '1px solid #eee', textAlign: 'right', fontWeight: 'bold' }}>
                        ${simulationResult.financial_projection_clp.total_production_cost_clp.toLocaleString('es-CL')}
                      </td>
                    </tr>
                    <tr style={{ background: '#f8f9fa' }}>
                      <td style={{ padding: '10px 5px', fontWeight: 'bold' }}>Inversión Neta Total:</td>
                      <td style={{ padding: '10px 5px', textAlign: 'right', fontWeight: 'bold', color: '#27ae60', fontSize: '1.1rem' }}>
                        ${simulationResult.financial_projection_clp.total_estimated_net_investment_clp.toLocaleString('es-CL')}
                      </td>
                    </tr>
                    <tr>
                      <td style={{ padding: '8px 0', color: '#7f8c8d' }}>CPM (Costo x Mil Impactos Efectivos):</td>
                      <td style={{ padding: '8px 0', textAlign: 'right', color: '#7f8c8d' }}>
                        ${simulationResult.financial_projection_clp.effective_cpm_vac_clp.toLocaleString('es-CL')}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div style={{ flex: '1 1 300px' }}>
                <h3 style={{ borderBottom: '2px solid #2c3e50', paddingBottom: '5px' }}>Desglose por Comuna</h3>
                <ul style={{ listStyle: 'none', padding: 0 }}>
                  {simulationResult.breakdown_by_commune.map((c, i) => (
                    <li key={i} style={{ padding: '8px 0', borderBottom: '1px solid #eee', display: 'flex', justifyContent: 'space-between' }}>
                      <span>{c.commune_name}</span>
                      <span style={{ fontWeight: 'bold' }}>${c.total_net_media_clp.toLocaleString('es-CL')}</span>
                    </li>
                  ))}
                </ul>
              </div>

            </div>

          </div>
        )}
      </div>

    </div>
  );
}
