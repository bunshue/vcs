import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.05,2*np.pi,500)
y = np.sin(x)
plt.plot(x,y,ls="-.",lw=2,c="c",label="Sin")    # 繪製sin線

plt.axhspan(ymin=0.0,ymax=0.5,fc='y',alpha=0.3) # 水平參考區間
plt.axvspan(xmin=0.5*np.pi,xmax=1.5*np.pi, fc='r',alpha=0.3)    # 垂直參考區間

plt.legend()

plt.show()

