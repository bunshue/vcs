import numpy as np

x = np.array([1, 2, 3])         # 1 x 3 陣列 x
y = np.array([2, 3, 4])         # 1 x 3 陣列 y
print(f'x = {x}')
print(f'y = {y}')
print('='*50)
y = y.reshape(-1,1)             # y 改為 3 x 1 陣列 
print(f'新的 y = \n{y}')
print('='*50)
print(f'x + y = \n{x+y}')

