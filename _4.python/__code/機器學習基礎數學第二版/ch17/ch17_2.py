# ch17_2.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 1000, 100000)          # 建立含100000個元素的陣列
y = [(1+1/x)**x for x in x]
#plt.axis([0, 10, 0, 3])
plt.plot(x, y, label="Euler's Number")

plt.legend(loc="best")                      # 建立圖例
plt.grid()
plt.show()




