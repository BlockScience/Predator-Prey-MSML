natural_death_policy1 = {
    "name": "Natural Death Policy V1",
    "description": "Anyone over the maximum age dies and anyone with no food dies",
    "logic": """Filter list by the above""",
}

natural_death_policy = {
    "name": "Natural Death Policy",
    "description": "The policy which determines which agents die.",
    "constraints": [],
    "policy_options": [natural_death_policy1],
    "domain": [
        "Agents Space",
    ],
    "codomain": [
        "Agents Space",
    ],
    "parameters_used": ["Maximum Age Parameter"],
    "metrics_used": [],
}

agent_policies = [natural_death_policy]
