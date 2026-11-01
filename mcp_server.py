# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Thermal Shock Hormesis Dose Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentThermalShockHormesisDose

mcp = FastMCP("PersonalAgentThermalShockHormesisDose")
client = PersonalAgentThermalShockHormesisDose()

@mcp.tool()
def calculate_cold_exposure_dose(
    water_temp_c: float,
    duration_minutes: float,
    immersion_type: str = "water_immersion"
) -> str:
    """Calculates neurochemical surge, BAT thermogenesis, and safety margins for deliberate cold exposure."""
    import json
    return json.dumps(client.calculate_cold_exposure_dose(water_temp_c, duration_minutes, immersion_type), indent=2)

@mcp.tool()
def calculate_sauna_heat_dose(
    sauna_temp_c: float,
    duration_minutes: float,
    humidity_pct: float = 15.0
) -> str:
    """Calculates cardiovascular load, HSP70 induction, and electrolyte loss for deliberate heat exposure."""
    import json
    return json.dumps(client.calculate_sauna_heat_dose(sauna_temp_c, duration_minutes, humidity_pct), indent=2)

if __name__ == "__main__":
    mcp.run()
