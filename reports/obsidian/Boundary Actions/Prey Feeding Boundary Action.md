## Description

Boundary action which returns the prey that might eat.
## Called By
1. [[Agent]]

## Followed By
1. [[Prey Feeding Policy]]

## Constraints

## Codomain Spaces
1. [[Agents Space]]

## Boundary Action Options:
### 1. Prey Feeding Boundary Action V1
#### Description
All hungry prey eats
#### Logic
Filter to just prey and then filter out any prey that are not hungry.

