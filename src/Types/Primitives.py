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

primitive_types = [EntityType, SimulationLogType, Size2DType, AgentEntityType]
