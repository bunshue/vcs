# ch7_4.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False 
x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, 'm', lw=2)
plt.annotate('局部極大值',
            xy=(2, 1),
            xytext=(2.5, 1.2),           
            arrowprops=dict(color='g',shrink=0.05)) 
plt.ylim(-1.5, 1.5)
plt.show()



