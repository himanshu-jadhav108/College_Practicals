# Experiment No.-3
# Name :- Himanshu H. Jadhav
# Roll No:- 27
# Batch :- S-2
# Telephone Book Database using Hash Table

class HashTable:
    def __init__(self, size=10, method="linear"):
        self.size = size
        self.table = [None] * self.size
        self.method = method   # collision handling method

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)   # sum of ASCII values
        return total % self.size

    def hash2(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return 7 - (total % 7)

    def insert(self, name, phone):
        index = self.hash_function(name)
        i = 0
        while self.table[index] is not None and self.table[index][0] != name:
            if self.method == "linear":
                index = (self.hash_function(name) + i) % self.size
            elif self.method == "quadratic":
                index = (self.hash_function(name) + i * i) % self.size
            elif self.method == "double":
                index = (self.hash_function(name) + i * self.hash2(name)) % self.size
            else:
                print("Unknown collision handling method")

            i += 1
            if i >= self.size:
                print("Hash table is full, cannot insert", name)
                return

        self.table[index] = (name, phone)

    def search(self, name):
        index = self.hash_function(name)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == name:
                print(f"\nPhone number of {name}: {self.table[index][1]}")
                return self.table[index][1]

            if self.method == "linear":
                index = (self.hash_function(name) + i) % self.size
            elif self.method == "quadratic":
                index = (self.hash_function(name) + i * i) % self.size
            elif self.method == "double":
                index = (self.hash_function(name) + i * self.hash2(name)) % self.size

            i += 1
            if i >= self.size:
                break

        print(f"\n{name} not found in telephone book.")
        return None

    def display(self):
        print("\nTelephone Book:")
        for i in range(len(self.table)):
            if self.table[i] is None:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}: Name = {self.table[i][0]}, Phone = {self.table[i][1]}")

# Example usage
print("=== Linear Probing ===")
ht_linear = HashTable(size=10, method="linear")
ht_linear.insert("ABCD", "1234567890")
ht_linear.insert("DCBA", "9876543210")
ht_linear.insert("Shadow", "5656565656")
ht_linear.insert("Engineer", "8888888888")
ht_linear.insert("DAC", "1111111111")
ht_linear.display()
ht_linear.search("Engineer")

print("\n=== Quadratic Probing ===")
ht_quad = HashTable(size=10, method="quadratic")
ht_quad.insert("ABCD", "1234567890")
ht_quad.insert("DCBA", "9876543210")
ht_quad.insert("Shadow", "5656565656")
ht_quad.insert("Engineer", "8888888888")
ht_quad.insert("DAC", "1111111111")
ht_quad.display()
ht_quad.search("Shadow")

print("\n=== Double Hashing ===")
ht_double = HashTable(size=10, method="double")
ht_double.insert("ABCD", "1234567890")
ht_double.insert("DCBA", "9876543210")
ht_double.insert("Shadow", "5656565656")
ht_double.insert("Engineer", "8888888888")
ht_double.insert("DAC", "1111111111")
ht_double.display()
ht_double.search("ABCD")
