import numpy as np
import yaml

# ---- GLOBAL CONSTANTS ----
SEED = 42
N_ANTS = 30
PHEROMONE_DROP_FOOD = 0.15
PHEROMONE_DROP_HOME = 0.1
ANT_VIEW_DIST = 2
PHEROMONE_SENSE_RADIUS = 3
CELL_SIZE = 26
ANT_RADIUS = 10
INERTIA = 0.6
FOOD_PHEROMONE_DECAY = 0.95
HOME_PHEROMONE_DECAY = 0.9
YAML_MAP_FILE = "world.yaml"

random_state = np.random.RandomState(SEED)


def load_map_from_yaml(filepath):
    """
    Loads rectangles as obstacles, nest and food as lists of possibly non-integer 2D points.
    Returns width, height, list of rectangles, list of nest positions, list of food positions
    """
    with open(filepath, "r") as f:
        mdata = yaml.safe_load(f)
    width = mdata['width']
    height = mdata['height']
    rectangles = []
    if "obstacles" in mdata:
        for obs in mdata["obstacles"]:
            if obs.get("type") == "rect":
                # Each obstacle is a rectangle with (x, y, w, h)
                rectangles.append(
                    (float(obs["x"]), float(obs["y"]), float(obs["w"]), float(obs["h"]))
                )
            # If you want to support other types, add parsing here
    nest_list = [tuple(pos) for pos in mdata.get('nest',[])]
    food_list = [tuple(pos) for pos in mdata.get('food',[])]
    return width, height, rectangles, nest_list, food_list


def point_in_rect(px, py, rx, ry, rw, rh):
    """Returns True iff point (px,py) is inside rectangle (rx,ry,rw,rh)."""
    return (rx <= px <= rx+rw) and (ry <= py <= ry+rh)


def collides_with_obstacle(x, y, rectangles):
    """Returns True iff (x, y) is inside ANY given rectangle in rectangles."""
    return any(point_in_rect(x, y, *rect) for rect in rectangles)
