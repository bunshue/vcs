# ch31_3.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 定義長條的位置
xpos = [1,2,3,4,5,6,7,8,9,10]
ypos = [1,2,3,4,5,6,7,8,9,10]
zpos = [0,0,0,0,0,0,0,0,0,0]
# 定自長條的外形
dx = np.ones(10)                # 寬度
dy = np.ones(10) * 0.5          # 深度
dz = [1,2,3,4,5,6,7,8,9,10]     # 高度
ax.bar3d(xpos, ypos, zpos, dx, dy, dz,
         color='lightgreen',
         edgecolor='black')
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
plt.show()
















