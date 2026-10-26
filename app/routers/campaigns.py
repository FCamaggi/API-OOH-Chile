from fastapi import APIRouter
from app.data.seed_rm import repo
from app.schemas import CampaignSimulationRequest, CampaignSimulationResponse

router = APIRouter(prefix="/v1/campaigns", tags=["Simulador de Campañas y Precios Netos"])


@router.post(
    "/simulate",
    response_model=CampaignSimulationResponse,
    summary="Simula alcance OTS/VAC, inversión neta (descuento 30-55%) y riesgo legal Ley 21.473",
)
def simulate_campaign(payload: CampaignSimulationRequest) -> CampaignSimulationResponse:
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

    months_factor = payload.duration_weeks / 4.0
    total_ots = int(sum(f.audience_metrics.weekly_ots_gross * payload.duration_weeks for _, f in approved_faces))
    total_vac = int(sum(f.audience_metrics.weekly_vac_impacts * payload.duration_weeks for _, f in approved_faces))

    total_list_clp = int(sum(f.commercial_pricing.list_price_clp_monthly * months_factor for _, f in approved_faces))
    total_net_media_clp = int(sum(f.commercial_pricing.estimated_net_price_clp * months_factor for _, f in approved_faces))
    total_prod_clp = int(sum(f.commercial_pricing.production_cost_clp for _, f in approved_faces))
    total_net_investment = total_net_media_clp + total_prod_clp

    avg_discount = (
        round(1.0 - (total_net_media_clp / total_list_clp), 2) if total_list_clp > 0 else 0.0
    )
    cpm_vac = int(round((total_net_investment / total_vac) * 1000)) if total_vac > 0 else 0

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
    )
