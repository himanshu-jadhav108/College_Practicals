class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# i. Insert node in BST
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

# ii. Longest path (Height of tree)
def longest_path(root):
    if root is None:
        return 0
    return 1 + max(longest_path(root.left), longest_path(root.right))

# iii. Minimum value in tree
def find_min(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.data

# iv. Mirror tree (swap left and right pointers)
def mirror(root):
    if root:
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)

# v. Search value in BST
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

# Inorder traversal for visualization
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

values = [50, 30, 70, 20, 40, 60, 80]   
root = None
for v in values:
    root = insert(root, v)


print("\nLongest Path Length:", longest_path(root))
print("Minimum Value:", find_min(root))

x = 40
print(f"Search {x}:", "Found" if search(root, x) else "Not Found")

mirror(root)