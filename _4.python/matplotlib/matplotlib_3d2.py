"""



"""

# 3D plot 集合 2

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

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小             解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(num = '3D繪圖 集合 1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#XXXXXXX1
ax = fig.add_subplot(231, projection='3d')  #第一張圖

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))

x = np.arange(-10, 11, 1)   # -10 .... 10
y = np.arange(-10, 11, 1)   # -10 .... 10
X, Y = np.meshgrid(x, y)

Z = np.add(np.power(X, 2), np.power(Y, 2))
surf = ax.plot_surface(X, Y, Z, cmap = cm.gist_rainbow)
fig.colorbar(surf, shrink = 0.5, aspect = 5)

ax.set_title('XXXXXXX1')

#XXXXXXX2
ax = fig.add_subplot(232, projection='3d')  #第二張圖

π = np.pi
θ = np.linspace(-5*π, 5*π, 200)

x = np.cos(θ)
y = np.sin(θ)
z = θ/(5*π)

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))
plt.plot(x, y, z)
ax.set_title('3D 畫圖')

#XXXXXXX3
ax = fig.add_subplot(233, projection='3d')  #第三張圖

x = np.random.randn(100)
y = np.random.randn(100)
z = np.random.randn(100)

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))
ax.scatter(x, y, z, c='r')

ax.set_title('XXXXXXX3')

#XXXXXXX4
ax = fig.add_subplot(234, projection='3d')  #第四張圖

#曲面 contour

x = y  = np.linspace(-3, 3, 300)
X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X**2 + Y**2))

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))
ax.plot_surface(X, Y, Z)

ax.set_title('曲面 surface')

#XXXXXXX5
ax = fig.add_subplot(235, projection='3d')  #第五張圖

#曲面 contour
plt.contour(X, Y, Z)
ax.set_title('曲面 contour')

#XXXXXXX6
ax = fig.add_subplot(236, projection='3d')  #第六張圖

#曲面 contourf
plt.contourf(X, Y, Z)
ax.set_title('曲面 contourf')


plt.show()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小             解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(num = '3D繪圖 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#XXXXXXX1
ax = fig.add_subplot(231, projection='3d')  #第一張圖

t = np.linspace(-2 * np.pi, 2 * np.pi)      
x, y = np.meshgrid(t, t)                
z = np.sin(np.sqrt(x ** 2 + y ** 2))        
ax.plot_surface(x, y, z)   #畫出三軸資料所構成的曲面
plt.tight_layout()

ax.set_title('XXXXXXX1')

#繪製曲面 – plot_surface()
ax = fig.add_subplot(232, projection='3d')  #第二張圖

t = np.linspace(-5, 5, num=50)  
x, y = np.meshgrid(t, t)            
z = x * y                       

ax.plot_surface(x, y, z)

ax.set_title('繪製曲面')

#給曲面套上顏色

ax = fig.add_subplot(233, projection='3d')  #第三張圖

t = np.linspace(-5, 5)
x, y = np.meshgrid(t, t)
z = x * y

ax.plot_surface(x, y, z, cmap='viridis') 
ax.set_title('給曲面套上顏色')

#繪製 3D 長條圖
ax = fig.add_subplot(234, projection='3d')  #第四張圖

#plt.rcParams['font.size'] = 16

#fig = plt.figure(figsize=(12, 8))

xpos = np.arange(10)        
ypos = np.arange(10)        
zpos = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)                
dz = np.arange(10) + 1

ax.bar3d(xpos, ypos, zpos, dx, dy, dz)      

ax.set_title('繪製 3D 長條圖')


#繪製 3D 散佈圖 – scatter3D()

ax = fig.add_subplot(235, projection='3d')  #第五張圖

plt.rcParams['font.size'] = 16
x = np.random.randn(1000)       
y = np.random.randn(1000)       
z = np.random.randn(1000)       

ax.scatter3D(x, y, z)

ax.set_title('繪製 3D 散佈圖 – scatter3D()')

#XXXXXXX6
ax = fig.add_subplot(236, projection='3d')  #第六張圖

x = np.linspace(0, 5, 10)
y = np.linspace(0, 5, 10)
X, Y = np.meshgrid(x, y)

Z = 2*X + Y
#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))
ax.scatter(X, Y, Z+0.7*np.random.randn(10,10))
ax.plot_surface(X, Y, Z, alpha=0.3)

ax.set_title('XXXXXXX6')

plt.show()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小             解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(num = '3D繪圖 集合 3', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#XXXXXXX1
ax = fig.add_subplot(231, projection='3d')  #第一張圖

#圓環與直線

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))

#ax.set_aspect("equal")

# draw ring
p = np.mgrid[0:2.*np.pi:20j]
x = 3.*np.cos(p)*np.sin(np.pi/6.)
y = 3.*np.sin(p)*np.sin(np.pi/6.)
z = 3.*np.cos(np.pi/6.)
ax.plot(x, y, z, color="r")
ax.plot(p/3., p/3., p/3., color="b")
#plt.savefig("matplot-3D-1.png")

