from pheromone import FoodPheromone, HomePheromone
from utils import (
    CELL_SIZE,
    ANT_RADIUS,
    YAML_MAP_FILE,
    load_map_from_yaml,
    collides_with_obstacle
)
import numpy as np

class World:
    def __init__(self, yaml_file=YAML_MAP_FILE):
        # Load map from yaml: continuous world
        self.width, self.height, self.rectangles, self.nest_list, self.food_list = load_map_from_yaml(yaml_file)
        self.food_pheromones: list[FoodPheromone] = []
        self.home_pheromones: list[HomePheromone] = []
        self.food_map = self.food_list[:]  # positions of food (continuous)
        self.nest_map = self.nest_list[:]  # positions of nest (continuous)
        self.nest_center = tuple(np.mean(np.array(self.nest_map), axis=0))

    def evaporate_pheromones(self):
        # Remove those that decay below threshold
        self.food_pheromones = [p for p in self.food_pheromones if p.evaporate()]
        self.home_pheromones = [p for p in self.home_pheromones if p.evaporate()]

    def drop_food_pheromone(self, x, y):
        # Drop a puntual food pheromone at position (x, y)
        self.food_pheromones.append(FoodPheromone((x, y)))

    def drop_home_pheromone(self, x, y):
        self.home_pheromones.append(HomePheromone((x, y)))

    def in_obstacle(self, x, y):
        # True if (x, y) is inside any rectangle
        return collides_with_obstacle(x, y, self.rectangles)

    def in_nest(self, x, y):
        # True if (x, y) is near any nest point
        for nx, ny in self.nest_map:
            if np.hypot(x-nx, y-ny) < ANT_RADIUS/float(CELL_SIZE):
                return True
        return False

    def in_food(self, x, y):
        # True if (x, y) is near any food point
        for fx, fy in self.food_map:
            if np.hypot(x-fx, y-fy) < ANT_RADIUS/float(CELL_SIZE):
                return True
        return False