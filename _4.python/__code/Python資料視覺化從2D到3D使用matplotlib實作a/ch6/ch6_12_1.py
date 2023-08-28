# ch6_12_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
ax = plt.subplot()
ax.plot(x, y1, lw = 2)              # 線條寬度是 2
ax.plot(x, y2, linewidth = 5)       # 線條寬度是 5                
plt.show()




