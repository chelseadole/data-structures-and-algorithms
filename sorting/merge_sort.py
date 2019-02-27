"""Merge Sort algorithm. 

"Divide and conquer" style sorting algorithm, which takes an input list. It breaks
the list into subsections, and sorts these with each other until they have a length of 1.
"""


def merge_sort(lst):
    """Merge Sort."""
    if len(lst) <= 1:
        return lst

    center = len(lst) // 2
    left = lst[center:]
    right = lst[:center]

    while 