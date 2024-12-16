simulation_meta_policy_option1 = {
    "name": "Simulation Meta Policy V1",
    "description": "Baseline simulation meta policy.",
    "logic": """The timestep will be incremented by 1 and a full simulation log will be returned.""",
}

simulation_meta_policy = {
    "name": "Simulation Meta Policy",
    "description": "The policy which determines the simulation metadata updates.",
    "constraints": [],
    "policy_options": [simulation_meta_policy_option1],
    "domain": [],
    "codomain": [
        "Timestep Space",
        "Simulation Log Space",
    ],
    "parameters_used": [],
    "metrics_used": [],
}


meta_policies = [simulation_meta_policy]
