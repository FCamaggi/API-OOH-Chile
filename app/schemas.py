from typing import Any, Literal, Optional
from pydantic import BaseModel, Field


ComplianceStatus = Literal[
    "VERIFIED_LEGAL",
    "PARTIAL_COMPLIANCE",
    "UNREGISTERED_CLANDESTINE",
    "ZONING_VIOLATION_RISK",
    "EXPIRED_PERMIT",
]

Ley21473Class = Literal["ELEMENTO_MENOR", "ELEMENTO_MAYOR"]

StructureCategory = Literal[
    "STREET_FURNITURE",
    "LARGE_FORMAT_ROADSIDE",
    "TRANSPORT_NETWORK",
    "BUILDING_FACADE",
]

TechType = Literal[
    "DOOH_LED",
    "STATIC_BACKLIGHT",
    "STATIC_PAPER",
    "TRIVISION",
]


class CommuneRM(BaseModel):
    commune_code: str = Field(..., description="Código Único Territorial CUT (ej. 13123)")
    commune_name: str
    province_name: str
    ring_tier: int = Field(..., ge=1, le=4, description="Anillo operativo RM (1 a 4)")
    utm_tax_rate_standard: float = Field(..., description="Derecho semestral estándar en UTM/m2")
    utm_tax_rate_led: float = Field(..., description="Derecho semestral pantallas LED en UTM/m2")
    gis_rest_endpoint: Optional[str] = None


class LocationInfo(BaseModel):
    lat: float
    lng: float
    utm_x: float
    utm_y: float
    srid_geographic: int = 4326
    srid_projected: int = 32719
    address_raw: str
    address_normalized: str
    sii_parcel_rol: Optional[str] = None
    dtpm_stop_code: Optional[str] = None
    commune_code: str
    commune_name: str
    province_name: str
    region_code: str = "RM"
    road_type: str
    highway_kilometer: Optional[float] = None
    speed_limit_kmh: int = 50


class StructureInfo(BaseModel):
    category: StructureCategory
    sub_type: str
    land_regime: Literal["BNUP", "PRIVATE_LOT", "FISCAL_FENCE"]
    total_height_m: float
    installation_date: Optional[str] = None


class OwnershipInfo(BaseModel):
    owner_id: str
    media_owner_name: str
    media_owner_rut: str
    mop_rnavc_status: Literal["ACTIVE", "EXPIRED", "NOT_REGISTERED"]
    commercial_contact: Optional[str] = None
    concession_id: Optional[str] = None
    concession_expiration_date: Optional[str] = None


class DimensionsInfo(BaseModel):
    width_m: float
    height_m: float
    area_m2: float


class TechnologyInfo(BaseModel):
    type: TechType
    illumination: str
    resolution_px: Optional[str] = None
    pixel_pitch_mm: Optional[float] = None
    slot_duration_sec: Optional[int] = None
    loop_slots_total: Optional[int] = None


class AudienceMetricsInfo(BaseModel):
    uoct_hourly_vehicles_avg: Optional[int] = None
    mop_tmda_daily_vehicles: Optional[int] = None
    dtpm_bip_daily_validations: Optional[int] = None
    sectra_occupancy_factor: float = 1.42
    weekly_ots_gross: int
    visibility_index_weight: float
    weekly_vac_impacts: int
    methodology: str = "OPEN_SYNTHETIC_UOCT_ADATRAP_V1"


class CommercialPricingInfo(BaseModel):
    billing_periodicity: Literal["MONTHLY", "WEEKLY", "CAMPAIGN_14D"] = "MONTHLY"
    list_price_clp_monthly: int
    production_cost_clp: int = 0
    estimated_net_discount_pct: float = 0.42
    estimated_net_price_clp: int
    estimated_annual_municipal_tax_clp: int


class FaceItem(BaseModel):
    face_id: str
    face_label: str
    azimuth_degrees: int
    orientation_cardinal: str
    traffic_flow_direction: str
    dimensions: DimensionsInfo
    technology: TechnologyInfo
    audience_metrics: AudienceMetricsInfo
    commercial_pricing: CommercialPricingInfo


class ComplianceAuditInfo(BaseModel):
    status: ComplianceStatus
    ley_21473_class: Ley21473Class
    dom_permit_number: Optional[str] = None
    dom_authorized_area_m2: Optional[float] = None
    municipal_patent_rol: Optional[str] = None
    patent_last_paid_semester: Optional[str] = None
    patent_taxed_area_m2: Optional[float] = None
    mop_vialidad_itf_resolution: Optional[str] = None
    mma_ds1_lum_certified: bool = False
    prc_zone_code: Optional[str] = None
    is_exclusive_residential: bool = False
    distance_to_nearest_hazard_m: Optional[float] = None
    permit_expiration_date: Optional[str] = None
    solidary_liability_risk_level: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    risk_flags: list[str] = Field(default_factory=list)


class SourceLineageItem(BaseModel):
    source_type: str
    reference_id: str
    verified_at: str


class AssetMetadataInfo(BaseModel):
    entity_resolution_confidence: float
    last_scraped_at: str
    last_audited_at: str
    sources: list[SourceLineageItem]


class AssetRecord(BaseModel):
    asset_id: str
    location: LocationInfo
    structure: StructureInfo
    ownership: OwnershipInfo
    faces: list[FaceItem]
    compliance_audit: ComplianceAuditInfo
    metadata: AssetMetadataInfo


class GeoJSONFeature(BaseModel):
    type: Literal["Feature"] = "Feature"
    id: str
    geometry: dict[str, Any]
    properties: dict[str, Any]


class GeoJSONFeatureCollection(BaseModel):
    type: Literal["FeatureCollection"] = "FeatureCollection"
    total_features: int
    features: list[GeoJSONFeature]


class CampaignSimulationRequest(BaseModel):
    campaign_name: str
    duration_weeks: int = Field(default=4, ge=1, le=52)
    exclude_non_compliant_assets: bool = True
    face_ids: list[str]


class CampaignSimulationResponse(BaseModel):
    campaign_name: str
    total_faces_evaluated: int
    compliant_faces_approved: int
    rejected_by_ley_21473_risk: int
    rejected_face_ids: list[str]
    communes_covered: list[str]
    total_ots_gross: int
    total_vac_impacts: int
    financial_projection_clp: dict[str, Any]


class MunicipalInboundRecord(BaseModel):
    record_id: str
    address: str
    sii_parcel_rol: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    owner_rut: Optional[str] = None
    owner_name: Optional[str] = None
    structure_type: str = "MONUMENTAL_LED"
    area_m2: float
    dom_permit_number: Optional[str] = None
    municipal_patent_rol: Optional[str] = None


class MunicipalBatchIngestRequest(BaseModel):
    commune_code: str
    source_type: Literal["DOM_ART16", "RENTAS_PATENTES"]
    records: list[MunicipalInboundRecord]
