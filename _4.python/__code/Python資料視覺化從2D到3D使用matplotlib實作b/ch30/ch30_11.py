# ch30_11.py
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')
# matplotlib 官方測試數據
X, Y, Z = axes3d.get_test_data(0.05)
# 繪製 3D 框線圖
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5, alpha=0.3)
# 測試數據投影到 X, Y, Z 平面, 同時設定偏移將數據投影到牆面
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='jet')
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='jet')
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='jet')
# 建立顯示區間和設定座標軸名稱
ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-100, 100)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
plt.show()





 




