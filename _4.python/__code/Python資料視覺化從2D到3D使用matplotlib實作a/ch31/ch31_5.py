# ch31_5.py
import matplotlib.pyplot as plt
import numpy as np

# 定義 xpos, ypos, zpos 座標位置
x = list(range(1,6))
y = list(range(1,6))
xx, yy = np.meshgrid(x, y)
xpos = xx.ravel()
ypos = yy.ravel()
zpos = np.zeros(len(x)*len(y))
# 定義長條
dx = np.ones(len(x)*len(y)) * 0.6
dy = np.ones(len(x)*len(y)) * 0.6
z = np.linspace(1,3,25).reshape(len(x),len(y))
dz = z.ravel()
# 定義顏色
color = ["yellow","aqua","lightgreen","orange","blue"]
color_list = []
for i in range(len(x)):
    c = color[i]
    color_list.append([c] * len(y))
colors = np.asarray(color_list)
barcolors = colors.ravel()
# 建立 3D 軸物件
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
# 繪製 3D 長條圖
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=barcolors)  
# 顯示座標軸
ax.set_xlabel('X', color='b')
ax.set_ylabel('Y', color='b')
ax.set_zlabel('Z', color='b')
plt.show()














