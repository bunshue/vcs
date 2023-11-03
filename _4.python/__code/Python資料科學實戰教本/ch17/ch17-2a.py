import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, x, cosinus)
plt.show()
