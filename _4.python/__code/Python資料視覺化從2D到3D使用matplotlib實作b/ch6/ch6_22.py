# ch6_22.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "lightyellow"
fsize = 24                  # 字型大小                           
ax = plt.subplot()          # 建立圖表
ax.plot([1, 3])             # 繪製圖表
ax.set_xlabel('x 座標', fontsize=fsize)
ax.set_ylabel('y 座標', fontsize=fsize)
ax.set_title('資料布局', fontsize=fsize)
plt.show()


