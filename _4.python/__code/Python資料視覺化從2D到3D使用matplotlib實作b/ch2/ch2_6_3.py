# ch2_6_3.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['lines.linewidth'] = 9 # 設定線條寬度
x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.plot(x, y1, zorder=3)           # 繪製sin, zorder是 3
plt.plot(x, y2, zorder=2)           # 繪製cos, zorder是 2                
plt.show()




