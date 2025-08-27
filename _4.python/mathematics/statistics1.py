"""
統計專用

"""

import sys
import numpy as np

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

'''
a = 580
b = 600
c = 680
d = 620

a = 600
b = 600
c = 600
d = 600

arr = np.array([a, b, c, d])

print(a, b, c, d)
print(np.std(arr, ddof = 0))#lee use this  wiki use this

average = (a + b + c + d) / 4
print(average)

print(average + 2 * np.std(arr, ddof = 0))

#指定 ddof 參數，全名為 Delta Degree of Freedom，np.std() 預設的 ddof 是 0
#ddof=0，回傳 population standard deviation 母體標準差，分母(n)，有偏估計
#ddof=1，回傳 sample standard deviation 樣本標準差，分母(n-1)，無偏估計

print(np.std(arr, ddof = 1))#this



print('------------------------------------------------------------')	#60個

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

# 計算變異數
myvar = 0
for v in x:
    myvar += ((v - mean)**2)
myvar = myvar / len(x)
print(f"變異數 : {myvar}")

print('------------------------------------------------------------')	#60個

x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]
mean = sum(x) / len(x)

# 計算變異數
var = 0
for v in x:
    var += ((v - mean) ** 2)
sd = (var / len(x)) ** 0.5
print(f"標準差 : {sd:6.2f}")

print('------------------------------------------------------------')	#60個


N = 10000

random_numbers = []
for _ in range(N):
    random_numbers.append(np.random.randn())

"""
random_numbers = np.random.randn(N) #same
print(random_numbers.shape)
"""

max_temp = max(random_numbers)
min_temp = min(random_numbers)
mean_temp = sum(random_numbers) / len(random_numbers)

# 排序後取得中位數
random_numbers.sort()
median_temp = random_numbers[len(random_numbers) // 2]

print("max = {}".format(max_temp))
print("min = {}".format(min_temp))
print("mean = {}".format(mean_temp))
print("median = {}".format(median_temp))

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
'''
print("使用 statistics 模組")

"""

mean() 平均數
median() 中位數
median_low() median_high() 偶數個數據中 較高或較低的中位數
median_grouped() 數據分組(同樣述職的分成同一組)的中位數
mode()眾數 數據中出現最多次的數值
pstdev() pvariance() 計算數據的母體標準差和變異數
 stdev()  variance() 計算數據的樣本標準差和變異數

# mode()取眾數


statistics.pvariance(x) 母體變異數
statistics.variance(x)  樣本變異數
statistics.pstdev(x)    母體標準差
statistics.stdev(x)     樣本標準差
"""


print("------------------------------------------------------------")  # 60個


x = [66, 58, 25, 78, 58, 15, 120, 39, 82, 50]

print("使用 numpy 模組計算統計資料")
print(f"Numpy模組母體變異數  : {np.var(x):6.2f}")
print(f"Numpy模組樣本變異數  : {np.var(x,ddof=1):6.2f}")
print(f"Numpy模組母體標準差  : {np.std(x):6.2f}")
print(f"Numpy模組樣本標準差  : {np.std(x,ddof=1):6.2f}")

import statistics

print("使用 statistics 模組計算統計資料")
print(f"母體變異數 : {statistics.pvariance(x):6.2f}")
print(f"樣本變異數 : {statistics.variance(x):6.2f}")
print(f"母體標準差 : {statistics.pstdev(x):6.2f}")
print(f"樣本標準差 : {statistics.stdev(x):6.2f}")

print(f"平均 = {np.mean(x)}")
print(f"中位 = {np.median(x)}")
print(f"眾數 = {statistics.mode(x)}")
print(f"眾數 mode  : {statistics.mode(x)}")

print("平均 : ", round(statistics.mean(x), 2))

print("------------------------------------------------------------")  # 60個

import statistics

sc = [
    60,
    10,
    40,
    80,
    80,
    30,
    80,
    60,
    70,
    90,
    50,
    50,
    50,
    70,
    60,
    80,
    80,
    50,
    60,
    70,
    70,
    40,
    30,
    70,
    60,
    80,
    20,
    80,
    70,
    50,
    90,
    80,
    40,
    40,
    70,
    60,
    80,
    30,
    20,
    70,
]
print(f"平均成績 = {np.mean(sc)}")
print(f"中位成績 = {np.median(sc)}")
print(f"眾數成績 = {statistics.mode(sc)}")

