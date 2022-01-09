from util import test_sort, genlist
import big
import statistics

def swap(arr, i, j):
    if i < len(arr) and j < len(arr):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    else: raise IndexError(f'Swapping index out of range\n i: {i}, j: {j}, len(heap): {len(arr)}')


def partition(arr, p, r):

    # we set the last entry as the pivot and compare every entry with that pivot
    # if cur_entry <= pivot we increase counter i and swap with entry i


    i = p - 1
    pivot = arr[r]

    # -1 because we don't want to reach the pivot
    for j in range(p, r): 

        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, r)
    return i + 1

def find_median(arr, p, r):

    mid = int((p + r)/2)
    pivot = statistics.median([arr[p], arr[r], arr[mid]])
    pr = -1
    if pivot == arr[p]: pr = p
    elif pivot == arr[r]: pr = r
    else: pr = mid

    return (pr, pivot)

def better_partion(arr, p, r):

    res = find_median(arr, p, r)
    p_index, pivot = res[0], res[1]
    arr.pop(p_index)
    arr.insert(r, pivot)
    return partition(arr, p, r)

# def median_partition(arr, p, r):
#     i = p - 1
#     res = find_median(arr, p, r)
#     p_index, pivot = res[0], res[1]

#     # -1 because we don't want to reach the pivot
#     for j in range(p, r + 1): 

#         if j == p_index: continue
#         if arr[j] <= pivot:
#             i += 1
#             if i == p_index: i += 1
#             swap(arr, i, j)


#     if p == p_index: 
#         swap(arr, i, p_index)
#         return i
#     elif r == p_index: 
#         swap(arr, i + 1, p_index)
#         return i + 1
#     else: 
#         swap(arr, i + 1, p_index)
#         return i + 1



def quicksort(arr, p, r):

    # we partition the (sub)array arr into p,..,q,..,r such that:
    # arr[p~q-1] <= arr[q]
    # arr[q+1~r] >= arr[q]

    if p < r:
        q = better_partion(arr, p, r)
        quicksort(arr, p, q - 1) # exclude 
        quicksort(arr, q + 1, r) # press doubt

    

def wrapper(arr):
    quicksort(arr, 0, len(arr)-1)
    return arr

nums = [20,25,6,12,15,4,16,10]

# swap(nums, 0, 3)
# swap(nums, 6, 7)
# print(nums)
# q = better_partion(nums, 0, len(nums)-1)
# print(nums, q)

test_sort(wrapper, "quick sort", big.nums)


