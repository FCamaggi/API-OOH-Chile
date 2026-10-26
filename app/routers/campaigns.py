from fastapi import APIRouter
from fastapi import Depends
from app.dependencies import get_repository
from app.schemas import CampaignSimulationRequest, CampaignSimulationResponse

router = APIRouter(prefix="/v1/campaigns", tags=["Simulador de Campañas y Precios Netos"])


@router.post(
    "/simulate",
    response_model=CampaignSimulationResponse,
    summary="Simula alcance OTS/VAC, inversión neta (descuento 30-55%) y riesgo legal Ley 21.473",
)
def simulate_campaign(payload: CampaignSimulationRequest, repo = Depends(get_repository)) -> CampaignSimulationResponse:
    face_lookup: dict[str, tuple] = {}
    for asset in repo.list_assets():
        for face in asset.faces:
            face_lookup[face.face_id] = (asset, face)

    approved_faces = []
    rejected_face_ids = []
    communes_set: set[str] = set()

    for fid in payload.face_ids:
        if fid not in face_lookup:
            continue
        asset, face = face_lookup[fid]
        if payload.exclude_non_compliant_assets and asset.compliance_audit.status != "VERIFIED_LEGAL":
            rejected_face_ids.append(fid)
            continue
        approved_faces.append((asset, face))
        communes_set.add(asset.location.commune_name)

    discount_map = {
        "LIST_PRICE": 0.0,
        "CONSERVATIVE_30PCT": 0.30,
        "MARKET_AVERAGE_42PCT": 0.42,
        "STATE_TENDER_55PCT": 0.55,
    }

    pricing_strategy = payload.pricing_strategy or "MARKET_AVERAGE_42PCT"
    discount_multiplier = discount_map.get(pricing_strategy, 0.42)

    months_factor = payload.duration_weeks / 4.0
    total_ots = 0
    total_vac = 0
    total_list_clp = 0
    total_net_media_clp = 0
    total_prod_clp = 0

    from collections import defaultdict

    commune_data = defaultdict(lambda: {"total_list_price_clp": 0, "total_net_media_clp": 0, "total_ots_gross": 0})
    owner_data = defaultdict(lambda: {"total_list_price_clp": 0, "total_net_media_clp": 0, "total_ots_gross": 0})

    for asset, face in approved_faces:
        ots = face.audience_metrics.weekly_ots_gross * payload.duration_weeks
        vac = face.audience_metrics.weekly_vac_impacts * payload.duration_weeks
        list_clp = face.commercial_pricing.list_price_clp_monthly * months_factor
        net_clp = list_clp * (1.0 - discount_multiplier)
        prod_clp = face.commercial_pricing.production_cost_clp

        total_ots += ots
        total_vac += vac
        total_list_clp += list_clp
        total_net_media_clp += net_clp
        total_prod_clp += prod_clp

        commune_name = asset.location.commune_name
        owner_name = asset.ownership.media_owner_name

        commune_data[commune_name]["total_list_price_clp"] += int(list_clp)
        commune_data[commune_name]["total_net_media_clp"] += int(net_clp)
        commune_data[commune_name]["total_ots_gross"] += int(ots)

        owner_data[owner_name]["total_list_price_clp"] += int(list_clp)
        owner_data[owner_name]["total_net_media_clp"] += int(net_clp)
        owner_data[owner_name]["total_ots_gross"] += int(ots)

    total_ots = int(total_ots)
    total_vac = int(total_vac)
    total_list_clp = int(total_list_clp)
    total_net_media_clp = int(total_net_media_clp)
    total_prod_clp = int(total_prod_clp)
    total_net_investment = total_net_media_clp + total_prod_clp

    avg_discount = (
        round(1.0 - (total_net_media_clp / total_list_clp), 2) if total_list_clp > 0 else 0.0
    )
    cpm_vac = int(round((total_net_investment / total_vac) * 1000)) if total_vac > 0 else 0

    breakdown_by_commune = []
    for commune_name, data in commune_data.items():
        breakdown_by_commune.append({
            "commune_name": commune_name,
            **data
        })

    breakdown_by_owner = []
    for owner_name, data in owner_data.items():
        breakdown_by_owner.append({
            "media_owner_name": owner_name,
            **data
        })

    return CampaignSimulationResponse(
        campaign_name=payload.campaign_name,
        total_faces_evaluated=len(payload.face_ids),
        compliant_faces_approved=len(approved_faces),
        rejected_by_ley_21473_risk=len(rejected_face_ids),
        rejected_face_ids=rejected_face_ids,
        communes_covered=sorted(communes_set),
        total_ots_gross=total_ots,
        total_vac_impacts=total_vac,
        financial_projection_clp={
            "total_list_price_clp": total_list_clp,
            "total_production_cost_clp": total_prod_clp,
            "estimated_negotiated_discount_pct": avg_discount,
            "estimated_net_media_cost_clp": total_net_media_clp,
            "total_estimated_net_investment_clp": total_net_investment,
            "effective_cpm_vac_clp": cpm_vac,
        },
        breakdown_by_commune=breakdown_by_commune,
        breakdown_by_owner=breakdown_by_owner,
    )
