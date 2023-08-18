# ch2_7.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(0, 10, 500)           # 建立含500個元素的陣列
ypt1 = np.sin(xpt)                      # y陣列的變化
ypt2 = np.cos(xpt)

plt.plot(xpt, ypt1, label='sin')        # 預設顏色
plt.plot(xpt, ypt2, label='cos')        # 預設顏色
plt.xlabel('rad')
plt.ylabel('value')
plt.title('Sin and Cos function')
plt.grid()
plt.legend(loc='best')

plt.show()




