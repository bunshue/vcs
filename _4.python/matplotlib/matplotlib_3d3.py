# 3D plot 集合 3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個
'''
fig = plt.figure()

ax = fig.add_subplot(111, projection = '3d')

R = 5
x = np.arange(-R, R + 1, 0.5)
y = np.arange(-R, R + 1, 0.5)

print(x)
print(y)
X, Y = np.meshgrid(x, y)
#Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2
Z = R * R - np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

#畫線框圖
surf = ax.plot_wireframe(X, Y, Z)
fig.colorbar(surf, shrink = 0.5, aspect = 5)    #colorbar

#畫散佈圖
ax.scatter(X, Y, Z, c = 'r')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('線框圖 plot_wireframe + scatter')
#plt.title('線框圖 plot_wireframe + scatter')  same

plt.show()

print('------------------------------------------------------------')	#60個

start = 0
end = np.pi * 20   
step = np.pi / 180

x = np.arange(start, end, step)
y = np.sin(x)
z = np.cos(x) 

ax = plt.axes(projection = '3d')
ax.plot(x, y, z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('3D Plot')

plt.show()

print('------------------------------------------------------------')	#60個

#3D曲面

#建立一個figure
fig = plt.figure()
#创建3D轴对象
ax = fig.add_subplot(111, projection = '3d')

X = np.arange(-2, 2, 0.1)
Y = np.arange(-2, 2, 0.1)
#计算3维曲面分格线坐标
X,Y = np.meshgrid(X, Y)

#用于计算X/Y对应的Z值
def f(x,y):
    return (1 - y** 5 + x ** 5) * np.exp(-x ** 2 - y ** 2)
#plot_surface函数可绘制对应的曲面

#ax.plot_surface(X, Y, f(X,Y), rstride = 1, cstride = 1)
#修改曲面顏色, 使用cmap属性可指定曲面颜色
ax.plot_surface(X, Y, f(X, Y), rstride = 1, cstride = 1, cmap = plt.cm.hot)

plt.show()

print('------------------------------------------------------------')	#60個

#3D散点图的绘制使用scatter() 函数来绘制出散点

xs = np.random.randint(30, 40, 100)
ys = np.random.randint(20, 30, 100)
zs = np.random.randint(10, 20, 100)
xs2 = np.random.randint(50, 60, 100)
ys2 = np.random.randint(30, 40, 100)
zs2 = np.random.randint(50, 70, 100)
xs3 = np.random.randint(10, 30, 100)
ys3 = np.random.randint(40, 50, 100)
zs3 = np.random.randint(40, 50, 100)

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(xs, ys, zs)
ax.scatter(xs2, ys2, zs2, c = 'r', marker = '^')
ax.scatter(xs3, ys3, zs3, c = 'g', marker = '*')
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')

plt.show()

print('------------------------------------------------------------')	#60個

from matplotlib import cm

def f(x, y):
    n = np.sqrt(np.power(x, 2) + np.power(y, 2)) / 180 * np.pi
    return np.cos(n) + np.cos(3 * n)

width = 200
step = 10

x = np.arange(-width, width, step)
y = np.arange(-width, width, step)

X, Y = np.meshgrid(x, y) 
Z = f(X, Y)

ax = plt.axes(projection = '3d')

#ax.plot_surface(X, Y, Z)   不分層著色
ax.plot_surface(X, Y, Z, cmap = cm.coolwarm)    #分層著色
#ax.plot_wireframe(X, Y, Z)  #畫線框圖

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_box_aspect((1, 1, 0.5))  #調整各軸顯示比例
plt.title('3D Plot Surface')

plt.show()

print('------------------------------------------------------------')	#60個

"""
3D表面（彩色地图）
演示如何绘制使用CoolWarm颜色映射着色的3D曲面。使用“抗锯齿=假”使表面不透明。
还演示了使用线性定位器和Z轴刻度标签的自定义格式。
"""

from matplotlib import cm
from matplotlib.ticker import LinearLocator

fig, ax = plt.subplots(subplot_kw = {"projection" : "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap = cm.coolwarm, linewidth = 0, antialiased = False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

fig.colorbar(surf, shrink = 0.5, aspect = 5)    #colorbar

plt.show()

print('------------------------------------------------------------')	#60個

# 建立 3D 圖形
fig = plt.figure()
ax = fig.gca(projection='3d')

# 產生 3D 座標資料
z1 = np.random.randn(50)
x1 = np.random.randn(50)
y1 = np.random.randn(50)
z2 = np.random.randn(50)
x2 = np.random.randn(50)
y2 = np.random.randn(50)

# 繪製 3D 座標點
ax.scatter(x1, y1, z1, c=z1, cmap='Reds', marker='^', label='My Points 1')
ax.scatter(x2, y2, z2, c=z2, cmap='Blues', marker='o', label='My Points 2')

ax.legend()

plt.show()

print('------------------------------------------------------------')	#60個
'''
# 線框圖

from mpl_toolkits.mplot3d import axes3d

fig = plt.figure(
    num="3D繪圖 集合 1",
    figsize=(14, 14),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)
# fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# 生成一系列的測試數據
N = 0.05
X, Y, Z = axes3d.get_test_data(N)  # (1/N*6) X (1/N*6)
print(1 / N * 6)
print(X.shape)
print(Y.shape)
print(Z.shape)
# 畫線框圖
# ax.plot_wireframe(X, Y, Z)
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)

# cstride column 每幾點畫一條線 x軸
# rstride row    每幾點畫一條線 y軸

"""
rstride 	Array row stride (step size), defaults to 1
cstride 	Array column stride (step size), defaults to 1
rcount 	Use at most this many rows, defaults to 50
ccount 	Use at most this many columns, defaults to 50
X,Y,Z：輸入資料
rstride:行步長
cstride:列步長
rcount:行數上限
ccount:列數上限
"""

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()

sys.exit()

print("------------------------------------------------------------")  # 60個

from math import floor
from matplotlib import cm


def blending(t):
    return 6 * (t**5) - 15 * (t**4) + 10 * (t**3)


def lerp(g1, g2, t):
    return g1 + t * (g2 - g1)


def grad2(hashvalue, dx, dy):
    return [dy, dx + dy, dx, dx - dy, -dy, -dx - dy, -dx, -dx + dy][hashvalue % 8]


rand_table = np.random.randint(255, size=256).tolist()


def _perlin2(x, y):
    xi = floor(x)
    yi = floor(y)

    aa = rand_table[(rand_table[xi % 256] + yi) % 256]
    ba = rand_table[(rand_table[(xi + 1) % 256] + yi) % 256]
    ab = rand_table[(rand_table[xi % 256] + yi + 1) % 256]
    bb = rand_table[(rand_table[(xi + 1) % 256] + yi + 1) % 256]

    dx = x - xi
    dy = y - yi

    u = blending(dx)
    v = blending(dy)

    g1 = lerp(grad2(aa, dx, dy), grad2(ba, dx - 1, dy), u)
    g2 = lerp(grad2(ab, dx, dy - 1), grad2(bb, dx - 1, dy - 1), u)

    return lerp(g1, g2, v)


_perlin2 = np.frompyfunc(_perlin2, 2, 1)


def perlin2(x, y):
    cx, cy = np.meshgrid(x, y)
    return _perlin2(cx, cy).astype(float)


width = 100
x = np.arange(width)
y = np.arange(width)

X, Y = np.meshgrid(x, y)
Z = perlin2(x / 25, y / 25)

ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, Z, cmap=cm.gist_earth)  # 用地形高度顏色來著色
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_box_aspect((1, 1, 25 / width))
plt.title("Perlin noise")

plt.show()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
