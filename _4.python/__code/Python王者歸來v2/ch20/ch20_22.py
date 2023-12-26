# ch20_22.py
import matplotlib.pyplot as plt
import numpy as np

left = -2 * np.pi
right = 2 * np.pi
x = np.linspace(left, right, 100)

f1 = 2 * np.sin(x)                  # y陣列的變化
f2 = np.sin(2*x)
f3 = 0.5 * np.sin(x)

plt.plot(x, f1) 
plt.plot(x, f2)
plt.plot(x, f3)
plt.show()




