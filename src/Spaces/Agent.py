agents_space = {
    "name": "Agents Space",
    "schema": {
        "Agents": "Agent Array Type",
    },
}

agent_age_delta_space = {
    "name": "Agent Age Delta Space",
    "schema": {
        "Age Deltas": "Agent Age Delta Array Type",
    },
}

agent_food_delta_space = {
    "name": "Agent Food Delta Space",
    "schema": {
        "Food Deltas": "Agent Food Delta Array Type",
    },
}

agent_locations_space = {
    "description": "The space for denoting the locations of some agents",
    "name": "Agent Location Space",
    "schema": {
        "Agent Locations": "Agent Location Array Type",
    },
}


agents_spaces = [
    agents_space,
    agent_age_delta_space,
    agent_food_delta_space,
    agent_locations_space,
]
