# python import module : numpy

import numpy as np

print("建立陣列")
x = np.array([1, 2, 3])
y = np.arange(10)  # 類似 Python 的 range, 但是回傳 array
print(x)
print(y)

print("基本運算")
a = np.array([1, 2, 3, 6])
print(a)
b = np.linspace(0, 2, 4)  # 建立一個array, 在0與2的範圍之間讓4個點等分
print(b)
c = a - b
print(c)
print(a**2)

print("全域方法")
x = np.linspace(-np.pi, np.pi, 11) 
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sinc(x)
print("x")
print(x)
print("sin(x) = ")
print(y1)
print("cos(x) = ")
print(y2)
print("tan(x) = ")
print(y3)
print("sinc(x) = ")
print(y4)

print("亂數")
from numpy.random import rand
r = rand(3, 3)      # 建立一個 3x3 隨機矩陣
print(r)


