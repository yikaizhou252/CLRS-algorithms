import numpy as np
import math


# this method uses the golden ratio
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
    if i == 0: return 0
    elif i == 1: return 1
    else: return rec_fib(i - 1) + rec_fib(i - 2)



print(rec_fib(30))