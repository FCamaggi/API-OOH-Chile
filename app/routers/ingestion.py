from fastapi import APIRouter, HTTPException
from app.data.seed_rm import repo
from app.schemas import MunicipalBatchIngestRequest
from app.services.entity_resolution import compute_composite_match_score

router = APIRouter(prefix="/v1/ingestion", tags=["Ingesta y Spatial Entity Resolution"])


@router.post(
    "/municipal-batch",
    summary="Cruza un lote de registros DOM (Art. 16 Ley 21.473) o Rentas contra el inventario comercial",
)
def process_municipal_batch(payload: MunicipalBatchIngestRequest) -> dict:
    if payload.commune_code not in repo.communes:
        raise HTTPException(status_code=404, detail=f"Comuna '{payload.commune_code}' no existe en la RM")

    commune_assets = [
        a for a in repo.list_assets() if a.location.commune_code == payload.commune_code
    ]

    reconciliation_results = []
    for rec in payload.records:
        best_match = None
        best_score = -1.0
        for asset in commune_assets:
            comm_area = sum(f.dimensions.area_m2 for f in asset.faces)
            score_info = compute_composite_match_score(
                commercial_lat=asset.location.lat,
                commercial_lng=asset.location.lng,
                commercial_address=asset.location.address_raw,
                commercial_sii_rol=asset.location.sii_parcel_rol,
                commercial_area_m2=comm_area,
                commercial_owner_rut=asset.ownership.media_owner_rut,
                municipal_lat=rec.lat,
                municipal_lng=rec.lng,
                municipal_address=rec.address,
                municipal_sii_rol=rec.sii_parcel_rol,
                municipal_area_m2=rec.area_m2,
                municipal_owner_rut=rec.owner_rut,
            )
            if float(score_info["match_score"]) > best_score:
                best_score = float(score_info["match_score"])
                best_match = {
                    "record_id": rec.record_id,
                    "matched_asset_id": asset.asset_id,
                    **score_info,
                }
        reconciliation_results.append(best_match)

    return {
        "commune_code": payload.commune_code,
        "source_type": payload.source_type,
        "records_processed": len(payload.records),
        "results": reconciliation_results,
    }
