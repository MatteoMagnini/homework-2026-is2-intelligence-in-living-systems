from abc import ABC
from utils import FOOD_PHEROMONE_DECAY, HOME_PHEROMONE_DECAY

PHEROMONE_THRESHOLD = 0.01

class Pheromone(ABC):
    """
    Abstract pheromone.
    Each pheromone is a dict with 'x', 'y' and 'intensity' that decays over time.
    """
    def __init__(self, position, evaporation):
        self.x, self.y = position
        self.evaporation = evaporation
        self.intensity = 1.0

    def evaporate(self):
        self.intensity *= self.evaporation
        return self.intensity >= PHEROMONE_THRESHOLD


class FoodPheromone(Pheromone):
    def __init__(self, position):
        super().__init__(position, FOOD_PHEROMONE_DECAY)

class HomePheromone(Pheromone):
    def __init__(self, position):
        super().__init__(position, HOME_PHEROMONE_DECAY)