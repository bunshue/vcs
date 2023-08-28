# ch26_1.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
x = np.arange(0, 5) 
y = np.arange(0, 5) 
X, Y = np.meshgrid(x, y)                # 建立 X, Y
U = np.ones((5,5))                      # 建立 U
V = np.zeros((5,5))                     # 建立 V
plt.streamplot(X, Y, U, V, density=0.5)
plt.title("流線圖",fontsize=14,color='b')
plt.show()