ax.set_title('XXXXXXX1')

#XXXXXXX2
ax = fig.add_subplot(232, projection='3d')  #第二張圖

#三維球

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))

#ax.set_aspect("equal")

# draw sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="r")

# draw a point
xs=np.array([0,0,0,1])
ys=np.array([0,0,1,1])
zs=np.array([0,1,1,1])
ax.scatter(xs,ys,zs,color="y", s=100)

# draw a vector
ax.quiver(0,0,1,1,1,0,color='k')
ax.quiver(0,0,0,1,1,1,color='b',arrow_length_ratio = 0.1)

ax.set_xlabel('x', fontsize=15)
ax.set_ylabel('y', fontsize=15)
ax.set_zlabel('z', fontsize=15)

#plt.savefig('3D-sphere.png')

ax.set_title('三維球')

ax = fig.add_subplot(233, projection='3d')  #第三張圖

#3D quiver  3維向量

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))
#ax.set_aspect("equal")

v1=np.array([2,0,0])
v2=np.array([0,4,0])
v3=np.array([0,0,3])
v12=v1+v2
v123=v1+v2+v3
print('v12=',v12)
print('v123=',v123)
print('|v123|=',np.linalg.norm(v123))
phi=np.arctan(3/np.linalg.norm(v123))
print('phi=',phi,np.degrees(phi))
#ax.grid(True)
ax.quiver(-4,0,0,8,0,0,color='g',arrow_length_ratio = 0.05)
ax.quiver(0,-4,0,0,8,0,color='g',arrow_length_ratio = 0.05)
ax.quiver(0,0,-4,0,0,8,color='g',arrow_length_ratio = 0.05)
ax.scatter(0,0,0,'o')
ax.scatter(v1[0],v1[1],v1[2],'o')
ax.scatter(v1[0]+v2[0],v1[1]+v2[1],v1[2]+v2[2],'o')
ax.scatter(v1[0]+v2[0]+v3[0],v1[1]+v2[1]+v3[1],v1[2]+v2[2]+v3[2],'o')
ax.quiver(0,0,0,v1[0],v1[1],v1[2],color='b')
ax.quiver(v1[0],v1[1],v1[2],v2[0],v2[1],v2[2],color='b')
ax.quiver(v12[0],v12[1],v12[2],v3[0],v3[1],v3[2],color='b')
ax.quiver(0,0,0,v12[0],v12[1],v12[2],color='r',arrow_length_ratio = 0.1)
ax.quiver(0,0,0,v123[0],v123[1],v123[2],color='r',arrow_length_ratio = 0.1)
#plt.savefig("3-vectors.png")

ax.set_title('#3D quiver  3維向量')


ax = fig.add_subplot(234, projection='3d')  #第四張圖

#正交曲線座標系統
#球座標當中的三個曲面交出三條曲線，這三個曲線形成了廣義的正交曲線座標系統(generalized orthonormal curved coordinates)

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))

#ax.set_aspect("equal")

# draw 3 surfaces
r=1.        #r=constant
f,t= np.mgrid[0:2*np.pi:40j, 0:np.pi/2:40j]
x = r*np.cos(f)*np.sin(t)
y = r*np.sin(f)*np.sin(t)
z = r*np.cos(t)
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_zlim(0,2)
ax.plot_surface(x,y,z, alpha=0.5, color='r')

t=np.pi/4.  #theta=constant
r,f=np.mgrid[0:1.5:40j, 0:2.*np.pi:40j]
x=r*np.sin(t)*np.cos(f)
y=r*np.sin(t)*np.sin(f)
z=r*np.cos(t)
ax.plot_surface(x,y,z, alpha=0.3, color='g')

f=np.pi/4.  #phi=constant
r,t=np.mgrid[0:1.2:40j, 0:np.pi/2.:40j]
x=r*np.sin(t)*np.cos(f)
y=r*np.sin(t)*np.sin(f)
z=r*np.cos(t)
ax.plot_surface(x,y,z, alpha=0.5, color='b')

# intersection curves
t=np.pi/4.
f=np.pi/4.
r=np.linspace(0,1.2,40)
x=r*np.sin(t)*np.cos(f)
y=r*np.sin(t)*np.sin(f)
z=r*np.cos(t)
ax.plot(x, y, z, color="k", lw=4)

r=1.
t=np.pi/4.
f=np.linspace(0,2.*np.pi,40)
x=r*np.sin(t)*np.cos(f)
y=r*np.sin(t)*np.sin(f)
z=r*np.cos(t)
ax.plot(x, y, z, color="k", lw=4)

r=1.
f=np.pi/4.
t=np.linspace(0,np.pi/2,40)
x=r*np.sin(t)*np.cos(f)
y=r*np.sin(t)*np.sin(f)
z=r*np.cos(t)
ax.plot(x, y, z, color="k", lw=4)

