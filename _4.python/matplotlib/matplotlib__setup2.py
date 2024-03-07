"""
plt之基本設定

"""

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

print("兩Y軸不同刻度, plot + bar")

import matplotlib.gridspec as gridspec

x = np.linspace(0, 6.28, 10)
y = np.sin(x * 2)
y2 = np.sin(x * 2) * np.sin(x * 2) * 10

fig = plt.figure(figsize=(12, 8))  # 圖像大小[英吋]
gs = gridspec.GridSpec(4, 1, figure=fig)
ax = fig.add_subplot()

ax.plot(x, y, marker="", alpha=0.8)
ax.grid(20)

axx = ax.twinx()
axx.bar(
    x,
    y2,
    alpha=0.2,
    label="hold_volume",
    color="pink",
)
ax.set_title("兩Y軸不同刻度 plot + bar", size=20)

plt.show()

print("------------------------------------------------------------")  # 60個

# 舊金山市中心（1991–2020年正常值，1849年至今極端數據）

# 月份 	1月 	2月 	3月 	4月 	5月 	6月 	7月 	8月 	9月 	10月 	11月 	12月 	全年

# 平均高溫 °C
listy1 = [
    14.3,
    15.8,
    16.7,
    17.2,
    17.8,
    19.2,
    19.1,
    19.9,
    21.2,
    21.0,
    17.6,
    14.4,
]  # , 17.8

# 平均低溫 °C
listy2 = [8.1, 8.8, 9.4, 9.8, 10.8, 11.7, 12.4, 13.1, 13.1, 12.4, 10.4, 8.3]  # , 10.7

# 平均降雨量 mm
listy3 = [112, 111, 80, 41, 18, 5.1, 0.25, 1.5, 2.5, 24, 66, 121]  # , 581

# 在同一張圖 畫 兩條曲線
month = np.arange(1, 13)
print(type(month))
print(month)

plt.plot(month, listy1, "r-.s", lw=2, markersize=5, label="平均高溫")
plt.plot(month, listy2, "g-.s", lw=2, markersize=5, label="平均低溫")
plt.plot(month, listy3, "b--*", lw=2, markersize=5, label="平均降雨量")

"""
plt.plot(listx, listy, color = "red", ls = "--")
plt.plot(listx, listy, color = "red", ls = "--")
plt.plot(listx, listy, color = "red", ls = "--")
"""

# 同一個指令畫兩條線
# plt.plot(month, listy1, 'r-.s', month, listy2, 'y-s')

plt.legend()

month_chi = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
plt.xticks(month, month_chi, rotation=45)

plt.xlim(0.5, 12.5)  # x軸顯示邊界
plt.ylim(-10, 150)  # y軸顯示邊界

plt.grid(color="k", ls=":", lw=2, alpha=0.5)  # 畫格點
plt.grid(color="r", linestyle=":", linewidth="1", alpha=0.5)  # 畫格點

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


'''
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter


def piformat(x, pos):
    """刻度間距是 1/2 Pi"""
    return r"$\frac{%d\pi}{%d}$" % (int(np.round(x / (np.pi / 2))), 2)


plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot()

ax.plot(x, y, label="sin(x)", color="g", linewidth=3)

# 建立刻度間距 pi/2
ax.xaxis.set_major_locator(MultipleLocator(np.pi / 2))

# 建立刻度標籤
ax.xaxis.set_major_formatter(FuncFormatter(piformat))

plt.title("Sin函數的刻度標籤是數學符號")

plt.grid()

plt.show()

'''
print("------------------------------------------------------------")  # 60個


import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

from math import log2, factorial
from matplotlib import pyplot

import numpy

offset = 0.3

# x = np.linspace(-10, 10, 51)
# y00 = x ** 2

x = np.linspace(-2 * np.pi, 2 * np.pi, 51)
y00 = np.cos(x)

y01 = y00 + offset * 1
y02 = y00 + offset * 2
y03 = y00 + offset * 3
y04 = y00 + offset * 4
y05 = y00 + offset * 5
y06 = y00 + offset * 6
y07 = y00 + offset * 7
y08 = y00 + offset * 8
y09 = y00 + offset * 9
y10 = y00 + offset * 10
y11 = y00 + offset * 11
y12 = y00 + offset * 12
y13 = y00 + offset * 13
y14 = y00 + offset * 14
y15 = y00 + offset * 15
y16 = y00 + offset * 16


num = 6
styles = ["r-.", "g-*", "b-o", "y-x", "c-^", "m-+", "k-d"]
legends = ["对数", "线性", "线性对数", "平方", "立方", "几何级数", "阶乘"]
y_datas = [y00, y01, y02, y03, y04, y05, y06]
for index, y_data in enumerate(y_datas):
    pyplot.plot(x, y_data, styles[index])
pyplot.legend(legends)
# pyplot.xticks(numpy.arange(1, 7, step=1))
# pyplot.yticks(numpy.arange(0, 751, step=50))
pyplot.show()



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


