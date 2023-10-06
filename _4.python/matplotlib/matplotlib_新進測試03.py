import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

def piformat(x, pos):
    ''' 刻度間距是 1/2 Pi '''
    return r"$\frac{%d\pi}{%d}$" % (int(np.round(x/(np.pi/2))),2)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot()

ax.plot(x,y,label="sin(x)",color="g",linewidth=3)
# 建立刻度間距 pi/2
ax.xaxis.set_major_locator(MultipleLocator(np.pi/2))
# 建立刻度標籤
ax.xaxis.set_major_formatter(FuncFormatter(piformat)) 

plt.title('Sin函數的刻度標籤是數學符號')

plt.grid()

plt.show()      





