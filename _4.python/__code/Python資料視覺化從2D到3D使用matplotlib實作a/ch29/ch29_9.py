# ch29_9.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10)
# 第 A 組資料
x1 = np.random.randn(100)
y1 = np.random.randn(100)
z1 = np.random.randn(100)
# 第 B 組資料
x2 = np.random.randn(100)
y2 = np.random.randn(100)
z2 = np.random.randn(100)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# 繪製散點圖
ax.scatter(x1,y1,z1,c=z1,cmap='Oranges',marker='d',label='A 資料組')
ax.scatter(x2,y2,z2,c=z2,cmap='Blues',marker='*',label='B 資料組')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.legend()                                 # 建立圖例
plt.show()




