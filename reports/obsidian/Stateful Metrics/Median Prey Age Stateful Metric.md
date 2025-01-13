Description: The median age of prey

Type: [[Integer Type]]

Symbol: None

Domain: None

## Parameters Used

## Variables Used
1. [[Global State]].Agents
2. [[Agent State]].Agent Type

## Python Implementation
```python
def median_prey_age_stateful_metric(state, params):
    prey = [
        x["Age"]
        for x in state["Stateful Metrics"]["Prey Stateful Metric"](state, params)
    ]
    return median(prey) if len(prey) > 0 else None
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/StatefulMetrics/Agent.py#L44](../../../src/Implementations/Python/StatefulMetrics/Agent.py#L44)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/StatefulMetrics/Agent.py#L91](../../../../src/StatefulMetrics/Agent.py#L91)

