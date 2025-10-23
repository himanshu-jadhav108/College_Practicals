class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = []
    
    # Enqueue (Add order)
    def enqueue(self, order):
        if len(self.queue) == self.size:
            print("Cannot accept more orders (Queue Full).")
        else:
            self.queue.append(order)
            print(f"Order '{order}' added successfully.")

    # Dequeue (Serve order)
    def dequeue(self):
        if len(self.queue) == 0:
            print("(Queue Empty) No orders to serve.")
        else:
            served = self.queue.pop(0)
            print(f"🍕 Order '{served}' served successfully.")

    # Display Orders
    def display(self):
        if len(self.queue) == 0:
            print("No pending orders.")
        else:
            print("📋 Pending Orders:", self.queue)


# ----------- Main Simulation ------------
M = int(input("Enter maximum number of orders (M): "))
q = Queue(M)

while True:
    print("\n--- Pizza Parlor Order System ---")
    print("1. Add Order")
    print("2. Serve Order")
    print("3. Display Orders")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        order = input("Enter order name: ")
        q.enqueue(order)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
