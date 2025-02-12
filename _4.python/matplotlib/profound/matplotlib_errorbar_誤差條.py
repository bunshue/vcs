"""
matplotlib_誤差條

plt.errorbar()函数用于表现有一定置信区间的带误差数据。
plt.errorbar(x, y,   # x,y: 数据点的位置坐标
    yerr=None,       # xerr: 数据的误差范围
    xerr=None,       # yerr: 数据的误差范围
    fmt='',          # fmt: 数据点的标记样式 以及 相互之间连接线样式
    ecolor=None,     # ecolor: 误差棒的线条颜色
    elinewidth=None, # elinewidth: 误差棒的线条粗细
    capsize=None,    # capsize: 误差棒边界横杠的大小
    capthick=None    # capthick: 误差棒边界横杠的厚度
)
其他参数：
  # ms: 数据点的大小
  # mfc: 数据点的颜色
  # mec: 数据点边缘的颜色

x：数据点的水平位置
y：数据点的垂直位置
yerr：y轴方向的数据点的误差计算方法
xerr：x轴方向的数据点的误差计算方法
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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

# 10 個點 每個點有 x誤差+-0.03 y誤差+-0.2
x = np.linspace(0, 1, 10)  # 頭尾共N個等距
y = np.exp(x)
y = x

y_error = np.random.rand(10) / 2  # 誤差是個陣列, 對應到每個x

# fmt(數據點標記樣式) :   'o' ',' '.' 'x' '+' 'v' '^' '<' '>' 's' 'd' 'p'

# 樣式1
# plt.errorbar(x, y, y/4) # 指定y誤差的長度 固定或陣列

# 樣式2
# dx, dy = 0.03, 0.2
# plt.errorbar(x, y, xerr=dx, yerr=dy, fmt="bo:")

# plt.errorbar(x, y, xerr=dx, yerr=dy, ecolor="r", capsize=3)
# plt.errorbar(x, y, fmt="o", yerr=dy, ecolor="r", color="b", capsize=3)
# plt.errorbar(x, y, fmt="o-", yerr=dy, ecolor="r", color="b", capsize=3)

# plt.errorbar(x, y, yerr=dy, fmt="r.")
# plt.errorbar(x, y, yerr=dy, fmt="o", color="black", ecolor="lightgray", elinewidth=3, capsize=0)

# 使用 uplims = True
# plt.errorbar(x, y, fmt="o-", yerr=dy, ecolor="r", color="b", uplims=True, capsize=3)

# 使用 uplims=True, lolims=True
# plt.errorbar(x, y, yerr=dy, ecolor="r", uplims=True, lolims=True)

# 樣式3
# plt.errorbar(x, y, yerr=y_error, fmt="o", ecolor="r", color="b", elinewidth=2, capsize=4)

# 樣式4
plt.errorbar(x, y, yerr=y_error, fmt="o", ecolor="r", color="b", elinewidth=2, capsize=4,
             ms=5,
             mfc="wheat",
             mec="salmon",
             )
show()

# 製作誤差範圍
error = 0.05 + 0.15 * x  # 误差范围函数
error_range = [error * 0.3, error]  # 下置信度和上置信度

plt.errorbar(
    x,
    y,
    yerr=error_range,
    fmt="o:",
    ecolor="hotpink",
    elinewidth=3,
    ms=5,
    mfc="wheat",
    mec="salmon",
    capsize=3,
)
show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)  # 頭尾共N個等距
y = np.sin(x) * 2
dy = 0.5
up = [True, False] * 10  # 上限串列
lo = [False, True] * 10  # 下限串列
plt.errorbar(x, y, yerr=dy, uplims=up, lolims=lo, ecolor="r")

show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 20)  # 頭尾共N個等距
y = np.sin(x) * 2
dy = 0.2 + 0.01 * x
dy_range = [dy * 0.5, dy]  # (下方誤差, 上方誤差)
plt.errorbar(x, y, fmt="o-", yerr=dy_range, ecolor="r", color="b", capsize=3)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from scipy import stats

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
population_mean = sum(population) / 10000.0

sample_size = 1000
intervals = []
sample_means = []

for sample in range(25):
    sample = np.random.choice(a=population, size=sample_size)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)
    sample_stdev = sample.std()
    sigma = sample_stdev / math.sqrt(sample_size - 1)
    z_critical = stats.norm.ppf(q=0.975)
    margin_of_error = z_critical * sigma
    cc1 = sample_mean - margin_of_error
    cc2 = sample_mean + margin_of_error
    if cc1 > cc2:
        confidence_interval = (cc1, cc2)
    else:
        confidence_interval = (cc2, cc1)
    intervals.append(confidence_interval)

plt.figure(figsize=(9, 9))
plt.errorbar(
    x=np.arange(0.1, 25, 1),
    y=sample_means,
    yerr=[(top - bot) / 2 for top, bot in intervals],
    fmt="o",
)
plt.hlines(xmin=0, xmax=25, y=population_mean, linewidth=2.0, color="red")
show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
x = np.arange(10)
y = 3 * np.cos(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)  # 頭尾共N個等距

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

show()

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


