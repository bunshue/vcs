# ch10_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(100)
y = x
t = x                   # 色彩隨 y 軸值變化
plt.scatter(x, y, c=t, cmap='rainbow')
plt.show()




