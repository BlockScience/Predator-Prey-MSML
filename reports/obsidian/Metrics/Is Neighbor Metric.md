Description: A metric for filtering to only neighboring tiles.

Type: [[Location Type]]

Symbol: None

## Logic
For each of the agents in the first domain, query to find which of the agents in the second space are valid neighbors and return as a nested list for each location all their valid neighbors

## Parameters Used
1. [[Site Size]]

## Variables Used

## Domain Spaces
1. [[Agents Space]]
2. [[Agents Space]]
## Metrics Used
## Python Implementation
```python
def is_neighbor_metric(state, params, spaces):
    out = []
    query_agents = spaces[0]["Agents"]
    other_agents = spaces[1]["Agents"]
    for agent in query_agents:
        neighbors = other_agents
        x = agent["Location"][0]
        y = agent["Location"][1]
        neighbors = [a for a in neighbors if a != agent]
        neighbors = [
            a
            for a in neighbors
            if (abs(x - a["Location"][0]) + abs(y - a["Location"][1])) == 1
        ]
        out.append(neighbors)
    return out
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Metrics/Agent.py](../../../src/Implementations/Python/Metrics/Agent.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Metrics/Site.py](../../../../src/Metrics/Site.py)

