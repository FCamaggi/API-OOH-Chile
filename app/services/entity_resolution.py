"""
Motor de Reconciliación Espacial (Spatial Entity Resolution) para cruzar
la oferta comercial OOH/DOOH contra los padrones municipales (DOM Art. 16 Ley 21.473
y Roles de Patentes de Propaganda en Rentas Municipales).
"""
import math
import re
import unicodedata
from typing import Optional


ABBREVIATIONS_MAP = {
    r"\bAVDA\b": "AVENIDA",
    r"\bAV\b": "AVENIDA",
    r"\bESQ\b": "ESQUINA",
    r"\bPJE\b": "PASAJE",
    r"\bPTE\b": "PUENTE",
    r"\bNTE\b": "NORTE",
    r"\bSTA\b": "SANTA",
    r"\bSTO\b": "SANTO",
    r"\bGRAL\b": "GENERAL",
    r"\bPDTE\b": "PRESIDENTE",
}


def normalize_chilean_address(raw_address: str) -> str:
    """Normaliza direcciones de la Región Metropolitana para fuzzy matching."""
    text = unicodedata.normalize("NFKD", raw_address).encode("ascii", "ignore").decode("ascii")
    text = text.upper().strip()
    text = re.sub(r"[.,;#\-/]", " ", text)
    for pattern, replacement in ABBREVIATIONS_MAP.items():
        text = re.sub(pattern, replacement, text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_rut(rut: Optional[str]) -> str:
    if not rut:
        return ""
    return re.sub(r"[^0-9K]", "", rut.upper())


def wgs84_to_utm19s_approx(lat: float, lng: float) -> tuple[float, float]:
    """
    Conversión proyectada rápida a UTM Datum WGS84 Huso 19 Sur (EPSG:32719)
    centrada en la Región Metropolitana de Santiago para cálculos en metros.
    """
    # Referencia central RM: Providencia (-33.42628, -70.61094) -> (350214.5, 6299812.1)
    meters_per_deg_lat = 110900.0
    meters_per_deg_lng = 92900.0
    utm_x = 350214.5 + (lng - (-70.61094)) * meters_per_deg_lng
    utm_y = 6299812.1 + (lat - (-33.42628)) * meters_per_deg_lat
    return round(utm_x, 1), round(utm_y, 1)


def euclidean_distance_m(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    x1, y1 = wgs84_to_utm19s_approx(lat1, lng1)
    x2, y2 = wgs84_to_utm19s_approx(lat2, lng2)
    return math.hypot(x2 - x1, y2 - y1)


def token_similarity(addr_a: str, addr_b: str) -> float:
    norm_a = normalize_chilean_address(addr_a)
    norm_b = normalize_chilean_address(addr_b)
    if not norm_a or not norm_b:
        return 0.0
    if norm_a == norm_b:
        return 1.0
    tokens_a = set(norm_a.split())
    tokens_b = set(norm_b.split())
    intersection = len(tokens_a & tokens_b)
    union = len(tokens_a | tokens_b)
    return round(intersection / union, 3) if union else 0.0


def compute_composite_match_score(
    *,
    commercial_lat: float,
    commercial_lng: float,
    commercial_address: str,
    commercial_sii_rol: Optional[str],
    commercial_area_m2: float,
    commercial_owner_rut: Optional[str],
    municipal_lat: Optional[float],
    municipal_lng: Optional[float],
    municipal_address: str,
    municipal_sii_rol: Optional[str],
    municipal_area_m2: float,
    municipal_owner_rut: Optional[str],
) -> dict[str, float | str | list[str]]:
    """
    Aplica la ecuación del Documento 2 (SDD):
    Match_Score = 0.40 * S_espacial + 0.25 * S_direccion + 0.20 * S_estructural + 0.15 * S_titular
    """
    # 1. S_espacial (40%)
    if commercial_sii_rol and municipal_sii_rol and commercial_sii_rol.strip() == municipal_sii_rol.strip():
        s_espacial = 1.0
    elif municipal_lat is not None and municipal_lng is not None:
        dist = euclidean_distance_m(commercial_lat, commercial_lng, municipal_lat, municipal_lng)
        if dist <= 10.0:
            s_espacial = 1.0
        elif dist <= 35.0:
            s_espacial = round(1.0 - ((dist - 10.0) / 25.0) * 0.60, 3)
        else:
            s_espacial = 0.0
    else:
        # Sin coordenadas en el padrón municipal: inferencia desde coincidencia de dirección exacta
        s_espacial = 0.75 if token_similarity(commercial_address, municipal_address) >= 0.75 else 0.20

    # 2. S_direccion (25%)
    s_direccion = token_similarity(commercial_address, municipal_address)

    # 3. S_estructural (20%) y detección de subdeclaración de m2 (>15%)
    flags: list[str] = []
    if commercial_area_m2 > 0 and municipal_area_m2 > 0:
        area_diff_ratio = abs(commercial_area_m2 - municipal_area_m2) / commercial_area_m2
        if area_diff_ratio <= 0.10:
            s_estructural = 1.0
        elif area_diff_ratio <= 0.25:
            s_estructural = 0.75
        else:
            s_estructural = 0.50
        if (commercial_area_m2 - municipal_area_m2) / commercial_area_m2 > 0.15:
            flags.append("AREA_SUBDECLARATION_GT_15PCT")
    else:
        s_estructural = 0.50

    # 4. S_titular (15%)
    rut_a = normalize_rut(commercial_owner_rut)
    rut_b = normalize_rut(municipal_owner_rut)
    s_titular = 1.0 if (rut_a and rut_b and rut_a == rut_b) else 0.40

    composite_score = round(
        (0.40 * s_espacial) + (0.25 * s_direccion) + (0.20 * s_estructural) + (0.15 * s_titular),
        3,
    )

    if composite_score >= 0.82:
        decision = "AUTO_MERGED"
    elif composite_score >= 0.60:
        decision = "PENDING_MANUAL_REVIEW"
    else:
        decision = "NO_MATCH"

    return {
        "match_score": composite_score,
        "decision": decision,
        "s_espacial": s_espacial,
        "s_direccion": s_direccion,
        "s_estructural": s_estructural,
        "s_titular": s_titular,
        "detected_flags": flags,
    }
