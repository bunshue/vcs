import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 2*np.pi, 50)       # 建立 35 個點
y1 = np.sin(x)
plt.scatter(x, y1, c='b', marker='x')   # 繪製 sine wave
y2 = np.cos(x)
plt.scatter(x, y2, c='g', marker='X')   # 繪製 cos wave

plt.show()
