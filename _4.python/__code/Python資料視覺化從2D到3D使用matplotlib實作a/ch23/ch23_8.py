# ch23_8.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
up = [True,False] * 10      # 上限串列
lo = [False,True] * 10      # 下限串列
plt.errorbar(x,y,yerr=dy,uplims=up,lolims=lo,ecolor='r')
plt.show()


      
