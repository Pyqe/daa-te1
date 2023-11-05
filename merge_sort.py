def merge_arrays(arr, arr2):
    res = []
    p = 0
    p2 = 0
    while p < len(arr) and p2 < len(arr2):
        if arr[p] <= arr2[p2]:
            res.append(arr[p])
            p += 1
        else:
            res.append(arr2[p2])
            p2 += 1
    
    if p < len(arr):
        res.extend(arr[p:])
    if p2 < len(arr2):
        res.extend(arr2[p2:])
    
    return res

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        res = merge_sort(arr[:mid])
        res2 = merge_sort(arr[mid:])
        return merge_arrays(res, res2)