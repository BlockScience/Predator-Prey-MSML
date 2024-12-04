## Description

The policy which determines where agents move to.
## Called By
1. [[Agent Movement Boundary Action]]
## Domain Spaces
1. [[Agents Space]]
## Followed By
1. [[Update Agent Locations Mechanism]]
## Codomain Spaces
1. [[Agent Location Space]]
## Constraints
## Parameters Used
## Metrics Used
1. [[Neighboring Valid Tiles Metric]]
2. [[Open Locations Stateful Metric]]
## Policy Options
### 1. Random Agent Movement with Sieve
#### Description
A policy where agents move randomly 1 square but the movements are implemented with a sieve
#### Logic
While the length of the agents to move is greater than 0 and has reduced in size since the last iteration:
1. Iterate through the list of agents, if they have a valid tile to move to, add it to the output, and switch out the tiles from busy squares, otherwise add them to the new sieve
2. The loop terminates when the remaining agents have no space to move to or there are no more agents

