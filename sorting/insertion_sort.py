"""Insertion Sort algorithm.

NOTES:

* Algorithm iterates through each element in an array, and moves it back until it's in the correct place
* If item is larger than the index before, it leaves it in place

"""


def insertion_sort(lst):
    """Insertion sort algorithm."""
    for i in range(1, len(lst)):
        start_val = lst[i]
        next_val = i - 1
        while next_val >= 0 and start_val < lst[next_val]:
            lst[next_val + 1] = lst[next_val]
            next_val -= 1
        lst[next_val + 1] = start_val
    return lst

print(insertion_sort([5, 4, 3, 2, 1]))
