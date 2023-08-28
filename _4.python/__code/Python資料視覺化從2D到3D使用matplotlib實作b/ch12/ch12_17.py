# ch12_17.py
import matplotlib.pyplot as plt
import numpy as np

N = 100
x = np.linspace(-3.0, 3.0, N)
y = np.linspace(-3.0, 3.0, N)
xx, yy = np.meshgrid(x, y)
# 當建立重疊影像時, 需要有相同的 extent
extent = np.min(x), np.max(x), np.min(y), np.max(y)

fig = plt.figure()
z1 = np.add.outer(range(8), range(8)) % 2           # 棋盤
plt.imshow(z1, cmap='gray',extent=extent)           # 影像 1

z2 = np.sin(xx) + np.cos(yy)                        # 影像 2 公式
plt.imshow(z2, cmap='jet', alpha=0.8,
           interpolation='bilinear',extent=extent)  # 影像 2
plt.show()


      
