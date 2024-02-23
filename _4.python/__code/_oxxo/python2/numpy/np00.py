# encoding:UTF-8
# pip3 install numpy

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a[0], b[1])

a = np.append(a, b)
print(a)

d = a[1]
print(d)

a2 = np.delete(a, 1)
print(a2)
a3 = np.insert(a, 1, d)
print(a3)
