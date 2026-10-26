import pytest
from etl.connectors.dtpm_ingestor import parse_dtpm_gtfs_stops

def test_parse_dtpm_gtfs_stops():
    csv_content = """stop_id,stop_code,stop_name,stop_lat,stop_lon
T-13-118-OP-10,PB14,Parada 1, -33.39343, -70.66986
T-13-118-OP-11,PB15,Parada 2, -33.39443, -70.66986"""

    parsed = parse_dtpm_gtfs_stops(csv_content, "13101")
    assert len(parsed) == 2

    stop1 = parsed[0]
    assert stop1["dtpm_stop_code"] == "PB14"
    assert stop1["address_raw"] == "Parada 1"
    assert stop1["address_normalized"] == "PARADA 1"
    assert stop1["commune_code"] == "13101"
    assert stop1["lat"] == -33.39343
    assert stop1["lng"] == -70.66986
    # Calculate UTMs directly using the helper logic
    # utm_x = 350214.5 + (-70.66986 - (-70.61094)) * 92900.0 = 350214.5 + (-0.05892) * 92900.0 = 344740.832 -> 344740.8
    # utm_y = 6299812.1 + (-33.39343 - (-33.42628)) * 110900.0 = 6299812.1 + (0.03285) * 110900.0 = 6303455.165 -> 6303455.2
    assert stop1["utm_x"] == 344740.8
    assert stop1["utm_y"] == 6303455.2
    assert stop1["structure_category"] == "STREET_FURNITURE"
    assert stop1["structure_sub_type"] == "BUS_SHELTER"
