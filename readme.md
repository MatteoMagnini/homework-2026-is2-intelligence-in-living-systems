# IS2 — Two Bridges Ant Foraging Scenario

## Overview

You are provided with a codebase that implements a continuous 2D artificial ant foraging scenario. Your goal is to enable the simulation of *emergent collective intelligence* in a colony of simple agents (ants). The foraging environment features obstacles and multiple possible paths (bridges) between nest and food.

**Your task:**  
Implement the missing behaviour ("TODOs") in the `Ant` class (`ant.py`) so that intelligent foraging emerges from distributed local interactions.

---

## Repo Structure

```
twoBridgesScenario/
├─ init.py          # Program entry point: run this to start the simulation
├─ utils.py             # Global parameters, constants, YAML/map handling, utility functions
├─ world.py             # Continuous environment (food, nest, obstacles, pheromone lists)
├─ pheromone.py         # Classes for point-based pheromones, food & home
├─ ant.py               # Ant agent logic (your focus!)
├─ view.py              # Pygame GUI: visualisation of ants, pheromones, obstacles, food, nest
├─ world.yaml           # Map definition (edit only if you want new layouts!)
└─ ...
```

---

## Setup Instructions (with Poetry)

1. **Install poetry**
    - If you don't have it yet:
      ```bash
      pip install poetry
      ```
      or see: [Poetry official installation](https://python-poetry.org/docs/#installation)
      
2. **Create and install the virtual environment and all dependencies:**
    ```bash
    poetry install
    ```

3. **Open a shell in the poetry environment:**
    ```bash
    poetry shell
    ```

4. **(If you need, add dependencies such as pygame manually):**
    ```bash
    poetry add pygame numpy pyyaml
    ```

---

## Submission
Upload only the ant.py file to the moodle assignment!
Deadline is the 6th of April at 11:59 PM.

---

## Launching the Simulation

From the root of your repo (where `twoBridgesScenario/__init__.py` is located), run:

```bash
python -m twoBridgesScenario
```

The GUI window should open.

**At the start, ants will not move. This is expected!**

After you implement the required methods, collective foraging trails should emerge.

---

## Your Assignment

- **Only modify `ant.py`. Do not change other files!**
- Open `twoBridgesScenario/ant.py`.
- All code you need to write is marked with `TODO` comments.
- Read the docstrings and comments carefully.
- Implement the skills (food pickup/drop, pheromone following, random walk, movement logic, etc.) as instructed.
- Follow the principles of bio-inspired, local, distributed intelligence.
- Try **NOT** to use global information (only the ant's perception of its local environment and pheromones).
- All other files (`utils`, `world`, `pheromone`, `view`, `YAML`) are infrastructural.
  - *You should not and must not edit them.*

---

## Success Criteria

- If you complete the TODOs correctly, **the colony should develop clear trails over time, preferring the shorter bridge, even though individual ants only have local and noisy information.**
- The behaviour should be robust to changes in random seed, number of ants, and map structure.
- The GUI will let you visually inspect the quality of the emergent foraging.

---

## Hints

- Tune hyperparameters (pheromone drop rates, decay rates, inertia, sense radius, etc.) if needed, but only in `utils.py` and only if instructed by your professor (otherwise leave them as is).
- If ants do not move after your implementation, debug your movement and perception methods.

---

Good luck — and enjoy watching the emergence of collective intelligence!