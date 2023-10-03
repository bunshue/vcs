import matplotlib.pyplot as plt
import numpy as np
import itertools as it

colorused = it.cycle(['b','c','g','k','m','r','y']) # 定義顏色
x = np.linspace(1, 10, 10)                          # 建立 x
y = np.random.random((7,10))                        # 建立 y
for yy in y:    
    plt.scatter(x, yy, c=next(colorused), marker='*')
plt.xticks(np.arange(0,11,step=1.0))

plt.show()

