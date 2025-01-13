## Description

A mechanism which increments the current timestep
## Called By
1. [[Simulation Meta Policy]]
## Domain Spaces
1. [[Timestep Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
Add the delta timestep to the current timestep

## Updates

1. [[Global]].[[Global State-Timestep|Timestep]]
## Python Implementation
```python
def increment_time_mechanism(state, params, spaces):
    state["Timestep"] += spaces[0]["Timestep"]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Meta.py#L1](../../../src/Implementations/Python/Mechanisms/Meta.py#L1)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Mechanisms/Meta.py#L2](../../../../src/Mechanisms/Meta.py#L2)

