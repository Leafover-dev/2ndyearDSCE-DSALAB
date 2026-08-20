class ArrayOperations:
    def __init__(self, array):
        self.array = array
    # Insert element at a specified index
    def insert(self, element, index):
        self.array.insert(index, element)
        print(f"Array after insertion: {self.array}")

    # Delete element at a specified index
    def delete(self, index):
        if 0 <= index < len(self.array):
            removed_element = self.array.pop(index)
            print(f"Array after deletion of element {removed_element}: {self.array}")
        else:
            print("Index out of range")


    # Sorting the array in ascending order
    def sort(self):
        self.array.sort()
        print(f"Array after sorting: {self.array}")


    # Searching for an element using linear search
    def search(self, element):
        if element in self.array:
            index = self.array.index(element)
            print(f"Element {element} found at index {index}")
        else:
            print(f"Element {element} not found")

# Driver Code
if __name__== "__main__":
    # Initial array
    arr_ops = ArrayOperations([10, 20, 30, 40, 50])

    # Inserting an element
    arr_ops.insert(25, 2)

    # Deleting an element
    arr_ops.delete(4)

    # Sorting the array
    arr_ops.sort()

    # Searching for an element
    arr_ops.search(30)
    arr_ops.search(60)