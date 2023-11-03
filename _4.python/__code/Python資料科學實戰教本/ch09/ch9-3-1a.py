import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.subplot(1, 2, 1)
plt.plot(x, sinus, "r-o")
plt.subplot(1, 2, 2)
plt.plot(x, cosinus, "g--")
plt.show()

