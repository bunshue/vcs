'''
參考 使用Matplotlib绘制3D图形
https://paul.pub/matplotlib-3d-plotting/

參考 Python 使用 Matplotlib 繪製 3D 資料圖形教學與範例
https://officeguide.cc/python-matplotlib-three-dimensional-plotting-tutorial-examples/
'''

# 3D plot 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.collections import PolyCollection
from mpl_toolkits.mplot3d import axes3d
from matplotlib.cm import viridis as colormap

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
fig = plt.figure(num = '3D繪圖 集合 1', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#線形圖
ax = fig.add_subplot(231, projection='3d')  #第一張圖
x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)
z = np.add(x, y)

ax.plot(x, y, z)
ax.set_title('線形圖')

#散點圖
ax = fig.add_subplot(232, projection='3d')  #第二張圖

count = 100
range = 100

xs = np.random.rand(count) * range
ys = np.random.rand(count) * range
zs = np.random.rand(count) * range

ax.scatter(xs, ys, zs, s=zs, c=zs)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_title('散點圖')


#線框圖
ax = fig.add_subplot(233, projection='3d')  #第三張圖

step = 0.04
maxval = 1.0

# Create supporting points in polar coordinates
r = np.linspace(0, 1.2, 50)
p = np.linspace(0, 2*np.pi, 50)
R, P = np.meshgrid(r, p)
# Transform them to cartesian system
X, Y = R*np.cos(P), R*np.sin(P)

Z = ((R**2 - 1)**2)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=colormap)
ax.set_zlim3d(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')
ax.set_title('3D surface plot')




#曲面圖
ax = fig.add_subplot(234, projection='3d')  #第四張圖

# 產生 3D 座標資料
z1 = np.random.randn(50)
x1 = np.random.randn(50)
y1 = np.random.randn(50)
z2 = np.random.randn(50)
x2 = np.random.randn(50)
y2 = np.random.randn(50)

p = np.mgrid[0:2.*np.pi:20j]
x = 3.*np.cos(p)*np.sin(np.pi/6.)
y = 3.*np.sin(p)*np.sin(np.pi/6.)
z = 3.*np.cos(np.pi/6.)
ax.plot(x, y, z, color="r")
ax.plot(p/3., p/3., p/3., color="b")
#plt.savefig("matplot-3D-1.png")
print ('plot is done')

ax.set_title('XXXXXXX2')


#等高線
ax = fig.add_subplot(235, projection='3d')  #第五張圖


#柱狀圖
ax = fig.add_subplot(236, projection='3d')  #第六張圖

np.random.seed(59)
month = np.arange(1, 12)
years = [2016, 2017, 2018, 2019]

def get_color(value_array):
    color = []
    for v in value_array:
        if (v < 50):
            color.append('y')
        elif (v < 100):
            color.append('g')
        elif (v < 150):
            color.append('b')
        elif (v < 200):
            color.append('c')
        elif (v < 250):
            color.append('m')
        else:
            color.append('r')
    return color

for year, c in zip(years, ['b','c','r','m']):
    value = np.random.rand(len(month)) * 300
    ax.bar(month, value, year, zdir='y', color=get_color(value), alpha=0.7)
    for i in np.arange(0, 12):
        ax.bar

ax.set_xlabel('Month')
ax.set_xticks(np.arange(1, 13))
ax.set_ylabel('Year')
ax.set_yticks(np.arange(2016, 2020))
ax.set_zlabel('Precipitation')
ax.set_title('柱狀圖')


plt.show()


#plt.figure(figsize=(8,8))	#設定圖片視窗大小
fig = plt.figure(num = '3D繪圖 集合 2', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示


#多邊形
ax = fig.add_subplot(231, projection='3d')  #第一張圖

np.random.seed(59)
month = np.arange(0, 13)
years = [2016, 2017, 2018, 2019]

precipitation = []
for year in years:
    value = np.random.rand(len(month)) * 300
    value[0], value[-1] = 0, 0
    precipitation.append(list(zip(month, value)))

poly = PolyCollection(precipitation, facecolors=['b','c','r','m'])
poly.set_alpha(0.7)

ax.add_collection3d(poly, zs=years, zdir='y')
ax.set_xlabel('Month')
ax.set_xlim3d(0, 12)
ax.set_ylabel('Year')
ax.set_ylim3d(2015, 2020)
ax.set_zlabel('Precipitation')
ax.set_zlim3d(0, 300)
ax.set_title('多邊形')


#3D 座標點
#在三維空間中繪製座標點是最常用到的基本功能。
ax = fig.add_subplot(232, projection='3d')  #第二張圖

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

ax.legend() # 顯示圖例

ax.set_title('3D 座標點')

#3D 曲線
#這是將 3D 的曲線與座標點畫在同一張圖的範例。
ax = fig.add_subplot(233, projection='3d')  #第三張圖

# 產生 3D 座標資料
z = np.linspace(0, 15, 100)
x = np.sin(z)
y = np.cos(z)

# 繪製 3D 曲線
ax.plot(x, y, z, color='gray', label='My Curve')

# 產生 3D 座標資料
x2 = np.sin(z) + 0.1 * np.random.randn(100)
y2 = np.cos(z) + 0.1 * np.random.randn(100)

# 繪製 3D 座標點
ax.scatter(x2, y2, z, c=z, cmap='jet', label='My Points')

ax.legend() # 顯示圖例

ax.set_title('3D 曲線')

#Wireframe 圖形
#這是 3D 的 wireframe 網格圖形範例。
ax = fig.add_subplot(234, projection='3d')  #第四張圖

# 產生測試資料
X, Y, Z = axes3d.get_test_data(0.05)

# 繪製 Wireframe 圖形
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax.set_title('Wireframe 圖形')

#3D 曲面
#這是繪製 3D 曲面的範例。
ax = fig.add_subplot(235, projection='3d')  #第五張圖

# 產生測試資料
X, Y, Z = axes3d.get_test_data(0.05)    #這一個不知道是什麼函數

# 繪製 3D 曲面圖形
ax.plot_surface(X, Y, Z, cmap='seismic')

ax.set_title('3D 曲面')


#3D 向量場
#這是繪製 3D 向量場（vector field）的範例。
ax = fig.add_subplot(236, projection='3d')  #第六張圖

# 產生格點資料
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))

