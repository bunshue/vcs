# ch30_1.py
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)
# 繪製曲線表面
ax.plot_surface(X, Y, Z, cmap="bwr")
ax.set_xlabel('X',color='b')
ax.set_ylabel('Y',color='b')
ax.set_zlabel('Z',color='b')
ax.set_title('繪製曲線表面',fontsize=14,color='b')
plt.show()




