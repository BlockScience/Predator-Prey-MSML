## Description

Returns a list of potential agents that might die
## Followed By
1. [[Natural Death Policy]]

## Constraints
## Codomain Spaces
1. [[Agents Space]]

## Metrics Used

## Parameters Used

## Control Action Options:
### 1. Natural Death Control Action V1
#### Description
Simply return all agents
#### Logic
Return all agents
#### Python Implementation
```python
def natural_death_control_action_v1(state, params, spaces):
    return [{"Agents": state["Agents"]}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/ControlActions/Agent.py#L1](../../../src/Implementations/Python/ControlActions/Agent.py#L1)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/ControlActions/Agent.py#L2](../../../../src/ControlActions/Agent.py#L2)

