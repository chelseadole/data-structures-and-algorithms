"""Implementation of a doubly linked list."""


class Node:
    """A single node of a doubly linked list."""

    def __init__(self, value, next_val=None, prev_val=None):
        """Initialization of Node class."""
        self.value = value
        self.next = next_val
        self.prev = prev_val


class DLL:
    """Doubly linked list."""

    def __init__(self):
        """Initialization of Doubly Linked List class."""
        self.head = None
        self.tail = None

    def insert(self, val):
        """Insert value into head of DLL."""
        node = Node(val, self.head, None)
        if not self.head:
            self.head = self.tail = node
        else:
            self.head.prev = node
            self.head = node

    def remove(self, val):
        """Remove a value from a DLL."""
        curr = self.head

        while curr:
            if curr.value == val:
                if curr.prev:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                else:
                    self.head = curr.next
                    curr.next.prev = None
            curr = curr.next

    def show(self):
        """Print DLL."""
        dll = []
        curr = self.head
        while curr:
            dll.append(str(curr.value))
            curr = curr.next
        print(" --> ".join(dll))
