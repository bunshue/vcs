# ch7_11.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.linspace(0, 1, 1000)
theta = 2 * 2*np.pi * r
ax.plot(theta, r, color='g', lw=3)

i = 500
radius, thistheta = r[i], theta[i]
ax.plot([thistheta], [radius], 'o')         # 指定位置繪點
ax.annotate('極座標文字註解',
            xy=(thistheta, radius),         # theta, radius
            xytext=(0.8, 0.2),              # 百分比
            color='b',                      # 藍色
            textcoords='figure fraction',   # 座標格式是百分比
            arrowprops=dict(arrowstyle="->",
                            color='m'),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
plt.show()



