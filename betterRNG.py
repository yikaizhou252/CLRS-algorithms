import numpy as np
import random



def betterRNG(a, b):
    n = np.ceil(np.log2(b-a))
    while True:
        result = a

        for i in range(1, n):
            result += 2**(i-1) * random.randint(0,1)

        if result <= b: return result



betterRNG(1,10)