#Name: Himanshu H. Jadhav
#Roll No. : SE-27
#Batch : S2
#Doubly-Linked-List

class Seat:
    def __init__(self, no):
        self.no = no
        self.prev = None
        self.next = None

def create_row(n):
    head = Seat(1)
    curr = head
    for i in range(2, n+1):
        node = Seat(i)
        curr.next = node
        node.prev = curr
        curr = node
    return head

class Theater:
    def __init__(self, rows=10, seats=7):
        self.rows = rows
        self.seats = seats
        self.heads = [create_row(seats) for _ in range(rows)]

    def display(self):
        for r in range(self.rows):
            print(f"Row {r+1}: ", end="")
            curr = self.heads[r]
            if not curr:
                print("All seats booked")
            else:
                while curr:
                    print(curr.no, end=" ")
                    curr = curr.next
                print()

    def book(self, row, seat):
        if row < 1 or row > self.rows or seat < 1 or seat > self.seats:
            print("Invalid row or seat number!")
            return
        curr = self.heads[row-1]
        while curr and curr.no != seat:
            curr = curr.next
        if not curr:
            print(f"Seat {seat} in Row {row} is already booked!")
            return
        # Remove the node from doubly linked list
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.heads[row-1] = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        print(f"Seat {seat} booked in Row {row}")

    def cancel(self, row, seat):
        if row < 1 or row > self.rows or seat < 1 or seat > self.seats:
            print("Invalid row or seat number!")
            return
        node = Seat(seat)
        head = self.heads[row-1]
        # Insert at beginning if list empty or seat is smaller than head
        if not head or seat < head.no:
            node.next = head
            if head:
                head.prev = node
            self.heads[row-1] = node
            print(f"Seat {seat} canceled in Row {row}")
            return
        # Insert in sorted order
        curr = head
        while curr.next and curr.next.no < seat:
            curr = curr.next
        # If seat already exists
        if curr.next and curr.next.no == seat:
            print(f"Seat {seat} in Row {row} is already available!")
            return
        node.next = curr.next
        if curr.next:
            curr.next.prev = node
        curr.next = node
        node.prev = curr
        print(f"Seat {seat} canceled in Row {row}")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    t = Theater()

    while True:
        print("\n1.Display  2.Book  3.Cancel  4.Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            t.display()
        elif ch == 2:
            r = int(input("Row(1-10): "))
            s = int(input("Seat(1-7): "))
            t.book(r, s)
        elif ch == 3:
            r = int(input("Row(1-10): "))
            s = int(input("Seat(1-7): "))
            t.cancel(r, s)
        elif ch == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
