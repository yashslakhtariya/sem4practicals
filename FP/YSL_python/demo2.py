import numpy as np
import time

# create a NumPy array and a Python list with 10 million elements
arr = np.arange(10000000)
lst = list(range(10000000))

# measure the time it takes to square each element of the array and list
start = time.time()
arr_squared = arr ** 2
print("Time taken to square NumPy array:", time.time() - start)

start = time.time()
lst_squared = [i ** 2 for i in lst]
print("Time taken to square Python list:", time.time() - start)
