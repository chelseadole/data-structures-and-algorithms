"""Quick Sort algorithm.

Algorithm arbitrarily picks a "pivot" element from the array, and iterates
from both ends of array to center: switching elements at beginning and end
pointers when end_elem is smaller than pivot and start_elem is larger than
pivot. When the two pointers meet, both quicksorted halves of the array are
then Quicksorted again. This repeats until each "section" has length of 1.
"""


def quick_sort(lst):
    """Create a sorted copy of the given list using quick sort."""
    if len(lst) <= 1:
        return lst

    pivot = lst[0]

    left = [x for x in lst[1:] if x <= pivot]
    right = [x for x in lst[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)
