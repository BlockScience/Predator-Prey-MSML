## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EES0(["Age"])
EES0 --- EE0
EES1(["Food"])
EES1 --- EE0
end

subgraph X5["Age & Food Mechanisms"]
direction TB
X1["Update Food Mechanism"]
X1 --> EES1
X2["Increase Agent Age Mechanism"]
X2 --> EES0
X3[Domain]

direction LR
direction TB
X3 --"Agent Food Delta Space"--> X1
X3 --"Agent Age Delta Space"--> X2
end
class X1 internal-link;
class X2 internal-link;
class X4 internal-link;
class EE0 internal-link;

```

## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EES0(["Age"])
EES0 --- EE0
EES1(["Food"])
EES1 --- EE0
end

subgraph X5["Age & Food Mechanisms"]
direction TB
X1["Update Food Mechanism"]
X1 --> EES1
X2["Increase Agent Age Mechanism"]
X2 --> EES0
X3[Domain]

direction LR
direction TB
X3 --"Agent Food Delta Space"--> X1
X3 --"Agent Age Delta Space"--> X2
end
class X1 internal-link;
class X2 internal-link;
class X4 internal-link;
class EE0 internal-link;

```

## Description

Block Type: Parallel Block
Mechanisms for updating food and age
## Components
1. [[Update Food Mechanism]]
2. [[Increase Agent Age Mechanism]]

## All Blocks
1. [[Increase Agent Age Mechanism]]
2. [[Update Food Mechanism]]

## Constraints

## Domain Spaces
1. [[Agent Food Delta Space]]
2. [[Agent Age Delta Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Agent Age Delta Space]]
2. [[Agent Food Delta Space]]
3. [[Empty Space]]
4. [[Terminating Space]]

## Metrics Used

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Age|Age]]
2. [[Agent]].[[Agent State-Food|Food]]

