import random
import numpy as np
from numpy.random.mtrand import rand


def rng():
    return random.randint(0,1)



# this only works if it is a power of 2
def rec_rando(a, b):


    # recursive case:
    if b - a > 1:

        mid = int((b - a)/2) + a
        _a = rec_rando(a, mid)
        _b = rec_rando(mid + 1, b)

        # if _a is None: return _b
        # elif _b is None: return _a
        return _a if rng() == 1 else _b

    # base case: both are handled equally
    # 1) a + 1 == b
    
    elif b - a == 1:
        return a if rng() == 1 else b

    # 2) a == b
    else: 
        return a if rng() == 1 else None

def betterRNG(a, b):
    n = int(np.ceil(np.log2(b-a)))
    while True:
        result = a

        for i in range(0, n):
            result += 2**i * random.randint(0,1)

        if result <= b: return result


def test_suite(func, trials, low_bound=1, up_bound=10):

    arr = []
    for i in range(up_bound):
        arr.append(0)

    j = 0

    while j < trials:
        cur = func(low_bound, up_bound)
        if cur is not None: arr[cur - 1] = arr[cur - 1] + 1
        j += 1

    for i in range(len(arr)):
        print(f'number of {i + 1}: {arr[i]}')



test_suite(betterRNG, 100000, 1, 13)
# test_suite(rec_rando, 100000, 1, 16)