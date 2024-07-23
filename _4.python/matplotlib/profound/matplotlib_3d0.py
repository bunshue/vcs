"""
3D plot 集合 0

3D 畫圖基本

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

from mpl_toolkits.mplot3d import axes3d

print("------------------------------------------------------------")  # 60個

x = np.array([1,2,3,4,5])
y = np.array([6,7,8])

#x軸1~5, y軸6~8, 編織出來15個點 xx, yy
xx, yy = np.meshgrid(x,y)

print('xx = \n', xx)
print('yy = \n', yy)

plt.scatter(xx,yy,marker='o',c='m')

plt.title("畫出 meshgrid")

plt.show()

print("------------------------------------------------------------")  # 60個

# 建立影像和 3D 軸物件
fig = plt.figure()

ax = fig.add_subplot(111, projection="3d")

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x, y)
Z = np.add(np.power(X, 2), np.power(Y, 2))  # Z = X^2 + Y^2

surf = ax.plot_wireframe(X, Y, Z)
ax.set_title("線框圖")

plt.show()

"""

ax = plt.figure()
ax.add_subplot(projection='3d')

ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
ax.set_title('繪製曲線表面',fontsize=14,color='b')
ax.set_title('wireframe( )函數的實例',fontsize=16,color='b');

"""



print("------------------------------------------------------------")  # 60個

import cv2

"""
from mpl_toolkits import mplot3d

"""

filename = 'mola_1024x512_200mp.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/_material/ims3.bmp'

IMG_GRAY = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.title('使用 matplotlib 顯示圖片, 需先BGR轉RGB')
plt.imshow(cv2.cvtColor(IMG_GRAY, cv2.COLOR_BGR2RGB))
plt.show()

print('image.shape內容 :', IMG_GRAY.shape)

H, W = IMG_GRAY.shape

x = np.linspace(W - 1, 0, W)
y = np.linspace(0, H - 1, H)

X, Y = np.meshgrid(x, y)
Z = IMG_GRAY[0 : H, 0 : W]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='gist_earth')  # 150為剖面採樣數
ax.auto_scale_xyz([W - 1, 0], [0, H - 1], [0, 300])
plt.show()

print("------------------------------------------------------------")  # 60個




from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 8))

ax = fig.add_subplot(111, projection="3d")

# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
# height value
Z = np.sin(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap("rainbow"))
"""
============= ================================================
        Argument      Description
        ============= ================================================
        *X*, *Y*, *Z* Data values as 2D arrays
        *rstride*     Array row stride (step size), defaults to 10
        *cstride*     Array column stride (step size), defaults to 10
        *color*       Color of the surface patches
        *cmap*        A colormap for the surface patches.
        *facecolors*  Face colors for the individual patches
        *norm*        An instance of Normalize to map values to colors
        *vmin*        Minimum value to map
        *vmax*        Maximum value to map
        *shade*       Whether to shade the facecolors
        ============= ================================================
"""

# I think this is different from plt12_contours
ax.contourf(X, Y, Z, zdir="z", offset=-2, cmap=plt.get_cmap("rainbow"))
"""
==========  ================================================
        Argument    Description
        ==========  ================================================
        *X*, *Y*,   Data values as numpy.arrays
        *Z*
        *zdir*      The direction to use: x, y or z (default)
        *offset*    If specified plot a projection of the filled contour
                    on this position in plane normal to zdir
        ==========  ================================================
"""

ax.set_zlim(-2, 2)

plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


import matplotlib.pyplot as plt
import numpy as np

def f1(x, y):                                # 左邊曲面函數
    return (np.power(x,2) + np.power(y, 2))
def f2(x, y):                                # 右邊曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y, 2))
    return (np.sin(r))

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立 XY 座標
# 建立子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
# 左邊子圖乎叫 f1
ax[0].plot_surface(X, Y, f1(X,Y), cmap='hsv')   # 繪製 3D 圖
# 左邊子圖乎叫 f2
ax[1].plot_surface(X, Y, f2(X,Y), cmap='hsv')   # 繪製 3D 圖
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = plt.axes(projection="3d")

# 3D plot

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 3D plot

plt.show()

print("------------------------------------------------------------")  # 60個



