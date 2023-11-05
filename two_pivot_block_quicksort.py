def insertion_sort(arr):
    res = arr
    for i in range(len(arr)):
        cur = res[i]
        j = i - 1
        while j >= 0 and res[j] > cur:
            res[j + 1] = res[j]
            j -= 1
        res[j + 1] = cur
    return res

BLOCK_SIZE = 1024
K = 5
PIVOT1 = 0
PIVOT2 = 2

def two_pivot_block_quicksort(arr):
    if len(arr) <= K:
        return insertion_sort(arr)
    else:
        res = arr

        res[:K] = insertion_sort(res[:K])
        res[PIVOT1], res[0] = res[0], res[PIVOT1]
        res[PIVOT2], res[-1] = res[-1], res[PIVOT2]

        p = 1
        p2 = 1
        p3 = 1
        pos = [0] * min(BLOCK_SIZE, len(arr) - 2)
        while p3 < len(arr) - 1:
            cur_block = min(BLOCK_SIZE, len(arr) - 1 - p3)

            cnt = 0
            for i in range(cur_block):
                pos[cnt] = i
                cnt += res[p3 + i] <= res[-1]
            for i in range(cnt):
                res[p3 + pos[i]], res[p2 + i] = res[p2 + i], res[p3 + pos[i]]

            cnt2 = 0
            for i in range(cnt):
                pos[cnt2] = i
                cnt2 += res[p2 + i] < res[0]
            for i in range(cnt2):
                res[p2 + pos[i]], res[p + i] = res[p + i], res[p2 + pos[i]]

            p3 += cur_block
            p2 += cnt
            p += cnt2
        
        res[0], res[p - 1] = res[p - 1], res[0]
        res[-1], res[p2] = res[p2], res[-1]

        res[:p - 1] = two_pivot_block_quicksort(res[:p - 1])
        res[p:p2] = two_pivot_block_quicksort(res[p:p2])
        res[p2 + 1:] = two_pivot_block_quicksort(res[p2 + 1:])
        return res