# 產生向量場資料
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))

# 繪製向量場
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)

ax.set_title('3D 向量場')


plt.show()


#plt.figure(figsize=(8,8))	#設定圖片視窗大小
fig = plt.figure(num = '3D繪圖 集合 3', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示


# 3D surface plot
ax = fig.add_subplot(231, projection='3d')  #第一張圖

#111
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

surf = ax.plot_wireframe(X, Y, Z)
ax.set_title('線框圖111')


#曲面圖
ax = fig.add_subplot(232, projection='3d')  #第二張圖

#444
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

surf = ax.plot_surface(X, Y, Z, cmap = cm.hsv)
#surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_rainbow)
#fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title('曲面圖')


#XXXXXXX3
ax = fig.add_subplot(233, projection='3d')  #第三張圖

#333
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

ax.plot_wireframe(X, Y, Z, alpha=0.1)
ax.contour(X, Y, Z, cmap=cm.Accent, linewidths=2)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title('等高線333')



#XXXXXXX4
ax = fig.add_subplot(234, projection='3d')  #第四張圖

X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)

#R = np.sqrt(X**2 + Y**2)
#R = np.sqrt(X**2 + Y**2)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2
#Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)


#XXXXXXX5
ax = fig.add_subplot(235, projection='3d')  #第五張圖


x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
#Z = (1.0 - X)**2 + 100.0 * (Y - X*X)**2
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)

ax.set_title('XXXXXXX5')

#XXXXXXX6
ax = fig.add_subplot(236, projection='3d')  #第六張圖

#
#
#
#ax.set_title('XXXXXXX6')


plt.show()







'''
#製作動圖
for angle in np.arange(95, 180, 12):
    ax.set_zlabel("Angle: " + str(angle))
    ax.view_init(30, angle)
    filename = "./" + str(angle) + ".png"
    plt.savefig(filename)
    print("Save " + filename + " finish")
'''

