# ch4_14.py
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(0,13.3,0.01)

y1 = 17.5 - 2.5 * x
y2 = 8 - 0.6 * x
y3 = np.minimum(y1,y2)  # 取較低值

plt.plot(x,y1,color="blue",label="17.5 - 2.5x")
plt.plot(x,y2,color="green",label="8 - 0.6x")
plt.ylim(0, 10)
plt.fill_between(x, 0, y3, color='yellow')
plt.legend()
plt.show()














