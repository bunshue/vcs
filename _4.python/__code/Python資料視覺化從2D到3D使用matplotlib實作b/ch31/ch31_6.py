# ch31_6.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 建立影像和 3D 軸物件
fig = plt.figure(figsize=(8,3))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
# 建立 x, y, z
_x = np.arange(3)
_y = np.arange(6)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
z = np.zeros(len(_x) * len(_y))
# 建立 dx, dy, dz
dx = np.ones(len(x))
dy = dx
dz = x + y
# 建立 3D 長條圖
ax1.bar3d(x,y,z,dx,dy,dz,shade=True,edgecolor='w',color='g')
ax1.set_title('含陰影',fontsize=16,color='m')
ax1.set_xlabel('X',color='b')
ax1.set_ylabel('Y',color='b')
ax1.set_zlabel('Z',color='b')
ax2.bar3d(x,y,z,dx,dy,dz,shade=False,edgecolor='w',color='g')
ax2.set_title('不含陰影',fontsize=16,color='m')
ax2.set_xlabel('X',color='b')
ax2.set_ylabel('Y',color='b')
ax2.set_zlabel('Z',color='b')
plt.show()














