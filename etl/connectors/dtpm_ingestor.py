"""
Pipeline 1: Conector de Datos Abiertos del DTPM (Red Movilidad).
Procesa el Consolidado de Paradas / GTFS stops.txt (+11.000 puntos en la RM).
"""
import csv
import io
from app.services.entity_resolution import normalize_chilean_address, wgs84_to_utm19s_approx


def parse_dtpm_stops_csv(csv_text: str, default_commune_code: str = "13101") -> list[dict]:
    reader = csv.DictReader(io.StringIO(csv_text.strip()))
    parsed_stops: list[dict] = []
    for row in reader:
        lat = float(row["stop_lat"])
        lng = float(row["stop_lon"])
        utm_x, utm_y = wgs84_to_utm19s_approx(lat, lng)
        stop_code = row.get("stop_code") or row.get("stop_id") or "UNKNOWN"
        stop_name = row.get("stop_name", "")
        parsed_stops.append(
            {
                "dtpm_stop_code": stop_code,
                "address_raw": stop_name,
                "address_normalized": normalize_chilean_address(stop_name),
                "commune_code": row.get("commune_code", default_commune_code),
                "lat": lat,
                "lng": lng,
                "utm_x": utm_x,
                "utm_y": utm_y,
                "structure_category": "STREET_FURNITURE",
                "structure_sub_type": "BUS_SHELTER",
            }
        )
    return parsed_stops
