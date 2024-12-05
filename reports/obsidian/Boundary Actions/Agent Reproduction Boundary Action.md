## Description

Boundary action which determines which agents are eligible for reproduction.
## Called By
1. [[Agent]]

## Followed By
1. [[Agent Reproduction Policy]]

## Constraints

## Codomain Spaces
1. [[Agents Space]]

## Metrics Used

## Parameters Used
1. [[Reproduction Food Threshold]]

## Boundary Action Options:
### 1. Reproduction Threshold Reproduction Boundary Action
#### Description
All agents with food equal to or over the reproduction threshold reproduce
#### Logic
Return all agents eligible for reproduction after shuffling
#### Python Implementation
```python
def reproduction_threshold_reproduction_boundary_action(state, params, spaces):
    agents = [
        x for x in state["Agents"] if x["Food"] >= params["Reproduction Food Threshold"]
    ]
    shuffle(agents)
    return [{"Agents": agents}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/BoundaryActions/Agent.py](../../../src/Implementations/Python/BoundaryActions/Agent.py)

