# ch20_16.py
import matplotlib.pyplot as plt
import numpy as np

points = 30
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(points):                     # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.random.randint(1,11,points)          # 建立 x
y = np.random.randint(1,11,points)          # 建立 y
size = (points * np.random.rand(points))**2 # 散點大小數列
plt.scatter(x, y, s=size, c=colors)         # 繪製散點
plt.xticks(np.arange(0,12,step=1.0))        # x 軸刻度
plt.yticks(np.arange(0,12,step=1.0))        # y 軸刻度
plt.show()



