# ch20_2.py
import numpy as np
import math

a = np.array([1, 1])
b = np.array([5, 5])
c = np.array([1, 5])
d = np.array([5, 1])

ab = b - a                              # 向量ab
cd = d - c                              # 向量bc

norm_a = np.linalg.norm(ab)             # 計算向量大小
norm_b = np.linalg.norm(cd)             # 計算向量大小
                    
dot_ab = np.dot(ab, cd)                 # 計算向量內積

cos_angle = dot_ab / (norm_a * norm_b)  # 計算cos值
rad = math.acos(cos_angle)              # acos轉成弧度
deg = math.degrees(rad)                 # 轉成角度
print('角度是 = {}'.format(deg))








