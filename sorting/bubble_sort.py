"""
BubbleSort algorithm.

NOTES:

* Algorithm iterates through array "lst" len(lst) times
* The first number to be "properly sorted" will be the largest number, which is
  placed at the end of the lst

"""

import sys


def bubble_sort(lst):
    """Sort list by using BubbleSort algorithm."""
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    """Print input, timeit, and output of sorting algorithm."""
    import timeit as ti
    input_list = [3, 5, 2, 10, 22, 4, 23]
    try:
        if len(sys.argv) > 1:
            input_list = [int(i) for i in sys.argv[1::]]
        original_list = input_list[:]
        print('Sorting array...')
        sort_time = ti.timeit("bubble_sort(input_list)", setup="from __main__ import bubble_sort, input_list")

        print("BubbleSort! \nInput: {} \nSort time: {} secs \nOutput: {}".format(original_list, sort_time, input_list))

    except:
        print("""Input numbers must be formatted as separated numbers. \nExample: \n$ python bubble_sort.py 1 2 3 4 5""")
