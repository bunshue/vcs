# ch29_12_1.py
import matplotlib.pyplot as plt
import numpy as np

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
Z = np.exp(-(0.1*X**2+0.1*Y**2))    # 建立 Z 資料
np.random.seed(10)
c = np.random.rand(N, N)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
sc = ax.scatter(X, Y, Z, c=c, marker='o', cmap='hsv')
fig.colorbar(sc)
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
plt.show()



