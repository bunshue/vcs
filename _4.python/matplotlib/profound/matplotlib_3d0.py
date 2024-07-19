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









print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

