Description: The list of agents which are prey

Type: [[Agent Array Type]]

Symbol: None

Domain: None

## Parameters Used

## Variables Used
1. [[Global State]].Agents
2. [[Agent State]].Agent Type

## Python Implementation
```python
def prey_stateful_metric(state, params):
    return [agent for agent in state["Agents"] if agent["Agent Type"] == "Prey"]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/StatefulMetrics/Agent.py#L4](../../../src/Implementations/Python/StatefulMetrics/Agent.py#L4)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/StatefulMetrics/Agent.py#L7](../../../../src/StatefulMetrics/Agent.py#L7)

