from util import test_sort, binsearch
import big
name = "insertion sort"
def insertion_sort(lst: list):
    
    for j in range (1, len(lst)):

        key = lst[j] 
        i = j - 1

        while i > -1 and lst[i] > key:
            lst[i+1] = lst[i]
            i = i -1

        lst[i+1] = key

    return lst


def r_insertion_sort(lst: list):
    n = len(lst)
    i = 0
    targ = lst[n - 1]
    
    if n > 1: 
        sublist = r_insertion_sort(lst[:n - 1])
        i = binsearch(sublist, targ)
        sublist.insert(i, targ)
        return sublist

    # n = 1 is base case where arr is trivially sorted
    return lst

def r_wrapper(lst):
    return r_insertion_sort(lst)
    

lst = [5,2,4,7,1,3,2,6,4.2]
test_sort(insertion_sort, "recursive insertion search")