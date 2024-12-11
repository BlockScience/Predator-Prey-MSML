## Description

Returns a list of locations that might potentially have food growth
## Followed By
1. [[Food Growth Policy]]

## Constraints
## Codomain Spaces
1. [[Locations Space]]

## Metrics Used

## Parameters Used
1. [[Maximum Food per Tile]]

## Control Action Options:
### 1. Food Growth Control Action V1
#### Description
Simply pick all sites that do not have the maximum food yet
#### Logic
Filter out sites with maximum food and otherwise pass the rest through
#### Python Implementation
```python
def food_growth_control_action_v1(state, params, spaces):
    sites = [
        site
        for site in state["Sites"]
        if site["Food"] < params["Maximum Food per Tile"]
    ]
    return [{"Locations": sites}]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/ControlActions/Site.py](../../../src/Implementations/Python/ControlActions/Site.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/ControlActions/Site.py](../../../../src/ControlActions/Site.py)

