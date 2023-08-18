# ch20_7.py
import numpy as np

a = np.array([4, 2])
b = np.array([1, 3])

ab_cross = np.cross(a, b)               # 計算向量外積
area = np.linalg.norm(ab_cross) / 2     # 向量長度除以2
                    
print('area = {0:5.2f}'.format(area))








