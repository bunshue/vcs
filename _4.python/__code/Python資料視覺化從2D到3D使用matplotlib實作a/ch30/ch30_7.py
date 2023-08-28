# ch30_7.py
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)
# 用 3D 線框繪製曲線表面
ax.plot_wireframe(X, Y, Z, cstride=5, rstride=5, color='g')
plt.show()




