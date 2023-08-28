# ch2_17_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 100, 10000)    # 建立含10000個元素的陣列
y = [(1+1/x)**x for x in x]
plt.plot(x, y)
plt.title('Euler Number',fontsize=24,loc='left',color='b',
          fontweight='bold')
plt.show()




