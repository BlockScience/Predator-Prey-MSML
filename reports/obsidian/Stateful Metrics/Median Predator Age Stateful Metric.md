Description: The median age of predators

Type: [[Age Type]]

Symbol: None

Domain: None

## Parameters Used

## Variables Used
1. [[Global State]].Agents
2. [[Agent State]].Agent Type

## Python Implementation
```python
def median_predator_age_stateful_metric(state, params):
    return median(
        [
            x["Age"]
            for x in state["Stateful Metrics"]["Predator Stateful Metric"](
                state, params
            )
        ]
    )
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/StatefulMetrics/Agent.py](../../../src/Implementations/Python/StatefulMetrics/Agent.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/StatefulMetrics/Agent.py](../../../../src/StatefulMetrics/Agent.py)

