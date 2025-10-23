class Node:
    def __init__(self, prn, name):
        self.prn = prn
        self.name = name
        self.next = None

class PinnacleClub:
    def __init__(self):
        self.head = None  # Head is the president
        self.tail = None  # Tail is the secretary

    # Add president at the beginning
    def add_president(self, prn, name):
        new_node = Node(prn, name)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Add secretary at the end
    def add_secretary(self, prn, name):
        new_node = Node(prn, name)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Add member in the middle
    def add_member(self, prn, name):
        new_node = Node(prn, name)
        if self.head is None or self.tail is None:
            print("List is empty or incomplete. Add both president and secretary first.")
            return
        
        # If only president exists
        if self.head == self.tail:
            print("Add secretary before adding members.")
            return
            
        temp = self.head
        while temp.next != self.tail and temp.next is not None:
            temp = temp.next
        new_node.next = self.tail
        temp.next = new_node

    # Delete president
    def delete_president(self):
        if self.head is None:
            print("List is empty.")
            return
        self.head = self.head.next

    # Delete secretary
    def delete_secretary(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp

    # Delete member by PRN
    def delete_member(self, prn):
        if self.head is None:
            print("List is empty.")
            return
        if self.head.prn == prn:
            self.delete_president()
            return
        if self.tail.prn == prn:
            self.delete_secretary()
            return
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.prn == prn:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        print("Member not found.")

    # Display all members
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        print("Club Members (PRN - Name):")
        temp = self.head
        while temp:
            print(f"{temp.prn} - {temp.name}")
            temp = temp.next

    # Count total number of members
    def count_members(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Concatenate another club list
    def concatenate(self, other):
        if self.head is None:
            self.head = other.head
            self.tail = other.tail
        elif other.head is not None:
            self.tail.next = other.head
            self.tail = other.tail

# ----------------------------
# Sample Usage
# ----------------------------
if __name__ == "__main__":
    divA = PinnacleClub()
    divA.add_president(101, "Alice")
    divA.add_secretary(104, "Diana")
    divA.add_member(102, "Bob")
    divA.add_member(103, "Charlie")
    
    print("Division A:")
    divA.display()
    print("Total members in Div A:", divA.count_members())

    print("\nAfter deleting Bob:")
    divA.delete_member(102)
    divA.display()
    print("Total members now:", divA.count_members())

    # Division B
    divB = PinnacleClub()
    divB.add_president(201, "Eve")
    divB.add_member(202, "Frank")
    divB.add_secretary(203, "Grace")
    
    print("\nDivision B:")
    divB.display()

    # Concatenate
    divA.concatenate(divB)
    print("\nAfter concatenation of Div A and Div B:")
    divA.display()
    print("Total combined members:", divA.count_members())
