from typing import Optional
from fastapi import APIRouter, Query
from fastapi import Depends
from app.dependencies import get_repository
from app.schemas import TechType

router = APIRouter(prefix="/v1/faces", tags=["Caras Publicitarias y Planificación (Faces)"])


@router.get(
    "/search",
    summary="Buscador de caras publicitarias para compra de medios con métricas OTS/VAC y tarifas netas",
)
def search_faces(
    repo = Depends(get_repository),
    commune_code: Optional[str] = Query(default=None),
    tech_type: Optional[TechType] = Query(default=None),
    min_area_m2: Optional[float] = Query(default=None, ge=0),
    max_net_price_clp: Optional[int] = Query(default=None, ge=0),
    min_weekly_vac: Optional[int] = Query(default=None, ge=0),
    only_verified_legal: bool = Query(default=False, description="Excluye activos con riesgo de responsabilidad solidaria Ley 21.473"),
) -> list[dict]:
    results: list[dict] = []
    for asset in repo.list_assets():
        if commune_code and asset.location.commune_code != commune_code:
            continue
        if only_verified_legal and asset.compliance_audit.status != "VERIFIED_LEGAL":
            continue
        for face in asset.faces:
            if tech_type and face.technology.type != tech_type:
                continue
            if min_area_m2 is not None and face.dimensions.area_m2 < min_area_m2:
                continue
            if max_net_price_clp is not None and face.commercial_pricing.estimated_net_price_clp > max_net_price_clp:
                continue
            if min_weekly_vac is not None and face.audience_metrics.weekly_vac_impacts < min_weekly_vac:
                continue
            results.append(
                {
                    "face_id": face.face_id,
                    "asset_id": asset.asset_id,
                    "commune_code": asset.location.commune_code,
                    "commune_name": asset.location.commune_name,
                    "address_normalized": asset.location.address_normalized,
                    "media_owner_name": asset.ownership.media_owner_name,
                    "compliance_status": asset.compliance_audit.status,
                    "face_label": face.face_label,
                    "dimensions": face.dimensions.model_dump(),
                    "technology": face.technology.model_dump(),
                    "audience_metrics": face.audience_metrics.model_dump(),
                    "commercial_pricing": face.commercial_pricing.model_dump(),
                }
            )
    return results
