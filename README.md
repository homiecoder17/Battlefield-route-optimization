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
| `X` | Obstacle | inf | Completely blocked |
| `S` | Start | - | Starting position |
| `G` | Goal | - | Destination |

## How It Works

1. **Grid Generation** — A dynamic battlefield grid (random 5x5 to 30x30) is generated with various terrain types
2. **Cost Function** — Each cell has a movement cost based on terrain type (1 to inf)
3. **Heuristic Function** — Manhattan distance estimates distance to goal
4. **A\* Algorithm** — Uses priority queue (heapq) with f(n) = g(n) + h(n) to find optimal path

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

## Current Progress (50%)

- [x] Dynamic grid generation with 6 terrain types
- [x] Start and goal placement
- [x] Movement logic (4-directional neighbors)
- [x] Multi-factor cost function
- [x] Heuristic function (Manhattan Distance)
- [x] Grid display
- [x] A* algorithm (coded, not yet executed)
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
