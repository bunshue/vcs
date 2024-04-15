"""
各種函數畫圖

"""

# 畫y=x^2
# 畫y=sin(x)

import math
import matplotlib.pyplot as plt

x = []
y = []
for i in range(10):
    print(i)
    x.append(i)
    y.append(i * i)  # y=x^2
    # y.append(math.sin(i))  #y=sin(x)

plt.plot(x, y)  # 繪圖

plt.show()

print("------------------------------------------------------------")  # 60個

# 畫直線 y = x * 9 / 5 + 32     F = C*9/5 + 32

import math
import matplotlib.pyplot as plt

x = []
y = []
for i in range(0, 100):
    # print(i)
    x.append(i)
    y.append(i * 9 / 5 + 32)  # y = x * 9 / 5 + 32

plt.plot(x, y)  # 繪圖

plt.show()

print("------------------------------------------------------------")  # 60個

# 畫更精細的y=sin(x)

import math
import matplotlib.pyplot as plt

x = []
y = []
for i in range(100):
    # print(i)
    x.append(i)
    y.append(math.sin(i / 10))  # y=sin(x)

plt.plot(x, y)  # 繪圖

plt.show()

print("------------------------------------------------------------")  # 60個

# 畫2^x
# 畫exp(x)

import math
import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []
for i in range(100 + 1):
    # print(i)
    x.append(i)
    y1.append(2 ** (i / 10))  # y=2^x
    y2.append(math.exp(i / 10))  # y=2^x

plt.plot(x, y1)  # 繪圖
# plt.plot(x, y2)  # 繪圖
plt.grid()  # 加上格線

plt.show()


print("------------------------------------------------------------")  # 60個

# 畫一個半徑為100的圓的上半部 圓心在(0, 0)

import math
import matplotlib.pyplot as plt

# 繪製半徑100的圓（y >= 0）

# 圓的方程式
r = 100  # 半徑

x = []
y = []
for i in range(-100, 100 + 1):
    # print(i)
    x.append(i)
    y.append(math.sqrt(100 * 100 - i * i))

plt.plot(x, y)  # 繪圖
plt.grid()  # 加上格線
# plt.axis("equal")  # 軸比例

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
