site_stateful_metrics = {
    "name": "Site Stateful Metrics",
    "notes": "Stateful metrics for sites",
    "metrics": [
        {
            "type": "Locations Array Type",
            "name": "Open Locations Stateful Metric",
            "description": "The list of open sites with no agent",
            "variables_used": [("Global State", "Sites"), ("Site State", "Agent")],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Locations Array Type",
            "name": "Filled Locations Stateful Metric",
            "description": "The list of sites with agents on them",
            "variables_used": [("Global State", "Sites"), ("Site State", "Agent")],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Locations Array Type",
            "name": "Prey Locations Stateful Metric",
            "description": "The list of sites with prey on them",
            "variables_used": [("Global State", "Sites"), ("Site State", "Agent")],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Locations Array Type",
            "name": "Predator Locations Stateful Metric",
            "description": "The list of sites with predators on them",
            "variables_used": [("Global State", "Sites"), ("Site State", "Agent")],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Food Type",
            "name": "Median Site Food Stateful Metric",
            "description": "The median food in sites",
            "variables_used": [("Global State", "Sites"), ("Site State", "Food")],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
    ],
}


site_stateful_metrics = [site_stateful_metrics]
