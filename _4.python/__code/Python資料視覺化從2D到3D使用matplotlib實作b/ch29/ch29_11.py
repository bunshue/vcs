# ch29_11.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
N = 150
# 建立折線用的 3D 座標資料
z = np.linspace(0, 20, N)
x1 = np.cos(z)
y1 = np.sin(z)
# 繪製 3D 折線
ax.plot(x1, y1, z, color='m', label='plot')

# 建立散點用的 3D 座標資料, z 則沿用
x2 = np.cos(z) + np.random.randn(N) * 0.1
y2 = np.sin(z) + np.random.randn(N) * 0.1
# 繪製 3D 散點
ax.scatter(x2,y2,z,c=z,cmap='hsv',label='scatter')

ax.legend()
plt.show()




