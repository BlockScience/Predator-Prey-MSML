## Description

The policy which determines the simulation metadata updates.
## Called By
## Domain Spaces
1. [[Empty Space]]
## Followed By
1. [[Increment Time Mechanism]]
2. [[Log Simulation Data Mechanism]]
## Codomain Spaces
1. [[Timestep Space]]
2. [[Simulation Log Space]]
## Constraints
## Parameters Used
## Metrics Used
## Policy Options
### 1. Simulation Meta Policy V1
#### Description
Baseline simulation meta policy.
#### Logic
The timestep will be incremented by 1 and a full simulation log will be returned.
#### Python Implementation
```python
def simulation_meta_policy_v1(state, params, spaces):
    space1 = {"Timestep": 1}
    space2 = {}

    space2["Timestep"] = state["Timestep"] + 1

    for key in [
        "Open Locations Stateful Metric",
        "Filled Locations Stateful Metric",
        "Prey Locations Stateful Metric",
        "Predator Locations Stateful Metric",
        "Median Site Food Stateful Metric",
        "Prey Stateful Metric",
        "Predator Stateful Metric",
        "Number of Prey Stateful Metric",
        "Number of Predators Stateful Metric",
        "Median Predator Food Stateful Metric",
        "Median Prey Food Stateful Metric",
        "Median Predator Age Stateful Metric",
        "Median Prey Age Stateful Metric",
    ]:
        space2[key] = state["Stateful Metrics"][key](state, params)

    return [space1, space2]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Meta.py#L1](../../../src/Implementations/Python/Policies/Meta.py#L1)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Policies/Meta.py#L2](../../../../src/Policies/Meta.py#L2)

