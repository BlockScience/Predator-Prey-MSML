Description: The list of open sites with no agent

Type: [[Locations Array Type]]

Symbol: None

Domain: None

## Parameters Used

## Variables Used
1. [[Global State]].Sites
2. [[Site State]].Agent

## Python Implementation
```python
def open_locations_stateful_metric(state, params):
    return [site for site in state["Sites"] if site["Agent"] is None]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/StatefulMetrics/Site.py](../../../src/Implementations/Python/StatefulMetrics/Site.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/StatefulMetrics/Site.py](../../../../src/StatefulMetrics/Site.py)

