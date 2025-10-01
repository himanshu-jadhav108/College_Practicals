# Experiment No. 4 - Constraint Satisfaction Problem - Map ColoringS

# Define the map: each region and its neighbors
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Define available colors
colors = ['Red', 'Green', 'Blue']

# Initialize assignments
assignment = {}

def is_consistent(region, color):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack():
    # If all regions are assigned, return the assignment
    if len(assignment) == len(neighbors):
        return assignment

    # Select unassigned region
    unassigned = [r for r in neighbors if r not in assignment][0]

    for color in colors:
        if is_consistent(unassigned, color):
            assignment[unassigned] = color
            result = backtrack()
            if result:
                return result
            # Backtrack
            del assignment[unassigned]

    return None

solution = backtrack()
print("Color Assignments:", solution)