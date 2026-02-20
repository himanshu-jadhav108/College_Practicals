#Name: Himanshu H. Jadhav
#Roll No. : SE-27
#Batch : S2
#Queue

class PizzaQueue:
    def __init__(self, max_orders):
        self.queue = []
        self.max_orders = max_orders

    # Add job/order to the queue
    def add_order(self, order):
        if len(self.queue) >= self.max_orders:
            print("Queue Full! Cannot accept more orders.")
        else:
            self.queue.append(order)
            print(f"Order '{order}' added successfully.")

    # Serve/delete order from the queue (FIFO)
    def serve_order(self):
        if len(self.queue) == 0:
            print("No orders to serve.")
        else:
            order = self.queue.pop(0)
            print(f"Order '{order}' served successfully.")

    # Display current queue
    def display_queue(self):
        if len(self.queue) == 0:
            print("No pending orders.")
        else:
            print("Current Orders in Queue:", end=" ")
            print(" <- ".join(self.queue))

# ------------------ MAIN PROGRAM ------------------
if __name__ == "__main__":
    M = int(input("Enter maximum number of orders the parlor can accept: "))
    pizza_queue = PizzaQueue(M)

    while True:
        print("\n===== Pizza Parlor Job Queue Menu =====")
        print("1. Add Order")
        print("2. Serve Order")
        print("3. Display Queue")
        print("4. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            order = input("Enter order name: ")
            pizza_queue.add_order(order)
        elif choice == 2:
            pizza_queue.serve_order()
        elif choice == 3:
            pizza_queue.display_queue()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")
