"""
matplotlib_箭袋圖

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

x_pos = 0
y_pos = 0
x_direct = 1
y_direct = 1
plt.quiver(x_pos, y_pos, x_direct, y_direct)
plt.title("Quiver()函數繪製單一箭頭")

plt.show()

print("------------------------------------------------------------")  # 60個

x_pos = 0
y_pos = 0
x_direct = 1
y_direct = 1
plt.quiver(x_pos, y_pos, x_direct, y_direct, color="b")
plt.title("Quiver()函數繪製單一藍色箭頭")
plt.xlim([-1, 10])
plt.ylim([-1, 10])

plt.show()

print("------------------------------------------------------------")  # 60個

x_pos = [0, 0]
y_pos = [0, 0]
x_direct = [1, 1]
y_direct = [1, -1]
plt.quiver(x_pos, y_pos, x_direct, y_direct, color=["b", "g"])
plt.title("Quiver()函數繪製藍色和綠色箭頭")
plt.axis([-2, 2, -2, 2])

plt.show()

print("------------------------------------------------------------")  # 60個

x_pos = [0, 0]
y_pos = [0, 0]
x_direct = [1, 1]
y_direct = [1, -1]
plt.quiver(
    x_pos,
    y_pos,
    x_direct,
    y_direct,
    color=["b", "g"],
    angles="xy",
    scale_units="xy",
    scale=1,
)
plt.title("繪製藍色和綠色箭頭,箭頭長度單位與座標軸相同")
plt.axis([-2, 2, -2, 2])

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(-10, 11)
y = np.arange(-10, 11)
X, Y = np.meshgrid(x, y)
U, V = X, Y
plt.quiver(X, Y, U, V)
plt.title("箭袋 Quiver", fontsize=14, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(-10, 11)
y = np.arange(-10, 11)
X, Y = np.meshgrid(x, y)
U, V = X, Y
plt.quiver(X, Y, U, V)
plt.title("箭袋 Quiver", fontsize=14, color="b")
plt.axis("equal")
plt.xticks([])
plt.yticks([])

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(-10, 11)
y = np.arange(-10, 11)
X, Y = np.meshgrid(x, y)
U, V = X, Y
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.set_title("箭袋 Quiver", fontsize=14, color="b")
ax.set_aspect("equal")
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(-3, 3.5, 0.5)
y = np.arange(-3, 3.5, 0.5)
X, Y = np.meshgrid(x, y)
U = np.sin(X) * Y
V = np.cos(X) * X
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.set_title("箭袋 Quiver", fontsize=14, color="b")
ax.set_aspect("equal")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(-2, 2.2, 0.2)
y = np.arange(-2, 2.2, 0.2)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
U, V = np.gradient(Z)
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.set_title("箭袋 Quiver", fontsize=14, color="b")
ax.set_aspect("equal")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(-2, 2.2, 0.2)
y = np.arange(-2, 2.2, 0.2)
X, Y = np.meshgrid(x, y)  # 建立 X, Y
Z = X**2 + Y**2
U, V = np.gradient(Z)  # 建立 U, V
C = U + V  # 定義箭頭顏色的數據
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V, C)  # 繪製預設的彩色箭袋
ax.set_title("箭袋 Quiver", fontsize=14, color="b")
ax.set_aspect("equal")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(-2, 2.2, 0.2)
y = np.arange(-2, 2.2, 0.2)
X, Y = np.meshgrid(x, y)  # 建立 X, Y
Z = X**2 + Y**2
U, V = np.gradient(Z)  # 建立 U, V
C = U + V  # 定義箭頭顏色的數據
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V, C, cmap="hsv")  # 繪製預設的彩色箭袋
ax.set_title("箭袋 Quiver, cmap='hsv'", fontsize=14, color="b")
ax.set_aspect("equal")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
