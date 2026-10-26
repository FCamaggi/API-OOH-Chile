import React from 'react';
import { HashRouter as Router, Routes, Route, Link } from 'react-router-dom';
import MapViewer from './components/MapViewer';
import DocsViewer from './components/DocsViewer';
import './main.css';

function App() {
  return (
    <Router>
      <div style={{ display: 'flex', flexDirection: 'column', height: '100vh', margin: 0, fontFamily: 'sans-serif' }}>
        <header style={{ background: '#2c3e50', color: 'white', padding: '1rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h1 style={{ margin: 0, fontSize: '1.5rem' }}>API OOH Chile</h1>
          <nav>
            <Link to="/" style={{ color: 'white', textDecoration: 'none', marginRight: '1rem' }}>Map</Link>
            <Link to="/docs" style={{ color: 'white', textDecoration: 'none' }}>API Docs</Link>
          </nav>
        </header>
        <main style={{ flex: 1, display: 'flex', position: 'relative' }}>
          <Routes>
            <Route path="/" element={<MapViewer />} />
            <Route path="/docs" element={<DocsViewer />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
