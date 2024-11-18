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
