import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x**2)
plt.figure()
plt.plot(x, y, label="$sin(x)$", color='red', lw=2)
plt.plot(x, z, label="$cos(x^2)$", color='b')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('Volt/Time chart')
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()

