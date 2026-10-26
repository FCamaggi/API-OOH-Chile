import pytest
from app.schemas import (
    AssetRecord, FaceItem, LocationInfo, StructureInfo, OwnershipInfo,
    ComplianceAuditInfo, AssetMetadataInfo, DimensionsInfo, TechnologyInfo,
    AudienceMetricsInfo, CommercialPricingInfo
)
from app.services.regulatory_validator import evaluate_ley_21473_restrictions

@pytest.fixture
def base_asset():
    location = LocationInfo(
        lat=-33.4569, lng=-70.6483, utm_x=346513.0, utm_y=6296723.0,
        address_raw="Av. Libertador Bernardo O'Higgins",
        address_normalized="AVENIDA LIBERTADOR BERNARDO OHIGGINS",
        commune_code="13101", commune_name="SANTIAGO",
        province_name="SANTIAGO", road_type="LOCAL", speed_limit_kmh=50
    )
    structure = StructureInfo(
        category="LARGE_FORMAT_ROADSIDE", sub_type="MONOPOL",
        land_regime="PRIVATE_LOT", total_height_m=12.5
    )
    ownership = OwnershipInfo(
        owner_id="OWNER_123", media_owner_name="Test Media",
        media_owner_rut="76.123.456-7", mop_rnavc_status="ACTIVE"
    )
    compliance_audit = ComplianceAuditInfo(
        status="VERIFIED_LEGAL", ley_21473_class="ELEMENTO_MAYOR",
        is_exclusive_residential=False, distance_to_nearest_hazard_m=50.0,
        solidary_liability_risk_level="LOW", risk_flags=[]
    )
    metadata = AssetMetadataInfo(
        entity_resolution_confidence=0.9, last_scraped_at="2023-01-01T00:00:00Z",
        last_audited_at="2023-01-01T00:00:00Z", sources=[]
    )
    return AssetRecord(
        asset_id="ASSET_TEST", location=location, structure=structure,
        ownership=ownership, faces=[], compliance_audit=compliance_audit,
        metadata=metadata
    )

@pytest.fixture
def led_face():
    dimensions = DimensionsInfo(width_m=4.0, height_m=3.0, area_m2=12.0)
    technology = TechnologyInfo(type="DOOH_LED", illumination="INTERNAL")
    audience_metrics = AudienceMetricsInfo(weekly_ots_gross=1000, visibility_index_weight=0.8, weekly_vac_impacts=800)
    commercial_pricing = CommercialPricingInfo(list_price_clp_monthly=1000000, estimated_net_price_clp=580000, estimated_annual_municipal_tax_clp=100000)
    return FaceItem(
        face_id="FACE_LED", face_label="A", azimuth_degrees=90,
        orientation_cardinal="E", traffic_flow_direction="W_TO_E",
        dimensions=dimensions, technology=technology,
        audience_metrics=audience_metrics, commercial_pricing=commercial_pricing
    )

@pytest.fixture
def static_face():
    dimensions = DimensionsInfo(width_m=4.0, height_m=3.0, area_m2=12.0)
    technology = TechnologyInfo(type="STATIC_BACKLIGHT", illumination="FRONTAL")
    audience_metrics = AudienceMetricsInfo(weekly_ots_gross=1000, visibility_index_weight=0.8, weekly_vac_impacts=800)
    commercial_pricing = CommercialPricingInfo(list_price_clp_monthly=500000, estimated_net_price_clp=290000, estimated_annual_municipal_tax_clp=50000)
    return FaceItem(
        face_id="FACE_STATIC", face_label="B", azimuth_degrees=270,
        orientation_cardinal="W", traffic_flow_direction="E_TO_W",
        dimensions=dimensions, technology=technology,
        audience_metrics=audience_metrics, commercial_pricing=commercial_pricing
    )


