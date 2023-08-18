# ch21_9.py
import numpy as np

A = np.matrix([[3, 2], [1, 2]])
A_inv = np.linalg.inv(A)
B = np.matrix([[5], [-1]])
print('{}'.format(A_inv * B))






 








