AgentAgeDeltaArrayType = {
    "name": "Agent Age Delta Array Type",
    "type": "AgentAgeDeltaArrayType",
    "notes": """An array where the objects the form of {"Agent": [[Agent Entity Type]], "Delta Age": [[Float Type]]}""",
}

AgentArrayType = {
    "name": "Agent Array Type",
    "type": "AgentArrayType",
    "notes": """An array of [[agent entity type]]""",
}

AgentFoodDeltaArrayType = {
    "name": "Agent Food Delta Array Type",
    "type": "AgentFoodDeltaArrayType",
    "notes": """An array where the objects the form of {"Agent": [[Agent Entity Type]], "Delta Food": [[Types/Food Type|Food Type]]}""",
}


AgentLocationArrayType = {
    "name": "Agent Location Array Type",
    "type": "AgentLocationArrayType",
    "notes": """An array where the objects the form of {"Agent": [[Agent Entity Type]], "Location": [[Location Type]]}""",
}

FoodLocationArrayType = {
    "name": "Food Location Array Type",
    "type": "FoodLocationArrayType",
    "notes": """An array where the objects the form of {"Location": [[Location Type]], "Food": [[Types/Food Type|Food Type]]}""",
}

LocationsArrayType = {
    "name": "Locations Array Type",
    "type": "LocationsArrayType",
    "notes": """An array of [[Location Type]]""",
}


data_types = [
    AgentAgeDeltaArrayType,
    AgentArrayType,
    AgentFoodDeltaArrayType,
    AgentLocationArrayType,
    FoodLocationArrayType,
    LocationsArrayType,
]
