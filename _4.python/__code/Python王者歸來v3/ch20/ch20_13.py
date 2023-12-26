# ch20_13.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 10, 500)   # 建立含500個元素的陣列
ypt1 = np.sin(xpt)              # y陣列的變化
ypt2 = np.cos(xpt)
plt.scatter(xpt, ypt1)          # 用預設顏色
plt.scatter(xpt, ypt2)          # 用預設顏色
plt.show()




