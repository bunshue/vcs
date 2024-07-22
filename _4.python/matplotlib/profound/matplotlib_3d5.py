"""
第29章：基礎 3D 繪圖
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

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_title('3D圖表',fontsize=16,color='b')
plt.show()

print("------------------------------------------------------------")  # 60個

z = np.linspace(0, 1, 300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.plot(x, y, z)

plt.show()

print("------------------------------------------------------------")  # 60個

z = np.linspace(0, 1, 300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.plot3D(x, y, z)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(0, 20, 0.1)
y = np.sin(x)
z = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.plot(x, y, z, color='m', lw=3)

plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
x = np.random.random(150)*10            # 建立150個0 - 10的隨機數
y = np.random.random(150)*15            # 建立150個0 - 15的隨機數
z = np.random.random(150)*20            # 建立150個0 - 20的隨機數
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.scatter(x, y, z)

plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
x = np.random.random(150)*10            # 建立150個0 - 10的隨機數
y = np.random.random(150)*15            # 建立150個0 - 15的隨機數
z = np.random.random(150)*20            # 建立150個0 - 20的隨機數
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.scatter3D(x, y, z)
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
x = np.random.random(150)*10            # 建立150個0 - 10的隨機數
y = np.random.random(150)*15            # 建立150個0 - 15的隨機數
z = np.random.random(150)*20            # 建立150個0 - 20的隨機數
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.scatter(x, y, z, marker='*', color='m')

plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
x_heights = np.random.randint(120,190,50)
y_weights = np.random.randint(30,100,50)
z_ages = np.random.randint(low=10,high=35,size=50)
# 性別標籤 1 是男生, 0 是女生
gender = np.random.choice([0, 1],50)   
# 建立軸物件
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# 繪製散點圖
ax.scatter(x_heights,y_weights,z_ages,c=gender)
ax.set_xlabel('身高 (單位 : 公分)',color='m')
ax.set_ylabel('體重 (單位 : 公斤)',color='m')
ax.set_zlabel('年齡 (單位 : 歲',color='m')
ax.set_title('不同年齡體重與身高分佈圖',fontsize=16,color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

z = np.linspace(0,1,300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)
c = x + y
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.scatter(x, y, z, c = c)

plt.show()

print("------------------------------------------------------------")  # 60個

z = np.linspace(0,1,300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)
c = x + y
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.scatter(x, y, z, c=c, cmap='hsv')
plt.show()

print("------------------------------------------------------------")  # 60個

np.random.seed(10)
# 第 A 組資料
x1 = np.random.randn(100)
y1 = np.random.randn(100)
z1 = np.random.randn(100)
# 第 B 組資料
x2 = np.random.randn(100)
y2 = np.random.randn(100)
z2 = np.random.randn(100)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# 繪製散點圖
ax.scatter(x1,y1,z1,c=z1,cmap='Oranges',marker='d',label='A 資料組')
ax.scatter(x2,y2,z2,c=z2,cmap='Blues',marker='*',label='B 資料組')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.legend()                                 # 建立圖例

plt.show()

print("------------------------------------------------------------")  # 60個

z = np.linspace(0,1,300)
x = z * np.sin(30*z)
y = z * np.cos(30*z)
c = x + y
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
sc = ax.scatter(x, y, z, c=c, cmap='hsv')   # 散點圖物件
fig.colorbar(sc)                            # 資料條
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
N = 150
# 建立折線用的 3D 座標資料
z = np.linspace(0, 20, N)
x1 = np.cos(z)
y1 = np.sin(z)
# 繪製 3D 折線
ax.plot(x1, y1, z, color='m', label='plot')

# 建立散點用的 3D 座標資料, z 則沿用
x2 = np.cos(z) + np.random.randn(N) * 0.1
y2 = np.sin(z) + np.random.randn(N) * 0.1
# 繪製 3D 散點
ax.scatter(x2,y2,z,c=z,cmap='hsv',label='scatter')

ax.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(0.5*X**2+0.5*Y**2))    # 建立 Z 資料
np.random.seed(10)
c = np.random.rand(N, N)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')
fig.colorbar(sc)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(0.1*X**2+0.1*Y**2))    # 建立 Z 資料
np.random.seed(10)
c = np.random.rand(N, N)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')
fig.colorbar(sc)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(X**2+Y**2))            # 建立 Z 資料
np.random.seed(10)
c = np.random.rand(N, N)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')
fig.colorbar(sc)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
plt.show()

print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




plt.rcParams["font.family"] = ["Microsoft JhengHei"]

