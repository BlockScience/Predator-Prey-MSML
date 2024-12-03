## Description

A mechanism which creates a new agent
## Called By
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
2. [[Global]].[[Global State-Sites|Sites]]
## Python Implementation
```python
def create_agents_mechanism(state, params, spaces):
    pass
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Agent.py](../../../src/Implementations/Python/Mechanisms/Agent.py)

