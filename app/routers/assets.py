from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from fastapi import Depends
from app.dependencies import get_repository
from app.schemas import (
    AssetRecord,
    ComplianceStatus,
    GeoJSONFeature,
    GeoJSONFeatureCollection,
    StructureCategory,
    TechType,
)
from app.services.entity_resolution import euclidean_distance_m

router = APIRouter(prefix="/v1/assets", tags=["Inventario Físico (Assets)"])


@router.get(
    "",
    response_model=list[AssetRecord] | GeoJSONFeatureCollection,
    summary="Búsqueda geoespacial y multicriterio de estructuras OOH/DOOH en las 52 comunas RM",
)
def search_assets(
    repo = Depends(get_repository),
    commune_code: Optional[str] = Query(default=None, description="Código CUT comunal (ej. 13123,13114)"),
    bbox: Optional[str] = Query(default=None, description="min_lng,min_lat,max_lng,max_lat"),
    near: Optional[str] = Query(default=None, description="lat,lng,radius_m (ej. -33.42628,-70.61094,1000)"),
    structure_category: Optional[StructureCategory] = Query(default=None),
    tech_type: Optional[TechType] = Query(default=None),
    compliance_status: Optional[ComplianceStatus] = Query(default=None),
    media_owner_rut: Optional[str] = Query(default=None),
    format: str = Query(default="json", pattern="^(json|geojson)$"),
) -> list[AssetRecord] | GeoJSONFeatureCollection:
    items = repo.list_assets()

    if commune_code:
        allowed_codes = {c.strip() for c in commune_code.split(",") if c.strip()}
        items = [a for a in items if a.location.commune_code in allowed_codes]

    if structure_category:
        items = [a for a in items if a.structure.category == structure_category]

    if tech_type:
        items = [
            a for a in items if any(f.technology.type == tech_type for f in a.faces)
        ]

    if compliance_status:
        items = [a for a in items if a.compliance_audit.status == compliance_status]

    if media_owner_rut:
        items = [
            a for a in items if a.ownership.media_owner_rut.lower() == media_owner_rut.lower()
        ]

    if bbox:
        try:
            min_lng, min_lat, max_lng, max_lat = [float(x) for x in bbox.split(",")]
        except ValueError as exc:
            raise HTTPException(status_code=400, detail="Formato bbox inválido. Use min_lng,min_lat,max_lng,max_lat") from exc
        items = [
            a
            for a in items
            if min_lng <= a.location.lng <= max_lng and min_lat <= a.location.lat <= max_lat
        ]

    if near:
        try:
            c_lat, c_lng, radius_m = [float(x) for x in near.split(",")]
        except ValueError as exc:
            raise HTTPException(status_code=400, detail="Formato near inválido. Use lat,lng,radius_m") from exc
        items = [
            a
            for a in items
            if euclidean_distance_m(c_lat, c_lng, a.location.lat, a.location.lng) <= radius_m
        ]

    if format == "geojson":
        features = [
            GeoJSONFeature(
                id=a.asset_id,
                geometry={"type": "Point", "coordinates": [a.location.lng, a.location.lat]},
                properties={
                    "asset_id": a.asset_id,
                    "commune_code": a.location.commune_code,
                    "commune_name": a.location.commune_name,
                    "address_normalized": a.location.address_normalized,
                    "structure_category": a.structure.category,
                    "sub_type": a.structure.sub_type,
                    "media_owner_name": a.ownership.media_owner_name,
                    "faces_count": len(a.faces),
                    "compliance_status": a.compliance_audit.status,
                    "solidary_liability_risk_level": a.compliance_audit.solidary_liability_risk_level,
                    "risk_flags": a.compliance_audit.risk_flags,
                },
            )
            for a in items
        ]
        return GeoJSONFeatureCollection(total_features=len(features), features=features)

    return items


@router.get(
    "/{asset_id}",
    response_model=AssetRecord,
    summary="Obtiene la ficha maestra tricapa (Asset + Faces + Compliance) de un soporte físico",
)
def get_asset_by_id(asset_id: str, repo = Depends(get_repository)) -> AssetRecord:
    asset = repo.get_asset(asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail=f"Asset '{asset_id}' no encontrado en la Región Metropolitana")
    return asset
