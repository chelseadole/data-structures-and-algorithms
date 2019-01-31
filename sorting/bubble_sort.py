"""
BubbleSort algorithm.

NOTES:

* Algorithm iterates through array "lst" len(lst) times
* The first number to be "properly sorted" will be the largest number, which is
  placed at the end of the lst

"""

import sys, ast

def bubble_sort(lst):
    """Sort list by using BubbleSort algorithm."""
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    import timeit as ti

    try:
        if len(sys.argv) > 1:
            input_list = [int(i) for i in sys.argv[1].split()]
        else:
            input_list = [3, 5, 2, 10, 22, 4, 23]

        original_list = input_list.copy()

        print('Sorting array...')
        sort_time = ti.timeit("bubble_sort(input_list)",
                              setup="from __main__ import input_list, bubble_sort")

        print(f"""
            BubbleSort! 
            
            Input: {original_list}
            Sort time: {sort_time} secs
            Output: {input_list}
            
        """)
    except:
        print("""Input numbers to sort must be formatted as a string of separated numbers. \nExample: \n$ python bubble_sort.py '1 2 3 4 5'""")
