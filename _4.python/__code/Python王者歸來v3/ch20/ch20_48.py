# ch20_48.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
ax = plt.subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
ax.plot(theta, r, 'm', lw=3)
plt.title("極座標圖表",fontsize=16)
plt.tight_layout()      # 圖表標題可以緊縮佈局
plt.show()



