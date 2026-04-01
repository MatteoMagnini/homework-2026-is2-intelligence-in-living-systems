from pheromone import HomePheromone, FoodPheromone
from utils import *
import numpy as np
import random

def compute_pheromone_vector(agent_x, agent_y, pheromone_list, sense_radius):
    """
    Returns the direction vector resulting from the weighted sum
    of all pheromones perceived within sense_radius.
    Each pheromone contributes proportionally to intensity/distance.
    """
    vec = np.array([0.0, 0.0])
    norm_sum = 0.0
    for p in pheromone_list:
        dx = p.x - agent_x
        dy = p.y - agent_y
        dist = np.hypot(dx, dy)
        if sense_radius > dist > 1e-8:
            weight = p.intensity / dist
            vec += np.array([dx, dy]) * weight
            norm_sum += abs(weight)
    if norm_sum > 0:
        vec = vec / (norm_sum + 1e-8)
    else:
        vec = np.array([0.0, 0.0])
    return vec


def random_direction():
    """
    Returns a random normalized movement vector.
    """
    angle = random.uniform(0, 2*np.pi)
    return np.array([np.cos(angle), np.sin(angle)])


class Ant:
    def __init__(self, idx, world):
        cx, cy = world.nest_center
        self.x = cx + np.random.randn()*0.3
        self.y = cy + np.random.randn()*0.3
        self.has_food = False
        self.idx = idx
        self.prev_vec = np.array([0.0, 0.0]) # inertia vector

    def pick_up_food(self, world):
        """
        Picks up food if nearby and not already carrying it.
        """
        if self.has_food:
            return False
        for fx, fy in world.food_map:
            if np.hypot(self.x - fx, self.y - fy) < ANT_VIEW_DIST:
                self.has_food = True
                return True
        return False

    def drop_food(self, world):
        """
        Drops food if carrying and close to nest.
        """
        if not self.has_food:
            return False
        for nx, ny in world.nest_map:
            if np.hypot(self.x - nx, self.y - ny) < ANT_VIEW_DIST:
                self.has_food = False
                return True
        return False

    def move(self, world, direction_vec, step_size=1.0):
        """
        Moves in the direction, using step_size.
        If collision, tries random direction.
        """
        tries = 10
        for _ in range(tries):
            move_vec = direction_vec
            nx = self.x + move_vec[0] * step_size
            ny = self.y + move_vec[1] * step_size
            if 0 <= nx < world.width and 0 <= ny < world.height and not world.in_obstacle(nx, ny):
                self.prev_vec = move_vec
                self.x, self.y = nx, ny
                return True
            direction_vec = random_direction()
        return False

    def move_to_nest(self, world):
        """
        Moves towards the nest; if visible, moves directly,
        otherwise follows home pheromone vector with inertia.
        """
        for nx, ny in world.nest_map:
            if np.hypot(self.x - nx, self.y - ny) < ANT_VIEW_DIST:
                # TODO: move the ant towards the nest point (nx, ny) because the ant sees it
                return True
        if world.home_pheromones:
            # TODO: move the ant towards the pheromones (use the vectorial sum weighted by the intensity)
            return True
        return False

    def follow_food_pheromone(self, world):
        """
        Moves towards weighted direction of nearby food pheromones.
        """
        # TODO: implement following food pheromones
        return False

    def random_walk(self, world):
        """
        Moves randomly, but still weighs previous movement as inertia.
        """
        # TODO: implement random walk
        return True

    def step(self, world):
        """
        Subsumption logic: executes skills in priority order.
        """
        if self.pick_up_food(world): return
        if self.drop_food(world): return
        if self.has_food:
            if self.move_to_nest(world): return
        if self.follow_food_pheromone(world): return
        self.random_walk(world)