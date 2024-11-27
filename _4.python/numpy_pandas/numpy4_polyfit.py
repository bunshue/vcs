"""
#numpy 做 多項式擬合 polyfit

numpy.polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)


多項式poly1d()的方法

　　　a.　　p(0.5)表示當x = 0.5時，多項式的值為多少

　　　b.　　p.r表示當多項式為 0 時，此等式的根

　　　c.　　p.c表示生成多項式的系數數組

　　　d.　　p.order表示返回最高項的次方數

　　　e.　　p[1]表示返回第一項的系數

　　　f.　　多項式支持實數的四則運算

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

print("3階擬合")
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
z = np.polyfit(x, y, 3)
print(z)

p = np.poly1d(z)
print(p(0.5))

print(p(3.5))

print(p(10))

print("30階擬合, 會震盪")
p30 = np.poly1d(np.polyfit(x, y, 30))
print(p30(4))
print(p30(5))
print(p30(4.5))

xp = np.linspace(-2, 6, 100)
plt.plot(x, y, "r.-", xp, p(xp), "g-", xp, p30(xp), "b--")
# plt.plot(x, y, 'r.-')
plt.scatter(x, y)
plt.ylim(-2, 2)
plt.show()

print("------------------------------------------------------------")  # 60個

# python多項式擬合：np.polyfit 和 np.polyld

# 1. 原始數據：假如要擬合的數據yyy來自sin函數，np.sin

xxx = np.arange(0, 1000)  # x值，此時表示弧度
yyy = np.sin(xxx * np.pi / 180)  # 函數值，轉化成度

# 2. 測試不同階的多項式，例如7階多項式擬合，
# 使用np.polyfit擬合，
# 使用np.polyld得到多項式系數

# 七階多項式擬合
z1 = np.polyfit(xxx, yyy, 7)  # 用7次多項式擬合，可改變多項式階數；
p1 = np.poly1d(z1)  # 得到多項式系數，按照階數從高到低排列
print(p1)  # 顯示多項式

# 3. 求對應xxx的各項擬合函數值

yvals = p1(xxx)  # 可直接使用yvals=np.polyval(z1,xxx)

# 4. 繪圖如下

plt.plot(xxx, yyy, "*", label="original values")
plt.plot(xxx, yvals, "r", label="polyfit values")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend(loc=4)  # 指定legend在圖中的位置，類似象限的位置
plt.title("polyfitting")
plt.show()


# 5. np.polyfit函數：採用的是最小二次擬合，
#  numpy.polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False)，前三個參數是必須的
# 6. np.polyld函數：得到多項式系數，主要有三個參數
#   c_or_r : array_like
#   r : bool, optional
#   variable : str, optional

# 參數1表示：在沒有參數2（也就是參數2默認False時），參數1是一個數組形式，且表示從高到低的多項式系數項，
# 例如參數1為[4,5,6]表示： 4x^2+5x+6 (降冪排列)
# 參數2表示：為True時，表示將參數1中的參數作為根來形成多項式，即參數1為[4,5,6]時表示：(x-4)(x-5)(x-6)=0，
# 也就是：1x^3-15x^2+74x-120
# 參數3表示：換參數標識，用慣了x，可以用 t，s之類的

# 用法：
# 1. 直接進行運算，例如多項式的平方，分別得到

xx = np.poly1d([1, 2, 3])  # 1x^2+2x+3
print(xx)
yy = xx**2  # 求平方，或者用 xx * xx => 1x^4+4x^3+10x^2+12x+9
print(yy)

# 2. 求值：

print(yy(1))
# yy(1) = 36

# 3. 求根：即等式為0時的未知數值
# yy.r
print(yy.r)

# 4. 得到系數形成數組：
# yy.c 為：array([ 1,  4, 10, 12,  9])
print(yy.c)

# 5. 返回最高次冪數：
# yy.order = 4
print(yy.order)

# 6. 返回系數：
print(yy[0])  # 表示冪為0的系數
print(yy[1])  # 表示冪為1的系數

print("------------------------------------------------------------")  # 60個

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24]
y = [
    100,
    88,
    75,
    60,
    50,
    55,
    55,
    56,
    58,
    58,
    61,
    63,
    68,
    71,
    71,
    75,
    76,
    88,
    93,
    97,
    97,
    100,
]

coef = np.polyfit(x, y, 3)  # 迴歸直線係數
model = np.poly1d(coef)  # 線性迴歸方程式
reg = np.linspace(1, 24, 100)

plt.scatter(x, y)
plt.title("網路購物調查")
plt.xlabel("點鐘", fontsize=14)
plt.ylabel("購物人數", fontsize=14)
plt.plot(reg, model(reg), color="red")

plt.show()

x = np.linspace(0, 20, num=21)  # 使用linspace()產生陣列
y = np.linspace(0, 20, num=21)  # 使用linspace()產生陣列

y[7] = 20
y[14] = 0

coef = np.polyfit(x, y, 3)  # 迴歸直線係數
model = np.poly1d(coef)  # 線性迴歸方程式
reg = np.linspace(1, 24, 100)

plt.scatter(x, y)
plt.title("網路購物調查")
plt.xlabel("點鐘", fontsize=14)
plt.ylabel("購物人數", fontsize=14)
plt.plot(reg, model(reg), color="red")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.metrics import r2_score

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24]
y = [
    100,
    88,
    75,
    60,
    50,
    55,
    55,
    56,
    58,
    58,
    61,
    63,
    68,
    71,
    71,
    75,
    76,
    88,
    93,
    97,
    97,
    100,
]

coef = np.polyfit(x, y, 3)  # 迴歸直線係數
model = np.poly1d(coef)  # 線性迴歸方程式

cc = r2_score(y, model(x))
print("r2 :", cc)

print(f"18點購物人數預測 = {model(18).round(2)}")
print(f"20點購物人數預測 = {model(20).round(2)}")

print("------------------------------------------------------------")  # 60個

x = np.array([1, 2, 3])  # 拜訪次數, 單位是100
y = np.array([5, 10, 20])  # 銷售考卷數, 單位是100

a, b = np.polyfit(x, y, 1)  # 迴歸直線
print("斜率 a = {0:5.2f}".format(a))
print("截距 a = {0:5.2f}".format(b))

y2 = a * x + b
plt.scatter(x, y)  # 繪製散佈圖
plt.plot(x, y2)  # 繪製迴歸直線

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.array([22, 26, 23, 28, 27, 32, 30])  # 溫度
y = np.array([15, 35, 21, 62, 48, 101, 86])  # 飲料銷售數量

a, b = np.polyfit(x, y, 1)  # 迴歸直線
print(f"斜率 a = {a:5.2f}")
print(f"截距 b = {b:5.2f}")

y2 = a * x + b
plt.scatter(x, y)  # 繪製散佈圖
plt.plot(x, y2)  # 繪製迴歸直線

sold = a * 31 + b
print("氣溫31度時的銷量 = {}".format(int(sold)))
plt.plot(31, int(sold), "-o")

plt.show()

print("------------------------------------------------------------")  # 60個

print("計算迴歸直線")

# 資料
x = np.array([23, 24, 28, 24, 27, 21, 18, 25, 28, 20])  # 氣溫
y = np.array([37, 22, 62, 32, 74, 16, 10, 69, 83, 7])  # 果汁販賣數量

# 迴歸直線
a, b = np.polyfit(x, y, 1)
y2 = a * x + b
print("斜率: {0}, 截距:{1}".format(a, b))

# 繪圖
plt.scatter(x, y)  # 散布圖
plt.plot(x, y2)  # 迴歸直線

# 預測在氣溫33度時的販賣數量
# a * 33 + b

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

temperature = [25, 31, 28, 22, 27, 30, 29, 33, 32, 26]  # 天氣溫度
rev = [900, 1200, 950, 600, 720, 1000, 1020, 1500, 1420, 1100]  # 營業額

print(f"相關係數 = {np.corrcoef(temperature,rev).round(2)}")
plt.scatter(temperature, rev)
plt.title("天氣溫度與冰品銷售")
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)

plt.show()

print("------------------------------------------------------------")  # 60個

temperature = [25, 31, 28, 22, 27, 30, 29, 33, 32, 26]  # 天氣溫度
rev = [900, 1200, 950, 600, 720, 1000, 1020, 1500, 1420, 1100]  # 營業額

coef = np.polyfit(temperature, rev, 1)  # 迴歸直線係數
reg = np.poly1d(coef)  # 線性迴歸方程式
print(coef.round(2))
print(reg)

print("------------------------------------------------------------")  # 60個

temperature = [25, 31, 28, 22, 27, 30, 29, 33, 32, 26]  # 天氣溫度
rev = [900, 1200, 950, 600, 720, 1000, 1020, 1500, 1420, 1100]  # 營業額

coef = np.polyfit(temperature, rev, 1)  # 迴歸直線係數
reg = np.poly1d(coef)  # 線性迴歸方程式
print(f"當溫度是 35 度時冰品銷售金額 = {reg(35).round(0)}")

print("------------------------------------------------------------")  # 60個

temperature = [25, 31, 28, 22, 27, 30, 29, 33, 32, 26]  # 天氣溫度
rev = [900, 1200, 950, 600, 720, 1000, 1020, 1500, 1420, 1100]  # 營業額

coef = np.polyfit(temperature, rev, 1)  # 迴歸直線係數
reg = np.poly1d(coef)  # 線性迴歸方程式

plt.scatter(temperature, rev)
plt.plot(temperature, reg(temperature), color="red")
plt.title("天氣溫度與冰品銷售")
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)

plt.show()

print("------------------------------------------------------------")  # 60個

temperature = [22, 25, 26, 27, 28, 29, 30, 31, 32, 33]  # 天氣溫度
rev = [600, 900, 1100, 720, 950, 1020, 1000, 1200, 1420, 1500]  # 營業額

coef = np.polyfit(temperature, rev, 2)  # 迴歸直線係數
reg = np.poly1d(coef)  # 線性迴歸方程式
print(reg)
plt.scatter(temperature, rev)
plt.plot(temperature, reg(temperature), color="red")
plt.title("天氣溫度與冰品銷售")
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)
plt.show()

print("------------------------------------------------------------")  # 60個

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24]
y = [
    100,
    88,
    75,
    60,
    50,
    55,
    55,
    56,
    58,
    58,
    61,
    63,
    68,
    71,
    71,
    75,
    76,
    88,
    93,
    97,
    97,
    100,
]

plt.scatter(x, y)
plt.title("網路購物調查")
plt.xlabel("點鐘", fontsize=14)
plt.ylabel("購物人數", fontsize=14)

plt.show()

print("------------------------------------------------------------")  # 60個

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24]
y = [
    100,
    88,
    75,
    60,
    50,
    55,
    55,
    56,
    58,
    58,
    61,
    63,
    68,
    71,
    71,
    75,
    76,
    88,
    93,
    97,
    97,
    100,
]

coef = np.polyfit(x, y, 3)  # 迴歸直線係數
model = np.poly1d(coef)  # 線性迴歸方程式
reg = np.linspace(1, 24, 100)

plt.scatter(x, y)
plt.title("網路購物調查")
plt.xlabel("點鐘", fontsize=14)
plt.ylabel("購物人數", fontsize=14)
plt.plot(reg, model(reg), color="red")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.metrics import r2_score

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24]
y = [
    100,
    88,
    75,
    60,
    50,
    55,
    55,
    56,
    58,
    58,
    61,
    63,
    68,
    71,
    71,
    75,
    76,
    88,
    93,
    97,
    97,
    100,
]

coef = np.polyfit(x, y, 3)  # 迴歸直線係數
model = np.poly1d(coef)  # 線性迴歸方程式
print(r2_score(y, model(x)).round(3))

print("------------------------------------------------------------")  # 60個

from sklearn.metrics import r2_score

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24]
y = [
    100,
    88,
    75,
    60,
    50,
    55,
    55,
    56,
    58,
    58,
    61,
    63,
    68,
    71,
    71,
    75,
    76,
    88,
    93,
    97,
    97,
    100,
]

coef = np.polyfit(x, y, 3)  # 迴歸直線係數
model = np.poly1d(coef)  # 線性迴歸方程式
print(f"18點購物人數預測 = {model(18).round(2)}")
print(f"20點購物人數預測 = {model(20).round(2)}")

print("------------------------------------------------------------")  # 60個

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24]
y = [
    100,
    21,
    75,
    49,
    15,
    98,
    55,
    31,
    33,
    82,
    61,
    80,
    32,
    71,
    99,
    15,
    66,
    88,
    21,
    97,
    30,
    5,
]

coef = np.polyfit(x, y, 3)  # 迴歸直線係數
model = np.poly1d(coef)  # 線性迴歸方程式
reg = np.linspace(1, 24, 100)

plt.scatter(x, y)
plt.title("網路購物調查")
plt.xlabel("點鐘", fontsize=14)
plt.ylabel("購物人數", fontsize=14)
plt.plot(reg, model(reg), color="red")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.metrics import r2_score

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 23, 24]
y = [
    100,
    21,
    75,
    49,
    15,
    98,
    55,
    31,
    33,
    82,
    61,
    80,
    32,
    71,
    99,
    15,
    66,
    88,
    21,
    97,
    30,
    5,
]

coef = np.polyfit(x, y, 3)  # 迴歸直線係數
model = np.poly1d(coef)  # 線性迴歸方程式
print(r2_score(y, model(x)).round(3))

print("------------------------------------------------------------")  # 60個

temperature = [25, 31, 28, 22, 27, 30, 29, 33, 32, 26]  # 天氣溫度
rev = [900, 1200, 950, 600, 720, 1000, 1020, 1500, 1420, 1100]  # 營業額

print(f"相關係數 = {np.corrcoef(temperature,rev).round(2)}")

plt.scatter(temperature, rev)
plt.title("天氣溫度與冰品銷售")
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)

plt.show()


print("------------------------------------------------------------")  # 60個

temperature = [25, 31, 28, 22, 27, 30, 29, 33, 32, 26]  # 天氣溫度
rev = [900, 1200, 950, 600, 720, 1000, 1020, 1500, 1420, 1100]  # 營業額

coef = np.polyfit(temperature, rev, 1)  # 迴歸直線係數
reg = np.poly1d(coef)  # 線性迴歸方程式
print(coef.round(2))
print(reg)

print("------------------------------------------------------------")  # 60個

temperature = [25, 31, 28, 22, 27, 30, 29, 33, 32, 26]  # 天氣溫度
rev = [900, 1200, 950, 600, 720, 1000, 1020, 1500, 1420, 1100]  # 營業額

coef = np.polyfit(temperature, rev, 1)  # 迴歸直線係數
reg = np.poly1d(coef)  # 線性迴歸方程式
print(f"當溫度是 35 度時冰品銷售金額 = {reg(35).round(0)}")

print("------------------------------------------------------------")  # 60個

temperature = [25, 31, 28, 22, 27, 30, 29, 33, 32, 26]  # 天氣溫度
rev = [900, 1200, 950, 600, 720, 1000, 1020, 1500, 1420, 1100]  # 營業額

coef = np.polyfit(temperature, rev, 1)  # 迴歸直線係數
reg = np.poly1d(coef)  # 線性迴歸方程式

plt.scatter(temperature, rev)
plt.plot(temperature, reg(temperature), color="red")
plt.title("天氣溫度與冰品銷售")
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)

plt.show()

print("------------------------------------------------------------")  # 60個

times = [1, 2, 3]  # 臉書行銷次數
rev = [10, 18, 19]  # 增加業績

coef = np.polyfit(times, rev, 2)  # 二次函數係數
reg = np.poly1d(coef)  # 二次函數迴歸方程式
print(reg)
plt.scatter(times, rev)
plt.plot(times, reg(times), color="red")
plt.title("臉書行銷與業績增加金額")
plt.xlabel("臉書行銷次數", fontsize=14)
plt.ylabel("增加業績金額", fontsize=14)

plt.show()

print("------------------------------------------------------------")  # 60個

temperature = [22, 25, 26, 27, 28, 29, 30, 31, 32, 33]  # 天氣溫度
rev = [600, 900, 1100, 720, 950, 1020, 1000, 1200, 1420, 1500]  # 營業額

coef = np.polyfit(temperature, rev, 2)  # 迴歸直線係數
reg = np.poly1d(coef)  # 線性迴歸方程式
print(reg)
plt.scatter(temperature, rev)
plt.plot(temperature, reg(temperature), color="red")
plt.title("天氣溫度與冰品銷售")
plt.xlabel("溫度", fontsize=14)
plt.ylabel("營業額", fontsize=14)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
