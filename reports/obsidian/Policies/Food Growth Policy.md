## Description

The policy determines the amount of food growth per site.
## Called By
## Domain Spaces
1. [[Locations Space]]
## Followed By
## Codomain Spaces
1. [[Location Food Delta Space]]
## Constraints
## Parameters Used
1. [[Food Growth Rate]]
2. [[Maximum Food per Tile]]
## Metrics Used
## Policy Options
### 1. Constant Food Growth Policy
#### Description
Add a constant rate of food growth to each location up to the maximum
#### Logic
For each location, the delta is equal to min(Food + params["Food Growth Rate"], params["Maximum Food per Tile"])

