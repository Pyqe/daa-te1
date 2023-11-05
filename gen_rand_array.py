import random

def gen_rand_array(sz, arr_type):
    arr = []
    for i in range(sz):
        arr.append(random.randint(0, 2 ** 32 - 1))
    if arr_type == 0:
        arr.sort()
        return arr
    elif arr_type == 1:
        return arr
    else:
        arr.sort(reverse=True)
        return arr