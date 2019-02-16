"""Implementation of a singly linked list."""


class Node:
    """A single node of a linked list."""

    def __init__(self, value, next_val=None):
        """Initialization of Node class."""
        self.value = value
        self.next = next_val


class LinkedList:
    """Singly linked list."""

    def __init__(self, head=None, tail=None):
        """Initialization of LinkedList class."""
        self.head = head
        self.tail = tail

    def insert(self, data):
        """Insert a node into a linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if not self.head:
            self.tail = new_node
