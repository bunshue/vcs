import numpy as np 

a = np.arange(16)
print(a)
print("---------------------------")
b = a.reshape((4, 4))
print(b)
print("===========================")
c = np.array(range(10), float)
print(c)
print("---------------------------")
d = c.reshape((5, 2))
print(d)


