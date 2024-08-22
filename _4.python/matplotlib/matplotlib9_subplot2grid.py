"""
Matplotlib 多圖顯示(subplot()/subplot2grid()/subplots())

plt.subplot2grid()

"""
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

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(12, 8))

"""
plt.subplot2grid((3,3),(0,0), colspan = 3)

    使用plt.subplot2grid()做圖
    (3,3): 表示把窗口分成3行3列
    (0,0): 表示從未置(0,0)開始做圖
    colspan: column範圍
    rowspan: row範圍
"""
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
ax3 = plt.subplot2grid((3, 3), (1, 2), colspan=1, rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=1, rowspan=1)

ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel("ax4_x")
ax4.set_ylabel("ax4_y")

ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1, rowspan=1)
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.gridspec as gridspec

plt.figure(figsize=(12, 8))

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # stands for axes
ax1.plot([1, 2], [1, 2])
ax1.set_title("ax1_title")
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel("ax4_x")
ax4.set_ylabel("ax4_y")
ax5 = plt.subplot2grid((3, 3), (2, 1))

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize=(12, 8))

ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax2 = plt.subplot2grid((3, 3), (0, 2), rowspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (1, 1))  # rowspan/colspan默認爲1
ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=2)
ax5.plot([1, 2, 3, 4, 1])

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