ax.set_title(r"3 surfaces $r=1, \theta=\pi/4, \phi=\pi/4$" \
            " meet in 3 curves", fontsize=15)
ax.set_xlabel('x', fontsize=15)
ax.set_ylabel('y', fontsize=15)
ax.set_zlabel('z', fontsize=15)
#plt.savefig("3-surfaces-spherical-intersec-curves.png")


ax.set_title('正交曲線座標系統')


ax = fig.add_subplot(235, projection='3d')  #第五張圖

#三維等位面與法線

#ax = fig.gca(projection='3d') old
#ax = fig.add_axes(Axes3D(fig))

x=np.linspace(2.,5.,10)
y=np.linspace(2.,5.,10)
X,Y=np.meshgrid(x,y)
Z=np.sqrt(X**2+Y**2)
Z2=np.sqrt(X**2+Y**2-2.)
Z3=np.sqrt(X**2+Y**2-3.)
ax.scatter([3], [4], [5], color="k", s=40)

#ax.set_aspect("equal")

ax.plot_surface(X, Y, Z, label='C=0')
ax.plot_surface(X, Y, Z2, label='C=6')
ax.plot_surface(X, Y, Z3, label='C=12')
ax.quiver(3.,4.,5.,6./5.,8./5.,-10./5.,color='b')
ax.set_title("$f(x,y,z)=x^2+y^2-z=C$", fontsize=15)
#ax.plot_surface(X, Y, Z)

ax.set_xlabel('x', fontsize=15)
ax.set_ylabel('y', fontsize=15)
ax.set_zlabel('z', fontsize=15)
#ax.legend()

ax.set_title('三維等位面與法線')

#XXXXXXX6
ax = fig.add_subplot(236, projection='3d')  #第六張圖

#1. 首先在進行 3D Plot 時除了導入 matplotlib ，還要額外添加一個模塊，即 Axes 3D 3D 坐標軸顯示：

#import matplotlib
#matplotlib.use("Agg")

#2. 接下來給進 X 和 Y 值，並將 X 和 Y 編織成柵格。每一個（X, Y）點對應的高度值我們用下面這個函數來計算。使用ax.plot_surface繪出網格表面圖形，並將一個 colormap rainbow 填充顏色。

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=plt.get_cmap('rainbow'))

#3.將三維圖像投影到 XY 平面上做一個等高線圖。

ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))

#其中，rstride 和 cstride 分別代表 row 和 column 的跨度。 可比較兩個圖分別是跨度為1 和 5 的效果。 

#3D基本操作
#import matplotlib
#matplotlib.use("Agg")

#fig = plt.figure()

#ax = Axes3D(fig)
# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=plt.get_cmap('rainbow'))
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
#plt.savefig("mat-3D-mv1.png")


ax.set_title('XXXXXXX6')

plt.show()


sys.exit()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小             解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(num = '3D繪圖 集合 4', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#XXXXXXX1
ax = fig.add_subplot(231, projection='3d')  #第一張圖




ax.set_title('XXXXXXX1')

#XXXXXXX2
ax = fig.add_subplot(232, projection='3d')  #第二張圖



ax.set_title('XXXXXXX2')

#XXXXXXX3
ax = fig.add_subplot(233, projection='3d')  #第三張圖


ax.set_title('XXXXXXX3')

#XXXXXXX4
ax = fig.add_subplot(234, projection='3d')  #第四張圖


ax.set_title('XXXXXXX4')


#XXXXXXX5
ax = fig.add_subplot(235, projection='3d')  #第五張圖


ax.set_title('XXXXXXX5')

#XXXXXXX6
ax = fig.add_subplot(236, projection='3d')  #第六張圖



ax.set_title('XXXXXXX6')

plt.show()


print('------------------------------------------------------------')	#60個

#          編號                          圖像大小             解析度    背景色                      邊框顏色                      邊框有無
fig = plt.figure(num = '3D繪圖 集合 5', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#XXXXXXX1
ax = fig.add_subplot(231, projection='3d')  #第一張圖




ax.set_title('XXXXXXX1')

#XXXXXXX2
ax = fig.add_subplot(232, projection='3d')  #第二張圖



ax.set_title('XXXXXXX2')

#XXXXXXX3
ax = fig.add_subplot(233, projection='3d')  #第三張圖


ax.set_title('XXXXXXX3')

#XXXXXXX4
ax = fig.add_subplot(234, projection='3d')  #第四張圖


ax.set_title('XXXXXXX4')


#XXXXXXX5
ax = fig.add_subplot(235, projection='3d')  #第五張圖


ax.set_title('XXXXXXX5')

#XXXXXXX6
ax = fig.add_subplot(236, projection='3d')  #第六張圖



ax.set_title('XXXXXXX6')

plt.show()

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


