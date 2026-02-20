import time

# Map regions and neighbors
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

colors = ['Red', 'Green', 'Blue']
assignment = {}

def print_assignment():
    print("Current Assignment:")
    for region in sorted(neighbors):
        color = assignment.get(region, "None")
        print(f"  {region}: {color}")
    print("\n")

def is_consistent(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack():
    if len(assignment) == len(neighbors):
        return assignment

    unassigned = [r for r in neighbors if r not in assignment][0]

    for color in colors:
        if is_consistent(unassigned, color):
            assignment[unassigned] = color
            print(f"Assigning {color} to {unassigned}")
            print_assignment()
            time.sleep(0.5)  # visualize delay
            result = backtrack()
            if result:
                return result
            print(f"Backtracking on {unassigned}")
            del assignment[unassigned]

    return None

solution = backtrack()
print("✅ Final Color Assignment:")
for region, color in solution.items():
    print(f"  {region}: {color}")
