import matplotlib.pyplot as plt
import numpy as np

points = 30
x = np.random.randint(1,11,points)          # 建立 x
y = np.random.randint(1,11,points)          # 建立 y
colors = np.random.rand(points)             # 色彩數列
size =  (30 * np.random.rand(points))**2    # 散點大小數列
plt.scatter(x, y, s=size, c=colors)
plt.xticks(np.arange(0,12,step=1.0))
plt.yticks(np.arange(0,12,step=1.0))

plt.show()
