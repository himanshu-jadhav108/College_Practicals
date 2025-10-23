# Experiment No. 4
# Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert at the end (to create list easily)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        print("1->", temp.next)
        while temp.next:
            temp = temp.next
            print("2->", temp.next)
        temp.next = new_node
        print("3->", temp.next)

    # Insert after a given node
    def insert_after(self, prev_data, new_data):
        temp = self.head
        while temp:
            if temp.data == prev_data:   # find the node
                new_node = Node(new_data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
        print("Node with data", prev_data, "not found!")

    # Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> " if temp.next else "\n")
            temp = temp.next

# --- Demo ---
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print("Before Insertion:")
ll.display()

ll.insert_after(20, 25)   # Insert 25 after 20

print("After Insertion:")
ll.display()
