# python import module : math

import math
import numpy as np

print('------------------------------------------------------------')	#60個

print("圓周率 : ", math.pi)
print("圓周率 : " + str(math.pi))

for count in range(20):
    print("sin(" + str(count) + "度) = " + str(math.sin(2*math.pi*count/360)) + ", cos(" + str(count) + "度) = " + str(math.cos(2*math.pi*count/360)))

nums = [1,2,3,4,5,6,7,8,9,10]
result = math.fsum(nums)
print("1加到10 為 : " + str(result))

n = 16
r = math.sqrt(n)
print("16的平方根 為 : "+str(r))

print('取1024以2為底的log：')
print(math.log(1024, 2)) # 10

print('------------------------------------------------------------')	#60個
 
# Test algebraic functions
print("exp(1.0) =", math.exp(1))
print("log(3.78) =", math.log(math.e))
print("log10(10, 10) =", math.log(10, 10))
print("sqrt(4.0) =", math.sqrt(4.0))
 
# Test trigonometric functions
print("sin(PI / 2) =", math.sin(math.pi / 2))
print("cos(PI / 2) =", math.cos(math.pi / 2))
print("tan(PI / 2) =", math.tan(math.pi / 2))
print("degrees(1.57) =", math.degrees(1.57))
print("radians(90) =", math.radians(90))

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

angle = 30

math.sin(math.pi * angle / 2)

print('------------------------------------------------------------')	#60個


import math

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

import math
print('gcd(16, 40) = {}'.format(math.gcd(16, 40)))
print('gcd(28, 56) = {}'.format(math.gcd(28, 63)))

print('------------------------------------------------------------')	#60個

#degrees(x) 將x由弧度轉角度
#radians(x) 將x由角度轉弧度

rad = np.arctan2(3, 4)  # 求角度（radian）
th = np.degrees(rad)    # 轉成度數

import math
rad = math.atan2(3, 2)  # 計算角度（radian）
th = math.degrees(rad)  # 轉成度數
th

import math
10 * math.cos(math.radians(60)) 

# 計算角度
rad = math.acos(3/5)
deg = math.degrees(rad)
print(deg)

print('------------------------------------------------------------')	#60個



import math

r = 6371                        # 地球半徑
x1, y1 = 22.2838, 114.1731      # 香港紅磡車站經緯度
x2, y2 = 25.0452, 121.5168      # 台北車站經緯度

d = r*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                math.cos(math.radians(y1-y2)))

print(f"distance = {d:6.1f}")


print('------------------------------------------------------------')	#60個

import math
for i in range(10):
    x = math.sqrt(i)
    print(x)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


