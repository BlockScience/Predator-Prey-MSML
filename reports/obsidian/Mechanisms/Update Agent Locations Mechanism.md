## Description

A mechanism for updating the locations of agents
## Called By
1. [[Agent Movement Policy]]
## Domain Spaces
1. [[Agent Location Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
Update the agent locations in the sites and at the agent level

## Updates

1. [[Site]].[[Site State-Agent|Agent]]
2. [[Agent]].[[Agent State-Location|Location]]
## Python Implementation
```python
def update_agent_locations_mechanism(state, params, spaces):
    for entry in spaces[0]["Agent Locations"]:
        agent = entry["Agent"]
        old_loc = agent["Location"]
        loc = entry["Location"]
        assert (
            state["Sites Matrix"][loc[0]][loc[1]]["Agent"] is None
        ), "Agent is already at this location!"
        state["Sites Matrix"][old_loc[0]][old_loc[1]]["Agent"] = None
        agent["Location"] = loc
        state["Sites Matrix"][loc[0]][loc[1]]["Agent"] = agent
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Site.py](../../../src/Implementations/Python/Mechanisms/Site.py)

