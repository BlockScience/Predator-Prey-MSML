## Description

Updates the agent food based on the delta
## Called By
1. [[Increase Agent Age Policy]]
2. [[Prey Feeding Policy]]
3. [[Hunt Prey Policy]]
4. [[Agent Reproduction Policy]]
## Domain Spaces
1. [[Agent Food Delta Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
Updates the agent food based on the delta

## Updates

1. [[Agent]].[[Agent State-Food|Food]]
## Python Implementation
```python
def update_food_mechanism(state, params, spaces):
    for values in spaces[0]["Food Deltas"]:
        values["Agent"]["Food"] += values["Delta Food"]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Agent.py](../../../src/Implementations/Python/Mechanisms/Agent.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Mechanisms/Agent.py](../../../../src/Mechanisms/Agent.py)

