# ch2_12_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.plot(x, y1, color='tab:orange') # 設定 orange           
plt.plot(x, y2, color='tab:purple') # 設定 purple
plt.show()




