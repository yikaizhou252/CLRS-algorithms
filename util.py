
import math
from numpy import random
import time
import big

def genlist(low, high, size):
    return list(random.randint(low, high, size=(size)))

def test_sort(sort_fn, name, lst=genlist(0, 100, 10000)):

    err = False
    print(f'\nSorting: {lst}')
    start_time = time.time()
    lst = sort_fn(lst)
    my_duration = time.time() - start_time
    print(f'Result: {lst}\n')

    for i in range(0, len(lst)-1):
        if lst[i] <= lst[i+1]: continue
        else: 
            err = True
            break
    
    start_time = time.time()
    lst.sort()
    dur = time.time() - start_time
    print(f'Encountered sorting errors at {lst[i]}, {lst[i+1]}') if err else print(f'It took {my_duration} sec. to sort {len(lst)} random inputs with {name}')
    print(f'Python took {dur} sec.\n')

def binsearch(nums, targ, index=0):
        
        midex = int(len(nums)/2)
        mid = nums[midex]
        
        # up = nums[:mid:]
        # down = nums[mid+1::]
        
        if targ == mid : return midex + index

        elif len(nums) == 1 : 
                if targ < nums[0]: return midex + index
                else: return midex + index + 1 
        
        elif targ < mid : return binsearch(nums[:midex:], targ, index)
            
        elif targ > mid : return binsearch(nums[midex::], targ, index+midex)    

local_nums = genlist(-100, 100, 150)

def find_max_sub(func, nums=big.nums):
    nums = local_nums
    # print(nums)
    start_time = time.time()
    res = func(nums)
    duration = time.time() - start_time
    print(f'It took {duration} sec. to find the max sub of {res} using {func.__name__}')

def test_fib(func, i):
    start_time = time.time()
    res = func(i)
    duration = time.time() - start_time
    print(f'It took {duration} sec. to find {res} using {func.__name__}')

