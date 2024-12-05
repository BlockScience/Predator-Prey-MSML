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


site_metrics.append(
    {
        "type": "Location Type",
        "name": "Is Neighbor Metric",
        "description": "A metric for filtering to only neighboring tiles.",
        "variables_used": [],
        "parameters_used": ["Site Size"],
        "metrics_used": [],
        "domain": ["Locations Space", "Locations Space"],
        "logic": "For each of the locations in the first domain, query to find which of the locations in the second space are valid neighbors and return as a nested list for each location all their valid neighbors",
        "symbol": None,
    }
)
