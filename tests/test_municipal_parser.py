import pytest
from etl.connectors.municipal_parser import normalize_municipal_rows
from app.schemas import MunicipalInboundRecord

def test_normalize_municipal_rows_basic():
    raw_rows = [
        {
            "ROL PATENTE": "1234-5",
            "DIRECCION": "Av. Las Condes 1234",
            "M2": "15,5 m2",
            "RUT": "76.543.210-K",
            "nombre": "Publicidad XYZ",
            "permiso_dom": "9876",
        },
        {
            "N_ROL": "5432-1",
            "UBICACION": "Providencia 567",
            "SUPERFICIE": "20.5",
            "rut": "12.345.678-9",
            "razon social": "Otra Empresa",
            "n_permiso": "1234",
        }
    ]

    records = normalize_municipal_rows(raw_rows, "13114")

    assert len(records) == 2

    assert isinstance(records[0], MunicipalInboundRecord)
    assert records[0].municipal_patent_rol == "1234-5"
    assert records[0].address == "Av. Las Condes 1234"
    assert records[0].area_m2 == 15.5
    assert records[0].owner_rut == "76.543.210-K"
    assert records[0].owner_name == "Publicidad XYZ"
    assert records[0].dom_permit_number == "9876"
    assert records[0].record_id is not None

    assert isinstance(records[1], MunicipalInboundRecord)
    assert records[1].municipal_patent_rol == "5432-1"
    assert records[1].address == "Providencia 567"
    assert records[1].area_m2 == 20.5
    assert records[1].owner_rut == "12.345.678-9"
    assert records[1].owner_name == "Otra Empresa"
    assert records[1].dom_permit_number == "1234"

def test_normalize_municipal_rows_empty_and_missing_values():
    raw_rows = [
        {
            "DIRECCION": "Av. Kennedy 5413",
            "M2": "N/A"
        },
        {
            # No direccion or ubicacion
            "SUPERFICIE": ""
        }
    ]

    records = normalize_municipal_rows(raw_rows, "13114")

    assert len(records) == 2

    assert records[0].address == "Av. Kennedy 5413"
    assert records[0].area_m2 == 0.0
    assert records[0].municipal_patent_rol is None

    assert records[1].address == ""
    assert records[1].area_m2 == 0.0

def test_normalize_municipal_rows_coordinate_parsing():
    raw_rows = [
        {
            "DIRECCION": "Alameda 123",
            "LAT": "-33.4372",
            "LONGITUD": "-70.6506",
            "M2": "10"
        }
    ]

    records = normalize_municipal_rows(raw_rows, "13101")
    assert len(records) == 1
    assert records[0].lat == -33.4372
    assert records[0].lng == -70.6506
