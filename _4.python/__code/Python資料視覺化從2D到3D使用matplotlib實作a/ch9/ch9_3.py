# ch9_3.py
import matplotlib.pyplot as plt
#import numpy as np

x = [x for x in range(101)]
y = [(y * y) for y in x]
plt.scatter(x ,y, c='g')
plt.show()



