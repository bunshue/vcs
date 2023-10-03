import matplotlib.pyplot as plt
import numpy as np

N= 5000
x = np.random.rand(N)
y = np.random.rand(N)

fig, ax = plt.subplots(2,1)
# 建立子圖 0 的散點圖和色彩條
ax0 = ax[0].scatter(x, y, c=y, cmap='brg')
fig.colorbar(ax0, ax=ax[0])
# 建立子圖 1 的散點圖和色彩條
ax1 = ax[1].scatter(x, y, c=y, cmap='hsv')
fig.colorbar(ax1, ax=ax[1])

plt.show()

