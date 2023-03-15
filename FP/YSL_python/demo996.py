# NumPy (Numerical Python)
import numpy as np

a = np.array(["YSL", 64])
print(type(a))
print(a)

b = np.array([1,2,3,4,5])
c = b[3:0] # null
c[:] = 64
print(b)
print(c)

#but

c = b[0:3]
c[:] = 64
print(b) # [64,64,64,4,5] because array slicing is MUTABLE, so it also changes original array
print(c)
