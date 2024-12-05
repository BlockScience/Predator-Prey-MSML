## Description

The policy which determines if and how agents reproduce.
## Called By
1. [[Agent Reproduction Boundary Action]]
## Domain Spaces
1. [[Agents Space]]
## Followed By
1. [[Create Agents Mechanism]]
2. [[Update Food Mechanism]]
## Codomain Spaces
1. [[Agents Space]]
2. [[Agent Food Delta Space]]
## Constraints
## Parameters Used
1. [[Reproduction Food Needed]]
2. [[Reproduction Food Threshold]]
3. [[Reproduction Probability]]
## Metrics Used
1. [[Is Neighbor Metric]]
2. [[Neighboring Valid Tiles Metric]]
3. [[Open Locations Stateful Metric]]
4. [[Predator Stateful Metric]]
5. [[Prey Stateful Metric]]
## Policy Options
### 1. Agent Reproduction Policy V1
#### Description
Simple reproduction method where randomly agents will reproduce with others if they are on nearby tiles and have enough food (and are of the same type).
#### Logic
1. Get valid prey/predators with the stateful metrics
2. Filter the agents to be only the ones which have at least the [[Reproduction Food Threshold]]
3. For the group of predators and then the group of prey do the following, where agents is the variable representing the agents of that type still in play...
A1. Create a filtered list of agents based on randomly being under [[Reproduction Probability]], these agents that will reproduce
A2. Loop over each agent in this reproduction and do the following:
AA1. Check that they are still in the agents list (have not reproduced), otherwise continue on
AA2. Find valid_mates by filtering agents array with [[Is Neighbor Metric]], if length is 0 then continue
AA3. Find valid open spaces with [[Neighboring Valid Tiles Metric]], if length is 0 then continue
AA4. Randomly pick a valid mate and a valid open location
AA5. Add to the spaces -[[Reproduction Food Needed]] for both of the mates
AA6. Add a newly created anget that has food of 2 * [[Reproduction Food Needed]]
#### Python Implementation
```python
def agent_reproduction_policy_v1(state, params, spaces):

    space1 = {"Agents": []}
    space2 = {"Food Deltas": []}

    # Find the agents and open locations
    predators = state["Stateful Metrics"]["Predator Stateful Metric"](state, params)
    prey = state["Stateful Metrics"]["Prey Stateful Metric"](state, params)
    open_locations = state["Stateful Metrics"]["Open Locations Stateful Metric"](
        state, params
    )
    open_locations = [x["Location"] for x in open_locations]

    # Filter to having enough food
    predators = [
        agent
        for agent in predators
        if agent["Food"] >= params["Reproduction Food Threshold"]
    ]
    prey = [
        agent
        for agent in prey
        if agent["Food"] >= params["Reproduction Food Threshold"]
    ]
    for agents in [predators, prey]:
        reproducing_agents = [
            agent_i
            for agent_i in agents
            if random() <= params["Reproduction Probability"]
        ]
        for agent in reproducing_agents:
            if agent not in agents:
                continue
            valid_mates = state["Metrics"]["Is Neighbor Metric"](
                state, params, [{"Agents": [agent]}, {"Agents": agents}]
            )[0]
            if len(valid_mates) == 0:
                continue

            mate = choice(valid_mates)

            # Valid locations for birth on either agent
            valid_locations = state["Metrics"]["Neighboring Valid Tiles Metric"](
                state,
                params,
                [
                    {"Locations": [agent["Location"], mate["Location"]]},
                    {"Locations": open_locations},
                ],
            )
            valid_locations = valid_locations[0].union(valid_locations[1])
            if len(valid_locations) == 0:
                continue
            new_location = choice(list(valid_locations))
            agents.remove(agent)
            agents.remove(mate)
            open_locations.remove(new_location)

            space1["Agents"].append(
                {
                    "Age": 0,
                    "Agent Type": agent["Agent Type"],
                    "Food": params["Reproduction Food Needed"] * 2,
                    "Location": new_location,
                }
            )
            space2["Food Deltas"].append(
                {"Agent": agent, "Delta Food": -params["Reproduction Food Needed"]}
            )
            space2["Food Deltas"].append(
                {"Agent": mate, "Delta Food": -params["Reproduction Food Needed"]}
            )
    return [space1, space2]
```
Implementation Path (only works if vault is opened at level including the src folder): [../../../src/Implementations/Python/Policies/Agent.py](../../../src/Implementations/Python/Policies/Agent.py)

