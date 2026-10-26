import React from 'react';

export default function DocsViewer() {
  return (
    <div style={{ width: '100%', height: '100%' }}>
      <iframe
        src="/docs"
        style={{ width: '100%', height: '100%', border: 'none' }}
        title="API Documentation"
      />
    </div>
  );
}
