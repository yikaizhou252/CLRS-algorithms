import math
from util import find_max_sub
from big import nums


def max_cross(arr, low, high, mid):

    # sentinels
    left_sum, right_sum = -math.inf, -math.inf
    max_left, max_right = 0, 0

    # mid towards left-side


    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        
        if left_sum < sum:
            left_sum = sum
            max_left = i

    sum = 0 
    for j in range(mid + 1, high + 1):
        sum += arr[j]

        if right_sum < sum:
            right_sum = sum
            max_right = j


    return(max_left, max_right, left_sum + right_sum)



def find_maximum_subarray(arr, low, high):


    # base case:
    if high == low: return (low, high, arr[low])

    else:
        mid = int((low+high)/2)
        left_tuple = (left_low, left_high, left_sum) = find_maximum_subarray(arr, low, mid)
        right_tuple = (right_low, right_high, right_sum) = find_maximum_subarray(arr, mid + 1, high)
        cross_tuple = (cross_low, cross_high, cross_sum) = max_cross(arr, low, high, mid)
        
    # recursive case:
    if left_tuple[2] >=  right_tuple[2] and left_tuple[2] >= cross_tuple[2]:
        # print(left_tuple)
        return left_tuple

    elif right_tuple[2] >= left_tuple[2] and right_tuple[2] >= cross_tuple[2]:
        return right_tuple

    else: return cross_tuple



def brute_force(arr):

    # flatten the array 
    brr = [0]
    for i in range(len(arr)):
        brr.append(brr[i] + arr[i])
    
    # print(brr)
    max = float('-inf')

    for i in range(0, len(brr)):
        for j in range(i+1, len(brr)):
            if brr[j]-brr[i] >= max: max = brr[j]-brr[i]
    # print(max)
    return(max)

def divide_and_conquer(nums):
    return (find_maximum_subarray(nums, 0, len(nums)-1))[2]
        


find_max_sub(divide_and_conquer)
find_max_sub(brute_force)
#
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# ans = find_maximum_subarray(nums, 0, len(nums)-1)
# print(ans[2])
