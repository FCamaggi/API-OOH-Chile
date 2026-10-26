import React from 'react';
import { HashRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import MapViewer from './components/MapViewer';
import DocsViewer from './components/DocsViewer';
import CampaignsViewer from './components/CampaignsViewer';
import ComplianceViewer from './components/ComplianceViewer';
import './main.css';

// A simple helper component for navigation links to highlight active route
function NavLink({ to, children }) {
  const location = useLocation();
  const isActive = location.pathname === to;
  return (
    <Link
      to={to}
      style={{
        color: isActive ? '#ecf0f1' : '#95a5a6',
        textDecoration: 'none',
        marginRight: '1.5rem',
        fontWeight: isActive ? 'bold' : 'normal',
        borderBottom: isActive ? '2px solid #ecf0f1' : 'none',
        paddingBottom: '4px'
      }}
    >
      {children}
    </Link>
  );
}

function App() {
  return (
    <Router>
      <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', margin: 0, fontFamily: 'sans-serif' }}>
        <header style={{ background: '#2c3e50', color: 'white', padding: '1rem 2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <h1 style={{ margin: 0, fontSize: '1.5rem', marginRight: '3rem' }}>API OOH Chile</h1>
            <nav style={{ display: 'flex', alignItems: 'center', marginTop: '4px' }}>
              <NavLink to="/">Explorar Mapa</NavLink>
              <NavLink to="/campaigns">Simulador de Campañas</NavLink>
              <NavLink to="/compliance">Auditoría (Ley N° 21.473)</NavLink>
              <NavLink to="/docs">API Docs</NavLink>
            </nav>
          </div>
        </header>
        <main style={{ flex: 1, display: 'flex', position: 'relative', overflow: 'hidden' }}>
          <Routes>
            <Route path="/" element={<MapViewer />} />
            <Route path="/campaigns" element={<CampaignsViewer />} />
            <Route path="/compliance" element={<ComplianceViewer />} />
            <Route path="/docs" element={<DocsViewer />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
