# ch3_33.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.plot(x, y1, label='Sin')                    
plt.plot(x, y2, label='Cos')
plt.legend()
plt.grid(c='y',linestyle='--',lw=1) # 顯示虛線格線
plt.show()




