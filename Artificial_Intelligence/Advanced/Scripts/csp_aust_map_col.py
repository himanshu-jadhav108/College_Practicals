import time

# Australian states and neighbors
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []  # Tasmania has no land borders
}

colors = ['Red', 'Green', 'Blue', 'Yellow']
assignment = {}

def print_assignment():
    for state in sorted(neighbors):
        color = assignment.get(state, "None")
        print(f"{state}: {color}")
    print()

def is_consistent(state, color):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack():
    if len(assignment) == len(neighbors):
        return assignment

    unassigned = [s for s in neighbors if s not in assignment][0]

    for color in colors:
        if is_consistent(unassigned, color):
            assignment[unassigned] = color
            print(f"Assigning {color} to {unassigned}")
            print_assignment()
            time.sleep(0.5)
            result = backtrack()
            if result:
                return result
            del assignment[unassigned]
            print(f"Backtracking on {unassigned}")
    return None

solution = backtrack()
print("✅ Final Australia Map Coloring:")
for state, color in solution.items():
    print(f"{state}: {color}")
