## Description

A mechanism which adds to the simulation log
## Called By
1. [[Simulation Meta Policy]]
## Domain Spaces
1. [[Simulation Log Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
Append the space to the simulation log

## Updates

1. [[Global]].[[Global State-Simulation Log|Simulation Log]]
## Python Implementation
```python
def log_simulation_data_mechanism(state, params, spaces):
    state["Simulation Log"].append(spaces[0])
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Meta.py#L5](../../../src/Implementations/Python/Mechanisms/Meta.py#L5)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Mechanisms/Meta.py#L14](../../../../src/Mechanisms/Meta.py#L14)

