"""
Motor Abierto de Cálculo de Audiencias e Impactos OOH/DOOH (OTS y VAC Sintético).
Combina conteos horarios Traffic UOCT, validaciones bip! ADATRAP (DTPM/Metro),
censos viales TMDA (MOP) y tasas de ocupación vehicular EOD SECTRA.
"""
import math
from typing import Optional


def calculate_visibility_index(
    area_m2: float,
    tech_type: str,
    illumination: str,
    azimuth_degrees: int,
    slot_duration_sec: Optional[int] = None,
    loop_slots_total: Optional[int] = None,
) -> float:
    """
    Calcula el factor de ponderación visual (entre 0.100 y 1.000) para transformar
    OTS bruto en Impactos Ajustados por Visibilidad (VAC).
    """
    # 1. Factor por superficie (escala logarítmica desde 2 m2 hasta 48+ m2)
    area_clamped = max(1.5, min(area_m2, 60.0))
    area_factor = 0.45 + 0.55 * (math.log(area_clamped / 1.5) / math.log(60.0 / 1.5))

    # 2. Factor de iluminación
    if tech_type == "DOOH_LED" or illumination in ("SELF_EMISSIVE_LED", "INTERNAL_LED"):
        light_factor = 1.0
    elif illumination == "EXTERNAL_SPOTLIGHT":
        light_factor = 0.85
    else:
        light_factor = 0.65

    # 3. Factor de orientación / ángulo visual
    angle_factor = 0.95 if (azimuth_degrees % 90) != 0 else 0.85

    # 4. Factor de exposición en loop digital DOOH
    loop_factor = 1.0
    if tech_type == "DOOH_LED" and slot_duration_sec and loop_slots_total and loop_slots_total > 1:
        # Ajuste por rotación de spots dentro del cono de aproximación vehicular
        share_of_voice = 1.0 / float(loop_slots_total)
        loop_factor = min(1.0, share_of_voice * 3.6)

    weight = area_factor * light_factor * angle_factor * loop_factor
    return round(max(0.10, min(weight, 1.00)), 3)


def compute_open_audience_metrics(
    area_m2: float,
    tech_type: str,
    illumination: str,
    azimuth_degrees: int,
    uoct_hourly_vehicles_avg: Optional[int] = None,
    mop_tmda_daily_vehicles: Optional[int] = None,
    dtpm_bip_daily_validations: Optional[int] = None,
    sectra_occupancy_factor: float = 1.42,
    slot_duration_sec: Optional[int] = None,
    loop_slots_total: Optional[int] = None,
) -> dict[str, float | int]:
    """
    Calcula weekly_ots_gross, visibility_index_weight y weekly_vac_impacts
    sin depender de licencias cerradas.
    """
    daily_vehicular_persons = 0.0
    if uoct_hourly_vehicles_avg:
        # 18 horas de flujo activo diario equivalente
        daily_vehicular_persons += uoct_hourly_vehicles_avg * 18.0 * sectra_occupancy_factor
    elif mop_tmda_daily_vehicles:
        daily_vehicular_persons += mop_tmda_daily_vehicles * sectra_occupancy_factor

    daily_transit_persons = float(dtpm_bip_daily_validations or 0) * 1.35
    weekly_ots_gross = int(round((daily_vehicular_persons + daily_transit_persons) * 7.0))

    vis_weight = calculate_visibility_index(
        area_m2=area_m2,
        tech_type=tech_type,
        illumination=illumination,
        azimuth_degrees=azimuth_degrees,
        slot_duration_sec=slot_duration_sec,
        loop_slots_total=loop_slots_total,
    )
    weekly_vac_impacts = int(round(weekly_ots_gross * vis_weight))

    return {
        "weekly_ots_gross": weekly_ots_gross,
        "visibility_index_weight": vis_weight,
        "weekly_vac_impacts": weekly_vac_impacts,
    }
