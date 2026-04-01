from utils import N_ANTS, SEED
from world import World
from pheromone import FoodPheromone, HomePheromone
from ant import Ant
from view import AntColonyView
import random


try:
    import numpy as np
except ImportError:
    np = None


def set_random_states(seed: int = SEED) -> None:
    random.seed(seed)
    if np is not None:
        np.random.seed(seed)

def main():
    set_random_states(SEED)
    # Setup world/environment
    environment = World()
    # Ant agents
    ants = [Ant(i, environment) for i in range(N_ANTS)]
    # GUI/View
    view = AntColonyView(environment, ants)

    def simulation_step():
        for ant in ants:
            ant.step(environment)
        environment.evaporate_pheromones()

    view.run(simulation_step, fps=15)  # Adjust fps as needed

if __name__ == "__main__":
    main()