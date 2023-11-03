import numpy as np 

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])
 
print(type(a))
print(a.dtype)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.ndim)
print(a.nbytes)  