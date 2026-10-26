// formatters.js

export const formatComplianceStatus = (status) => {
  const map = {
    'VERIFIED_LEGAL': 'Verificado (Legal)',
    'PARTIAL_COMPLIANCE': 'Cumplimiento Parcial',
    'UNREGISTERED_CLANDESTINE': 'No Registrado / Clandestino',
    'ZONING_VIOLATION_RISK': 'Riesgo de Violación de Zona',
    'EXPIRED_PERMIT': 'Permiso Expirado',
  };
  return map[status] || status;
};

export const formatStructureCategory = (category) => {
  const map = {
    'STREET_FURNITURE': 'Mobiliario Urbano',
    'LARGE_FORMAT_ROADSIDE': 'Gran Formato en Ruta',
    'TRANSPORT_NETWORK': 'Red de Transporte',
    'BUILDING_FACADE': 'Fachada de Edificio',
  };
  return map[category] || category;
};

export const formatTechType = (type) => {
  const map = {
    'DOOH_LED': 'LED / Digital',
    'STATIC_BACKLIGHT': 'Estático Iluminado (Backlight)',
    'STATIC_PAPER': 'Estático (Papel/Tela)',
    'TRIVISION': 'Trivisión',
  };
  return map[type] || type;
};

export const formatRiskFlag = (flag) => {
  const map = {
    'MISSING_DOM_OBRA_MENOR_PERMIT': 'Falta Permiso de Obra Menor (DOM)',
    'MISSING_MUNICIPAL_PATENT_PAYMENT': 'Falta Pago de Patente Municipal',
    'AREA_SUBDECLARATION_GT_15PCT': 'Subdeclaración de Área > 15%',
    'RESIDENTIAL_EXCLUSIVE_ZONE_VIOLATION': 'Violación de Zona Exclusiva Residencial',
    'UNAUTHORIZED_LED_ILLUMINATION': 'Iluminación LED No Autorizada',
    'MISSING_MOP_ITF_RESOLUTION': 'Falta Resolución MOP ITF',
    'EXPIRED_DOM_PERMIT': 'Permiso DOM Expirado',
  };
  return map[flag] || flag;
};

export const formatPricingStrategy = (strategy) => {
  const map = {
    'LIST_PRICE': 'Precio de Lista (Sin Descuento)',
    'CONSERVATIVE_30PCT': 'Conservador (30% Descuento)',
    'MARKET_AVERAGE_42PCT': 'Promedio de Mercado (42% Descuento)',
    'STATE_TENDER_55PCT': 'Licitación Estatal (55% Descuento)',
  };
  return map[strategy] || strategy;
};

export const formatLiabilityRiskLevel = (level) => {
  const map = {
    'LOW': 'Bajo',
    'MEDIUM': 'Medio',
    'HIGH': 'Alto',
    'CRITICAL': 'Crítico'
  };
  return map[level] || level;
};
