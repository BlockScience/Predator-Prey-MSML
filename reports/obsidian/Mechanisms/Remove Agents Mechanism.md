## Description

A mechanism for removing agents
## Called By
1. [[Natural Death Policy]]
## Domain Spaces
1. [[Agents Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
Remove the agents that are in the agents space

## Updates

1. [[Global]].[[Global State-Agents|Agents]]
## Python Implementation
```python
def remove_agents_mechanism(state, params, spaces):
    state["Agents"] = [
        agent for agent in state["Agents"] if agent not in spaces[0]["Agents"]
    ]
    for agent in spaces[0]["Agents"]:
        state["Sites Matrix"][agent["Location"][0]][agent["Location"][1]][
            "Agent"
        ] = None
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Agent.py](../../../src/Implementations/Python/Mechanisms/Agent.py)

