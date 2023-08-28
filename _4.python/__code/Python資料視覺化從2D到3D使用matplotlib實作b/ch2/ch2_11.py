# ch2_11.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.plot(x,y1,color=((0/255,255/255,255/255)))  # 設定青色cyan            
plt.plot(x,y2,color=((255/255,0/255,0/255)))    # 設定紅色red
plt.show()




