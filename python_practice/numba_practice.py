import numpy as np
from numba import jit, prange


def example_function(n):  
    trace = 0.0 
    for i in range(n.shape[0]):   
        trace += np.tanh(n[i, i])  
    return n + trace 
   
   
n = np.arange(10000).reshape(100, 100) 
%timeit example_function(n)


@jit(nopython=True)
def example_function(n):  
    trace = 0.0 
    for i in range(n.shape[0]):   
        trace += np.tanh(n[i, i])  
    return n + trace 
   
   
n = np.arange(10000).reshape(100, 100) 
%timeit example_function(n)



import random
# Serial version
@jit(nopython=True)
def monte_carlo_pi_serial(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

# Parallel version
@jit(nopython=True, parallel=True)
def monte_carlo_pi_parallel(nsamples):
    acc = 0
    # Only change is here
    for i in prange(nsamples):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples
    
   
%time monte_carlo_pi_serial(int(4e8))
%time monte_carlo_pi_parallel(int(4e8))





print("******************************")

import random
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

%time print(monte_carlo_pi(10_000_000))



import numba
import random
@numba.jit(nopython=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples



import numba
import random

@numba.jit(nopython=True, parallel=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in numba.prange(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

print(monte_carlo_pi(10_000_000))


from numba import jit, int32

@jit(int32(int32))
def plusone(x):
    return x+1


%time print(monte_carlo_pi(10_000_000))



