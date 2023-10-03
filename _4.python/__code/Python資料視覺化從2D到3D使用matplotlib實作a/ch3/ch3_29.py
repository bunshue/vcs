import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
sin_line, = plt.plot(x, y1,label="Sin",linestyle='--')                         
cos_line, = plt.plot(x, y2,label="Cos",lw=3)

sin_legend = plt.legend(handles=[sin_line], loc=1)  # 建立sin圖表物件
plt.gca().add_artist(sin_legend)    # 手動將sin圖例加入圖表
plt.legend(handles=[cos_line], loc=4)               # 建立cos圖表

plt.show()




