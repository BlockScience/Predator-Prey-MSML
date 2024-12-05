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

site_metrics.append(
    {
        "type": "Location Type",
        "name": "Neighboring Valid Tiles Metric",
        "description": "A metric of the non-busy tiles that are neighbors. The first domain element is the locations to query, the second is the busy tiles (or the free tiles if you want to flip it and have the returned values be the potential mates/tiles where there is a neighboring agent).",
        "variables_used": [],
        "parameters_used": ["Site Size"],
        "metrics_used": [],
        "domain": ["Locations Space", "Locations Space"],
        "logic": "Query the location neighbors then filter out any that are busy",
        "symbol": None,
    }
)
