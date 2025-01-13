## Description

A mechanism which updates agent ages
## Called By
1. [[Increase Agent Age Policy]]
## Domain Spaces
1. [[Agent Age Delta Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
Update each agent age by iterating through the list of agent updates from the domain

## Updates

1. [[Agent]].[[Agent State-Age|Age]]
## Python Implementation
```python
def update_agent_age_mechanism(state, params, spaces):
    for values in spaces[0]["Age Deltas"]:
        values["Agent"]["Age"] += values["Delta Age"]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Agent.py#L16](../../../src/Implementations/Python/Mechanisms/Agent.py#L16)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Mechanisms/Agent.py#L26](../../../../src/Mechanisms/Agent.py#L26)

