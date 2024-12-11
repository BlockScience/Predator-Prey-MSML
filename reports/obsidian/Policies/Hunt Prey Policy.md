## Description

The policy which determines how and when prey are hunted.
## Called By
1. [[Hunt Prey Boundary Action]]
## Domain Spaces
1. [[Agents Space]]
## Followed By
1. [[Update Food Mechanism]]
2. [[Remove Agents Mechanism]]
## Codomain Spaces
1. [[Agent Food Delta Space]]
2. [[Agents Space]]
## Constraints
## Parameters Used
## Metrics Used
1. [[Neighboring Valid Tiles Metric]]
2. [[Predator Stateful Metric]]
3. [[Prey Locations Stateful Metric]]
## Policy Options
### 1. Hunt Prey V1
#### Description
If a valid prey is in a nearby site then it is eaten. If there are multiple then there is a random choice.
#### Logic

#### Python Implementation
```python
def hunt_prey_policy_v1(state, params, spaces):
    possible_prey = state["Stateful Metrics"]["Prey Locations Stateful Metric"](
        state, params
    )
    possible_prey = [x["Location"] for x in possible_prey]
    predators = state["Stateful Metrics"]["Predator Stateful Metric"](state, params)

    space1 = {"Food Deltas": []}
    space2 = {"Agents": []}

    for predator in predators:
        options = state["Metrics"]["Neighboring Valid Tiles Metric"](
            state,
            params,
            [{"Locations": [predator["Location"]]}, {"Locations": possible_prey}],
        )[0]
        if len(options) > 0:
            prey = choice(list(options))
            possible_prey.remove(prey)
            prey = state["Sites Matrix"][prey[0]][prey[1]]["Agent"]
            food = prey["Food"]
            space1["Food Deltas"].append({"Agent": predator, "Delta Food": food})
            space2["Agents"].append(prey)
    return [space1, space2]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Agent.py](../../../src/Implementations/Python/Policies/Agent.py)

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Policies/Agent.py](../../../../src/Policies/Agent.py)

