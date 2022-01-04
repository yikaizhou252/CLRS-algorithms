
import math
from numpy import random
import time
import big

def genlist(low, high, size):
    return list(random.randint(low, high, size=(size)))

def pprint(sort_fn, name, lst=genlist(0, 100, 700)):
    print(f'\nSorting: {lst}')
    start_time = time.time()
    lst = sort_fn(lst)
    duration = time.time() - start_time
    print(f'Result: {lst}\n')
    print(f'It took {duration} sec. to sort {len(lst)} inputs with {name}\n')

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