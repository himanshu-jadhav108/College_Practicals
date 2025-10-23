# Node of Doubly Linked List
class Node:
    def __init__(self, time):
        self.time = time
        self.prev = None
        self.next = None

# Doubly Linked List for appointments
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def create_slots(self, start=7, end=17):
        for t in range(start, end + 1):
            new = Node(t)
            if not self.head:
                self.head = new
                tail = new
            else:
                tail.next = new
                new.prev = tail
                tail = new

    # (a) Display free slots
    def display(self):
        if not self.head:
            print("No free slots available")
            return
        temp = self.head
        slots = []
        while temp:
            slots.append(temp.time)
            temp = temp.next
        print("Free Slots:", slots)

    # (b) Book appointment (remove slot)
    def book(self, time):
        temp = self.head
        while temp:
            if temp.time == time:  # slot found
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next  # booked first slot
                if temp.next:
                    temp.next.prev = temp.prev
                print(f"Appointment booked at {time}:00")
                return
            temp = temp.next
        print(f"Slot {time}:00 is not available")

dll = DoublyLinkedList()
dll.create_slots(9, 17)   # Create slots from 9AM to 5PM

dll.display()        # Show free slots
dll.book(10)         # Book 10 AM
dll.book(14)         # Book 2 PM
dll.display()        # Show remaining free slots