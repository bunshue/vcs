"""
等差數列 等比數列
等差級數 等比級數

"""

print("------------------------------------------------------------")  # 60個

# 等差數列 等差級數

for i in range(10):
    print(i)

x = range(11)  # 0, 1, 2, ... 10
s = sum(x)
print("等差級數 :", s)

x = range(3, 21, 3)  # 3, 6, 9, ... 18
for i in x:
    print(i)
s = sum(x)
print("等差級數 :", s)

print("------------------------------------------------------------")  # 60個

# 等比數列 等比級數

r = 2
A0 = 1
x = []
y = []
total = 0
for i in range(10 + 1):
    print(i)
    x.append(i)
    y.append(A0 * r**i)
    total += A0 * r**i

print(x)
print(y)
print(total)

import matplotlib.pyplot as plt

plt.plot(x, y)  # 繪圖
plt.show()

print("------------------------------------------------------------")  # 60個

print("一萬元 年利率3.5%")
money = 10000
rate = 0.035
n = 5
for i in range(n):
    money *= 1 + rate
    print(f"第 {i+1} 年本金和 : {int(money)}")

print("------------------------------------------------------------")  # 60個
# 定義GetRoundArea函式，可傳入radius半徑，並傳回圓面積
def GetRoundArea(radius):
    # 傳回圓面積，圓面積公式為 半徑 *  半徑 * 3.14
    return radius * radius * 3.14


r = int(input("請輸入半徑："))
RoundArea = GetRoundArea(r)
print("圓形半徑 %d，面積為 %d" % (r, RoundArea))

print("------------------------------------------------------------")  # 60個


# 畫一些函數

# y = cos(x)
# y = x ^ 2

x = []
y = []
for i in range(-5, 5 + 1):
    print(i)
    x.append(i)
    #y.append(math.cos(i))   # y = cos(x)
    y.append(i * i)         # y = x ^ 2

print(x)
print(y)
print(total)

import matplotlib.pyplot as plt

plt.plot(x, y)  # 繪圖
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

import math
import scipy

print("積分")

def my_funciton1(x):
    # y = math.cos(x)
    y = x ** 2
    # y = math.sqrt(25 - x**2)  # 上半圓
    # y = x**2 + 2 * x + 5  # f(x) = x**2 + 2x + 5
    return y

#area, err = scipy.integrate.quad(my_funciton1, -math.pi/2, math.pi/2)
area, err = scipy.integrate.quad(my_funciton1, -5, 5)
print("積分結果 :", area)
print("誤差 :", err)

print("------------------------------------------------------------")  # 60個


