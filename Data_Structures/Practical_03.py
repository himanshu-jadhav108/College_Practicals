#Name: Himanshu H. Jadhav
#Roll No. : SE-27
#Batch : S2
#Hashing

class HashTable:
    def __init__(self, size=10 , method="linear"):
        self.size = size
        self.table = [None] * size
        self.method = method
    
    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size
    
    def hash2(self, key):
        return 7 - (sum(ord(c) for c in key) % 7)
    
    def insert(self, name, phone):
        index0 = self.hash_function(name)
        i = 0
        while i < self.size :
            if self.method == "linear":
                index = (index0 + i) % self.size
            elif self.method == "quadratic":
                index = (index0 + i**2) % self.size
            elif self.method == "double":
                index = (index0 + i * self.hash2(name)) % self.size
            else:
                print("Unknown Collision Method!!!")
                return

            if self.table[index] is None or self.table[index][0] == name:
                self.table[index] = (name, phone)
                return

            i += 1
        print(f"Hash Table is full, cannot insert {name}")

    def search(self, name):
        index0 = self.hash_function(name)
        i = 0
        while i < self.size:
            if self.method == "linear":
                index = (index0 + i) % self.size
            elif self.method == "quadratic":
                index = (index0 + i**2) % self.size
            elif self.method == "double":
                index = (index0 + i*self.hash2(name)) % self.size

            if self.table[index] is None:
                break
            if self.table[index][0] == name:
                print(f"\nPhone number of {name}: {self.table[index][1]}")
                return self.table[index][1]

            i += 1

        print(f"\n{name} not found in telephone book.")
        return None
  
    def display(self):
        print("\nTelephone Book:")
        for i, entry in enumerate(self.table):
            if entry is None:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}: Name = {entry[0]}, Phone = {entry[1]}")


print("Choose Collision Handling Method:")
print("1. Linear Probing")
print("2. Quadratic Probing")
print("3. Double Hashing")
choice = input("Enter choice (1/2/3): ")
method_map = {"1": "linear", "2": "quadratic", "3": "double"}
method = method_map.get(choice, "linear")

n = int(input("Enter number of clients: "))
hash_table = HashTable(method=method)

for _ in range(n):
    name = input("Enter client name: ")
    phone = input("Enter client phone number: ")
    hash_table.insert(name, phone)

hash_table.display()

search_name = input("\nEnter name to search for phone number: ")
hash_table.search(search_name)
