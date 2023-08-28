# ch31_7.py
import matplotlib.pyplot as plt
import numpy as np

# 建立影像和 3D 軸物件
fig = plt.figure()
ax = fig.gca(projection = '3d')
# 建立 x, y, z
_x = np.linspace(0, 10, 10)
_y = np.linspace(1, 10, 3)
_xx, _yy = np.meshgrid(_x, _y)
_zz = np.exp(-_xx * (1. / _yy))
x = _xx.flatten()
y = _yy.flatten()
z = np.zeros(_zz.size)
# 建立 dx, dy, dz, 也就是定義長條
dx = .25 * np.ones(_zz.size)
dy = .25 * np.ones(_zz.size)
dz = _zz.flatten()
# 定義顏色
color = ["yellow","aqua","lightgreen"]
color_list = []
for i in range(len(_y)):
    c = color[i]
    color_list.append([c] * len(_x))
colors = np.asarray(color_list)
barcolors = colors.ravel()
# 建立 3D 長條圖
ax.bar3d(x, y, z, dx, dy, dz, color=barcolors, alpha=0.5)
# 顯示座標軸
ax.set_xlabel('x',color='b')
ax.set_ylabel('y',color='b')
ax.set_zlabel('z',color='b')
plt.show()














