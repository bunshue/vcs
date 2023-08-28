# ch30_12.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
# 建立數據
N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)
c = np.random.rand(N, N)
Z = 10 * np.exp(-(0.5*X**2+0.5*Y**2))
# 繪製 3D 框線圖
ax.plot_wireframe(X,Y,Z,rstride=5,cstride=5,color='g')
# 數據投影到 X, Y, Z 平面, 同時設定偏移將數據投影到牆面
cset = ax.contourf(X,Y,Z,zdir='z',offset=-10,cmap='cool')
cset = ax.contourf(X,Y,Z,zdir='x',offset=-10,cmap='cool')
cset = ax.contourf(X,Y,Z,zdir='y',offset=10,cmap='cool')
# 建立顯示區間和設定座標軸名稱
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-10, 10)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
plt.show()



