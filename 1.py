import random
import heapq

# Grid size
ROWS = random.randint(5,30)
COLS = random.randint(5,30)

# Symbols
EMPTY = '.'           # Open/flat ground
OBSTACLE = 'X'        # Wall / impassable
ENEMY = 'E'           # Enemy zone (risky)
START = 'S'           # Start point
GOAL = 'G'            # Goal point

# Terrain types
NORMAL_ROAD = 'N'     # Good condition road (easy to move)
MUDDY = 'M'           # Muddy terrain (slows movement)
POOR_ROAD = 'P'       # Poor condition road (harder to move)

# -------------------------------
# 1. Generate Dynamic Grid
# -------------------------------
def generate_grid(rows, cols):
    grid = [[EMPTY for _ in range(cols)] for _ in range(rows)]

    # Place terrain, obstacles, and enemies randomly
    for i in range(rows):
        for j in range(cols):
            r = random.random()
            if r < 0.15:                   # 15% chance -> Obstacle
                grid[i][j] = OBSTACLE
            elif r < 0.22:                 # 7% chance -> Enemy zone
                grid[i][j] = ENEMY
            elif r < 0.37:                 # 15% chance -> Normal road
                grid[i][j] = NORMAL_ROAD
            elif r < 0.47:                 # 10% chance -> Muddy terrain
                grid[i][j] = MUDDY
            elif r < 0.55:                 # 8% chance -> Poor road
                grid[i][j] = POOR_ROAD
            # else remains EMPTY (45%)

    return grid

# -------------------------------
# 2. Place Start and Goal
# -------------------------------
def place_start_goal(grid):
    rows = len(grid)
    cols = len(grid[0])

    start = (0, 0)
    goal = (rows - 1, cols - 1)

    grid[start[0]][start[1]] = START
    grid[goal[0]][goal[1]] = GOAL

    return start, goal

# -------------------------------
# 3. Get Neighbors
# -------------------------------
def get_neighbors(grid, x, y):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] != OBSTACLE:
                neighbors.append((nx, ny))

    return neighbors

# -------------------------------
# 4. Cost Function
# -------------------------------
def get_cost(cell):
    if cell == EMPTY:                          # Open ground
        return 2
    elif cell == NORMAL_ROAD:                  # Good road
        return 1
    elif cell == MUDDY:                        # Muddy terrain
        return 3
    elif cell == POOR_ROAD:                    # Poor road
        return 4
    elif cell == ENEMY:                        # Enemy zone
        return 5
    elif cell == START or cell == GOAL:         # Start/Goal
        return 1
    else:                                      # Obstacle
        return float('inf')

# -------------------------------
# 5. Heuristic (Manhattan Distance)
# -------------------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# -------------------------------
# 6. Display Grid
# -------------------------------
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

# -------------------------------
# 7. A* Algorithm
# -------------------------------
def astar(grid, start, goal):
    # Priority queue: (f_cost, node)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Track where each node came from (for path reconstruction)
    came_from = {}

    # g(n): actual cost from start to each node
    cost_so_far = {start: 0}

    while open_list:
        # Pop node with lowest f(n)
        current = heapq.heappop(open_list)[1]

        # If we reached the goal, stop
        if current == goal:
            break

        # Explore all neighbors
        for neighbor in get_neighbors(grid, current[0], current[1]):
            # g(n) = cost so far + cost to move to neighbor
            new_cost = cost_so_far[current] + get_cost(grid[neighbor[0]][neighbor[1]])

            # Only update if we found a cheaper path
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                # f(n) = g(n) + h(n)
                priority = new_cost + heuristic(goal, neighbor)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return came_from, cost_so_far

# -------------------------------
# MAIN EXECUTION
# -------------------------------
grid = generate_grid(ROWS, COLS)
start, goal = place_start_goal(grid)

print("Generated Battlefield:\n")
print_grid(grid)

print("\nStart:", start)
print("Goal:", goal)

print("\nNeighbors of Start:", get_neighbors(grid, start[0], start[1]))
print("Heuristic (Start -> Goal):", heuristic(start, goal))

print("\n--- Cell Costs ---")
print("Open Ground  (.) :", get_cost('.'))
print("Normal Road  (N) :", get_cost('N'))
print("Muddy        (M) :", get_cost('M'))
print("Poor Road    (P) :", get_cost('P'))
print("Enemy Zone   (E) :", get_cost('E'))
print("Obstacle     (X) :", get_cost('X'))