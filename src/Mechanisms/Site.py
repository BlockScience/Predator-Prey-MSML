update_food_locations_mechanism = {
    "name": "Update Food Locations Mechanism",
    "description": "A mechanism for updating food locations",
    "constraints": [],
    "logic": """Add the delta food to each locations food amount""",
    "domain": ["Location Food Delta Space"],
    "parameters_used": [],
    "updates": [
        ("Site", "Food", False),
    ],
}

update_agent_locations_mechanism = {
    "name": "Update Agent Locations Mechanism",
    "description": "A mechanism for updating the locations of agents",
    "constraints": [],
    "logic": """Update the agent locations in the sites and at the agent level""",
    "domain": ["Agent Location Space"],
    "parameters_used": [],
    "updates": [
        ("Site", "Agent", False),
        ("Agent", "Location", False),
    ],
}

site_mechanisms = [update_food_locations_mechanism, update_agent_locations_mechanism]
