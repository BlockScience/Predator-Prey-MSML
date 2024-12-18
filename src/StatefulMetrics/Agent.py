agent_stateful_metric = {
    "name": "Agent Stateful Metrics",
    "notes": "Stateful metrics for agents",
    "metrics": [
        {
            "type": "Agent Array Type",
            "name": "Prey Stateful Metric",
            "description": "The list of agents which are prey",
            "variables_used": [
                ("Global State", "Agents"),
                ("Agent State", "Agent Type"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Agent Array Type",
            "name": "Predator Stateful Metric",
            "description": "The list of agents which are predators",
            "variables_used": [
                ("Global State", "Agents"),
                ("Agent State", "Agent Type"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Integer Type",
            "name": "Number of Prey Stateful Metric",
            "description": "The number of prey",
            "variables_used": [
                ("Global State", "Agents"),
                ("Agent State", "Agent Type"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Integer Type",
            "name": "Number of Predators Stateful Metric",
            "description": "The number of predators",
            "variables_used": [
                ("Global State", "Agents"),
                ("Agent State", "Agent Type"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Food Type",
            "name": "Median Predator Food Stateful Metric",
            "description": "The median amount of food predators have",
            "variables_used": [
                ("Global State", "Agents"),
                ("Agent State", "Agent Type"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Food Type",
            "name": "Median Prey Food Stateful Metric",
            "description": "The median amount of food prey have",
            "variables_used": [
                ("Global State", "Agents"),
                ("Agent State", "Agent Type"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Integer Type",
            "name": "Median Predator Age Stateful Metric",
            "description": "The median age of predators",
            "variables_used": [
                ("Global State", "Agents"),
                ("Agent State", "Agent Type"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
        {
            "type": "Integer Type",
            "name": "Median Prey Age Stateful Metric",
            "description": "The median age of prey",
            "variables_used": [
                ("Global State", "Agents"),
                ("Agent State", "Agent Type"),
            ],
            "parameters_used": [],
            "symbol": None,
            "domain": None,
        },
    ],
}

agent_stateful_metrics = [agent_stateful_metric]
