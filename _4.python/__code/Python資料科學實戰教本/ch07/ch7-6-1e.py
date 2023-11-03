import numpy as np

a = np.array([[1,2,3,4,5,6,7,8]])
b = a.reshape(2, 4)
print(b.shape)
print("---------------------------")
c = np.expand_dims(b, axis=0)
d = np.expand_dims(b, axis=1)
print(c.shape, d.shape)
print("---------------------------")
e = np.squeeze(c)
f = np.squeeze(d)
print(e.shape, f.shape)