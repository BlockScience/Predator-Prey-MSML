## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EE1[("Site")]
EES0(["Food"])
EES0 --- EE0
EES1(["Food"])
EES1 --- EE1
end

subgraph X5["Food Eating Mechanisms"]
direction TB
X1["Update Food Locations Mechanism"]
X1 --> EES1
X2["Update Food Mechanism"]
X2 --> EES0
X3[Domain]

direction LR
direction TB
X3 --"Location Food Delta Space"--> X1
X3 --"Agent Food Delta Space"--> X2
end
```

## Description

Block Type: Parallel Block
Mechanisms for when food is eaten by prey
## Components
1. [[Update Food Locations Mechanism]]
2. [[Update Food Mechanism]]

## All Blocks
1. [[Update Food Locations Mechanism]]
2. [[Update Food Mechanism]]

## Constraints

## Domain Spaces
1. [[Location Food Delta Space]]
2. [[Agent Food Delta Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Agent Food Delta Space]]
2. [[Empty Space]]
3. [[Location Food Delta Space]]
4. [[Terminating Space]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Food|Food]]
2. [[Site]].[[Site State-Food|Food]]

