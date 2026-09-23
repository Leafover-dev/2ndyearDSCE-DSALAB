class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None or self.table[new_index] == "DELETED":
                self.table[new_index] = key
                print(key, "inserted")
                return
        print("Hash table is full")

    def search(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                break
            if self.table[new_index] == key:
                print(key, "found at index", new_index)

                return
        print(key, "not found")

    def delete(self, key):
        index = self.hash_function(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] == key:
                self.table[new_index] = "DELETED"
                print(key, "deleted")
                return
        print(key, "not found")

    def display(self):
        print("\nHash Table:")
        for i in range(self.size):
            print(i, ":", self.table[i])

# Main program
ht = HashTable(10)
ht.insert(25)
ht.insert(35)
ht.insert(15)
ht.insert(42)
ht.display()
ht.search(35)
ht.search(50)
ht.delete(35)
ht.display()