def test_condition_1_led_in_residential(base_asset, led_face):
    base_asset.compliance_audit.is_exclusive_residential = True
    new_asset = evaluate_ley_21473_restrictions(base_asset, [led_face])

    assert "PROHIBITED_LED_IN_RESIDENTIAL_ZONE_ART28" in new_asset.compliance_audit.risk_flags
    assert new_asset.compliance_audit.status == "ZONING_VIOLATION_RISK"

def test_no_condition_1_static_in_residential(base_asset, static_face):
    base_asset.compliance_audit.is_exclusive_residential = True
    new_asset = evaluate_ley_21473_restrictions(base_asset, [static_face])

    assert "PROHIBITED_LED_IN_RESIDENTIAL_ZONE_ART28" not in new_asset.compliance_audit.risk_flags
    assert new_asset.compliance_audit.status == "VERIFIED_LEGAL"

def test_no_condition_1_led_not_residential(base_asset, led_face):
    base_asset.compliance_audit.is_exclusive_residential = False
    new_asset = evaluate_ley_21473_restrictions(base_asset, [led_face])

    assert "PROHIBITED_LED_IN_RESIDENTIAL_ZONE_ART28" not in new_asset.compliance_audit.risk_flags
    assert new_asset.compliance_audit.status == "VERIFIED_LEGAL"

def test_condition_2_hazard_proximity_highway(base_asset, static_face):
    base_asset.location.road_type = "HIGHWAY_CONCESSION"
    base_asset.compliance_audit.distance_to_nearest_hazard_m = 39.9
    new_asset = evaluate_ley_21473_restrictions(base_asset, [static_face])

    assert "HAZARD_PROXIMITY_LT_40M_DECRETO24" in new_asset.compliance_audit.risk_flags

def test_condition_2_hazard_proximity_interurban(base_asset, static_face):
    base_asset.location.road_type = "INTERURBAN_ROUTE"
    base_asset.compliance_audit.distance_to_nearest_hazard_m = 15.0
    new_asset = evaluate_ley_21473_restrictions(base_asset, [static_face])

    assert "HAZARD_PROXIMITY_LT_40M_DECRETO24" in new_asset.compliance_audit.risk_flags

def test_no_condition_2_distance_40_or_more(base_asset, static_face):
    base_asset.location.road_type = "HIGHWAY_CONCESSION"
    base_asset.compliance_audit.distance_to_nearest_hazard_m = 40.0
    new_asset = evaluate_ley_21473_restrictions(base_asset, [static_face])

    assert "HAZARD_PROXIMITY_LT_40M_DECRETO24" not in new_asset.compliance_audit.risk_flags

def test_no_condition_2_wrong_road_type(base_asset, static_face):
    base_asset.location.road_type = "LOCAL"
    base_asset.compliance_audit.distance_to_nearest_hazard_m = 10.0
    new_asset = evaluate_ley_21473_restrictions(base_asset, [static_face])

    assert "HAZARD_PROXIMITY_LT_40M_DECRETO24" not in new_asset.compliance_audit.risk_flags

def test_no_condition_2_distance_none(base_asset, static_face):
    base_asset.location.road_type = "HIGHWAY_CONCESSION"
    base_asset.compliance_audit.distance_to_nearest_hazard_m = None
    new_asset = evaluate_ley_21473_restrictions(base_asset, [static_face])

    assert "HAZARD_PROXIMITY_LT_40M_DECRETO24" not in new_asset.compliance_audit.risk_flags

def test_both_conditions(base_asset, led_face):
    base_asset.compliance_audit.is_exclusive_residential = True
    base_asset.location.road_type = "HIGHWAY_CONCESSION"
    base_asset.compliance_audit.distance_to_nearest_hazard_m = 20.0

    new_asset = evaluate_ley_21473_restrictions(base_asset, [led_face])

    assert "PROHIBITED_LED_IN_RESIDENTIAL_ZONE_ART28" in new_asset.compliance_audit.risk_flags
    assert "HAZARD_PROXIMITY_LT_40M_DECRETO24" in new_asset.compliance_audit.risk_flags
    assert new_asset.compliance_audit.status == "ZONING_VIOLATION_RISK"
