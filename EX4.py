size = 5
queue = [None] * size
front = -1
rear = -1

def enqueue(item):
    global front, rear

    if rear == size - 1:
        print("Queue Overflow")
    else:
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = item
        print(item, "inserted")

def dequeue():
    global front, rear

    if front == -1 or front > rear:
        print("Queue Underflow")
    else:
        print(queue[front], "deleted")
        front += 1

def display():
    if front == -1 or front > rear:
        print("Queue is Empty")
    else:
        print("Queue Elements:")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()

enqueue(10)
enqueue(20)
enqueue(30)
display()

dequeue()
display()