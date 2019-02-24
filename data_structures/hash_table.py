"""Implementation of a hash table structure in Python.

Basically a Python dictionary. Data structures comprised of "keys" which point at
"values". When key/value pair is inserted into the hash table, the key is "hashed"
(encoded) into a hash value. This hash value is used as an index for an array. 

On "collisions" (where a hashed key is inserted into the table which already exists),
the structure appends both the unhashed key and value into an array at that hash index. 
Or it inserts it into a LinkedList there."""
from data_structures.singly_linked_list import LinkedList


class HashTable:

    def __init__(self, size):
        """Initialization of hash table of declared size."""
        if size and isinstance(size, int):
            self.size = size
            self.hash_table = [LinkedList()] * self.size
        else:
            raise ValueError("HashTable requires parameter \"size\" of type \"int\"")

    def _compress(self, key):
        """Compress a key into a compressed hashed index value between 0 and self.size,
        return compressed and hashed key value."""
        return hash(key) % self.size

    def insert(self, key, val):
        """Insert a value into Hash Table."""
        idx = self._compress(key)
        self.hash_table[idx].insert([key, val])

    def get(self, key):
        """Retrieve the value at <KEY> of HashTable."""
        idx = self._compress(key)
        val = self.hash_table[idx].hash_search(key)
        return val or "KEY: \"{}\" not in HashTable".format(key)

    def delete(self, key):
        """Delete the value at <KEY> from HashTable."""
        idx = self._compress(key)
        if self.hash_table[idx].hash_delete(key):
            return "Deleted KEY: \"{}\"".format(key)
        return "KEY: \"{}\" not in HashTable".format(key)

