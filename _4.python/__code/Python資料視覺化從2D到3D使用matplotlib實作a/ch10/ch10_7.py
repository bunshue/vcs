import matplotlib.pyplot as plt
import numpy as np

num = 100

x = np.random.random(100)           # 可以產生num個0.0至1.0之間的數字
y = np.random.random(100)
t = x                               # 色彩隨x軸變化
plt.scatter(x, y, s=100, c=t, cmap='brg')

plt.show()
   
