class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        # Simple hash based on sum of ASCII values of characters
        return sum(ord(char) for char in key) % self.size

    def insert(self, name, phone):
        index = self.hash_function(name)

        # Linear probing for collision handling
        while self.table[index] is not None:
            if self.table[index][0] == name:
                break  # Update existing entry
            index = (index + 1) % self.size

        self.table[index] = (name, phone)

    def search(self, name):
        index = self.hash_function(name)
        print(self.table[index])

        # Linear probing to find the correct entry
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == name:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break  # Came full circle, not found
        return None

    def display(self):
        print("\nTelephone Book:")
        for i, entry in enumerate(self.table):
            if entry:
                print(f"Index {i}: {entry[0]} -> {entry[1]}")
            else:
                print(f"Index {i}: Empty")

# Example usage
ht = HashTable()

# Inserting data
ht.insert("Alice", "1234567890")
ht.insert("Bob", "9876543210")
ht.insert("Charlie", "5555555555")
ht.insert("David", "8888888888")
ht.insert("Eve", "1111111111")

# Display table
ht.display()

# Searching
name = "Charlie"
number = ht.search(name)
if number:
    print(f"\nPhone number of {name}: {number}")
else:
    print(f"\n{name} not found in telephone book.")