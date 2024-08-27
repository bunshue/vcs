"""

雙y軸


"""
import matplotlib

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

print("兩Y軸不同刻度, plot + plot")

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()

ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("弧度", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax.legend(loc="best")

ax2 = ax.twinx()

ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Sinh(x)", color="blue")
ax2.legend(loc="best")

ax.set_title("兩Y軸不同刻度 plot + plot", size=20)

plt.show()

print("------------------------------------------------------------")  # 60個

# 新竹市平均高溫 °C
temperature_high = [
    19.1,
    19.4,
    21.6,
    25.6,
    28.9,
    31.5,
    33.2,
    32.8,
    31.2,
    28,
    25.1,
    21.1,
    26.5,
]

# 新竹市日均氣溫 °C
temperature_average = [
    15.7,
    16,
    18,
    21.9,
    25.2,
    27.9,
    29.3,
    28.9,
    27.3,
    24.4,
    21.5,
    17.7,
    22.8,
]

# 新竹市平均低溫 °C
temperature_low = [
    13.1,
    13.4,
    15.2,
    18.9,
    22.2,
    24.9,
    26,
    25.8,
    24.4,
    21.8,
    18.8,
    15.1,
    20,
]

# 新竹市平均降雨量 mm
rainfall_average = [
    75.7,
    123,
    159.8,
    161.9,
    249,
    252,
    120.2,
    197.1,
    174.5,
    53.6,
    51.1,
    57.7,
    1675.6,
]

print(len(temperature_high))
print(len(temperature_average))
print(len(temperature_low))
print(len(rainfall_average))

x = np.arange(0, 12, 1)
print(len(x))
print(x)

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()  # mirror the ax1
ax1.plot(x, temperature_high[:12], "r-")
ax1.plot(x, temperature_average[:12], "g-")
ax1.plot(x, temperature_low[:12], "b-")

ax2.plot(x, rainfall_average[:12], "yellow")

ax1.set_xlabel("月份")
ax1.set_ylabel("氣溫")
ax2.set_ylabel("雨量")

plt.show()

print("------------------------------------------------------------")  # 60個

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

fig, ax1 = plt.subplots(1, 1)

ax2 = ax1.twinx()  # 使用相同的 x 軸

ax1.plot(x, y0)
ax2.plot(x, y1, "g", lw="3")

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
