remove_agents_mechanism = {
    "name": "Remove Agents Mechanism",
    "description": "A mechanism for removing agents",
    "constraints": [],
    "logic": """Remove the agents that are in the agents space""",
    "domain": ["Agents Space"],
    "parameters_used": [],
    "updates": [
        ("Global", "Agents", False),
    ],
}

update_food_mechanism = {
    "name": "Update Food Mechanism",
    "description": "Updates the agent food based on the delta",
    "constraints": [],
    "logic": """Updates the agent food based on the delta""",
    "domain": ["Agent Food Delta Space"],
    "parameters_used": [],
    "updates": [
        ("Agent", "Food", False),
    ],
}

increase_agent_age_mechanism = {
    "name": "Increase Agent Age Mechanism",
    "description": "A mechanism which updates agent ages",
    "constraints": [],
    "logic": """Update each agent age by iterating through the list of agent updates from the domain""",
    "domain": ["Agent Age Delta Space"],
    "parameters_used": [],
    "updates": [
        ("Agent", "Age", False),
    ],
}

agent_mechanisms = [
    remove_agents_mechanism,
    update_food_mechanism,
    increase_agent_age_mechanism,
]
