#Experiment No. 2 - BFS and DFS Maze Solver 

from collections import deque

# Maze Representation (0 = free path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 0]
]

start = (0, 0)  # Start Point (row, col)
goal = (5, 5)   # Goal Point

# Possible Moves (Up, Down, Left, Right)
moves = [(1,0), (-1,0), (0,1), (0,-1)]

# ---------------- DFS Implementation ----------------
def dfs(maze, start, goal):
    stack = [(start, [start])]
    visited = set()
    
    while stack:
        (x, y), path = stack.pop()
        
        if (x, y) == goal:
            return path
        
        if (x, y) not in visited:
            visited.add((x, y))
            
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                    stack.append(((nx, ny), path + [(nx, ny)]))
    return None

# ---------------- BFS Implementation ----------------
def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == goal:
            return path
        
        if (x, y) not in visited:
            visited.add((x, y))
            
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0:
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None

# ---------------- Run Both ----------------
dfs_path = dfs(maze, start, goal)
bfs_path = bfs(maze, start, goal)

print("DFS Path:", dfs_path)
print("BFS Path (Shortest):", bfs_path)
