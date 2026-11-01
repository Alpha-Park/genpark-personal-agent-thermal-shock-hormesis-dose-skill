# -*- coding: utf-8 -*-
"""
Personal Agent Thermal Shock Hormesis Dose Client
Zero-dependency deliberate cold exposure (cryo/cold plunge) and deliberate heat exposure
(sauna) hormesis dose calculator, HSP70 induction modeler, and thermoregulation safety guard.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentThermalShockHormesisDose:
    """
    Quantifies cold and heat hormetic stimuli, tracking plasma norepinephrine surges,
    brown adipose tissue (BAT) thermogenesis, Heat Shock Protein (HSP70) upregulation,
    and post-exposure afterdrop temperature safety margins.
    """

    def calculate_cold_exposure_dose(
        self,
        water_temp_c: float,
        duration_minutes: float,
        immersion_type: str = "water_immersion"
    ) -> Dict[str, Any]:
        """
        Calculates neurochemical and metabolic response to deliberate cold exposure.
        Norepinephrine multiplier surges up to 530% below 15°C.
        """
        temp = max(1.0, min(24.0, float(water_temp_c)))
        dur = max(0.5, min(30.0, float(duration_minutes)))

        # Thermal gradient relative to standard skin temperature (33°C)
        gradient = max(0.0, 33.0 - temp)

        # Convective thermal transfer coefficient: water vs air
        is_water = "water" in immersion_type.lower() or "plunge" in immersion_type.lower()
        transfer_coeff = 24.0 if is_water else 1.0

        # Norepinephrine surge multiplier (up to 5.3x baseline at <= 4.5°C)
        if temp <= 15.0:
            ne_surge_factor = round(min(5.3, 1.0 + 4.3 * ((15.0 - temp) / 10.5)), 2)
        else:
            ne_surge_factor = 1.0

        # Brown Adipose Tissue (BAT) non-shivering thermogenesis (kcal)
        # Scaled by thermal gradient and exposure duration
        bat_kcal = round((gradient / 33.0) * (dur * 4.2) * (1.5 if is_water else 0.4), 1)

        # Core temperature afterdrop projection (Celsius drop 10-20 min post immersion)
        expected_afterdrop_c = round(min(1.8, 0.05 * dur * (gradient / 20.0) if is_water else 0.01 * dur), 2)

        # Minimum effective weekly threshold (Søberg Principle: 11 mins/week total)
        weekly_target_pct = round((dur / 11.0) * 100.0, 1)

        if temp < 5.0 and dur > 5.0:
            safety_warning = "HIGH HYPOTHERMIA RISK: Limit water immersion to <= 3-5 minutes at < 5°C."
        elif dur > 15.0 and is_water:
            safety_warning = "PROLONGED IMMERSION: Risk of motor impairment. Re-warm actively with horse stance."
        else:
            safety_warning = "OPTIMAL HORMESIS: Safe window. Allow spontaneous shivering for maximum BAT activation."

        return {
            "water_temp_c": temp,
            "duration_minutes": dur,
            "immersion_medium": "Cold Water Plunge" if is_water else "Cold Air / Cryo Chamber",
            "norepinephrine_multiplier": f"{ne_surge_factor}x baseline",
            "bat_thermogenesis_kcal": bat_kcal,
            "projected_afterdrop_c": f"-{expected_afterdrop_c} °C",
            "weekly_soberg_quota_pct": f"{weekly_target_pct}% of 11-min target",
            "safety_assessment": safety_warning,
            "rewarming_protocol": "End on cold. Do not immediately enter hot shower to preserve metabolic afterburn."
        }

    def calculate_sauna_heat_dose(
        self,
        sauna_temp_c: float,
        duration_minutes: float,
        humidity_pct: float = 15.0
    ) -> Dict[str, Any]:
        """
        Calculates cardiovascular strain, Heat Shock Protein (HSP70) kinetics,
        and sweat fluid requirements during deliberate sauna hyperthermia.
        """
        temp = max(50.0, min(115.0, float(sauna_temp_c)))
        dur = max(5.0, min(60.0, float(duration_minutes)))
        hum = max(5.0, min(100.0, float(humidity_pct)))

        # Effective thermal stress index (heat index approximation)
        thermal_stress_idx = temp + (hum * 0.18)

        # Heat Shock Protein (HSP70) activation score (threshold at ~75°C)
        temp_above_baseline = max(0.0, temp - 70.0)
        hsp70_score = round(min(100.0, (temp_above_baseline * 1.8) + (dur * 1.5) + (hum * 0.2)), 1)

        # Cardiovascular exertion equivalence: heart rate elevates to 110-150 bpm
        cardio_met_equiv = round(min(5.5, 1.5 + (temp_above_baseline * 0.06) + (dur * 0.03)), 1)
        cardio_equiv_str = "Brisk Walking / Zone 1" if cardio_met_equiv < 3.0 else ("Moderate Jogging / Zone 2" if cardio_met_equiv < 4.5 else "Vigorous Aerobic Exercise / Zone 3")

        # Estimated perspiration fluid loss (Liters)
        perspiration_liters = round(max(0.2, (dur / 60.0) * (0.8 + 0.015 * temp_above_baseline)), 2)
        sodium_loss_mg = round(perspiration_liters * 900.0)

        # Safe maximum exposure limit (minutes) to prevent core temp exceeding 38.8°C
        max_safe_mins = round(max(10.0, 45.0 - (temp_above_baseline * 0.6) - (hum * 0.15)), 0)

        # Weekly target (Laukkanen Cardiovascular Longevity Target: 57 mins/week total)
        weekly_laukkanen_pct = round((dur / 57.0) * 100.0, 1)

        return {
            "sauna_temperature_c": temp,
            "duration_minutes": dur,
            "humidity_pct": hum,
            "hsp70_induction_score": f"{hsp70_score} / 100",
            "cardiovascular_load_met": cardio_met_equiv,
            "cardiovascular_equivalence": cardio_equiv_str,
            "sweat_fluid_deficit_liters": perspiration_liters,
            "sweat_sodium_loss_mg": sodium_loss_mg,
            "max_safe_exposure_limit_mins": int(max_safe_mins),
            "weekly_laukkanen_quota_pct": f"{weekly_laukkanen_pct}% of 57-min longevity target",
            "rehydration_prescription": f"Consume {perspiration_liters} L water with {sodium_loss_mg} mg sodium post session."
        }
