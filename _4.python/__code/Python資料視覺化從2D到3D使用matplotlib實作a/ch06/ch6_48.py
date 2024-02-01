# ch6_48.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes([0.1,0.1,0.8,0.8])
x = np.linspace(0, 2*np.pi, 500)
ax.plot(x, np.sin(x)**2,'g')
plt.show()


