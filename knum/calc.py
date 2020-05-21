"""
Structure: stack & postfix expression for calc
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return True if not self.stack else False

    def size(self):
        return len(self.stack)


