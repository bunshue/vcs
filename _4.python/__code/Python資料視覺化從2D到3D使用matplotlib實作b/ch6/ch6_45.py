# ch6_45.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.facecolor"] = "lightyellow"

fig = plt.figure()
# 子圖 0 列和 1 列的高度比是 2:1
# 子圖 0 列和 1 列的寬度比是 2:1
gs = fig.add_gridspec(nrows=2, ncols=2, height_ratios=[2,1],
                      width_ratios=[2,1])
# 建立子圖物件
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1])
ax3 = fig.add_subplot(gs[1,:])
# x 軸資料
x = np.linspace(0, 2*np.pi, 500)
# 繪製子圖
ax1.plot(x, np.sin(x))
ax2.plot(x, np.sin(x)**2,'g')
ax3.plot(x, np.sin(x) + np.cos(x),'m')
# 建立軸標籤
ax1.set_ylabel("y")
ax3.set_xlabel("x")
ax3.set_ylabel("y")

plt.tight_layout()                  # 緊湊佈局
plt.show()


