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
