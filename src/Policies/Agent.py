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

increase_agent_age_policy1 = {
    "name": "Increase Agent Age Policy +1",
    "description": "Simple +1 to age and -1 to food",
    "logic": """Return spaces that increase age by 1 and decrease food by 1 for all agents in the domain""",
}

increase_agent_age_policy = {
    "name": "Increase Agent Age Policy",
    "description": "The policy which determines the age increase and the decrease in food.",
    "constraints": [],
    "policy_options": [increase_agent_age_policy1],
    "domain": [
        "Agents Space",
    ],
    "codomain": ["Agent Food Delta Space", "Agent Age Delta Space"],
    "parameters_used": [],
    "metrics_used": [],
}


agent_policies = [natural_death_policy, increase_agent_age_policy]
