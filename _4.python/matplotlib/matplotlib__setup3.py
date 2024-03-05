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
