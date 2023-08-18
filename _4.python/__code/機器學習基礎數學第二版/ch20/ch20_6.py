# ch20_6.py
import numpy as np
import math

a = np.array([4, 2])
b = np.array([1, 3])

norm_a = np.linalg.norm(a)              # 計算向量大小
norm_b = np.linalg.norm(b)              # 計算向量大小
                    
dot_ab = np.dot(a, b)                   # 計算向量內積

cos_angle = dot_ab / (norm_a * norm_b)  # 計算cos值
rad = math.acos(cos_angle)              # acos轉成弧度

area = norm_a * norm_b * math.sin(rad) / 2
print('area = {0:5.2f}'.format(area))








