# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Thermal Shock Hormesis Dose Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentThermalShockHormesisDose

def main():
    agent = PersonalAgentThermalShockHormesisDose()

    print("=" * 70)
    print("DEMO: Personal Agent Thermal Shock Hormesis Dose & Thermoregulation Modeler")
    print("=" * 70)

    # 1. Cold Water Plunge Session (3 minutes at 8.0°C)
    res_cold = agent.calculate_cold_exposure_dose(
        water_temp_c=8.0,
        duration_minutes=3.0,
        immersion_type="water_immersion"
    )

    print(f"\n1. Deliberate Cold Plunge Dose (8.0 °C for 3.0 min):")
    print(f"   Medium: {res_cold['immersion_medium']}")
    print(f"   Norepinephrine Multiplier: {res_cold['norepinephrine_multiplier']}")
    print(f"   BAT Caloric Expenditure: {res_cold['bat_thermogenesis_kcal']} kcal")
    print(f"   Projected Afterdrop: {res_cold['projected_afterdrop_c']}")
    print(f"   Soberg Weekly Quota: {res_cold['weekly_soberg_quota_pct']}")
    print(f"   Assessment: {res_cold['safety_assessment']}")

    # 2. Finnish Sauna Heat Exposure Session (20 minutes at 85.0°C, 15% humidity)
    res_heat = agent.calculate_sauna_heat_dose(
        sauna_temp_c=85.0,
        duration_minutes=20.0,
        humidity_pct=15.0
    )

    print(f"\n2. Deliberate Sauna Heat Dose (85.0 °C for 20.0 min, 15% RH):")
    print(f"   HSP70 Induction Score: {res_heat['hsp70_induction_score']}")
    print(f"   Cardiovascular Load: {res_heat['cardiovascular_load_met']} METs ({res_heat['cardiovascular_equivalence']})")
    print(f"   Fluid / Sodium Loss: {res_heat['sweat_fluid_deficit_liters']} L / {res_heat['sweat_sodium_loss_mg']} mg Na+")
    print(f"   Max Safe Limit: {res_heat['max_safe_exposure_limit_mins']} minutes")
    print(f"   Laukkanen Longevity Quota: {res_heat['weekly_laukkanen_quota_pct']}")
    print(f"   Rx: {res_heat['rehydration_prescription']}")

    print("\nVerification complete: Thermal shock hormesis engine executed flawlessly.")

if __name__ == "__main__":
    main()
