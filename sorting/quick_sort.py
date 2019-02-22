"""Quick Sort algorithm.

Algorithm arbitrarily picks a "pivot" element from the array, and iterates
from both ends of array to center: switching elements at beginning and end
pointers when end_elem is smaller than pivot and start_elem is larger than
pivot. When the two pointers meet, both quicksorted halves of the array are
then Quicksorted again. This repeats until each "section" has length of 1.
"""


def _partition(lst, beg_idx, end_idx):
    """Recursively QuickSort section."""
    if len(lst) > 0:
        pivot = beg_idx
        while beg_idx < end_idx:
            while lst[beg_idx] < pivot:
                beg_idx += 1
            while lst[end_idx] > pivot:
                end_idx -= 1
            lst[beg_idx], lst[end_idx] = lst[end_idx], lst[beg_idx]

        _partition(lst, beg_idx, split - 1)
        _partition(lst, split + 1, end_idx)


def quicksort(lst):
    """Quicksort algorithm."""
    return _partition(lst, 0, len(lst) - 1)
