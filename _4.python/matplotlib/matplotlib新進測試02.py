# 新進測試02


print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

from pylab import figure, show

fig = figure()
ax = fig.add_subplot(111, polar=True)
r = np.arange(0, 1, 0.001)
theta = 2 * 2 * np.pi * r
(line,) = ax.plot(theta, r, color="#ee8d18", lw=3)

ind = 800
thisr, thistheta = r[ind], theta[ind]
ax.plot([thistheta], [thisr], "o")

ax.annotate(
    "a polar annotation",
    xy=(thistheta, thisr),  # theta,radius
    xytext=(0.05, 0.05),  # fraction,fraction
    textcoords="figure fraction",
    arrowprops=dict(facecolor="black", shrink=0.05),
    horizontalalignment="left",
    verticalalignment="bottom",
)

plt.text(0.2, 1.2, "螺旋圖", fontsize=20)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
