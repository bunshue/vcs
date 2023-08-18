# ch15_5.py
import matplotlib.pyplot as plt
import numpy as np

x2 = np.linspace(-3, 3, 30)                 # 建立含30個元素的陣列
x4 = np.linspace(-3, 3, 30)                 # 建立含30個元素的陣列
y2 = 2**x2
y4 = 4**x4
plt.plot(x2, y2, label="2**x")
plt.plot(x4, y4, label="4**x")
plt.plot(0, 1, '-o')                        # 標記指數為0位置
plt.legend(loc="best")                      # 建立圖例
plt.axis([-3, 3, 0, 30])
plt.grid()
plt.show()




