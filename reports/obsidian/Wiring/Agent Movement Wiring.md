## Wiring Diagram (Zoomed Out)

- For display of only depth of 1 in the components/nested wirings
```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Agent")]
EE1[("Site")]
EES0(["Location"])
EES0 --- EE0
EES1(["Agent"])
EES1 --- EE1
end

subgraph X4["Agent Movement Wiring"]
direction TB
X1["Agent Movement Boundary Action"]
X2["Agent Movement Policy"]
X3["Update Agent Locations Mechanism"]
X3 --> EES1
X3 --> EES0
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agent Location Space' class=internal-link>Agent Location Space</a>"--->X3
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
EES0(["Location"])
EES0 --- EE0
EES1(["Agent"])
EES1 --- EE1
end

subgraph X4["Agent Movement Wiring"]
direction TB
X1["Agent Movement Boundary Action"]
X2["Agent Movement Policy"]
X3["Update Agent Locations Mechanism"]
X3 --> EES1
X3 --> EES0
X1--"<a href='Agents Space' class=internal-link>Agents Space</a>"--->X2
X2--"<a href='Agent Location Space' class=internal-link>Agent Location Space</a>"--->X3
end
class X1 internal-link;
class X2 internal-link;
class X3 internal-link;
class EE0 internal-link;
class EE1 internal-link;

```

## Description

Block Type: Stack Block
Wiring for agents moving
## Components
1. [[Agent Movement Boundary Action]]
2. [[Agent Movement Policy]]
3. [[Update Agent Locations Mechanism]]

## All Blocks
1. [[Agent Movement Boundary Action]]
2. [[Agent Movement Policy]]
3. [[Update Agent Locations Mechanism]]

## Constraints

## Domain Spaces
1. [[Empty Space]]

## Codomain Spaces
1. [[Terminating Space]]

## All Spaces Used
1. [[Agent Location Space]]
2. [[Agents Space]]
3. [[Empty Space]]
4. [[Terminating Space]]

## Metrics Used
1. [[Neighboring Valid Tiles Metric]]
2. [[Open Locations Stateful Metric]]

## Parameters Used

## Called By

## Calls

## All State Updates
1. [[Agent]].[[Agent State-Location|Location]]
2. [[Site]].[[Site State-Agent|Agent]]

