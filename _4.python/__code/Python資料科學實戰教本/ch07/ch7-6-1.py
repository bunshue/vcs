import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print("a=")
print(a)

b = a.ravel()
print("a.ravel()=" + str(b))
c = a.flatten()
print("a.flatten()=" + str(c))
d = np.ravel(a)
print("np.ravel(a)=" + str(d))

