from gen_rand_array import gen_rand_array
from two_pivot_block_quicksort import two_pivot_block_quicksort
from merge_sort import merge_sort

import os
import time

def compare_sort_algs(sz, arr_type):
    arr = gen_rand_array(sz, arr_type)
    print("-" * 32)
    print(["Sorted", "Random", "Reversed"][arr_type], "array of size", sz)

    try:
        start_time = time.time()
        res = two_pivot_block_quicksort(arr)
        end_time = time.time()
        print("Two Pivot Block Quicksort:", end_time - start_time)
    except:
        print("Two Pivot Block Quicksort: -")

    start_time = time.time()
    res2 = merge_sort(arr)
    end_time = time.time()
    print("Merge Sort:", end_time - start_time)

    filename = "datasets/" + str(sz) + "-" + str(arr_type) + ".in"
    f = open(filename, "w")
    for i in range(len(arr)):
        f.write(str(arr[i]))
        if i < len(arr):
            f.write(" ")
        else:
            f.write("\n")
    f.close()

    filename = "results/" + str(sz) + "-" + str(arr_type) + ".out"
    f = open(filename, "w")
    for i in range(len(res2)):
        f.write(str(res2[i]))
        if i < len(res2):
            f.write(" ")
        else:
            f.write("\n")
    f.close()

if __name__ == "__main__":
    if not os.path.exists("datasets"):
        os.makedirs("datasets")
    if not os.path.exists("results"):
        os.makedirs("results")

    for sz in [2 ** 9, 2 ** 13, 2 ** 16]:
        for arr_type in range(3):
            compare_sort_algs(sz, arr_type)