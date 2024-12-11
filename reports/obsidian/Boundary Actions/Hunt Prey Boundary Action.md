## Description

Boundary action which returns the prey that might eat.
## Called By
1. [[Agent]]

## Followed By
1. [[Hunt Prey Policy]]

## Constraints

## Codomain Spaces
1. [[Agents Space]]

## Metrics Used
1. [[Predator Stateful Metric]]

## Parameters Used
1. [[Hunger Threshold]]

## Boundary Action Options:
### 1. Hunt Prey Boundary Action V1
#### Description
All hungry predators seek out to eat prey
#### Logic
Filter to just predators and then filter out any predators that are not hungry.
#### Python Implementation
```python
def hunt_prey_boundary_action_v1(state, params, spaces):
    predators = state["Stateful Metrics"]["Predator Stateful Metric"](state, params)
    predators = [x for x in predators if x["Food"] <= params["Hunger Threshold"]]
    shuffle(predators)
    return [{"Agents": predators}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/BoundaryActions/Agent.py](../../../src/Implementations/Python/BoundaryActions/Agent.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/BoundaryActions/Agent.py](../../../../src/BoundaryActions/Agent.py)

