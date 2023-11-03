import numpy as np 

a = np.array([1,2,3])
print("a=" + str(a))

b = a[:, np.newaxis]
print("b=a[:,np.newaxis]->")
print(b)
print(b.shape)
b = a[np.newaxis, :]
print("b=a[np.newaxis,:]->")
print(b)
print(b.shape)