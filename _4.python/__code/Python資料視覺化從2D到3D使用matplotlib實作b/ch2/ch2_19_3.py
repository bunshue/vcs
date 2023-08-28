# ch2_19_3.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.plot(x, y1, color='c')          # 設定青色cyan            
plt.plot(x, y2, color='r')          # 設定紅色red
plt.title('Sin和Cos函數圖')
plt.show()




