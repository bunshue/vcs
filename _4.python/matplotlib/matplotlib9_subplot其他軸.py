"""
其他

軸相關

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

# 共同參數
N = 50  # 樣本數
x = np.linspace(0, 2 * np.pi, N)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個

fig = plt.figure()  # 建立畫布物件
ax = fig.add_subplot()  # 建立子圖(或稱軸物件)ax

ax.plot(x, y)
ax.set_title("標題", fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.image as img

plt.gcf().set_size_inches(12, 8)  # 設定圖框大小

# 第1張子圖
ax1 = plt.subplot(2, 2, 1)
ax1.plot(x, y)
ax1.set_title("apple", fontsize=12)

# 第2張子圖
ax2 = plt.subplot(2, 2, 2)
ax2.plot(x, y)
ax2.set_title("banana", fontsize=12)

# 第3張子圖
ax3 = plt.subplot(2, 2, 3)
ax3.plot(x, y)
ax3.set_title("cat", fontsize=12)

# 第4張子圖
ax4 = plt.subplot(2, 2, 4)
ax4.plot(x, y)
ax4.set_title("dog", fontsize=12)

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize=(12, 8))
fig.suptitle("Title 1")  # 主標題

ax1 = plt.subplot(221)  # 整體爲兩行兩列，創建其中的第一個子圖
ax1.set_title("Title 2", fontsize=12, color="y")  # 子標題
ax1.plot([1, 2, 3, 4, 5])

ax2 = plt.subplot(222)
ax2.plot([5, 4, 3, 2, 1])

ax3 = plt.subplot(223)
ax3.plot([1, 2, 3, 3, 3])

ax4 = plt.subplot(224)
ax4.plot([5, 4, 3, 3, 3])

plt.show()

print("------------------------------------------------------------")  # 60個


fig = plt.figure()

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust()

x = np.linspace(0, 2 * np.pi, num=100, endpoint=True)
y = np.sin(x)

ax1.plot(x,y)
ax1.set_title("左圖", color="b")

ax2.plot(x,y)
ax2.set_title("右圖", color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

# 在畫布切出子圖區 , 並繪製內容–add_subplot()

fig = plt.figure(figsize=(12, 8))  # 整個圖表大小為 12 x 8 英吋
fig.subplots_adjust(wspace=0.5, hspace=0.75)  # 調整子圖間距

ax1 = fig.add_subplot(2, 3, 1)  # ←編號 1 的子圖
ax1.plot(x, y)

ax3 = fig.add_subplot(2, 3, 3)  # ← 編號 3 的子圖
# 沒畫

ax5 = fig.add_subplot(2, 3, 5)  # ←編號 5 的子圖
ax5.plot(x, y)

ax6 = fig.add_subplot(2, 3, 6)  # ←編號 6 的子圖
ax6.plot(x, y)

# 設定子圖的座標範圍、座標說明文字與子圖標題
ax6.set_xlim(0, 3.14 / 2)
ax6.set_ylim(-0.1, 1.1)
ax6.set_xlabel("x-axis")
ax6.set_ylabel("y-axis")
ax6.set_title("y = sin(x)")
ax6.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# X,Y軸不顯示刻度
ax1.set_xticks([])
ax1.set_yticks([])


ax = fig.add_subplot()  # 建立子圖(或稱軸物件)ax
