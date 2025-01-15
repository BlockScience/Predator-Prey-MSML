from typing import List, TypedDict

mapping = {
    "EntityType": object,
    "SimulationLogType": List[
        TypedDict(
            "Simulation Log",
            {
                "Timestep": int,
                "Open Locations Stateful Metric": int,
                "Filled Locations Stateful Metric": int,
                "Prey Locations Stateful Metric": int,
                "Predator Locations Stateful Metric": int,
                "Median Site Food Stateful Metric": int,
                "Prey Stateful Metric": int,
                "Predator Stateful Metric": int,
                "Number of Prey Stateful Metric": int,
                "Number of Predators Stateful Metric": int,
                "Median Predator Food Stateful Metric": int,
                "Median Prey Food Stateful Metric": int,
                "Median Predator Age Stateful Metric": int,
                "Median Prey Age Stateful Metric": int,
            },
        )
    ],
}
