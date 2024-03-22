# plot 集合, 極坐標系 做圖

import matplotlib

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="plot 集合 1 函數曲線",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

r = 3
t = np.linspace(-2 * np.pi, 2 * np.pi, 200)
x = r * np.cos(t)
y = r * np.sin(t)


ax = plt.gca()
ax.set_aspect("equal")

plt.plot(x, y, lw=3)


# 第二張圖
plt.subplot(232)

r = np.sin(5 * t)
x = r * np.cos(t)
y = r * np.sin(t)

ax = plt.gca()
ax.set_aspect("equal")

plt.plot(x, y, lw=3)


# 第三張圖
plt.subplot(233)


pi = 3.14159
r = 3
t = np.linspace(-1 * pi, 1 * pi, 50)

x = r * np.cos(t)
y = r * np.sin(t)


r = 3 * (1 - np.sin(t))
x = r * np.cos(t)
y = r * np.sin(t)

plt.plot(x, y, lw=3)


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

