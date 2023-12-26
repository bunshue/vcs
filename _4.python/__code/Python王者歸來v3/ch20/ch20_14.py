# ch20_14.py
import matplotlib.pyplot as plt
import numpy as np

N = 50                                      # 色彩數列的點數
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(N):                          # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2*np.pi, N)            # 建立 50 個點
y1 = np.sin(x)
plt.scatter(x, y1, c=colors, marker='*')    # 繪製 sine 
y2 = np.cos(x)
plt.scatter(x, y2, c=colors, marker='s')    # 繪製 cos 
plt.show()



