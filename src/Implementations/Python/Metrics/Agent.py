def neighboring_valid_tiles_metric(state, params, spaces):
    out = []
    open_locations = spaces[1]["Locations"]
    dim_x = params["Site Size"][0]
    dim_y = params["Site Size"][1]
    for loc in spaces[0]["Locations"]:
        options = [
            ((loc[0] + x) % dim_x, (loc[1] + y) % dim_y)
            for x, y in zip([1, 0, -1, 0], [0, 1, 0, -1])
        ]
        options = set([x for x in options if x in open_locations])
        out.append(options)
    return out


def is_neighbor_metric(state, params, spaces):
    out = []
    query_agents = spaces[0]["Agents"]
    other_agents = spaces[1]["Agents"]
    for agent in query_agents:
        neighbors = other_agents
        x = agent["Location"][0]
        y = agent["Location"][1]
        neighbors = [a for a in neighbors if a != agent]
        neighbors = [
            a
            for a in neighbors
            if (abs(x - a["Location"][0]) + abs(y - a["Location"][1])) == 1
        ]
        out.append(neighbors)
    return out
