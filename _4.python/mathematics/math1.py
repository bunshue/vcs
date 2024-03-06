# python import module : math

import math
import numpy as np

print('------------------------------------------------------------')	#60個

'''
# 顯示數學常數
print("math.e = ", math.e)
print("math.pi = ", math.pi)


print('數學常數')
print("圓周率 : ", math.pi)
print("圓周率 : " + str(math.pi))
print("e : ", math.e)

print('------------------------------------------------------------')	#60個

print('數學函數')

# Test algebraic functions
print("exp(1.0) =", math.exp(1))
print("log(3.78) =", math.log(math.e))
print("log10(10, 10) =", math.log(10, 10))
print("sqrt(4.0) =", math.sqrt(4.0))

n = 16
r = math.sqrt(n)
print("16的平方根 為 : "+str(r))

print('取1024以2為底的log：')
print(math.log(1024, 2)) # 10

print('三角函數')
print("sin(PI / 2) =", math.sin(math.pi / 2))
print("cos(PI / 2) =", math.cos(math.pi / 2))
print("tan(PI / 2) =", math.tan(math.pi / 2))
print("degrees(1.57) =", math.degrees(1.57))
print("radians(90) =", math.radians(90))

for count in range(20):
    print("sin(" + str(count) + "度) = " + str(math.sin(2*math.pi*count/360)) + ", cos(" + str(count) + "度) = " + str(math.cos(2*math.pi*count/360)))

angle = 30
math.sin(math.pi * angle / 2)

print('------------------------------------------------------------')	#60個


# 數學函數
no = -19.536
print("測試值no = ", no)
print("math.fabs(no) =  ", math.fabs(no))
print("math.ceil(no) = ", math.ceil(no))
print("math.floor(no) = ", math.floor(no))
# 指數和對數函數
x, y = 13.536, 3.57
print("測試值x / y = ", x, "/", y)
print("math.exp(x) = ", math.exp(x))
print("math.log(x) = ", math.log(x))
print("math.pow(x,y) = ", math.pow(x,y))
print("math.sqrt(x) = ", math.sqrt(x))
# 三角函數
deg = 60.0
rad = math.radians(deg)
print("測試值deg / rad = ", deg, "/", rad)
print("math.sin(rad) = ", math.sin(rad))
print("math.cos(rad) = ", math.cos(rad))
print("math.tan(rad) = ", math.tan(rad)) 

print("------------------------------------------------------------")  # 60個

import math as m #以別名取代

print("sqrt(16)= ",m.sqrt(16)) #平方根
print("fabs(-8)= ",m.fabs(-8)) #取絕對值
print("fmod(16,5)= ",m.fmod(16,5)) # 16%5
print("floor(3.14)= ",m.floor(3.14)) # 3

"""
import math
x = 10
y = -2

z = math.fabs(x / y)
h = math.factorial(z)

if math.isnan(h) == False:
    print("計算後數值：", h)
    print("最大公約數：", math.gcd(h, x))
"""

print("------------------------------------------------------------")  # 60個

# 顯示數學常數
print("math.e = ", math.e)
print("math.pi = ", math.pi)
# 數學函數
no = -19.536
print("測試值no = ", no)
print("math.fabs(no) =  ", math.fabs(no))
print("math.ceil(no) = ", math.ceil(no))
print("math.floor(no) = ", math.floor(no))
# 指數和對數函數
x, y = 13.536, 3.57
print("測試值x / y = ", x, "/", y)
print("math.exp(x) = ", math.exp(x))
print("math.log(x) = ", math.log(x))
print("math.pow(x,y) = ", math.pow(x,y))
print("math.sqrt(x) = ", math.sqrt(x))
# 三角函數
deg = 60.0
rad = math.radians(deg)
print("測試值deg / rad = ", deg, "/", rad)
print("math.sin(rad) = ", math.sin(rad))
print("math.cos(rad) = ", math.cos(rad))
print("math.tan(rad) = ", math.tan(rad))

print('------------------------------------------------------------')	#60個


nums = [1,2,3,4,5,6,7,8,9,10]
result = math.fsum(nums)
print("1加到10 為 : " + str(result))

print('------------------------------------------------------------')	#60個
 
x1, y1 = 0, 0
x2, y2 = 4, 0
x3, y3 = 0, 3
 
a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print('計算三角形3個內角角度 : ',
      round(A * 100) / 100.0,
      round(B * 100) / 100.0,
      round(C * 100) / 100.0)

print('------------------------------------------------------------')	#60個

print('gcd(16, 40) = {}'.format(math.gcd(16, 40)))
print('gcd(28, 56) = {}'.format(math.gcd(28, 63)))

print('------------------------------------------------------------')	#60個

#degrees(x) 將x由弧度轉角度
#radians(x) 將x由角度轉弧度

rad = np.arctan2(3, 4)  # 求角度（radian）
th = np.degrees(rad)    # 轉成度數

rad = math.atan2(3, 2)  # 計算角度（radian）
th = math.degrees(rad)  # 轉成度數
th

10 * math.cos(math.radians(60)) 

# 計算角度
rad = math.acos(3/5)
deg = math.degrees(rad)
print(deg)

print('------------------------------------------------------------')	#60個

r = 6371                        # 地球半徑
x1, y1 = 22.2838, 114.1731      # 香港紅磡車站經緯度
x2, y2 = 25.0452, 121.5168      # 台北車站經緯度

d = r * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
                  math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
                  math.cos(math.radians(y1 - y2)))

print(f"distance = {d:6.1f}")

print('------------------------------------------------------------')	#60個

print('兩點距離')
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
print('兩點距離 : ', distance) 

print('------------------------------------------------------------')	#60個

import decimal

def acc_deciamal():
    a = 4.2
    b = 2.1
    print(a + b)
    print((a + b) == 6.3)

    # 使用decimal模块
    a = decimal.Decimal('4.2')
    b = decimal.Decimal('2.1')
    print(a + b)
    print((a + b) == decimal.Decimal('6.3'))


    a = decimal.Decimal('1.3')
    b = decimal.Decimal('1.7')
    print(a / b)
    with decimal.localcontext() as ctx:
        ctx.prec = 3
        print(a / b)

    nums = [1.23e+18, 1, -1.23e+18]
    print(sum(nums))
    print(math.fsum(nums))


acc_deciamal()

print('------------------------------------------------------------')	#60個

N = 30
times = 10000000000000              # 電腦每秒可處理數列數目
day_secs = 60 * 60 * 24             # 一天秒數
year_secs = 365 * day_secs          # 一年秒數
combinations = math.factorial(N)    # 組合方式
years = combinations / (times * year_secs)
print("需要 %d 年才可以獲得結果" % years)

print('------------------------------------------------------------')	#60個

z = 3 + 5j

print('實部', z.real)
print('虛部', z.imag)

print('------------------------------------------------------------')	#60個

import cmath
cc = cmath.sqrt(-1)
print(cc)

print('用 math 取 平方根 :')
cc = math.sqrt(16)
print(cc)

print('用 cmath 取 平方根 :')
cc = cmath.sqrt(16)
print(cc)

print('------------------------------------------------------------')	#60個

import cmath

def complex_math():
    a = complex(2, 4)
    b = 3 - 5j
    print(a.conjugate())

    # 正弦 余弦 平方根等
    print(cmath.sin(a))
    print(cmath.cos(a))
    print(cmath.sqrt(a))

complex_math()

print('------------------------------------------------------------')	#60個

r = 6371                        # 地球半徑
x1, y1 = 22.2838, 114.1731      # 香港紅磡車站經緯度
x2, y2 = 25.0452, 121.5168      # 台北車站經緯度

d = 6371 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
                     math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
                     math.cos(math.radians(y1 - y2)))

print("distance = ", d)



print('------------------------------------------------------------')	#60個



"""
分数运算

"""
from fractions import Fraction

def frac():
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(print(a + b))
    print(a.numerator, a.denominator)

    c = a + b
    print(float(c))
    print(type(c.limit_denominator(8)))
    print(c.limit_denominator(8))

frac()


print('------------------------------------------------------------')	#60個

from fractions import Fraction

p = Fraction(22, 7)
print('分數的使用 :', p)
print('分數的使用 : {}'.format(p))
print('分數的使用 : {}'.format(float(p)))

print('------------------------------------------------------------')	#60個

print('算圓周率')
sigma=0
k = 20

for n in range(0,k,1):
    if n & 1: #如果n是奇數
        sigma += float(-1/(2*n+1))
    else: #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))



print('------------------------------------------------------------')	#60個


print('蒙特卡羅方法求圓周率')

n_dots = 1000000
x = np.random.random(n_dots)
y = np.random.random(n_dots)
distance = np.sqrt(x ** 2 + y ** 2)
in_circle = distance[distance < 1]

pi = 4 * float(len(in_circle)) / n_dots
print(pi)


print('------------------------------------------------------------')	#60個

print("計算 pi")

import time

x = 10000000
pi = 0
time_st = time.time()
for i in range(1, x + 1):
    pi += 4 * ((-1) ** (i + 1) / (2 * i - 1))
    if i % 1000000 == 0:  # 隔1000000執行一次
        e_time = time.time() - time_st
        print("當 i={:7d} 時 PI={:20.19f}, 所花時間={}".format(i, pi, e_time))

print('------------------------------------------------------------')	#60個


"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

"""
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low**3 + mid**3 + high**3:
        print(num)





print('------------------------------------------------------------')	#60個

# 函数的定义和使用 - 求最大公约数和最小公倍数

def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(15, 27))
print(lcm(15, 27))


print('------------------------------------------------------------')	#60個



""" 標準差
math.sqrt(sum(pow(x - (sum(data) / len(data)), 2) for x in data) / len(data))

mean = sum(data) / len(data)
variance = sum(pow(x - mean, 2) for x in data) / len(data)
std = math.sqrt(variance)

"""

#math test
x = 10
y = -2

z = math.fabs(x / y)

z = 5
h = math.factorial(z)

if math.isnan(h) == False:
    print("計算後數值：", h)
    print("最大公約數：", math.gcd(h, x))

print('------------------------------------------------------------')	#60個

import math

r = 6371                        # 地球半徑
x1, y1 = 22.2838, 114.1731      # 香港紅磡車站經緯度
x2, y2 = 25.0452, 121.5168      # 台北車站經緯度

d = r*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                math.cos(math.radians(y1-y2)))

print(f"distance = {d:6.1f}")

'''


