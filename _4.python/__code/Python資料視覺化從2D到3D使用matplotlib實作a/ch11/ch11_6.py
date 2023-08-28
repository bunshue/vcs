# ch11_6.py
import matplotlib.pyplot as plt
import numpy as np

N= 5000
x = np.random.rand(N)
y = np.random.rand(N)
fig, ax = plt.subplots(3,1)
# 建立子圖 0 和 1 的散點圖和色彩條
ax0 = ax[0].scatter(x, y, c=x, cmap='GnBu')
ax1 = ax[1].scatter(x, y, c=x, cmap='GnBu')
fig.colorbar(ax0, ax=(ax[0],ax[1]))     # 共用色彩條
# 建立子圖 2 的散點圖和色彩條
ax2 = ax[2].scatter(x, y, c=y, cmap='hsv')
fig.colorbar(ax2, ax=ax[2])
plt.show()








