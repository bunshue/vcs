# ch20_19.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 500)                # 含500個元素的陣列
y = 1 - 0.5*np.abs(x-2)                   # y陣列的變化
plt.scatter(x,y,s=50,c=x,cmap='rainbow')  # 色彩隨 x 軸值變化
plt.show()




