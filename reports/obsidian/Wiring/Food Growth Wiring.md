## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Site")]
EES0(["Food"])
EES0 --- EE0
end

subgraph X4["Food Growth Wiring"]
direction TB
X1["Food Growth Control Action"]
X2["Food Growth Policy"]
X3["Update Food Locations Mechanism"]
X3 --"State Update"--> EES0
X1--"<a href='Locations Space' class=internal-link>Locations Space</a>"--->X2
X2--"<a href='Location Food Delta Space' class=internal-link>Location Food Delta Space</a>"--->X3
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class EE0 internal-link;

```

## Wiring Diagram

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Site")]
EES0(["Food"])
EES0 --- EE0
end

subgraph X4["Food Growth Wiring"]
direction TB
X1["Food Growth Control Action"]
X2["Food Growth Policy"]
X3["Update Food Locations Mechanism"]
X3 --"State Update"--> EES0
X1--"<a href='Locations Space' class=internal-link>Locations Space</a>"--->X2
X2--"<a href='Location Food Delta Space' class=internal-link>Location Food Delta Space</a>"--->X3
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class EE0 internal-link;

```

## Description

Block Type: Stack Block
Wiring for growth of food
## Components
1. [[Food Growth Control Action]]
2. [[Food Growth Policy]]
3. [[Update Food Locations Mechanism]]

## All Blocks
1. [[Food Growth Control Action]]
2. [[Food Growth Policy]]
3. [[Update Food Locations Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Empty Space]]
2. [[Location Food Delta Space]]
3. [[Locations Space]]
4. [[Terminating Space]]

## Metrics Used

## Parameters Used
1. [[Food Growth Rate]]
2. [[Maximum Food per Tile]]

## Called By

## Calls

## All State Updates
1. [[Site]].[[Site State-Food|Food]]

## Spec Source Code Location

Spec Path (only works if vault is opened at level including the src folder): [../../../../src/Wiring/Site.py#L5](../../../../src/Wiring/Site.py#L5)

