from utils import N_ANTS
from world import World
from pheromone import FoodPheromone, HomePheromone
from ant import Ant
from view import AntColonyView

def main():
    # Setup world/environment
    environment = World()
    # Ant agents
    ants = [Ant(i, environment) for i in range(N_ANTS)]
    # GUI/View
    view = AntColonyView(environment, ants)

    def simulation_step():
        for ant in ants:
            ant.step(environment)

    view.run(simulation_step, fps=15)  # Adjust fps as needed

if __name__ == "__main__":
    main()