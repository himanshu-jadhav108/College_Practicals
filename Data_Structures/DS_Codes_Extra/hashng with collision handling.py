class HashTable:
    def __init__(self, size, method="linear"):
        self.size = size
        self.table = [None] * size
        self.method = method

    # Primary hash function
    def hash1(self, key):
        if isinstance(key, str):
            total = sum(ord(c) for c in key)
            return total % self.size
        return key % self.size

    # Secondary hash for double hashing
    def hash2(self, key):
        if isinstance(key, str):
            total = sum(ord(c) for c in key)
            return 7 - (total % 7)
        return 7 - (key % 7)

    def insert(self, key, value):
        index = self.hash1(key)
        i = 0

        while self.table[index] is not None and self.table[index][0] != key:
            if self.method == "linear":
                index = (self.hash1(key) + i) % self.size
            elif self.method == "quadratic":
                index = (self.hash1(key) + i * i) % self.size
            elif self.method == "double":
                index = (self.hash1(key) + i * self.hash2(key)) % self.size
            else:
                print("Unknown collision handling method")

            i += 1
            if i >= self.size:
                print("Hash table is full!")
                return

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash1(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]

            if self.method == "linear":
                index = (self.hash1(key) + i) % self.size
            elif self.method == "quadratic":
                index = (self.hash1(key) + i * i) % self.size
            elif self.method == "double":
                index = (self.hash1(key) + i * self.hash2(key)) % self.size

            i += 1
            if i >= self.size:
                break

        return None

    def display(self):
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")


# Example usage
if __name__ == "__main__":
    print("Telephone Book using Hash Table (Linear Probing)")
    ht_linear = HashTable(10, method="linear")
    ht_linear.insert("ABCD", 1234567890)
    ht_linear.insert("DCBA", 9876543210)
    ht_linear.insert("kakde", 5656565656)
    ht_linear.insert("Shweeta", 8888888888)
    ht_linear.insert("DAC", 1111111111)
    ht_linear.display()
    #print("Search 112:", ht_linear.search(112))

    print("\nTelephone Book using Hash Table (Quadratic Probing)")
    ht_quadratic = HashTable(10, method="quadratic")
    ht_quadratic.insert("ABCD", 1234567890)
    ht_quadratic.insert("DCBA", 9876543210)
    ht_quadratic.insert("kakde", 5656565656)
    ht_quadratic.insert("Shweeta", 8888888888)
    ht_quadratic.insert("DAC", 1111111111)
    ht_quadratic.display()
    #print("Search 102:", ht_quadratic.search(102))

    print("\nTelephone Book using Hash Table (Double Hashing)")
    ht_double = HashTable(10, method="double")
    ht_double.insert("ABCD", 1234567890)
    ht_double.insert("DCBA", 9876543210)
    ht_double.insert("kakde", 5656565656)
    ht_double.insert("Shweeta", 8888888888)
    ht_double.insert("DAC", 1111111111)
    ht_double.display()
    #print("Search 101:", ht_double.search(101))
