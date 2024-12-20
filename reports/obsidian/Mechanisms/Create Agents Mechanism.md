## Description

A mechanism which creates a new agent
## Called By
1. [[Agent Reproduction Policy]]
## Domain Spaces
1. [[Agents Space]]
## Constraints
1. The locations of the new agents must not be in use already
## Metrics Used

## Parameters Used

## Logic
Adds the new agents to the agents array and updates the locations matrix

## Updates

1. [[Global]].[[Global State-Agents|Agents]]
2. [[Site]].[[Site State-Agent|Agent]]
## Python Implementation
```python
def create_agents_mechanism(state, params, spaces):
    for agent in spaces[0]["Agents"]:
        loc = agent["Location"]
        assert (
            state["Sites Matrix"][loc[0]][loc[1]]["Agent"] is None
        ), "Agent is already at this location!"
        state["Agents"].append(agent)
        state["Sites Matrix"][loc[0]][loc[1]]["Agent"] = agent
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Agent.py#L21](../../../src/Implementations/Python/Mechanisms/Agent.py#L21)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Mechanisms/Agent.py#L38](../../../../src/Mechanisms/Agent.py#L38)

