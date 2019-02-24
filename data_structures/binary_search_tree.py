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

    def insert(self, data):
        """Insert a value node into the BST."""
        if self.root is None:
            self.root = Node(data)
            return self.root
        elif data < self.root.value:
            self.root = self.insert(data, node.left)
        else:
            node.right = self.insert(data, node.right)


def insert(root, data):
    node = Node(data)
    if root is None:
        root = node
    elif root.data >= data:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, data)
    else:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, data)