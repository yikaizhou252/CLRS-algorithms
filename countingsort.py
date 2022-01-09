from util import test_sort



def counting_sort(arr, k):

    # init: we need an array of k + 1 size as counter
    b, c = [], []

    for i in range(0, k + 1):
        c.append(0)

    for i in range(0, len(arr)):
        b.append(0)

    
    # first traversal
    # count the occurence of each number in arr
    
    
    for i in range(0, len(arr)):
        c[arr[i]] += 1 
    

    # second traversal
    # find the cumulation of the occurence of each number in arr that is smaller or equal to arr[i]
    for i in range(1, len(c)):
        c[i] += c[i - 1]



    # final traversal
    # place a number exactly where it belongs giving metadata c

    for i in range(len(arr) - 1, -1, -1):
        b[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1
    return b


# nums = [6,0,2,0,1,3,4,6,1,3,2]
# res = counting_sort(nums, 6)

def wrapper(arr):
    return counting_sort(arr, 100)

test_sort(wrapper, "counting sort")


