import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5.0, 5.0, 30)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sinc(x)

plt.subplot(2, 2, 1)
plt.plot(x, y1, 'o-')
plt.title('sin')

plt.subplot(2, 2, 2)
plt.plot(x, y2, '.-')
plt.title('cos')

plt.subplot(2, 2, 3)
plt.plot(x, y3, 'o-')
plt.title('tan')

plt.subplot(2, 2, 4)
plt.plot(x, y4, '.-')
plt.title('sinc')

plt.show()

