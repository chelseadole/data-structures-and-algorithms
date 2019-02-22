"""
SelectionSort algorithm.

NOTES:

* Algorithm sorts an array by repeatedly finding the minimum element from the unsorted part of the list, and putting
  it at the beginning.
* Maintains two "subarrays": (1) the sorted section, and (2) the un-sorted section

"""
import sys


def selection_sort(lst):
    """Selection sort algorithm."""
    for i in range(len(lst) - 1):
        lowest_idx = i
        for j in range(i + 1, len(lst)):
            if lst[lowest_idx] > lst[j]:
                lowest_idx = j
        lst[i], lst[lowest_idx] = lst[lowest_idx], lst[i]
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
        sort_time = ti.timeit("selection_sort(input_list)", setup="from __main__ import selection_sort, input_list")

        print("SelectionSort! \nInput: {} \nSort time: {} secs \nOutput: {}".format(original_list, sort_time, input_list))

    except:
        print("""Input numbers must be formatted as separated numbers. \nExample: \n$ python selection_sort.py 1 2 3 4 5""")
