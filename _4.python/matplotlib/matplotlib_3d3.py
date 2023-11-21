"""

新進暫存

"""

# 3D plot 集合 3

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

fig = plt.figure(num = '3D繪圖 集合 2 散點圖', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

"""
ax = fig.add_subplot(111, projection='3d')  #第一張圖

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))
ax.scatter(x, y, z, c='r')
"""

# 3D surface plot
ax = fig.add_subplot(111, projection='3d')  #第一張圖

R = 5
x = np.arange(-R, R + 1, 0.5)
y = np.arange(-R, R + 1, 0.5)

print(x)
print(y)
X, Y = np.meshgrid(x, y)
#Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2
Z = R * R - np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

surf = ax.plot_wireframe(X, Y, Z)   #畫線框圖
ax.scatter(X, Y, Z, c='r')

#ax.set_title('線框圖111')

plt.show()

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt

start = 0
end = np.pi * 20   
step = np.pi / 180

x = np.arange(start, end, step)
y = np.sin(x)
z = np.cos(x) 

# 取得 mpl_toolkits.mplot3d.axes3d.Axes3D 實例
ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot(x, y, z)
plt.title('Axes3D Plot')

plt.show()

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
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

ax = plt.axes(projection='3d')

#ax.plot_surface(X, Y, Z)   不分層著色
ax.plot_surface(X, Y, Z, cmap = cm.coolwarm)    #分層著色
#ax.plot_wireframe(X, Y, Z)  #畫線框圖

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_box_aspect((1, 1, 0.5))  #調整各軸顯示比例
plt.title('Axes3D Plot Surface')

plt.show()

print('------------------------------------------------------------')	#60個

"""
3D表面（彩色地图）
演示如何绘制使用CoolWarm颜色映射着色的3D曲面。使用“抗锯齿=假”使表面不透明。
还演示了使用线性定位器和Z轴刻度标签的自定义格式。
"""

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

print('------------------------------------------------------------')	#60個

#線框圖

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
X, Y, Z = axes3d.get_test_data(0.05)

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()

sys.exit()

print('------------------------------------------------------------')	#60個

from math import floor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def blending(t):
    return 6 * (t ** 5) - 15 * (t ** 4) + 10 * (t ** 3)

def lerp(g1, g2, t):
    return g1 + t * (g2 - g1)

def grad2(hashvalue, dx, dy):
    return [dy, dx + dy, dx, dx - dy, -dy, -dx - dy, -dx, -dx + dy][hashvalue % 8];

rand_table = np.random.randint(255, size = 256).tolist()
def _perlin2(x, y):
    xi = floor(x)
    yi = floor(y)

    aa = rand_table[
        (rand_table[xi % 256] + yi) % 256
    ]
    ba = rand_table[
        (rand_table[(xi + 1) % 256] + yi) % 256
    ]
    ab = rand_table[
        (rand_table[xi % 256] + yi + 1) % 256
    ]
    bb = rand_table[
        (rand_table[(xi + 1) % 256] + yi + 1) % 256
    ]

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

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap = cm.gist_earth) # 用地形高度顏色來著色
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_box_aspect((1, 1, 25 / width))
plt.title('Perlin noise')
plt.show()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



