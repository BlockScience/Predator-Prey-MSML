update_food_locations_mechanism = {
    "name": "Update Food Locations Mechanism",
    "description": "A mechanism for updating food locations",
    "constraints": [],
    "logic": """Add the delta food to each locations food amount""",
    "domain": ["Location Food Delta Space"],
    "parameters_used": [],
    "updates": [
        ("Site", "Food", False),
    ],
}


site_mechanisms = [
    update_food_locations_mechanism,
]
