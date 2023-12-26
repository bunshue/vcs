# ex20_4.py
import matplotlib.pyplot as plt
import numpy as np

left = -np.pi
right = np.pi
x = np.linspace(left, right, 100)
y = np.sin(2*x)                  # y陣列的變化

plt.plot(x, y) 
plt.fill_between(x, 1, y, alpha=0.1)
plt.show()




