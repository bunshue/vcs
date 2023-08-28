# ch6_35.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "lightyellow"
fig = plt.figure()
x = np.arange(1,11)                         
ax1 = fig.add_subplot(2,2,1)        # 建立子圖表 1
ax1.plot(x, x)
ax1.set_title("子圖 221")
ax1 = fig.add_subplot(2,2,3)        # 建立子圖表 3
ax1.plot(x, x, 'g')
ax1.set_title("子圖 223")
ax1 = fig.add_subplot(1,2,2)        # 建立子圖表 2
ax1.plot(x, x, 'm')
ax1.set_title("子圖 122")
plt.tight_layout()                  # 緊湊佈局
plt.show()


