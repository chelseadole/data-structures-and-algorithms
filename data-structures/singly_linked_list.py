"""Implementation of a singly linked list."""


class Node:
    """A single node of a linked list."""

    def __init__(self, value, next_val=None):
        """Initialization of Node class."""
        self.value = value
        self.next = next_val


class LinkedList:
    """Singly linked list."""

    def __init__(self, head=None):
        """Initialization of LinkedList class."""
        if head:
            self.head = Node(head)
        else:
            self.head = None
        self.tail = None
        self.length = 0

    def insert(self, data):
        """Insert a node into a linked list."""
        new_node = Node(data, self.head, None)
        if not self.head:
            self.tail = new_node
        self.head = new_node
        self.length += 1

    def size(self):
        """Return length of List object."""
        return self.length

    def search(self, val):
        """Check to see if a Node with data "val" is in List."""
        curr = self.head
        iters = 1
        while curr:
            iters += 1
            if curr.value == val:
                return curr, iters
            curr = curr.next
        return curr

    def delete(self, val):
        """Check to see if Node is in List. If it is, delete it."""
        prev = None
        curr = self.head
        while curr:
            if curr.value == val:
                if prev:
                    prev.next = curr.next
                    return 'Deleted {}'.format(val)
            prev = curr
            curr = curr.next
        return '{} not found in LinkedList'.format(val)




