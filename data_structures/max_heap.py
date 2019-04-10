"""Max Heap implemented in python."""


class Node:
    """Node with a value, and two children."""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxHeap:
    """Max Heap data structure."""

    def __init__(self):
        self.root = None

    def insert(self, val):
        curr = self.root
        while curr:
            if curr.val < val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    return val
            elif curr.val >= val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    return val
        self.root = Node(val)

