from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ---------------- BST Operations ----------------

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def longest_path(root):
    if root is None:
        return 0
    return 1 + max(longest_path(root.left), longest_path(root.right))

def find_min(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.data

def swap(root):
    if root:
        root.left, root.right = root.right, root.left
        swap(root.left)
        swap(root.right)

def search(root, key):
    if root is None:
        return None
    if root.data == key:
        return root
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def level_order(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    level = 1
    while q:
        count = len(q)
        print(f"Level {level}: ", end="")
        for _ in range(count):
            node = q.popleft()
            print(node.data, end=" ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        print()
        level += 1

# ---------------- MAIN PROGRAM -----------------
if __name__ == "__main__":
    values = [50, 30, 70, 20, 40, 60, 80]
    root = None
    for v in values:
        root = insert(root, v)

    while True:
        print("\n===== Binary Search Tree Menu =====")
        print("1. Display Inorder Traversal")
        print("2. Display Level Order Traversal")
        print("3. Insert New Node")
        print("4. Longest Path (Height of Tree)")
        print("5. Find Minimum Value")
        print("6. Swap Left and Right Pointers (Mirror)")
        print("7. Search a Value")
        print("8. Count Total Nodes")
        print("9. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            print("Inorder Traversal:", end=" ")
            inorder(root)
            print()
        elif choice == 2:
            print("Level Order Traversal:")
            level_order(root)
        elif choice == 3:
            val = int(input("Enter value to insert: "))
            root = insert(root, val)
            print(f"Inserted {val} successfully.")
        elif choice == 4:
            print("Longest Path Length (Height):", longest_path(root))
        elif choice == 5:
            print("Minimum Value in BST:", find_min(root))
        elif choice == 6:
            swap(root)
            print("Swapped left and right pointers at every node (Mirror applied).")
        elif choice == 7:
            key = int(input("Enter value to search: "))
            found = search(root, key)
            print(f"{key} {'Found' if found else 'Not Found'} in BST.")
        elif choice == 8:
            print("Total Nodes in BST:", count_nodes(root))
        elif choice == 9:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")
