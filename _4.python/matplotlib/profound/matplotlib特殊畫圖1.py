"""
特殊畫圖1

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

"""
水平參考區間 垂直參考區間 垂直的灰色線條
"""

print("------------------------------------------------------------")  # 60個

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = 1 / (1 + np.exp(-x))

plt.axhline(y=0, color="blue", linestyle="--")
plt.axhline(y=0.5, color="red", linestyle=":")
plt.axhline(y=1.0, color="green", linestyle="--")
plt.plot(x, y, linewidth=2, c="gray")
plt.xlim(-2 * np.pi, 2 * np.pi)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = 1 / (1 + np.exp(-x))

plt.axhline(y=0, color="blue", linestyle="--")
plt.axhline(y=0.5, color="red", linestyle=":")
plt.axhline(y=1.0, color="green", linestyle="--")
plt.axvline(color="gray", linestyle="-.")  # 垂直的灰色線條
plt.plot(x, y, linewidth=2, c="gray")
plt.xlim(-2 * np.pi, 2 * np.pi)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = 1 / (1 + np.exp(-x))

plt.axhline(y=0, c="blue", ls="--")
plt.axhline(y=0.5, c="red", ls=":")
plt.axhline(y=1.0, c="green", ls="--")
plt.axvline(c="gray", ls="-.")  # 垂直的灰色線條
plt.axline((-2, 0), (2, 1), c="cyan", lw=3)  # 兩個點的連線
plt.axline((-1, 0), slope=0.5, c="y", lw=2)  # 點和斜率的線條
plt.plot(x, y, linewidth=2, c="gray")
plt.xlim(-2 * np.pi, 2 * np.pi)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0.05, 2 * np.pi, 500)
y = np.sin(x)
plt.plot(x, y, ls="-.", lw=2, c="c", label="Sin")  # 繪製sin線
plt.axhspan(ymin=0.0, ymax=0.5, fc="y", alpha=0.3)  # 水平參考區間

plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0.05, 2 * np.pi, 500)
y = np.sin(x)
plt.plot(x, y, ls="-.", lw=2, c="c", label="Sin")  # 繪製sin線

plt.axhspan(ymin=0.0, ymax=0.5, fc="y", alpha=0.3)  # 水平參考區間
plt.axvspan(xmin=0.5 * np.pi, xmax=1.5 * np.pi, fc="r", alpha=0.3)  # 垂直參考區間

plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