print("平均 : ", round(statistics.mean(sc), 2))

hist = [0] * 9
for s in sc:
    if s == 10:
        hist[0] += 1
    elif s == 20:
        hist[1] += 1
    elif s == 30:
        hist[2] += 1
    elif s == 40:
        hist[3] += 1
    elif s == 50:
        hist[4] += 1
    elif s == 60:
        hist[5] += 1
    elif s == 70:
        hist[6] += 1
    elif s == 80:
        hist[7] += 1
    elif s == 90:
        hist[8] += 1
width = 0.35
N = len(hist)
x = np.arange(N)
plt.rcParams["font.family"] = "Microsoft JhengHei"
plt.bar(x, hist, width)
plt.ylabel("學生人數")
plt.xlabel("分數")
plt.xticks(x, ("10", "20", "30", "40", "50", "60", "70", "80", "90"))
plt.title("成績表")

plt.show()

sys.exit()
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
statistics --- 數學統計函式

#平均值與中央位置量數
mean()資料的算術平均數（平均值）。
fmean()快速浮點數算數平均數，可調整權重。
geometric_mean()資料的幾何平均數。
harmonic_mean()資料的調和平均數。
median()資料的中位數（中間值）。 「中間兩數取平均」
median_low()資料中較小的中位數。 低中位數
median_high()資料中較大的中位數。 高中位數
median_grouped()分組資料的中位數或 50% 處。
mode()離散 (discrete) 或名目 (nomial) 資料中的眾數（出現次數最多次的值），只回傳一個。 眾數
multimode()離散或名目資料中的眾數（出現次數最多次的值）組成的 list。
quantiles()將資料分成數個具有相等機率的區間，即分位數 (quantile)。

#離度 (spread) 的測量
pstdev()資料的母體標準差。
pvariance()資料的母體變異數。
stdev()資料的樣本標準差。
variance()資料的樣本變異數。

#兩個輸入之間的關係統計
covariance()兩變數的樣本共變異數。
correlation()Pearson 與 Spearman 相關係數 (correlation coefficient)。
linear_regression()簡單線性迴歸的斜率和截距。

==================  ==================================================
Function            Description
==================  ==================================================
mean                Arithmetic mean (average) of data.
fmean               Fast, floating point arithmetic mean.
geometric_mean      Geometric mean of data.
harmonic_mean       Harmonic mean of data.
median              Median (middle value) of data.
median_low          Low median of data.
median_high         High median of data.
median_grouped      Median, or 50th percentile, of grouped data.
mode                Mode (most common value) of data.
multimode           List of modes (most common values of data).
quantiles           Divide data into intervals with equal probability.
==================  ==================================================

>>> mean([-1.0, 2.5, 3.25, 5.75])
2.625

>>> median([2, 3, 4, 5])
3.5

>>> stdev([2.5, 3.25, 5.5, 11.25, 11.75])  #doctest: +ELLIPSIS
4.38961843444...

