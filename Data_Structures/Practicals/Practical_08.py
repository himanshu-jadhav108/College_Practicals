#Name: Himanshu H. Jadhav
#Roll No. : SE-27
#Batch : S2
#Tree

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

# iii. Minimum value in BST
def find_min(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.data

# iv. Swap left and right pointers at every node
def swap(root):
    if root:
        root.left, root.right = root.right, root.left
        swap(root.left)
        swap(root.right)

# v. Search a value in BST
def search(root, key):
    if root is None:
        return None
    if root.data == key:
        return root
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

# Inorder traversal (to display tree)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# -------------------------------
# Example usage
values = [50, 30, 70, 20, 40, 60, 80]
root = None
for v in values:
    root = insert(root, v)

print("Inorder Traversal:")
inorder(root)

print("\nLongest Path Length:", longest_path(root))
print("Minimum Value:", find_min(root))

x = 40
print(f"Search {x}:", "Found" if search(root, x) else "Not Found")

swap(root)
print("Inorder after Swapping:")
inorder(root)
print()
