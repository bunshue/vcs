"""
matplotlib_間斷長條圖

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

fig, ax = plt.subplots()
ax.broken_barh([(50, 30), (100, 20)], (10, 5))
ax.set_xlabel("x-value")
ax.set_ylabel("y-value")
ax.grid(True)
ax.set_title("Broken_barh()", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

# 事先定義間斷長條圖數據 1
x_1 = [(2, 4), (9, 6)]
y_1 = (2, 3)
# 繪製間斷長條圖 1
plt.broken_barh(x_1, y_1, facecolors="m")
# 事先定義間斷長條圖數據 2
x_2 = [(5, 1), (8, 3), (12, 6)]
y_2 = (6, 3)
# 繪製間斷長條圖 2
plt.broken_barh(x_2, y_2, facecolors="g")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.title("Broken_barh()", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

# 定義間斷長條圖數據 1
x_1 = [(0, 7), (20, 4)]  # 定義時間
y_1 = (90, 30)  # 定義車速
plt.broken_barh(x_1, y_1, facecolors="g")
# 定義間斷長條圖數據 2
x_2 = [(7, 3), (17, 3)]  # 定義時間
y_2 = (40, 20)  # 定義車速
plt.broken_barh(x_2, y_2, facecolors="r")
# 定義間斷長條圖數據 3
x_3 = [(10, 7)]  # 定義時間
y_3 = (60, 30)  # 定義車速
plt.broken_barh(x_3, y_3, facecolors="b")
plt.xlabel("時間", fontsize=14, color="b")
plt.xticks(np.arange(0, 25, step=4))
plt.ylabel("車速", fontsize=14, color="b")
plt.title("每天不同時段行車速度表", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots()
ax.broken_barh([(60, 40), (130, 20)], (7, 10), facecolors="cyan")
ax.broken_barh([(10, 40), (90, 20), (120, 20)], (20, 10), facecolors=("m", "g", "b"))
ax.annotate(
    "學習中斷",
    (50, 25),
    xytext=(0.6, 0.92),
    textcoords="axes fraction",
    arrowprops=dict(fc="r", ec="r", shrink=0.05),
    fontsize=14,
    color="r",
    horizontalalignment="right",
    verticalalignment="top",
)
ax.set_ylim(5, 35)
ax.set_xlim(0, 160)
ax.set_xlabel("時間 : 單位秒", color="b")
ax.set_yticks([12, 25])
ax.set_yticklabels(labels=["雨星", "冰雨"], color="b")
ax.grid(True)
ax.set_title("學習觀察表", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
