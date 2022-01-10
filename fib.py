import numpy as np
import math
from util import test_fib


# this method uses the golden ratio
# this method is NOT quick
def quick_fib(i):
    eq = np.roots([1, -1, -1])
    golden, conj = eq[0], eq[1]

    
    return int((golden**i + conj**i)/math.sqrt(5))


# this method is iterative
def ite_fib(i):
    a = 0
    b = 1

    for k in range(int(i/2)):
        a += b
        b += a

    if i % 2 == 0: return a
    else: return b 
        

# this method is recursive
def rec_fib(i):
    if i == 1: return 1
    elif i == 2: return 1
    else: return rec_fib(i - 1) + rec_fib(i - 2)



memory = []

def dp_fib(i):

    f = 0
    if i == 1 or i == 2: f = 1
    else: 
        if i < len(memory) - 1:
            f = memory[i - 1]
        else:
            f = dp_fib(i - 1) + dp_fib(i - 2)

    while len(memory) - 1 < i - 1:
        memory.append(0)
    
    memory[i - 1] = f
    # print(memory)
    return f

test_fib(ite_fib, 100)
test_fib(dp_fib, 100)

# test_fib(rec_fib, 40)
# test_fib(rec_fib, 900)
# print(rec_fib(900))