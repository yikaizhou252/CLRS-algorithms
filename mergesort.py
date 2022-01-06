
import math
from util import test_sort
import big
name = "merge sort"


def merge(lst: list, p: int, q: int, r: int):

    arr = lst[p:q] # p, p+1, ..., q-1
    brr = lst[q:r] # q, q+1, ..., r-1

    arr.append(math.inf), brr.append(math.inf)

    i = 0
    j = 0

    for k in range(p, r):

        if arr[i] <= brr[j]: 
            lst[k] = arr[i]
            i += 1
        else:
            lst[k] = brr[j]
            j += 1

    # print(lst)

def sort(lst: list, p, r):

    if p + 1 < r:
        q = int((p+r)/2)
        sort(lst, p, q)
        sort(lst, q, r)
        merge(lst, p, q, r)
        # print("merge is called")
    
    # base case: returns both arrays of size 1 that are trivially sorted and ready to be merged
    # important: think of slices as line dividers, not as indices
    # divide and conquer uses dividers 
    return lst 

def merge_sort(lst):
    return sort(lst, p=0, r=len(lst))

lst = [5,2,4,7,1,3,2,6,4.2]
test_sort(merge_sort, name)
