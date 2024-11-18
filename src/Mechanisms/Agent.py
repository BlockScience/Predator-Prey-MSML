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


agent_mechanisms = [
    remove_agents_mechanism,
]
