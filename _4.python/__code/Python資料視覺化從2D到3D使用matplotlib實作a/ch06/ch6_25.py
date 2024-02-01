# ch6_25.py
import numpy as np
import matplotlib.pyplot as plt

def my_plot(ax, size):
    ax.plot([1, 3])             # 繪製圖表
    ax.set_xlabel('x 座標', fontsize=size)
    ax.set_ylabel('y 座標', fontsize=size)
    ax.set_title('資料布局', fontsize=size)    

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "lightyellow"
fsize = 24                  # 字型大小                           
ax1 = plt.subplot(2,2,1)    # 建立圖表
my_plot(ax1,fsize)
ax2 = plt.subplot(2,2,2)    # 建立圖表
my_plot(ax2,fsize)
ax3 = plt.subplot(2,2,3)    # 建立圖表
my_plot(ax3,fsize)
ax4 = plt.subplot(2,2,4)    # 建立圖表
my_plot(ax4,fsize)
plt.tight_layout()          # 緊湊佈局
plt.show()


