## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EE1[("Global")]
EES0(["Food"])
EES0 --- EE0
EES1(["Agents"])
EES1 --- EE1
end

subgraph X5["Prey Eaten Mechanisms"]
direction TB
X1["Update Food Mechanism"]
X1 --> EES0
X2["Remove Agents Mechanism"]
X2 --> EES1
X3[Domain]

direction LR
direction TB
X3 --"Agent Food Delta Space"--> X1
X3 --"Agents Space"--> X2
end
class X1 internal-link;
class X2 internal-link;
class X4 internal-link;
class EE0 internal-link;
class EE1 internal-link;

```

## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EE1[("Global")]
EES0(["Food"])
EES0 --- EE0
EES1(["Agents"])
EES1 --- EE1
end

subgraph X5["Prey Eaten Mechanisms"]
direction TB
X1["Update Food Mechanism"]
X1 --> EES0
X2["Remove Agents Mechanism"]
X2 --> EES1
X3[Domain]

direction LR
direction TB
X3 --"Agent Food Delta Space"--> X1
X3 --"Agents Space"--> X2
end
class X1 internal-link;
class X2 internal-link;
class X4 internal-link;
class EE0 internal-link;
class EE1 internal-link;

```

## Description

Block Type: Parallel Block
Wiring for predators eating prey
## Components
1. [[Update Food Mechanism]]
2. [[Remove Agents Mechanism]]

## All Blocks
1. [[Remove Agents Mechanism]]
2. [[Update Food Mechanism]]

## Constraints

## Domain Spaces
1. [[Agent Food Delta Space]]
2. [[Agents Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Agent Food Delta Space]]
2. [[Agents Space]]
3. [[Empty Space]]
4. [[Terminating Space]]

## Metrics Used

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Food|Food]]
2. [[Global]].[[Global State-Agents|Agents]]

