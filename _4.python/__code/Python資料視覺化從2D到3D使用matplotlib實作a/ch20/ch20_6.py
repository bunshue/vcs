# ch20_6.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
pts = 30
x = np.linspace(1, 2*np.pi, pts)
y = np.exp(np.sin(x))
plt.stem(x,y,linefmt='m',markerfmt='gD',basefmt='b-')
plt.show()


      
