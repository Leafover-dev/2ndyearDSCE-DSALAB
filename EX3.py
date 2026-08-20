class Stack:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []
    # Push an element onto the stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")
    # Pop an element from the stack
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop.")
        else:
            popped_item = self.stack.pop()
            print(f"Popped {popped_item} from stack")
            return popped_item
    # Peek the top element of the stack
    def peek(self):
        if self.is_empty():
            print("Stack is empty! No top element.")
        else:
            print(f"Top element is {self.stack[-1]}")
            return self.stack[-1]
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    # Return the number of elements in the stack
    def size(self):
        return len(self.stack)
    # Display the stack
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Current stack:", self.stack)
    # Driver Code

if __name__ == "__main__":
    stack = Stack()
    # Push some elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    # Display the stack
    stack.display()
    # Peek the top element
    stack.peek()
    # Pop an element
    stack.pop()
    # Display the stack after popping
    stack.display()
    # Check if stack is empty
    print("Is the stack empty?", stack.is_empty())
    # Get the size of the stack
    print("Size of the stack:", stack.size())
    # Pop all elements
    stack.pop()
    stack.pop()
    stack.pop()
    # Check if stack is empty after popping all elements
    print("Is the stack empty now?", stack.is_empty())