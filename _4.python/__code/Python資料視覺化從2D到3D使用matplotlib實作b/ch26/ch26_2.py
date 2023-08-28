# ch26_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(-3, 3) 
y = np.arange(-3, 3) 
X, Y = np.meshgrid(x, y)                # 建立 X, Y
U = -1 + X**2 - Y                       # 定義速度 U
V = 1 - X + Y**2                        # 定義速度 V
plt.streamplot(X, Y, U, V, density = 1) 
plt.title("流線圖",fontsize=14,color='b')
plt.show()

