import numpy as np 

a = np.array([[1,2,3],[4,5,6]])
print(a[0, 0], a[0, 1], a[0, 2])
print(a[1, 0], a[1, 1], a[1, 2])
print("---------------------------")
a[0, 0] = 6
a[1, 2] = 1
print(a)
