"""
BubbleSort algorithm.

NOTES:

* Algorithm iterates through array "lst" len(lst) times
* The first number to be "properly sorted" will be the largest number, which is
  placed at the end of the lst

"""

def bubble_sort(lst):
    """Sort list by using BubbleSort algorithm."""
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    import timeit as ti
    import random
    best_case = list(range(8))
    worst_case = list(range(8))[::-1]
    random_case = [random.randint(0, 8) for i in range(8)]

    print('Running best case...')
    best_time = ti.timeit("bubble_sort(best_case)",
                       setup="from __main__ import best_case, bubble_sort")

    print('Running worst case...')
    worst_time = ti.timeit("bubble_sort(worst_case)",
                       setup="from __main__ import worst_case, bubble_sort")

    print('Running random case...')
    random_time = ti.timeit("bubble_sort(random_case)",
                       setup="from __main__ import random_case, bubble_sort")

    print(f"""
        BubbleSort! 
        
        Input: [0, 1, 2, 3, 4, 5, 6, 7, 8]
        Sort time: {best_time} seconds
        
        Input: [8, 7, 6, 5, 4, 3, 2, 1, 0]
        Sort time: {worst_time} seconds
        
        Input: List of 8 randomized integers between 0 and 8
        Sort time: {random_time} seconds
    """)
