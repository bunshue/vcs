# ch20_5.py
import numpy as np
import matplotlib.pyplot as plt

x = np.array([8, 9, 10, 7, 8, 9, 5, 7, 9, 8])
y = np.array([12, 15, 16, 18, 6, 11, 3, 12, 11, 16])             
x_mean = np.mean(x)
y_mean = np.mean(y)
xpt1 = np.linspace(0, 12, 12)      
ypt1 = [y_mean for xp in xpt1]          # 平均購買次數
ypt2 = np.linspace(0, 20, 20)
xpt2 = [x_mean for yp in ypt2]          # 平均滿意度

plt.scatter(x, y)                       # 滿意度 vs 購買次數
plt.plot(xpt1, ypt1, 'g')               # 平均購買次數
plt.plot(xpt2, ypt2, 'g')               # 平均滿意度
plt.grid()
plt.show()









