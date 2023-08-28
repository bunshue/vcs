# ch9_11.py
import matplotlib.pyplot as plt
import numpy as np

points = 10
colors = np.array(['b','c','g','k','m','r','y','pink','purple','orange'])
x = np.random.randint(1,11,points)      # 建立 x
y1 = np.random.randint(1,11,points)     # 建立 y1
y2 = np.random.randint(1,11,points)     # 建立 y2
plt.scatter(x, y1, c=colors, label='Circle')
plt.scatter(x, y2, c=colors, marker='*', label='Star')
plt.xticks(np.arange(0,11,step=1.0))
plt.yticks(np.arange(0,11,step=1.0))
plt.legend()
plt.show()



