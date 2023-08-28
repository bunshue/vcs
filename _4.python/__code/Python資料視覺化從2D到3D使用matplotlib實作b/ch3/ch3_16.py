# ch3_16.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.xticks(np.arange(0,7,step=0.5),color='b')
plt.yticks(np.arange(-1,1.5,step=0.5),color='g')
plt.plot(x, y1, color='c')          # 設定青色cyan            
plt.plot(x, y2, color='r')          # 設定紅色red
plt.show()




