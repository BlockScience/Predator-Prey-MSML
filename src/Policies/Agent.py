natural_death_policy1 = {
    "name": "Natural Death Policy V1",
    "description": "Anyone over the maximum age dies and anyone with no food dies",
    "logic": """Filter list by the above""",
}

natural_death_policy = {
    "name": "Natural Death Policy",
    "description": "The policy which determines which agents die.",
    "constraints": [],
    "policy_options": [natural_death_policy1],
    "domain": [
        "Agents Space",
    ],
    "codomain": [
        "Agents Space",
    ],
    "parameters_used": ["Maximum Age Parameter"],
    "metrics_used": [],
}

increase_agent_age_policy1 = {
    "name": "Increase Agent Age Policy +1",
    "description": "Simple +1 to age and -1 to food",
    "logic": """Return spaces that increase age by 1 and decrease food by 1 for all agents in the domain""",
}

increase_agent_age_policy = {
    "name": "Increase Agent Age Policy",
    "description": "The policy which determines the age increase and the decrease in food.",
    "constraints": [],
    "policy_options": [increase_agent_age_policy1],
    "domain": [
        "Agents Space",
    ],
    "codomain": ["Agent Food Delta Space", "Agent Age Delta Space"],
    "parameters_used": [],
    "metrics_used": [],
}

prey_feeding_policy_option1 = {
    "name": "Prey Eat All Food Policy",
    "description": "Eat all the food at the location",
    "logic": """For every location the prey eats all the food available""",
}

prey_feeding_policy = {
    "name": "Prey Feeding Policy",
    "description": "The policy which determines the amount of food that each location will eat.",
    "constraints": [],
    "policy_options": [prey_feeding_policy_option1],
    "domain": [
        "Agents Space",
    ],
    "codomain": ["Location Food Delta Space", "Agent Food Delta Space"],
    "parameters_used": [],
    "metrics_used": ["Available Food Metric"],
}

agent_movement_policy_option1 = {
    "name": "Random Agent Movement with Sieve",
    "description": "A policy where agents move randomly 1 square but the movements are implemented with a sieve",
    "logic": """While the length of the agents to move is greater than 0 and has reduced in size since the last iteration:
1. Iterate through the list of agents, if they have a valid tile to move to, add it to the output, and switch out the tiles from busy squares, otherwise add them to the new sieve
2. The loop terminates when the remaining agents have no space to move to or there are no more agents""",
}

agent_movement_policy = {
    "name": "Agent Movement Policy",
    "description": "The policy which determines where agents move to.",
    "constraints": [],
    "policy_options": [agent_movement_policy_option1],
    "domain": [
        "Agents Space",
    ],
    "codomain": ["Agent Location Space"],
    "parameters_used": [],
    "metrics_used": [
        "Neighboring Valid Tiles Metric",
        "Open Locations Stateful Metric",
    ],
}

hunt_prey_policy_option1 = {
    "name": "Hunt Prey V1",
    "description": "If a valid prey is in a nearby site then it is eaten. If there are multiple then there is a random choice.",
    "logic": """""",
}

hunt_prey_policy = {
    "name": "Hunt Prey Policy",
    "description": "The policy which determines how and when prey are hunted.",
    "constraints": [],
    "policy_options": [hunt_prey_policy_option1],
    "domain": [
        "Agents Space",
    ],
    "codomain": ["Agent Food Delta Space", "Agents Space"],
    "parameters_used": [],
    "metrics_used": [
        "Neighboring Valid Tiles Metric",
        "Prey Locations Stateful Metric",
        "Predator Stateful Metric",
    ],
}

agent_reproduction_policy_option1 = {
    "name": "Agent Reproduction Policy V1",
    "description": "Simple reproduction method where randomly agents will reproduce with others if they are on nearby tiles and have enough food (and are of the same type).",
    "logic": """1. Get valid prey/predators with the stateful metrics
2. Filter the agents to be only the ones which have at least the [[Reproduction Food Threshold]]
3. For the group of predators and then the group of prey do the following, where agents is the variable representing the agents of that type still in play...
A1. Create a filtered list of agents based on randomly being under [[Reproduction Probability]], these agents that will reproduce
A2. Loop over each agent in this reproduction and do the following:
AA1. Check that they are still in the agents list (have not reproduced), otherwise continue on
AA2. Find valid_mates by filtering agents array with [[Is Neighbor Metric]], if length is 0 then continue
AA3. Find valid open spaces with [[Neighboring Valid Tiles Metric]], if length is 0 then continue
AA4. Randomly pick a valid mate and a valid open location
AA5. Add to the spaces -[[Reproduction Food Needed]] for both of the mates
AA6. Add a newly created anget that has food of 2 * [[Reproduction Food Needed]]""",
}

agent_reproduction_policy = {
    "name": "Agent Reproduction Policy",
    "description": "The policy which determines if and how agents reproduce.",
    "constraints": [],
    "policy_options": [agent_reproduction_policy_option1],
    "domain": [
        "Agents Space",
    ],
    "codomain": ["Agents Space", "Agent Food Delta Space"],
    "parameters_used": [
        "Reproduction Food Threshold",
        "Reproduction Probability",
        "Reproduction Food Needed",
    ],
    "metrics_used": [
        "Open Locations Stateful Metric",
        "Neighboring Valid Tiles Metric",
        "Predator Stateful Metric",
        "Prey Stateful Metric",
        "Is Neighbor Metric",
    ],
}


agent_policies = [
    natural_death_policy,
    increase_agent_age_policy,
    prey_feeding_policy,
    agent_movement_policy,
    hunt_prey_policy,
    agent_reproduction_policy,
]
