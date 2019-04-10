"""
Stack data structure. First in, last out.
"""


class Stack:

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, val):
        self.items.insert(0, val)

    def pop(self):
        if self.size() > 0:
            return self.items.pop(0)
        return "Cannot pop from empty Stack"
