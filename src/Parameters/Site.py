initial_site_parameter_set = {
    "name": "Initial Site Parameter Set",
    "notes": "A set of parameters for what the sites should look like in the beginning",
    "parameters": [
        {
            "variable_type": "2D Size Type",
            "name": "Site Size",
            "description": "The size of the site",
            "symbol": None,
            "domain": None,
            "parameter_class": "Functional",
        },
        {
            "variable_type": "Food Type",
            "name": "Initial Number of Food Tiles",
            "description": "The initial number of food tiles in the sites",
            "symbol": None,
            "domain": None,
            "parameter_class": "Functional",
        },
    ],
}


site_parameter_set = {
    "name": "Site Parameter Set",
    "notes": "A set of parameters for the sites",
    "parameters": [
        {
            "variable_type": "Food Type",
            "name": "Maximum Food per Tile",
            "description": "The maximum food that a tile can have",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Food Type",
            "name": "Food Growth Rate",
            "description": "The growth rate of food per epoch",
            "symbol": None,
            "domain": None,
            "parameter_class": "Behavioral",
        },
    ],
}


site_parameter_sets = [initial_site_parameter_set, site_parameter_set]
