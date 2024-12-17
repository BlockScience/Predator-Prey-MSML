Description: The median food in sites

Type: [[Food Type]]

Symbol: None

Domain: None

## Parameters Used

## Variables Used
1. [[Global State]].Sites
2. [[Site State]].Food

## Python Implementation
```python
def median_site_food_stateful_metric(state, params):
    return median([x["Food"] for x in state["Sites"]])
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/StatefulMetrics/Site.py](../../../src/Implementations/Python/StatefulMetrics/Site.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/StatefulMetrics/Site.py](../../../../src/StatefulMetrics/Site.py)

