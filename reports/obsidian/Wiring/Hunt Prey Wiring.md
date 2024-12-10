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

subgraph X4["Hunt Prey Wiring"]
direction TB
X1["Hunt Prey Boundary Action"]
X2["Hunt Prey Policy"]
X3["Prey Eaten Mechanisms"]
X3 --> EES0
X3 --> EES1
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>
<a href='Agents Space' class=internal-link>Agents Space</a>"---->X3
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
EE1[("Global")]
EES0(["Food"])
EES0 --- EE0
EES1(["Agents"])
EES1 --- EE1
end

subgraph X8["Hunt Prey Wiring"]
direction TB
X1["Hunt Prey Boundary Action"]
X2["Hunt Prey Policy"]
subgraph X7["Prey Eaten Mechanisms"]
direction TB
X3["Update Food Mechanism"]
X3 --> EES0
X4["Remove Agents Mechanism"]
X4 --> EES1
X5[Domain]

direction LR
direction TB
X5 --"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>"--> X3
X5 --"<a href='Agents Space' class=internal-link>Agents Space</a>"--> X4
end
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agent Food Delta Space' class=internal-link>Agent Food Delta Space</a>
<a href='Agents Space' class=internal-link>Agents Space</a>"---->X7
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
Wiring for agents hunting prey
## Components
1. [[Hunt Prey Boundary Action]]
2. [[Hunt Prey Policy]]
3. [[Prey Eaten Mechanisms]]

## All Blocks
1. [[Hunt Prey Boundary Action]]
2. [[Hunt Prey Policy]]
3. [[Remove Agents Mechanism]]
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
4. [[Terminating Space]]

## Metrics Used
1. [[Neighboring Valid Tiles Metric]]
2. [[Predator Stateful Metric]]
3. [[Prey Locations Stateful Metric]]

## Parameters Used
1. [[Hunger Threshold]]

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Food|Food]]
2. [[Global]].[[Global State-Agents|Agents]]

