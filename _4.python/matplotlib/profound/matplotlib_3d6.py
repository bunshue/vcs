"""
第31章：3D 長條圖

"""
# ch31_1.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

np.random.seed(10)              # 隨機數種子值

colors = ['m', 'r', 'g', 'b']   # 不同平面的顏色
yticks = [3, 2, 1, 0]           # y 座標平面
ax.set_yticks(yticks)           # 設定 y 軸刻度標記
# 依次在 y = 3, 2, 1, 0 平面繪製長條圖
for c, k in zip(colors, yticks):
    left = np.arange(12)        # 建立 x 軸座標 
    height = np.random.rand(12) # 建立長條高度
    ax.bar(left, height, zs=k, zdir='y', color=c, alpha=0.8) 
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
plt.show()







#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch31\ch31_2.py

# ch31_2.py
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
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='m',alpha=0.8)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
plt.show()

















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch31\ch31_3.py

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

















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch31\ch31_4.py

# ch31_4.py
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
         edgecolor='black',shade=False)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
plt.show()

















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch31\ch31_5.py

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















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch31\ch31_6.py

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















print("------------------------------------------------------------")  # 60個











