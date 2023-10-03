import matplotlib.pyplot as plt
import numpy as np

colorused = ['b','c','g','k','m','r','y']   # 定義顏色
x = np.linspace(0.0, 2*np.pi, 50)           # 建立 50 個點
y1 = np.sin(x)
colors = []
for i in range(50):                         # 隨機設定顏色
    colors.append(np.random.choice(colorused))
plt.scatter(x, y1, c=colors, marker='*')    # 繪製 sine 
y2 = np.cos(x)
plt.scatter(x, y2, c=colors, marker='s')    # 繪製 cos 

plt.show()



