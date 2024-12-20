## Description

Returns a list of potential agents that should have their age increased
## Followed By
1. [[Increase Agent Age Policy]]

## Constraints
## Codomain Spaces
1. [[Agents Space]]

## Metrics Used

## Parameters Used

## Control Action Options:
### 1. Increase Age Control Action V1
#### Description
Simply return all agents
#### Logic
Return all agents
#### Python Implementation
```python
def increase_agent_age_control_action_v1(state, params, spaces):
    return [{"Agents": state["Agents"]}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/ControlActions/Agent.py#L5](../../../src/Implementations/Python/ControlActions/Agent.py#L5)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/ControlActions/Agent.py#L23](../../../../src/ControlActions/Agent.py#L23)

