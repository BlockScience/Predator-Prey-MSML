agent_parameter_set = {
    "name": "Agent Parameter Set",
    "notes": "A set parameters for agents",
    "parameters": [
        {
            "variable_type": "Food Type",
            "name": "Hunger Threshold",
            "description": "The threshold for when an agent becomes hungry",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Float Type",
            "name": "Maximum Age Parameter",
            "description": "The maximum age an agent can reach",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
        {
            "variable_type": "Food Type",
            "name": "Reproduction Food Threshold",
            "description": "The amount of food needed for an agent to reporduce",
            "symbol": None,
            "domain": None,
            "parameter_class": "System",
        },
    ],
}


agent_parameter_sets = [agent_parameter_set]
