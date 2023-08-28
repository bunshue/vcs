# ch25_11.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(-2, 2.2, 0.2) 
y = np.arange(-2, 2.2, 0.2) 
X, Y = np.meshgrid(x, y)                    # 建立 X, Y
Z = X**2 + Y**2
U, V = np.gradient(Z)                       # 建立 U, V
C = U + V                                   # 定義箭頭顏色的數據
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V, C, cmap='hsv')        # 繪製預設的彩色箭袋
ax.set_title("箭袋 Quiver, cmap='hsv'",fontsize=14,color='b')
ax.set_aspect('equal')
plt.show()

