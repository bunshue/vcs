# ch12_12.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 10)
y = np.linspace(0, 2 * np.pi, 10)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx) + np.cos(yy)   # 建立影像

plt.imshow(z)
plt.show()





