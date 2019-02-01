"""
SelectionSort algorithm.

NOTES:

* Algorithm sorts an array by repeatedly finding the minimum element from the unsorted part of the list, and putting
  it at the beginning.
* Maintains two "subarrays": (1) the sorted section, and (2) the un-sorted section

"""
import sys, os

from commandline_results import print_commandline_results


def selection_sort(lst):
    """Selection sort algorithm."""
    for i in range(len(lst) - 1):
        lowest_idx = i
        for j in range(i+1, len(lst)):
            if lst[lowest_idx] > lst[j]:
                lowest_idx = j
        lst[i], lst[lowest_idx] = lst[lowest_idx], lst[i]
    return lst


if __name__ == '__main__':
    print_commandline_results('selection_sort', sys.argv)
    # import timeit as ti
    # try:
    #     if len(sys.argv) > 1:
    #         input_list = [int(i) for i in sys.argv[1::]]
    #     else:
    #         input_list = [3, 5, 2, 10, 22, 4, 23]
    #
    #     original_list = input_list.copy()
    #
    #     print('Sorting array...')
    #     sort_time = ti.timeit("selection_sort(input_list)",
    #                           setup="from __main__ import input_list, selection_sort")
    #
    #     print(f"""
    #         Selection Sort!
    #
    #         Input: {original_list}
    #         Sort time: {round(sort_time, 3)} secs
    #         Output: {input_list}
    #
    #     """)
    # except:
    #     print(
    #         """Input numbers to sort must be formatted as a string of separated numbers.
    #         \nExample:
    #         \n$ python selection_sort.py 1 2 3 4 5
    #         """)
