import timeit as ti
from sorting.selection_sort import selection_sort


def print_commandline_results(fn_name, argv_array):
    try:
        if len(argv_array) > 1:
            input_list = [int(i) for i in argv_array[1::]]
        else:
            input_list = [3, 5, 2, 10, 22, 4, 23]

        original_list = input_list.copy()
        print('Sorting array...')
        sort_time = ti.timeit(f"{fn_name}(input_list)",
                              setup=f"from __main__ import input_list, {fn_name}")

        print(f"""
            {fn_name} 

            Input: {original_list}
            Sort time: {round(sort_time, 3)} secs
            Output: {input_list}

        """)
    except:
        print(
            f"""Input numbers to sort must be formatted as a string of separated numbers. 
            \nExample: 
            \n$ python {fn_name}.py 1 2 3 4 5
            """)