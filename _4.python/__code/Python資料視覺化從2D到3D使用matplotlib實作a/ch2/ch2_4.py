# ch2_4.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y = np.sin(x)                       # sin函數
plt.plot(x, y)                      
plt.show()




