## Description

Boundary action which determines which agents can move and also the ordering of which ones move first.
## Called By
1. [[Agent]]

## Followed By
1. [[Agent Movement Policy]]

## Constraints

## Codomain Spaces
1. [[Agents Space]]

## Metrics Used

## Parameters Used

## Boundary Action Options:
### 1. All Agents Movement
#### Description
All agents move
#### Logic
Return all agents after randomly shuffling the order
#### Python Implementation
```python
def all_agents_move(state, params, spaces):
    agents = [x for x in state["Agents"]]
    shuffle(agents)
    return [{"Agents": agents}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/BoundaryActions/Agent.py#L17](../../../src/Implementations/Python/BoundaryActions/Agent.py#L17)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/BoundaryActions/Agent.py#L50](../../../../src/BoundaryActions/Agent.py#L50)

