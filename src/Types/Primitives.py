EntityType = {
    "name": "Entity Type",
    "type": "EntityType",
    "notes": "",
}
SimulationLogType = {
    "name": "Simulation Log Type",
    "type": "SimulationLogType",
    "notes": "Will be a list of entries expanding over time",
}

Size2DType = {
    "name": "2D Size Type",
    "type": "Size2DType",
    "notes": "A tuple of size two with two [[integer type]] that represents the 2D size of something",
}

AgentEntityType = {
    "name": "Agent Entity Type",
    "type": "AgentEntityType",
    "notes": "A representation of an [[Entities/Agent|agent]]",
}

IntegerType = {
    "name": "Integer Type",
    "type": "IntegerType",
    "notes": "An integer",
}

FloatType = {
    "name": "Float Type",
    "type": "FloatType",
    "notes": "A floating point number",
}

FoodType = {
    "name": "Food Type",
    "type": "FoodType",
    "notes": "A subclass of [[integer type]] which represents some amount of food",
}

LocationType = {
    "name": "Location Type",
    "type": "LocationType",
    "notes": "A type with x and y as integers representing the 0-indexed grid location",
}

AgentType = {
    "name": "Agent Type",
    "type": "AgentType",
    "notes": "A string of either 'Prey' or 'Predator'",
}

ProbabilityType = {
    "name": "Probability Type",
    "type": "ProbabilityType",
    "notes": "A probability which takes a value between 0 and 1 inclusive.",
}


primitive_types = [
    EntityType,
    SimulationLogType,
    Size2DType,
    AgentEntityType,
    IntegerType,
    FloatType,
    FoodType,
    LocationType,
    AgentType,
    ProbabilityType,
]
