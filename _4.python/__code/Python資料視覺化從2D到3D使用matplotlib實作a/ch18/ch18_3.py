# ch18_3.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
x = np.linspace(0, 10, 10)
y1 = x
y2 = 1.5 * x + 1.5
y3 = 2.0 * x + 2
plt.stackplot(x, y1, y2, y3)
plt.xlim((0, 10))
plt.ylim((0, 60))
plt.title('基礎數學公式的堆疊',fontsize=16,color='b')
plt.show()





  
      
