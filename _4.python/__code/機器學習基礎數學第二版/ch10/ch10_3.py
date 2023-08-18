# ch10_3.py
import matplotlib.pyplot as plt                                  
import numpy as np

x = np.array([1, 2, 3])                 # 拜訪次數, 單位是100
y = np.array([5, 10, 20])               # 銷售考卷數, 單位是100

a, b = np.polyfit(x, y, 1)              # 迴歸直線
print('斜率 a = {0:5.2f}'.format(a))
print('截距 a = {0:5.2f}'.format(b))

y2 = a*x + b
plt.scatter(x, y)                       # 繪製散佈圖
plt.plot(x, y2)                         # 繪製迴歸直線
plt.show()                      

