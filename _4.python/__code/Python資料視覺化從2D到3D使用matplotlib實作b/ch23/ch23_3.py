# ch23_3.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = np.sin(x) * 2
dy = 0.5
dx = 0.2
plt.errorbar(x,y,xerr=dx,yerr=dy,ecolor='r',capsize=3)
plt.show()


      
