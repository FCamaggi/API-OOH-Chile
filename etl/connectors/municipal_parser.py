"""
Pipeline 4: Estandarizador de Planillas Municipales recibidas vía Ley N° 20.285
(Transparencia Pasiva DOM Art. 16 Ley 21.473 y Padrón de Rentas Municipales).
"""
import uuid
import re
from app.services.entity_resolution import normalize_chilean_address, normalize_rut
from app.schemas import MunicipalInboundRecord


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

def normalize_municipal_rows(raw_rows: list[dict], commune_code: str) -> list[MunicipalInboundRecord]:
    normalized_records = []

    for row in raw_rows:
        normalized_row = {k.lower().strip().replace(" ", "_"): v for k, v in row.items()}

        # Mapeo de campos a MunicipalInboundRecord
        address = str(
            normalized_row.get("direccion") or
            normalized_row.get("ubicacion") or
            ""
        ).strip()

        owner_rut = str(
            normalized_row.get("rut") or
            ""
        ).strip()

        municipal_patent_rol = str(
            normalized_row.get("rol_patente") or
            normalized_row.get("n_rol") or
            normalized_row.get("rol") or
            ""
        ).strip() or None

        dom_permit_number = str(
            normalized_row.get("permiso_dom") or
            normalized_row.get("n_permiso") or
            ""
        ).strip() or None

        owner_name = str(
            normalized_row.get("nombre") or
            normalized_row.get("razon_social") or
            normalized_row.get("owner_name") or
            ""
        ).strip() or None

        sii_parcel_rol = str(
            normalized_row.get("rol_sii") or
            normalized_row.get("sii_parcel_rol") or
            ""
        ).strip() or None

        # Helper to parse area
        area_raw = str(normalized_row.get("m2") or normalized_row.get("superficie") or "0.0")
        # Extract the first valid float/int number from the string
        # Replaces comma with dot for decimals, e.g., "15,5 m2" -> "15.5"
        area_str = area_raw.replace(",", ".")
        match = re.search(r"[-+]?\d*\.\d+|\d+", area_str)
        area_m2 = float(match.group()) if match else 0.0

        # Helpers to parse lat/lng
        lat_raw = str(normalized_row.get("latitud") or normalized_row.get("lat") or "")
        lng_raw = str(normalized_row.get("longitud") or normalized_row.get("lng") or "")

        def parse_coord(coord_str: str) -> float | None:
            coord_str = coord_str.replace(",", ".")
            m = re.search(r"[-+]?\d*\.\d+|\d+", coord_str)
            return float(m.group()) if m else None

        lat = parse_coord(lat_raw)
        lng = parse_coord(lng_raw)

        record = MunicipalInboundRecord(
            record_id=str(uuid.uuid4()),
            address=address,
            sii_parcel_rol=sii_parcel_rol,
            lat=lat,
            lng=lng,
            owner_rut=owner_rut if owner_rut else None,
            owner_name=owner_name,
            area_m2=area_m2,
            dom_permit_number=dom_permit_number,
            municipal_patent_rol=municipal_patent_rol
        )
        normalized_records.append(record)

    return normalized_records
