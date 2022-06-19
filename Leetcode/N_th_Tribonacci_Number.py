from numba import jit
import numpy as np

x = [1,1,2,3]

@jit # Set "nopython" mode for best performance, equivalent to @njit
def go_fast(a): # Function is compiled to machine code when called the first time
    trace = 0.0
    for i in range(1000):   # Numba likes loops
        trace += 15 # Numba likes NumPy functions
    return a              # Numba likes NumPy broadcasting

print(go_fast(x))
