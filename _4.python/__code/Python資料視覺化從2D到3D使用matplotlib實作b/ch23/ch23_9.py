# ch23_9.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.2 + 0.01 * x
dy_range = [dy*0.5,dy]      # (下方誤差, 上方誤差)
plt.errorbar(x,y,fmt='o-',yerr=dy_range,ecolor='r',color='b',capsize=3)
plt.show()


      
