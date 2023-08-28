# ch31_1.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

np.random.seed(10)              # 隨機數種子值

colors = ['m', 'r', 'g', 'b']   # 不同平面的顏色
yticks = [3, 2, 1, 0]           # y 座標平面
ax.set_yticks(yticks)           # 設定 y 軸刻度標記
# 依次在 y = 3, 2, 1, 0 平面繪製長條圖
for c, k in zip(colors, yticks):
    left = np.arange(12)        # 建立 x 軸座標 
    height = np.random.rand(12) # 建立長條高度
    ax.bar(left, height, zs=k, zdir='y', color=c, alpha=0.8) 
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
plt.show()
















