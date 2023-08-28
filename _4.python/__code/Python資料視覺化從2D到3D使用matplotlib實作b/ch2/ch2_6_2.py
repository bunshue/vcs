# ch2_6_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['lines.linewidth'] = 9 # 設定線條寬度
x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.plot(x, y1)                     # 線條寬度是 9
plt.plot(x, y2, linewidth = 5)      # 線條寬度是 5                
plt.show()




