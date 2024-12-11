## Description

A mechanism for updating food locations
## Called By
1. [[Food Growth Policy]]
2. [[Prey Feeding Policy]]
## Domain Spaces
1. [[Location Food Delta Space]]
## Constraints
## Metrics Used

## Parameters Used

## Logic
Add the delta food to each locations food amount

## Updates

1. [[Site]].[[Site State-Food|Food]]
## Python Implementation
```python
def update_food_locations_mechanism(state, params, spaces):
    for loc in spaces[0]["Food Locations"]:
        state["Sites Matrix"][loc["Location"][0]][loc["Location"][1]]["Food"] += loc[
            "Food"
        ]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Mechanisms/Site.py](../../../src/Implementations/Python/Mechanisms/Site.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Mechanisms/Site.py](../../../../src/Mechanisms/Site.py)

