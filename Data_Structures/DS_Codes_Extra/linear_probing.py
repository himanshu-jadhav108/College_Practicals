# Experiment No.-3
# Simple Hash Table with Linear Probing for Telephone Book

TABLE_SIZE = 10  

class HashTable:
    def __init__(self):
        self.table = [None] * TABLE_SIZE

    def hash_function(self, name):
        # Simple hash: sum of ASCII values of characters in name
        return sum(ord(char) for char in name) % TABLE_SIZE

    def insert(self, name, phone):
        index = self.hash_function(name)

        # Linear probing for collision resolution
        for i in range(TABLE_SIZE):
            new_index = (index + i) % TABLE_SIZE
            if self.table[new_index] is None or self.table[new_index][0] == name:
                self.table[new_index] = (name, phone)
                return
        print("Hash table is full, cannot insert", name)

    def search(self, name):
        index = self.hash_function(name)

        for i in range(TABLE_SIZE):
            new_index = (index + i) % TABLE_SIZE
            if self.table[new_index] is None:
                return None  # Not found
            if self.table[new_index][0] == name:
                return self.table[new_index][1]  # Return phone number
        return None

    def display(self):
        print("\n--- Telephone Book ---")
        for i, entry in enumerate(self.table):
            print(f"Index {i}: {entry}")

# ---------- Main Program ----------

ht = HashTable()

# Insert clients
ht.insert("shyam", "9876543210")
ht.insert("Ram", "0123456789")
ht.insert("Shweta","8888888888")
ht.insert("Nitin", "1111111111")
ht.insert("Radha", "4444444444")

# Display table
ht.display()

# Search for a client
name = input("\nEnter name to search: ")
phone = ht.search(name)
if phone:
    print(f"{name}'s phone number is {phone}")
else:
    print(f"{name} not found in the telephone book.")
