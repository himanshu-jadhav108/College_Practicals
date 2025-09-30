#Singly-Linked-List

class Node:
    def __init__(self, prn, name):
        self.prn = prn
        self.name = name
        self.next = None

class PinnacleClub:
    def __init__(self):
        self.head = None  # President
        self.tail = None  # Secretary

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

    # Add member before secretary
    def add_member(self, prn, name):
        new_node = Node(prn, name)
        if self.head is None:
            print("List is empty. Add president and secretary first.")
            return
        # If only president and secretary
        if self.head == self.tail:
            self.head.next = new_node
            self.tail = new_node
            return
        # Insert before secretary
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        new_node.next = self.tail
        temp.next = new_node

    # Delete president
    def delete_president(self):
        if self.head is None:
            print("List is empty.")
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    # Delete secretary
    def delete_secretary(self):
        if self.head is None:
            print("List is empty.")
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = None
        self.tail = temp

    # Delete member by PRN
    def delete_member(self, prn):
        if self.head is None:
            print("List is empty.")
            return
        # Check president
        if self.head.prn == prn:
            self.delete_president()
            return
        # Check secretary
        if self.tail.prn == prn:
            self.delete_secretary()
            return
        # Check middle members
        prev = self.head
        curr = self.head.next
        while curr and curr != self.tail:
            if curr.prn == prn:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        print("Member not found.")

    # Display members with roles
    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        print("Club Members (PRN - Name - Role):")
        temp = self.head
        while temp:
            role = "Member"
            if temp == self.head:
                role = "President"
            elif temp == self.tail:
                role = "Secretary"
            print(f"{temp.prn} - {temp.name} - {role}")
            temp = temp.next

    # Count total members
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
        elif other.head:
            self.tail.next = other.head
            self.tail = other.tail

# EXAMPLE

if __name__ == "__main__":
    # Division A
    divA = PinnacleClub()
    divA.add_president(101, "Himanshu")
    divA.add_member(102, "Durgesh")
    divA.add_member(103, "Omkar")
    divA.add_secretary(104, "Ritesh")
    
    print("Division A:")
    divA.display()
    print("Total members in Div A:", divA.count_members())

    print("\nAfter deleting Durgesh:")
    divA.delete_member(102)
    divA.display()
    print("Total members now:", divA.count_members())

    # Division B
    divB = PinnacleClub()
    divB.add_president(201, "Kalpesh")
    divB.add_member(202, "Paritosh")
    divB.add_secretary(203, "Indrajeet")
    
    print("\nDivision B:")
    divB.display()

    # Concatenate A and B
    divA.concatenate(divB)
    print("\nAfter concatenation of Div A and Div B:")
    divA.display()
    print("Total combined members:", divA.count_members())
