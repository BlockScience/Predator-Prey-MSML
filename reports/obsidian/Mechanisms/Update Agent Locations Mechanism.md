## Description

A mechanism for updating the locations of agents
## Called By
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
    pass
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Site.py](../../../src/Implementations/Python/Mechanisms/Site.py)

