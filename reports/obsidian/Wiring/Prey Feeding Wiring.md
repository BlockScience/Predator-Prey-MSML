## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
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

subgraph X4["Prey Feeding Wiring"]
direction TB
X1["Prey Feeding Boundary Action"]
X2["Prey Feeding Policy"]
X3["Food Eating Mechanisms"]
X3 --> EES0
X3 --> EES1
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Location Food Delta Space' class=internal-link>Location Food Delta Space</a>
<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"---->X3
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class EE0 internal-link;
class EE1 internal-link;

```

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

subgraph X8["Prey Feeding Wiring"]
direction TB
X1["Prey Feeding Boundary Action"]
X2["Prey Feeding Policy"]
subgraph X7["Food Eating Mechanisms"]
direction TB
X3["Update Food Locations Mechanism"]
X3 --> EES1
X4["Update Food Mechanism"]
X4 --> EES0
X5[Domain]

direction LR
direction TB
X5 --"<a href='Location Food Delta Space' class=internal-link>Location Food Delta Space</a>"--> X3
X5 --"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"--> X4
end
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Location Food Delta Space' class=internal-link>Location Food Delta Space</a>
<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"---->X7
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class X4 internal-link;
class X6 internal-link;
class EE0 internal-link;
class EE1 internal-link;

```

## Description

Block Type: Stack Block
Wiring for when prey eats food
## Components
1. [[Prey Feeding Boundary Action]]
2. [[Prey Feeding Policy]]
3. [[Food Eating Mechanisms]]

## All Blocks
1. [[Prey Feeding Boundary Action]]
2. [[Prey Feeding Policy]]
3. [[Update Food Locations Mechanism]]
4. [[Update Food Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Empty Space]]

## All Spaces Used
1. [[Agent Food Delta Space]]
2. [[Agents Space]]
3. [[Empty Space]]
4. [[Location Food Delta Space]]
5. [[Terminating Space]]

## Metrics Used
1. [[Available Food Metric]]
2. [[Prey Stateful Metric]]

## Parameters Used
1. [[Hunger Threshold]]

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Food|Food]]
2. [[Site]].[[Site State-Food|Food]]

