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
        new_node = Node(data, self.head)
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
        while curr:
            if curr.value == val:
                return curr
            curr = curr.next
        return curr

    def delete(self, val):
        """Delete a value from list."""
        curr = self.head
        prev = None
        while curr:
            if curr.value == val:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = None
                return "Deleted {}".format(val)
            curr, prev = curr.next, curr
        return "{} not in LinkedList".format(val)

    def hash_delete(self, key):
        """Delete specifically implemented for HashTable. Deletes with assumption that val is a list.
        If val in list, delete and return val. If not in list, return None."""
        curr = self.head
        prev = None
        while curr:
            if curr.value[0] == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = None
                return curr
            curr, prev = curr.next, curr

    def hash_search(self, key):
        """"Search specially implemented for HashTable. Searches with assumption that val is a list."""
        curr = self.head
        while curr:
            if curr.value[0] == key:
                return curr.value[1]
            curr = curr.next
        return curr

