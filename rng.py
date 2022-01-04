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

        for i in range(1, n):
            result += 2**(i-1) * random.randint(0,1)

        if result <= b: return result

def _m_random(b):
    n = int(np.log2(b)) + 1
    while True:
        r = 0
        for i in range(n):
            r = 2*r + random.randint(0, 1)
        if r <= b:
            return r

def m_random(a, b):
    return _m_random(b - a) + a


def test_suite(func, trials, low_bound=1, up_bound=10):

    arr = []
    for i in range(up_bound):
        arr.append(0)

    j = 0
    # try:
    while j < trials:
        cur = func(low_bound, up_bound)
        if cur is not None: arr[cur - 1] = arr[cur - 1] + 1
        j += 1

    # except Exception as e:
    #     print(f'{e} problemo with: ', cur)


    # print(arr)
    for i in range(len(arr)):
        print(f'number of {i + 1}: {arr[i]}')

    # print(f'None count: {none_count}')


test_suite(m_random, 100000, 1, 16)
test_suite(rec_rando, 100000, 1, 16)