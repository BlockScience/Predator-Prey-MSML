## Description

Boundary action which returns the prey that might eat.
## Called By
1. [[Agent]]

## Followed By
1. [[Prey Feeding Policy]]

## Constraints

## Codomain Spaces
1. [[Agents Space]]

## Metrics Used
1. [[Prey Stateful Metric]]

## Parameters Used
1. [[Hunger Threshold]]

## Boundary Action Options:
### 1. Prey Feeding Boundary Action V1
#### Description
All hungry prey eats
#### Logic
Filter to just prey and then filter out any prey that are not hungry.
#### Python Implementation
```python
def prey_feeding_boundary_action_v1(state, params, spaces):
    prey = state["Stateful Metrics"]["Prey Stateful Metric"](state, params)
    prey = [x for x in prey if x["Food"] <= params["Hunger Threshold"]]
    return [{"Agents": prey}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/BoundaryActions/Agent.py](../../../src/Implementations/Python/BoundaryActions/Agent.py)

