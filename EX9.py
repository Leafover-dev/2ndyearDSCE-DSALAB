class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] < self.heap[i]:
                self.heap[parent], self.heap[i] = (self.heap[i], self.heap[parent])
                i = parent
            else:
                break
    def delete_max(self):
        if not self.heap:
            print("Heap is empty")
            return None
        max_value = self.heap[0]
        last_value = self.heap.pop()
        if self.heap:
            self.heap[0] = last_value
            self.heapify(0)
        return max_value

    def heapify(self, i):
        n = len(self.heap)
        while True:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == i:
                break
            self.heap[i], self.heap[largest] = (self.heap[largest], self.heap[i])
            i = largest
    def display(self):
        print("Heap:" ,self.heap)


# Main program
h = MaxHeap()
elements = [50, 30, 40, 10, 20, 35, 60]
for value in elements:
    h.insert(value)
print("After insertion:")
h.display()
deleted = h.delete_max()
print("Deleted maximum element:", deleted)
print("After deletion:")
h.display()