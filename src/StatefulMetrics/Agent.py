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
    ],
}

agent_stateful_metrics = [agent_stateful_metric]
