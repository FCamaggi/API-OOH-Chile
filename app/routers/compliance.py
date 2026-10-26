import io
import csv
from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse
from app.config import settings
from fastapi import Depends
from app.dependencies import get_repository
from app.schemas import ComplianceStatus, Ley21473Class

router = APIRouter(prefix="/v1/compliance", tags=["Auditoría y Fiscalización (Ley N° 21.473)"])


@router.get(
    "/discrepancies",
    summary="Detecta soportes clandestinos, sin permiso DOM o con subdeclaración de m2 en la RM",
)
def list_compliance_discrepancies(
    repo = Depends(get_repository),
    commune_code: Optional[str] = Query(default=None),
    status: Optional[ComplianceStatus] = Query(default=None),
    ley_21473_class: Optional[Ley21473Class] = Query(default=None),
) -> dict:
    discrepancies = []
    total_uncollected_utm = 0.0

    for asset in repo.list_assets():
        if asset.compliance_audit.status == "VERIFIED_LEGAL":
            continue
        if commune_code and asset.location.commune_code != commune_code:
            continue
        if status and asset.compliance_audit.status != status:
            continue
        if ley_21473_class and asset.compliance_audit.ley_21473_class != ley_21473_class:
            continue

        commercial_area = sum(f.dimensions.area_m2 for f in asset.faces)
        taxed_area = asset.compliance_audit.patent_taxed_area_m2 or 0.0
        undeclared_area = max(0.0, round(commercial_area - taxed_area, 2))

        commune_obj = repo.communes.get(asset.location.commune_code)
        annual_utm_rate = (commune_obj.utm_tax_rate_led * 2.0) if commune_obj else 4.0
        uncollected_utm = round(undeclared_area * annual_utm_rate, 2)
        total_uncollected_utm += uncollected_utm

        discrepancies.append(
            {
                "asset_id": asset.asset_id,
                "commune_code": asset.location.commune_code,
                "commune_name": asset.location.commune_name,
                "address_normalized": asset.location.address_normalized,
                "sii_parcel_rol": asset.location.sii_parcel_rol,
                "location": {"lat": asset.location.lat, "lng": asset.location.lng},
                "structure_sub_type": asset.structure.sub_type,
                "commercial_area_m2": commercial_area,
                "media_owner_name": asset.ownership.media_owner_name,
                "compliance_status": asset.compliance_audit.status,
                "ley_21473_class": asset.compliance_audit.ley_21473_class,
                "discrepancy_details": {
                    "dom_permit_number": asset.compliance_audit.dom_permit_number,
                    "municipal_patent_rol": asset.compliance_audit.municipal_patent_rol,
                    "patent_taxed_area_m2": taxed_area,
                    "undeclared_area_m2": undeclared_area,
                    "estimated_uncollected_annual_utm": uncollected_utm,
                    "mop_vialidad_itf_resolution": asset.compliance_audit.mop_vialidad_itf_resolution,
                    "risk_flags": asset.compliance_audit.risk_flags,
                    "advertiser_solidary_liability": True,
                },
            }
        )

    return {
        "query_context": {
            "commune_code": commune_code or "ALL_RM_52",
            "total_discrepancies_found": len(discrepancies),
            "estimated_annual_uncollected_tax_utm": round(total_uncollected_utm, 2),
            "estimated_annual_uncollected_tax_clp": int(round(total_uncollected_utm * settings.utm_value_clp)),
        },
        "items": discrepancies,
    }


@router.get(
    "/discrepancies/export",
    summary="Exporta discrepancias detectadas en formato CSV",
)
def export_compliance_discrepancies(
    repo = Depends(get_repository),
    commune_code: Optional[str] = Query(default=None),
) -> StreamingResponse:
    discrepancies = []

    for asset in repo.list_assets():
        if asset.compliance_audit.status == "VERIFIED_LEGAL":
            continue
        if commune_code and asset.location.commune_code != commune_code:
            continue

        commercial_area = sum(f.dimensions.area_m2 for f in asset.faces)
        taxed_area = asset.compliance_audit.patent_taxed_area_m2 or 0.0
        undeclared_area = max(0.0, round(commercial_area - taxed_area, 2))
        risk_flags_str = "|".join(asset.compliance_audit.risk_flags) if asset.compliance_audit.risk_flags else ""

        discrepancies.append(
            {
                "asset_id": asset.asset_id,
                "commune_name": asset.location.commune_name,
                "address_normalized": asset.location.address_normalized,
                "media_owner_name": asset.ownership.media_owner_name,
                "compliance_status": asset.compliance_audit.status,
                "commercial_area_m2": commercial_area,
                "patent_taxed_area_m2": taxed_area,
                "undeclared_area_m2": undeclared_area,
                "risk_flags": risk_flags_str,
            }
        )

    output = io.StringIO()
    writer = csv.DictWriter(
        output,
        fieldnames=[
            "asset_id",
            "commune_name",
            "address_normalized",
            "media_owner_name",
            "compliance_status",
            "commercial_area_m2",
            "patent_taxed_area_m2",
            "undeclared_area_m2",
            "risk_flags",
        ],
    )
    writer.writeheader()
    writer.writerows(discrepancies)

    # Seek to start
    output.seek(0)

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=discrepancies_{commune_code or 'ALL'}.csv"
        }
    )


@router.get(
    "/communes/{commune_code}/summary",
    summary="Resumen ejecutivo de auditoría OOH/DOOH para una municipalidad de la RM",
)
def get_commune_compliance_summary(commune_code: str, repo = Depends(get_repository)) -> dict:
    commune = repo.communes.get(commune_code)
    if not commune:
        raise HTTPException(status_code=404, detail=f"Comuna '{commune_code}' no existe en la Región Metropolitana")

    assets = [a for a in repo.list_assets() if a.location.commune_code == commune_code]
    verified = sum(1 for a in assets if a.compliance_audit.status == "VERIFIED_LEGAL")
    irregular = len(assets) - verified

    return {
        "commune_code": commune.commune_code,
        "commune_name": commune.commune_name,
        "province_name": commune.province_name,
        "ring_tier": commune.ring_tier,
        "total_assets_detected": len(assets),
        "verified_legal_count": verified,
        "irregular_or_clandestine_count": irregular,
        "compliance_rate_pct": round((verified / len(assets)) * 100.0, 1) if assets else 100.0,
    }
