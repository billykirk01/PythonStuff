class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

new_stack = Stack()

new_stack.push(5)

print(new_stack.stack)

new_stack.push(7)

print(new_stack.stack)

new_stack.pop()

print(new_stack.stack)

new_stack.pop()

print(new_stack.stack)