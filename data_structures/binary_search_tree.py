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

    def __init__(self, root=None):
        """Initialization of BST."""
        self.root = root

    def insert(self, root, data):
        """Insert a value node into the BST."""
        if root is None:
            return Node(data)
        else:
            if data < self.curr.value:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
            return root
