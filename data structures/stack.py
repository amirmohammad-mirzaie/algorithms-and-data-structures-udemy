class Stack:
    def __init__(self):
        self.stack = []
    # checking if the stack is empty
    def is_empy(self):
        return self.stack == []

    # pushing a new value to the stack
    def push(self, value):
        self.stack.append(value)

    # pop the latest value from the stack
    def pop(self):
        value = self.stack[-1]
        del self.stack[-1]

        return value

    # getting the last value in the stack
    def peek(self):
        return self.stack[-1]

    # getting the size of the stack
    def size_stack(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
print(stack.peek())
