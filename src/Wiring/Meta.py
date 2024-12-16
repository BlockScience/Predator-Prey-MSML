meta_wiring = []

meta_wiring.append(
    {
        "name": "Simulation Meta Wiring",
        "components": [
            "Simulation Meta Policy",
            "Simulation Meta Mechanisms",
        ],
        "description": "Wiring for meta simulation steps",
        "constraints": [],
        "type": "Stack",
    }
)

meta_wiring.append(
    {
        "name": "Simulation Meta Mechanisms",
        "components": [
            "Increment Time Mechanism",
            "Log Simulation Data Mechanism",
        ],
        "description": "Wiring for mechanisms that update the simulation log and simulation metadata",
        "constraints": [],
        "type": "Parallel",
    }
)
