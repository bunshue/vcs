# ch21_8.py
import numpy as np

A = np.matrix([[2, 3], [5, 7]])
B = np.linalg.inv(A)
print('A_inv = {}'.format(B))
print('E     = {}'.format((A * B).astype(np.int64)))





 








