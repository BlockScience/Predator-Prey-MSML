food_growth_policy_option1 = {
    "name": "Constant Food Growth Policy",
    "description": "Add a constant rate of food growth to each location up to the maximum",
    "logic": """For each location, the delta is equal to min(Food + params["Food Growth Rate"], params["Maximum Food per Tile"])""",
}

food_growth_policy_option2 = {
    "name": "Poisson Food Growth Policy",
    "description": "Food growth is based on the Poisson distribution",
    "logic": """For each location, the delta is equal to min(Food + POISSON(params["Food Growth Rate"]), params["Maximum Food per Tile"])""",
}

food_growth_policy = {
    "name": "Food Growth Policy",
    "description": "The policy determines the amount of food growth per site.",
    "constraints": [],
    "policy_options": [food_growth_policy_option1, food_growth_policy_option2],
    "domain": [
        "Locations Space",
    ],
    "codomain": [
        "Location Food Delta Space",
    ],
    "parameters_used": ["Food Growth Rate", "Maximum Food per Tile"],
    "metrics_used": [],
}

site_policies = [food_growth_policy]
