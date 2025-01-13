Description: The number of prey

Type: [[Integer Type]]

Symbol: None

Domain: None

## Parameters Used

## Variables Used
1. [[Global State]].Agents
2. [[Agent State]].Agent Type

## Python Implementation
```python
def number_of_prey_stateful_metric(state, params):
    return len(state["Stateful Metrics"]["Prey Stateful Metric"](state, params))
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/StatefulMetrics/Agent.py#L12](../../../src/Implementations/Python/StatefulMetrics/Agent.py#L12)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/StatefulMetrics/Agent.py#L31](../../../../src/StatefulMetrics/Agent.py#L31)

