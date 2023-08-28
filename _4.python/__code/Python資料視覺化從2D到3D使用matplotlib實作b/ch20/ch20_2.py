# ch20_2.py
import matplotlib.pyplot as plt
import numpy as np

pts = 15
x = np.linspace(1, 2*np.pi, pts)
y = np.random.randn(pts)
plt.stem(x,y)
plt.show()


      
