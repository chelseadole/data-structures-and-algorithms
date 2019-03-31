"""
Create a Queue from two stacks. First in, first out.
"""

from data_structures.stack import Stack


class Queue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, val):
        while self.s1.size() > 0:
            self.s2.push(self.s1.pop())
        self.s2.push(val)
        while self.s2.size() > 0:
            self.s1.push(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()

