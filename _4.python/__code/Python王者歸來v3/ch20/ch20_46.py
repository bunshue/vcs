# ch20_46.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(1,0,'bo')                  # 輸出藍點
plt.text(1,0,'sin(x)',fontsize=20)  # 輸出公式
plt.plot(x,y)
plt.grid()
plt.show()











