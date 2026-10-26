from app.schemas import AssetRecord, FaceItem

def evaluate_ley_21473_restrictions(asset: AssetRecord, faces: list[FaceItem]) -> AssetRecord:
    """
    Evaluates regulatory restrictions according to Ley N° 21.473 and Decreto MOP N° 24/2023.
    Returns a new modified AssetRecord (pure function).
    """
    new_asset = asset.model_copy(deep=True)

    has_led_face = any(face.technology.type == "DOOH_LED" for face in faces)

    if has_led_face and new_asset.compliance_audit.is_exclusive_residential:
        if "PROHIBITED_LED_IN_RESIDENTIAL_ZONE_ART28" not in new_asset.compliance_audit.risk_flags:
            new_asset.compliance_audit.risk_flags.append("PROHIBITED_LED_IN_RESIDENTIAL_ZONE_ART28")
        new_asset.compliance_audit.status = "ZONING_VIOLATION_RISK"

    distance = new_asset.compliance_audit.distance_to_nearest_hazard_m
    road_type = new_asset.location.road_type

    if distance is not None and distance < 40.0:
        if road_type in ("HIGHWAY_CONCESSION", "INTERURBAN_ROUTE"):
            if "HAZARD_PROXIMITY_LT_40M_DECRETO24" not in new_asset.compliance_audit.risk_flags:
                new_asset.compliance_audit.risk_flags.append("HAZARD_PROXIMITY_LT_40M_DECRETO24")

    return new_asset
