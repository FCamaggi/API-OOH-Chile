"""
Pipeline 4: Estandarizador de Planillas Municipales recibidas vía Ley N° 20.285
(Transparencia Pasiva DOM Art. 16 Ley 21.473 y Padrón de Rentas Municipales).
"""
from app.services.entity_resolution import normalize_chilean_address, normalize_rut


def standardize_municipal_record(row: dict, commune_code: str) -> dict:
    address_raw = str(row.get("direccion") or row.get("ubicacion") or "").strip()
    return {
        "commune_code": commune_code,
        "address_raw": address_raw,
        "address_normalized": normalize_chilean_address(address_raw),
        "owner_rut": normalize_rut(str(row.get("rut") or "")),
        "municipal_patent_rol": str(row.get("rol_patente") or row.get("rol") or "").strip() or None,
        "dom_permit_number": str(row.get("permiso_dom") or "").strip() or None,
        "area_m2": float(row.get("m2") or row.get("superficie") or 0.0),
    }