>>> data = [1, 2, 2, 4, 4, 4, 5, 6]
>>> mu = mean(data)
>>> pvariance(data, mu)
2.5
"""
import statistics

# 計算平均值
s = statistics.mean([1, 2, 3, 4, 4])
print(s)

# 計算平均值
s = statistics.mean([-1.0, 2.5, 3.25, 5.75])
print(s)

from fractions import Fraction as F

# 計算平均值
s = statistics.mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
print(s)

from decimal import Decimal as D

# 計算平均值
s = statistics.mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
print(s)

s = statistics.fmean([3.5, 4.0, 5.25])
print(s)
# 4.25

# 支援選擇性的加權
# 以 20% 的比重計算小考分數，20% 的比重計算作業分數，30% 的比重計算期中考試分數，以及 30% 的比重計算期末考試分數：

grades = [85, 92, 83, 91]

weights = [0.20, 0.20, 0.30, 0.30]

s = statistics.fmean(grades, weights)
print(s)

# 眾數
s = statistics.mode([1, 1, 2, 3, 3, 3, 3, 4])
print(s)

s = statistics.mode(["red", "blue", "blue", "red", "green", "red", "red"])
print(s)

# 標準差（即母體變異數的平方根）
s = statistics.pstdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
print(s)

data = [0.0, 0.25, 0.25, 1.25, 1.5, 1.75, 2.75, 3.25]

# 母體變異數
s = statistics.pvariance(data)
print(s)
# 1.25

# 如果已經計算出資料的平均值，你可以將其作為選擇性的第二個引數 mu 傳遞以避免重新計算：

# 計算平均值
mu = statistics.mean(data)

# 母體變異數
s = statistics.pvariance(data, mu)
print(s)
# 1.25

# 回傳樣本標準差（即樣本變異數的平方根）
s = statistics.stdev([1.5, 2.5, 2.5, 2.75, 3.25, 4.75])
print(s)

# 回傳 data 的樣本變異數
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

s = statistics.variance(data)
print(s)

# 如果已經計算出資料的平均值，你可以將其作為選擇性的第二個引數 mu 傳遞以避免重新計算：
mu = statistics.mean(data)
s = statistics.variance(data, mu)
print(s)

print("------------------------------------------------------------")  # 60個

"""
statistics.quantiles(data, *, n=4, method='exclusive')
將 data 分成 n 個具有相等機率的連續區間。
"""

# Decile cut points for empirically sampled data
data = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

s = [round(q, 1) for q in statistics.quantiles(data, n=10)]
print(s)

print("------------------------------------------------------------")  # 60個

# statistics.covariance(x, y, /)
# 回傳兩輸入 x 與 y 的樣本共變異數 (sample covariance)。共變異數是衡量兩輸入的聯合變異性 (joint variability) 的指標。
# 兩輸入必須具有相同長度（至少兩個）

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

y = [1, 2, 3, 1, 2, 3, 1, 2, 3]

s = statistics.covariance(x, y)
print(s)

z = [9, 8, 7, 6, 5, 4, 3, 2, 1]

s = statistics.covariance(x, z)
print(s)

s = statistics.covariance(z, x)
print(s)

print("------------------------------------------------------------")  # 60個

# statistics.correlation(x, y, /, *, method='linear')

# 回傳兩輸入的 Pearson 相關係數 (Pearson’s correlation coefficient)。Pearson 相關係數 r 的值介於 -1 與 +1 之間。它衡量線性關係的強度與方向。

# 以 Kepler 行星運動定律為例：

# Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and  Neptune

orbital_period = [88, 225, 365, 687, 4331, 10_756, 30_687, 60_190]  # days

dist_from_sun = [58, 108, 150, 228, 778, 1_400, 2_900, 4_500]  # million km

# Show that a perfect monotonic relationship exists

# s = statistics.correlation(orbital_period, dist_from_sun, method='ranked')
# print(s)

# Observe that a linear relationship is imperfect

s = round(statistics.correlation(orbital_period, dist_from_sun), 4)
print(s)

# Demonstrate Kepler's third law: There is a linear correlation
# between the square of the orbital period and the cube of the
# distance from the sun.

period_squared = [p * p for p in orbital_period]
dist_cubed = [d * d * d for d in dist_from_sun]

s = round(statistics.correlation(period_squared, dist_cubed), 4)
print(s)

print("------------------------------------------------------------")  # 60個

# statistics.linear_regression(x, y, /, *, proportional=False)

# 回傳使用普通最小平方法 (ordinary least square) 估計出的簡單線性迴歸 (simple linear regression) 參數中的斜率 (slope) 與截距 (intercept)。簡單線性迴歸描述自變數 (independent variable) x 與應變數 (dependent variable) y 之間的關係，用以下的線性函式表示：
year = [1971, 1975, 1979, 1982, 1983]

films_total = [1, 2, 3, 4, 5]

slope, intercept = statistics.linear_regression(year, films_total)

s = round(slope * 2019 + intercept)
print(s)


print("------------------------------------------------------------")  # 60個

# 繼續 correlation() 中的範例，我們看看基於主要行星的模型可以如何很好地預測矮行星的軌道距離：

model = statistics.linear_regression(period_squared, dist_cubed, proportional=True)

slope = model.slope

# Dwarf planets:   Pluto,  Eris,    Makemake, Haumea, Ceres

orbital_periods = [90_560, 204_199, 111_845, 103_410, 1_680]  # days

import math

predicted_dist = [math.cbrt(slope * (p * p)) for p in orbital_periods]

s = list(map(round, predicted_dist))
print(s)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
