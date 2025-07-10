"""
LineCollection_曲線集合

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

# 集合
# 曲線集合(LineCollection)

# 使用LineCollection顯示大量曲線
from matplotlib import collections as mc

lines = [
    [[100, 0], [195, 70], [158, 180], [42, 180], [5, 70], [100, 0]],
    [[300, 0], [395, 70], [358, 180], [242, 180], [205, 70], [300, 0]],
    [[200, 200], [295, 270], [258, 380], [142, 380], [105, 270], [200, 200]],
]

# print(lines)

# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(4, 4))  # 1X2 子圖
fig, ax = plt.subplots(1, 1, figsize=(4, 4))  # 1X1 子圖
line_collection = mc.LineCollection(lines, colors="r", linewidths=1)
ax.add_collection(line_collection)  # add_collection 只能用 ax

ax.set_aspect("equal")
ax.autoscale()
# ax.axis("off")
plt.show()

print("曲線數 :", len(line_collection.get_paths()))
print("曲線顏色數 :", len(line_collection.get_edgecolors()))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
