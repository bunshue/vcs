# ch13_15.py
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10000)
y = np.random.rand(10000)
plt.scatter(x, y, c=y, cmap='hsv')  # 色彩依 y 軸值變化
plt.colorbar()
plt.show()





