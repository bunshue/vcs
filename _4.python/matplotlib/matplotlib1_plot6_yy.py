"""

雙y軸


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

print("使用 plt.subplots() 做一圖")

x = np.linspace(0, 10, 50)
y = np.sin(x)

# fig, ax = plt.subplots() same
fig, ax = plt.subplots(1, 1)

ax.plot(x, y, "r-o", label="Sin(x)")
ax.set_xlabel("弧度", color="green")
ax.set_ylabel("Sin(x)", color="red")

ax.set_title("sin(x)", size=20)

plt.show()

print("------------------------------------------------------------")  # 60個

# 共同參數
x = np.linspace(0, 2 * np.pi, 30)
y = np.sin(x)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)

print("------------------------------------------------------------")  # 60個

print("兩Y軸不同刻度, plot + plot")

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()
ax2 = ax.twinx()  # 使用相同的 x 軸

# 第1軸
ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("弧度", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax.legend(loc="best")

# 第2軸
ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Sinh(x)", color="blue")
ax2.legend(loc="best")

ax.set_title("兩Y軸不同刻度 plot + plot", size=20)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()
ax2 = ax.twinx()  # 使用相同的 x 軸

lns1 = ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")

lns2 = ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Sinh(x)", color="blue")
# 自行建立圖例來顯示所有標籤
lns = lns1 + lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()
ax2 = ax.twinx()  # 使用相同的 x 軸

ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")

ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")

# 指定圖表標題文字
ax.set_title("Sin和Cos三角函數的波型", fontsize="large")

# 更改刻度的外觀
for tick in ax.xaxis.get_ticklabels():
    tick.set_fontsize("large")
    tick.set_fontname("Times New Roman")
    tick.set_color("blue")
    tick.set_weight("bold")
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()
ax2 = ax.twinx()  # 使用相同的 x 軸

ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")

ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")

plt.xticks(range(0, 11))
ax.set_yticks(np.linspace(-1, 1, 10))
ax2.set_yticks(np.linspace(0, 12000, 10))

plt.show()

print("------------------------------------------------------------")  # 60個

print("兩Y軸不同刻度, plot + bar")

import matplotlib.gridspec as gridspec

x = np.linspace(0, 6.28, 10)
y = np.sin(x * 2)
y2 = np.sin(x * 2) * np.sin(x * 2) * 10

fig = plt.figure(figsize=(12, 8))  # 圖像大小[英吋]
gs = gridspec.GridSpec(4, 1, figure=fig)
ax = fig.add_subplot()
ax2 = ax.twinx()  # 使用相同的 x 軸

ax.plot(x, y, marker="", alpha=0.8)
ax.grid(20)

ax2.bar(
    x,
    y2,
    alpha=0.2,
    label="hold_volume",
    color="pink",
)
ax.set_title("兩Y軸不同刻度 plot + bar", size=20)

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
ax2 = ax1.twinx()  # 使用相同的 x 軸

ax1.plot(x, temperature_high[:12], "r-")
ax1.plot(x, temperature_average[:12], "g-")
ax1.plot(x, temperature_low[:12], "b-")
ax1.set_xlabel("月份")
ax1.set_ylabel("氣溫")

ax2.plot(x, rainfall_average[:12], "yellow")
ax2.set_ylabel("雨量")

plt.show()

print("------------------------------------------------------------")  # 60個

dists = {
    "區名": [
        "中正區",
        "板橋區",
        "桃園區",
        "北屯區",
        "安南區",
        "三民區",
        "大安區",
        "永和區",
        "八德區",
        "前鎮區",
        "鳳山區",
        "信義區",
        "新店區",
    ],
    "人口": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
    "面積": [
        7.6071,
        23.1373,
        34.8046,
        62.7034,
        107.2016,
        19.7866,
        11.3614,
        5.7138,
        33.7111,
        19.1207,
        26.7590,
        11.2077,
        120.2255,
    ],
}

df = pd.DataFrame(dists, columns=["人口", "面積"], index=dists["區名"])
print(df)
fig, ax = plt.subplots()
fig.suptitle("分區統計")
ax.set_ylabel("人口")
ax.set_xlabel("分區")
ax2 = ax.twinx()  # 使用相同的 x 軸
ax2.set_ylabel("面積")
df["人口"].plot(ax=ax, style="b--o", use_index=True, rot=90)
df["面積"].plot(ax=ax2, style="g-s", use_index=True, rot=90)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
