site_metrics = []


site_metrics.append(
    {
        "type": "Food Type",
        "name": "Available Food Metric",
        "description": "A metric of the available food at each location.",
        "variables_used": [["Global State", "Sites"], ["Site State", "Food"]],
        "parameters_used": [],
        "metrics_used": [],
        "domain": ["Locations Space"],
        "logic": "Query the locations and their foods",
        "symbol": None,
    }
)
