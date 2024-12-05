agent_wiring = []

agent_wiring.append(
    {
        "name": "Natural Death Wiring",
        "components": [
            "Natural Death Control Action",
            "Natural Death Policy",
            "Remove Agents Mechanism",
        ],
        "description": "Wiring for growth of food",
        "constraints": [],
        "type": "Stack",
    }
)

agent_wiring.append(
    {
        "name": "Age & Food Mechanisms",
        "components": [
            "Update Food Mechanism",
            "Increase Agent Age Mechanism",
        ],
        "description": "Mechanisms for updating food and age",
        "constraints": [],
        "type": "Parallel",
    }
)


agent_wiring.append(
    {
        "name": "Increase Agent Age Wiring",
        "components": [
            "Increase Age Control Action",
            "Increase Agent Age Policy",
            "Age & Food Mechanisms",
        ],
        "description": "Wiring for updating of the agent age and decreasing their food from aging",
        "constraints": [],
        "type": "Stack",
    }
)

agent_wiring.append(
    {
        "name": "Food Eating Mechanisms",
        "components": [
            "Update Food Locations Mechanism",
            "Update Food Mechanism",
        ],
        "description": "Mechanisms for when food is eaten by prey",
        "constraints": [],
        "type": "Parallel",
    }
)

agent_wiring.append(
    {
        "name": "Prey Feeding Wiring",
        "components": [
            "Prey Feeding Boundary Action",
            "Prey Feeding Policy",
            "Food Eating Mechanisms",
        ],
        "description": "Wiring for when prey eats food",
        "constraints": [],
        "type": "Stack",
    }
)


agent_wiring.append(
    {
        "name": "Agent Movement Wiring",
        "components": [
            "Agent Movement Boundary Action",
            "Agent Movement Policy",
            "Update Agent Locations Mechanism",
        ],
        "description": "Wiring for agents moving",
        "constraints": [],
        "type": "Stack",
    }
)

agent_wiring.append(
    {
        "name": "Hunt Prey Wiring",
        "components": [
            "Hunt Prey Boundary Action",
            "Hunt Prey Policy",
            "Prey Eaten Mechanisms",
        ],
        "description": "Wiring for agents hunting prey",
        "constraints": [],
        "type": "Stack",
    }
)

agent_wiring.append(
    {
        "name": "Prey Eaten Mechanisms",
        "components": [
            "Update Food Mechanism",
            "Remove Agents Mechanism",
        ],
        "description": "Wiring for predators eating prey",
        "constraints": [],
        "type": "Parallel",
    }
)

agent_wiring.append(
    {
        "name": "Agent Reproduction Wiring",
        "components": [
            "Agent Reproduction Boundary Action",
            "Agent Reproduction Policy",
            "Agent Reproduction Mechanisms",
        ],
        "description": "Wiring for agents hunting prey",
        "constraints": [],
        "type": "Stack",
    }
)

agent_wiring.append(
    {
        "name": "Agent Reproduction Mechanisms",
        "components": [
            "Create Agents Mechanism",
            "Update Food Mechanism",
        ],
        "description": "Wiring for reproduction",
        "constraints": [],
        "type": "Parallel",
    }
)
