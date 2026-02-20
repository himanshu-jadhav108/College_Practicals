import heapq

# Maze: 0 = path, 1 = wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# Manhattan distance heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))  # (f, g, node, path)
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path

        # Explore neighbors
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            x, y = current[0] + dx, current[1] + dy
            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0:
                next_node = (x, y)
                if next_node not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(next_node, goal)
                    heapq.heappush(open_set, (new_f, new_g, next_node, path + [next_node]))

    return None

# Function to print maze with path
def print_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]  # deep copy

    for r, c in path:
        if (r, c) != start and (r, c) != goal:  # keep start and goal clear
            maze_copy[r][c] = "*"

    print("\nMaze with Path:")
    for r in range(len(maze_copy)):
        row_str = ""
        for c in range(len(maze_copy[0])):
            if (r, c) == start:
                row_str += "S "  # Start
            elif (r, c) == goal:
                row_str += "G "  # Goal
            elif maze_copy[r][c] == 1:
                row_str += "# "  # Wall
            elif maze_copy[r][c] == "*":
                row_str += "* "  # Path
            else:
                row_str += ". "  # Free space
        print(row_str)


# Run A*
path = astar(maze, start, goal)

if path:
    print("✅ A* Path Found:", path)
    print_maze_with_path(maze, path)
else:
    print("❌ No path found.")
