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

export const formatStructureSubType = (subType) => {
  const map = {
    'MONUMENTAL_LED': 'Monumental LED',
    'LED_SCREEN': 'Pantalla LED',
    'DIGITAL_MUPI': 'MUPI Digital',
    'STATIC_MUPI': 'MUPI Estático',
    'MINI_PALETA': 'Mini Paleta',
    'STATIC_BILLBOARD': 'Letrero Estático',
    'BUS_STOP_SHELTER': 'Refugio Peatonal',
    'WALL_MURAL': 'Mural en Fachada',
    'GIGA_BANNER': 'Tela Gigante (Giga Banner)',
  };
  return map[subType] || subType;
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

export const formatIllumination = (illumination) => {
  const map = {
    'SELF_EMISSIVE_LED': 'LED Auto-emisivo',
    'EXTERNAL_SPOTLIGHT': 'Iluminación Externa (Focos)',
    'INTERNAL_BACKLIGHT': 'Retroiluminación (Backlight)',
    'UNILLUMINATED': 'Sin Iluminación',
  };
  return map[illumination] || illumination;
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
    'UNREGISTERED_IN_DOM_AND_RENTAS': 'No Registrado en DOM ni Rentas',
    'MISSING_MOP_ITF_RUTA_68': 'Falta Informe MOP para Ruta 68',
    'HAZARD_PROXIMITY_LT_40M_DECRETO24': 'Proximidad a Peligro (< 40m, Decreto 24)',
    'MISSING_MOP_CONCESSION_INSPECTION_CERT': 'Falta Certificado de Inspección de Concesión MOP',
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
