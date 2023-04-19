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

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
fig = plt.figure(num = '3D繪圖 集合 1', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#XXXXXXX1
ax = fig.add_subplot(231, projection='3d')  #第一張圖

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)

X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)

ax.set_title('XXXXXXX1')



#XXXXXXX2
ax = fig.add_subplot(232, projection='3d')  #第二張圖


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


#XXXXXXX3
ax = fig.add_subplot(233, projection='3d')  #第三張圖

s = 0.05
x = np.arange(-2.0, 2.0 + s, s)
y = np.arange(-1.0, 3.0 + s, s)
X, Y = np.meshgrid(x, y)
Z = (1.0 - X)**2 + 100.0 * (Y - X*X)**2

#??? plot

ax.set_title('XXXXXXX3')

#XXXXXXX4
ax = fig.add_subplot(234, projection='3d')  #第四張圖

#
#
#
ax.set_title('XXXXXXX4')

#XXXXXXX5
ax = fig.add_subplot(235, projection='3d')  #第五張圖

#
#
#
ax.set_title('XXXXXXX5')

#XXXXXXX6
ax = fig.add_subplot(236, projection='3d')  #第六張圖

#
#
#
ax.set_title('XXXXXXX6')


plt.show()




