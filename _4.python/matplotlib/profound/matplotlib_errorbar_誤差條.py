"""
matplotlib_誤差條

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

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
plt.errorbar(x, y, yerr=dy)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
plt.errorbar(x, y, yerr=dy, ecolor="r", capsize=3)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
dx = 0.2
plt.errorbar(x, y, xerr=dx, yerr=dy, ecolor="r", capsize=3)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
plt.errorbar(x, y, fmt="o", yerr=dy, ecolor="r", color="b", capsize=3)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
plt.errorbar(x, y, fmt="o-", yerr=dy, ecolor="r", color="b", capsize=3)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
plt.errorbar(x, y, fmt="o-", yerr=dy, ecolor="r", color="b", uplims=True, capsize=3)
plt.title("uplims = True", color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
plt.errorbar(x, y, yerr=dy, ecolor="r", uplims=True, lolims=True)
plt.title("uplims, lolims = True", color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
up = [True, False] * 10  # 上限串列
lo = [False, True] * 10  # 下限串列
plt.errorbar(x, y, yerr=dy, uplims=up, lolims=lo, ecolor="r")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.2 + 0.01 * x
dy_range = [dy * 0.5, dy]  # (下方誤差, 上方誤差)
plt.errorbar(x, y, fmt="o-", yerr=dy_range, ecolor="r", color="b", capsize=3)

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
x = np.arange(10)
y = 3 * np.cos(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)

plt.errorbar(x, y + 3, yerr=yerr, label="誤差條使用預設")
plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label="uplims=True")
plt.errorbar(
    x, y + 1, yerr=yerr, uplims=True, lolims=True, label="uplims, lolims = True"
)
upperlimits = [True, False] * 5
lowerlimits = [False, True] * 5
plt.errorbar(
    x,
    y,
    yerr=yerr,
    uplims=upperlimits,
    lolims=lowerlimits,
    label="同時有uplims和lolims = True",
)
plt.legend(loc="lower left")
plt.xticks(np.arange(0, 10))
plt.title("誤差條的綜和應用", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
