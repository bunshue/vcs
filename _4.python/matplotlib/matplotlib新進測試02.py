"""
新進測試

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

# 製作資料範例
# 畫 y = 3 * x + 5

x = [x for x in range(-11, 11)]
# y1 = [3 * y + 5 for y in x]

y1 = [2 * y for y in x]
y2 = [(2 * y - 2) for y in x]
y3 = [(2 * y + 2) for y in x]

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x**2)
ax = plt.subplot()  # 回傳子圖物件
ax.plot(x, y)  # 使用子圖物件調用plot()函數

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 500)  # 建立含500個元素的陣列
y1 = np.sin(x)  # sin函數
y2 = np.cos(x)  # cos函數
ax = plt.subplot()
ax.plot(x, y1, lw=2)  # 線條寬度是 2
ax.plot(x, y2, linewidth=5)  # 線條寬度是 5

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x**2)
ax = plt.subplot()  # 回傳子圖物件
ax.plot(x, y)  # 使用子圖物件調用plot()函數
ax.set_title("Sin function")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()

print("------------------------------------------------------------")  # 60個

x = [x for x in range(9)]
squares = [y * y for y in range(9)]
ax = plt.subplot()
ax.plot(squares)
ax.set_aspect("equal")

plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.subplot()  # 建立圖表
ax.plot([1, 3])  # 繪製圖表
ax.set_xlabel("x 座標")
ax.set_ylabel("y 座標")
ax.set_title("資料布局")

plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.subplot()  # 建立圖表
ax.plot([1, 3])  # 繪製圖表
ax.set_xlabel("x 座標")
ax.set_ylabel("y 座標")
ax.set_title("資料布局")

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes([0.1, 0.1, 0.5, 0.8])
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
x = np.linspace(0, 2 * np.pi, 500)
ax.plot(x, np.sin(x) ** 2, "g")

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(2 * np.pi * x) + 1
fig = plt.figure()
ax = plt.axes()
# ax.set_xlim([1, 5])
# ax.set_ylim([-0.5, 2.5])
plt.plot(x, y)
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(2 * np.pi * x) + 1
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([1, 5])
ax.set_ylim([-0.5, 2.5])
plt.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

import numpy as np
import matplotlib.pyplot as plt 

# nodelist = ["city1","city2","city3","city4","city5","city6","city7","city8"]
dist = np.mat([[0.1,0.1],[0.9,0.5],[0.9,0.1],[0.45,0.9],[0.9,0.8],[0.7,0.9],[0.1,0.45],[0.45,0.1]])
m,n = np.shape(dist)

# 绘图
fig = plt.figure()

ax = fig.add_subplot(111)

for point in dist.tolist():
	plt.annotate("("+str(point[0])+", "+str(point[1])+")",xy = (point[0],point[1]))	
xlist = []
ylist = []
for px,py in zip(dist.T.tolist()[0],dist.T.tolist()[1]):
	xlist.append([px])
	ylist.append([py])

ax.plot(xlist,ylist,'r') 

plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
