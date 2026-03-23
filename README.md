# Battlefield Route Optimization System

A risk-aware pathfinding system that computes the safest and most cost-effective route across a simulated battlefield using the **A* (A-Star) Algorithm**.

## About

This project simulates a 2D battlefield grid with multiple terrain types. Each terrain has a different movement cost, and the system uses A* pathfinding to find the optimal route from start to goal — considering both distance and tactical risk.

Built as a **DAA (Design and Analysis of Algorithms) PBL Project**.

## Terrain Types

| Symbol | Terrain | Cost | Description |
|--------|---------|------|-------------|
| `N` | Normal Road | 1 | Best path, smooth road |
| `.` | Open Ground | 2 | Flat but no road |
| `M` | Muddy Terrain | 3 | Slows down movement |
| `P` | Poor Road | 4 | Broken/damaged road |
| `E` | Enemy Zone | 5 | Risky, enemy present |
| `L` | Landmine Zone | 7 | Very dangerous area |
| `X` | Obstacle | inf | Completely blocked |
| `S` | Start | - | Starting position |
| `G` | Goal | - | Destination |

## How It Works

1. **Grid Generation** — A dynamic battlefield grid is generated randomly with various terrain types
2. **Cost Function** — Each cell has an associated movement cost based on terrain type
3. **Heuristic Function** — Manhattan distance estimates distance to goal
4. **A\* Algorithm** *(coming soon)* — Combines actual cost `g(n)` + heuristic `h(n)` to find optimal path

### Core Formula
```
f(n) = g(n) + h(n)
```
- `g(n)` = Actual cost from Start to current node
- `h(n)` = Estimated cost from current node to Goal (Manhattan Distance)
- `f(n)` = Total estimated cost

## How to Run

```bash
python 1.py
```

## Sample Output

```
Generated Battlefield:

S . N M . X
N . E . P .
. X N . M N
P . . N . E
. M X . N G

Start: (0, 0)
Goal: (4, 5)

--- Cell Costs ---
Open Ground  (.) : 2
Normal Road  (N) : 1
Muddy        (M) : 3
Poor Road    (P) : 4
Enemy Zone   (E) : 5
Obstacle     (X) : inf
```

## Project Progress

- [x] Dynamic grid generation with 7 terrain types
- [x] Start and goal placement
- [x] Movement logic (4-directional neighbors)
- [x] Multi-factor cost function
- [x] Heuristic function (Manhattan Distance)
- [x] Grid display
- [ ] A* pathfinding algorithm
- [ ] Path reconstruction
- [ ] Path visualization
- [ ] Additional terrains (Forest, Mountain, Water)
- [ ] Performance analysis

## Tech Stack

- **Language:** Python
- **Algorithm:** A* (A-Star) Search
- **Data Structures:** 2D Array, Priority Queue (heapq)

## Team

University DAA PBL Project — 2nd Year
