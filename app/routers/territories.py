from typing import Optional
from fastapi import APIRouter, Query
from fastapi import Depends
from app.dependencies import get_repository
from app.schemas import CommuneRM

router = APIRouter(prefix="/v1", tags=["Territorios y Capas Base RM"])


@router.get(
    "/territories/communes",
    response_model=list[CommuneRM],
    summary="Lista las 52 comunas de la Región Metropolitana con sus anillos y tasas UTM/m2",
)
def get_rm_communes(
    repo = Depends(get_repository),
    ring_tier: Optional[int] = Query(default=None, ge=1, le=4, description="Filtrar por Anillo Operativo RM (1 a 4)"),
    province_name: Optional[str] = Query(default=None, description="Filtrar por provincia (Santiago, Cordillera, Chacabuco, Maipo, Melipilla, Talagante)"),
) -> list[CommuneRM]:
    return repo.list_communes(ring_tier=ring_tier, province_name=province_name)


@router.get(
    "/tiles/{z}/{x}/{y}.json",
    summary="Descriptor ligero de Vector Tiles (MVT) para el futuro visor cartográfico",
)
def get_vector_tile_preview(z: int, x: int, y: int, repo = Depends(get_repository)) -> dict:
    assets = repo.list_assets()
    return {
        "tile_coord": {"z": z, "x": x, "y": y},
        "layers": {
            "ooh_assets": [
                {
                    "asset_id": a.asset_id,
                    "lat": a.location.lat,
                    "lng": a.location.lng,
                    "commune_code": a.location.commune_code,
                    "structure_category": a.structure.category,
                    "compliance_status": a.compliance_audit.status,
                    "solidary_liability_risk_level": a.compliance_audit.solidary_liability_risk_level,
                }
                for a in assets
            ]
        },
    }
