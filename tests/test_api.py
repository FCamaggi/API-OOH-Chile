"""
Suite de pruebas determinista y autocontenida (0 dependencias externas de red o DB).
Diseñada para ejecutarse en < 1 segundo tanto localmente como en Google Jules.
"""
from fastapi.testclient import TestClient
from app.main import app
from app.services.audience_engine import compute_open_audience_metrics
from app.services.entity_resolution import (
    compute_composite_match_score,
    normalize_chilean_address,
)

client = TestClient(app)


def test_health_and_52_rm_communes_loaded() -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["rm_communes_loaded"] == 52


def test_list_communes_by_ring_tier() -> None:
    resp = client.get("/v1/territories/communes?ring_tier=1")
    assert resp.status_code == 200
    ring1 = resp.json()
    assert len(ring1) == 6
    names = {c["commune_name"] for c in ring1}
    assert "Providencia" in names
    assert "Las Condes" in names


def test_get_assets_json_and_geojson_rfc7946() -> None:
    resp_json = client.get("/v1/assets?commune_code=13123")
    assert resp_json.status_code == 200
    items = resp_json.json()
    assert len(items) == 1
    assert items[0]["asset_id"] == "CL-RM-PROV-00482"

    resp_geo = client.get("/v1/assets?format=geojson")
    assert resp_geo.status_code == 200
    fc = resp_geo.json()
    assert fc["type"] == "FeatureCollection"
    assert fc["total_features"] >= 4
    first_feat = fc["features"][0]
    assert first_feat["geometry"]["type"] == "Point"
    assert len(first_feat["geometry"]["coordinates"]) == 2


def test_compliance_discrepancies_ley_21473() -> None:
    resp = client.get("/v1/compliance/discrepancies?commune_code=13107")
    assert resp.status_code == 200
    body = resp.json()
    assert body["query_context"]["total_discrepancies_found"] == 1
    assert body["query_context"]["estimated_annual_uncollected_tax_utm"] > 0
    item = body["items"][0]
    assert item["asset_id"] == "CL-RM-HUEC-00109"
    assert "AREA_SUBDECLARATION_GT_15PCT" in item["discrepancy_details"]["risk_flags"]


def test_export_compliance_discrepancies_csv() -> None:
    resp = client.get("/v1/compliance/discrepancies/export?commune_code=13107")
    assert resp.status_code == 200
    assert resp.headers["content-type"] == "text/csv; charset=utf-8"
    assert 'filename=discrepancies_13107.csv' in resp.headers["content-disposition"]

    csv_content = resp.text
    assert "asset_id,commune_name,address_normalized,media_owner_name,compliance_status,commercial_area_m2,patent_taxed_area_m2,undeclared_area_m2,risk_flags" in csv_content
    assert "CL-RM-HUEC-00109" in csv_content
    assert "AREA_SUBDECLARATION_GT_15PCT" in csv_content


def test_campaign_simulation_excludes_non_compliant_assets() -> None:
    payload = {
        "campaign_name": "Campaña RM Q4",
        "duration_weeks": 4,
        "exclude_non_compliant_assets": True,
        "face_ids": [
            "CL-RM-PROV-00482-A",
            "CL-RM-LCON-01120-A",
            "CL-RM-PUDA-00304-A",  # Clandestino -> debe ser rechazado por Art. 31 Ley 21.473
        ],
    }
    resp = client.post("/v1/campaigns/simulate", json=payload)
    assert resp.status_code == 200
    sim = resp.json()
    assert sim["total_faces_evaluated"] == 3
    assert sim["compliant_faces_approved"] == 2
    assert sim["rejected_by_ley_21473_risk"] == 1
    assert "CL-RM-PUDA-00304-A" in sim["rejected_face_ids"]
    assert sim["financial_projection_clp"]["total_estimated_net_investment_clp"] > 0


def test_spatial_entity_resolution_and_subdeclaration_detection() -> None:
    assert (
        normalize_chilean_address("Avda. Providencia esq. Ricardo Lyon #120")
        == "AVENIDA PROVIDENCIA ESQUINA RICARDO LYON 120"
    )
    score = compute_composite_match_score(
        commercial_lat=-33.37912,
        commercial_lng=-70.64108,
        commercial_address="Américo Vespucio Norte 1450",
        commercial_sii_rol="02410-00082",
        commercial_area_m2=48.0,
        commercial_owner_rut="77.410.892-1",
        municipal_lat=-33.37915,
        municipal_lng=-70.64110,
        municipal_address="Av. Americo Vespucio Nte. 1450",
        municipal_sii_rol="02410-00082",
        municipal_area_m2=24.0,
        municipal_owner_rut="77410892-1",
    )
    assert score["decision"] == "AUTO_MERGED"
    assert "AREA_SUBDECLARATION_GT_15PCT" in score["detected_flags"]


def test_open_audience_engine_calculation() -> None:
    metrics = compute_open_audience_metrics(
        area_m2=32.0,
        tech_type="DOOH_LED",
        illumination="SELF_EMISSIVE_LED",
        azimuth_degrees=75,
        uoct_hourly_vehicles_avg=2500,
        dtpm_bip_daily_validations=4000,
        sectra_occupancy_factor=1.45,
        slot_duration_sec=10,
        loop_slots_total=6,
    )
    assert metrics["weekly_ots_gross"] > 0
    assert 0.10 <= metrics["visibility_index_weight"] <= 1.00
    assert metrics["weekly_vac_impacts"] > 0


import unittest

class TestAPIOOHChile(unittest.TestCase):
    def test_01_health_and_52_rm_communes(self) -> None:
        test_health_and_52_rm_communes_loaded()

    def test_02_list_communes_by_ring_tier(self) -> None:
        test_list_communes_by_ring_tier()

    def test_03_get_assets_json_and_geojson(self) -> None:
        test_get_assets_json_and_geojson_rfc7946()

    def test_04_compliance_discrepancies_ley_21473(self) -> None:
        test_compliance_discrepancies_ley_21473()

    def test_04b_export_compliance_discrepancies_csv(self) -> None:
        test_export_compliance_discrepancies_csv()

    def test_05_campaign_simulation(self) -> None:
        test_campaign_simulation_excludes_non_compliant_assets()

    def test_06_spatial_entity_resolution(self) -> None:
        test_spatial_entity_resolution_and_subdeclaration_detection()

    def test_07_open_audience_engine(self) -> None:
        test_open_audience_engine_calculation()

if __name__ == "__main__":
    unittest.main()
