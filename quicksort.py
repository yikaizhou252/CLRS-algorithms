from util import test_sort
import big

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


def quicksort(arr, p, r):

    # we partition the (sub)array arr into p,..,q,..,r such that:
    # arr[p~q-1] <= arr[q]
    # arr[q+1~r] >= arr[q]

    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1) # exclude 
        quicksort(arr, q + 1, r) # press doubt

    

def wrapper(arr):
    quicksort(arr, 0, len(arr)-1)
    return arr

nums = [10,20,25,6,12,15,4,16]

# swap(nums, 0, 3)
# swap(nums, 6, 7)
# print(nums)
q = partition(nums, 0, len(nums)-1)
print(nums, q)

test_sort(wrapper, "quick sort")

