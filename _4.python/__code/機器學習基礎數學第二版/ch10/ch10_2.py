# ch10_2.py                               
import numpy as np

x = np.array([1, 2, 3])                 # 拜訪次數, 單位是100
y = np.array([5, 10, 20])               # 銷售考卷數, 單位是100

a, b = np.polyfit(x, y, 1)
print('斜率 a = {0:5.2f}'.format(a))
print('截距 a = {0:5.2f}'.format(b))




