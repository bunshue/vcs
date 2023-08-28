# ch12_14.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.linspace(0, 2 * np.pi, 100)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx) + np.sin(yy)   # 建立影像
plt.imshow(z,cmap='hsv')
plt.show()





