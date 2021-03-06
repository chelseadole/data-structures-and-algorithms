"""Implementation of Binary Search Tree (BST) in python."""


class Node:
    """A single node in a BST."""

    def __init__(self, value, left=None, right=None):
        """Initialization of Node class for BST."""
        self.value = value
        self.left = left
        self.right = right


class BST:
    """Binary Search Tree."""

    def __init__(self, val):
        """Initialization of BST."""
        self.root = Node(val)

    def insert(self, value):
        """Insert a node value into the BST."""
        curr = self.root
        while curr:
            if value < curr.value:
                if curr.left is None:
                    curr.left = Node(value)
                    break
                else:
                    curr = curr.left
            elif value > curr.value:
                if curr.right is None:
                    curr.right = Node(value)
                    break
                else:
                    curr = curr.right
            else:
                break

    def search(self, value):
        """Search to see if a value is in BST."""
        curr = self.root
        while curr:
            if value == curr.value:
                return "VALUE: {} in BST".format(value)
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return "VALUE {} not in BST".format(value)