print('------------------------------------------------------------')	#60個

#認識正、負無限大

import math #匯入math模組
a = 1E309
print('a = 1E309, 輸出', a)

# 輸出True，表示它是NaN
print('為NaN?', math.isnan(float(a/a)))
b = -1E309
print('b = -1309, 輸出', b)

# 輸出True，表示它是Inf
print('為Inf? ', math.isinf(float(-1E309)))

print("------------------------------------------------------------")  # 60個

#將兩個複數進行加減乘除

num1 = 3 + 5j
num2 = 2-4j
print('相加：', num1 + num2)  #回傳  5 + 1j
print('相減：', num1 - num2)  #回傳  1 + 9j
print('相乘：', num1 * num2)  #回傳 26 - 2j
print('相除：', num1 / num2)  #回傳  -0.7 + 1.1j

print("------------------------------------------------------------")  # 60個

import math	#匯入math模組

# 使用math類別的相關方法
num1 = 3
num2 = 8

# 求平方、立方根
print('平方根：', math.sqrt(num1), ', ', num2 ** 0.5)
print(num1, '^ 3 = ', math.pow(num1, 3))
print(num2, '立方根：', math.pow(num2, 1.0/3))

print('餘數：', math.fmod(num1, num2),
      ', GCD =', math.gcd(num1, num2))
print('兩數平方後相加再開根號', math.hypot(num1, num2))

#自然對數
print('指數函式：', math.e)
print('方法exp(4) =', math.exp(4))


print("------------------------------------------------------------")  # 60個

import decimal  # decimal可以獲得比浮點數更精確的數值
ff = 20/3
print("浮點數  :", ff)
dd = decimal.Decimal(20/3)
print("Decimal :", dd)

print('------------------------------------------------------------')	#60個

import fractions

cc = fractions.Fraction(12, 18)
print(cc)

cc = fractions.Fraction(1.348)
print(cc)

cc = fractions.Fraction(fractions.Fraction(2, 5), fractions.Fraction(7, 13))
print(cc)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個






