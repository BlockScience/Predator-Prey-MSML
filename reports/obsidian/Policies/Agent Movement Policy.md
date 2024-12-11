## Description

The policy which determines where agents move to.
## Called By
1. [[Agent Movement Boundary Action]]
## Domain Spaces
1. [[Agents Space]]
## Followed By
1. [[Update Agent Locations Mechanism]]
## Codomain Spaces
1. [[Agent Location Space]]
## Constraints
## Parameters Used
## Metrics Used
1. [[Neighboring Valid Tiles Metric]]
2. [[Open Locations Stateful Metric]]
## Policy Options
### 1. Random Agent Movement with Sieve
#### Description
A policy where agents move randomly 1 square but the movements are implemented with a sieve
#### Logic
While the length of the agents to move is greater than 0 and has reduced in size since the last iteration:
1. Iterate through the list of agents, if they have a valid tile to move to, add it to the output, and switch out the tiles from busy squares, otherwise add them to the new sieve
2. The loop terminates when the remaining agents have no space to move to or there are no more agents
#### Python Implementation
```python
def random_agent_movement_with_sieve(state, params, spaces):
    sieve = spaces[0]["Agents"]
    open_locations = state["Stateful Metrics"]["Open Locations Stateful Metric"](
        state, params
    )
    open_locations = [x["Location"] for x in open_locations]
    out_space = {"Agent Locations": []}
    last = -1

    while len(sieve) > 0 and len(sieve) != last:
        last = len(sieve)
        hold = []
        while len(sieve) > 0:
            curr = sieve.pop()
            options = state["Metrics"]["Neighboring Valid Tiles Metric"](
                state,
                params,
                [{"Locations": [curr["Location"]]}, {"Locations": open_locations}],
            )[0]
            if len(options) == 0:
                hold.append(curr)
            else:
                new = choice(list(options))
                old = curr["Location"]
                open_locations.append(old)
                open_locations.remove(new)
                out_space["Agent Locations"].append({"Agent": curr, "Location": new})

        sieve = hold
    return [out_space]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Agent.py](../../../src/Implementations/Python/Policies/Agent.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Policies/Agent.py](../../../../src/Policies/Agent.py)

