# python import module : math

import math

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

print('------------------------------')  #30個
 
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

print('------------------------------')  #30個

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

print('------------------------------')  #30個

angle = 30

math.sin(math.pi * angle / 2)

print('------------------------------')  #30個



print('------------------------------')  #30個



