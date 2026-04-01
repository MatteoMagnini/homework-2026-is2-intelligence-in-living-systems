import time
import pygame
from utils import CELL_SIZE, ANT_RADIUS
import numpy as np

FPS = 60

class AntColonyView:
    def __init__(self, world, ants):
        self.world = world
        self.ants = ants

        self.width_px = int(world.width * CELL_SIZE)
        self.height_px = int(world.height * CELL_SIZE)

        pygame.init()
        self.screen = pygame.display.set_mode((self.width_px, self.height_px))
        pygame.display.set_caption("Ant Foraging - Continuous GUI")

    def draw_obstacles(self):
        for rect in self.world.rectangles:
            rx, ry, rw, rh = rect
            pygame.draw.rect(
                self.screen,
                (90, 90, 90),
                (int(rx*CELL_SIZE), int(ry*CELL_SIZE), int(rw*CELL_SIZE), int(rh*CELL_SIZE))
            )

    def draw_nest(self):
        for x, y in self.world.nest_map:
            pygame.draw.circle(
                self.screen,
                (30, 220, 40),
                (int(x*CELL_SIZE), int(y*CELL_SIZE)),
                int(CELL_SIZE)
            )

    def draw_food(self):
        for x, y in self.world.food_map:
            pygame.draw.circle(
                self.screen,
                (255, 220, 0),
                (int(x*CELL_SIZE), int(y*CELL_SIZE)),
                int(CELL_SIZE)
            )

    def draw_ants(self):
        for ant in self.ants:
            color = (230, 40, 30) if ant.has_food else (30, 30, 30)
            pygame.draw.circle(
                self.screen,
                color,
                (int(ant.x*CELL_SIZE), int(ant.y*CELL_SIZE)),
                ANT_RADIUS
            )
            pygame.draw.circle(
                self.screen,
                (0, 0, 0),
                (int(ant.x*CELL_SIZE), int(ant.y*CELL_SIZE)),
                ANT_RADIUS, 1
            )

    def draw_pheromones(self, pheromone_list, color_fn):
        """
        Each pheromone is an object with x, y, intensity.
        Draw them as semi-transparent circles, alpha proportional to intensity.
        """
        for p in pheromone_list:
            intensity = float(p.intensity)
            if intensity < 0.01:
                continue
            alpha = int(60 + 180 * np.clip(intensity, 0, 1))
            c = color_fn(intensity)
            surf = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*c, alpha), (CELL_SIZE//2, CELL_SIZE//2), CELL_SIZE//5)
            self.screen.blit(
                surf,
                (int(p.x * CELL_SIZE - CELL_SIZE / 2), int(p.y * CELL_SIZE - CELL_SIZE / 2))
            )

    def food_phero_color(self, intensity):
        val = np.clip(intensity/1.0, 0, 1)
        r = int(210 + 45*val)
        g = int(180 + 50*val)
        b = int(60 * (1-val))
        return (r, g, b)

    def home_phero_color(self, intensity):
        val = np.clip(intensity/1.0, 0, 1)
        r = int(90 + 90*val)
        g = int(140 + 80*val)
        b = int(210+45*val)
        return (r, g, b)

    def update(self):
        self.screen.fill((240, 240, 240))
        self.draw_obstacles()
        self.draw_nest()
        self.draw_food()
        self.draw_pheromones(self.world.food_pheromones, self.food_phero_color)
        self.draw_pheromones(self.world.home_pheromones, self.home_phero_color)
        self.draw_ants()
        pygame.display.flip()

    def run(self, step_fn, fps=FPS):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            step_fn()  # Advances simulation one tick
            self.update()
            clock.tick(fps)
            time.sleep(0.1)
        pygame.quit()