import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
siny = np.sin(x)

y = siny + np.random.rand(1, len(siny)) * 1.5 #加入雜訊的點集
y = y.tolist()[0]

plt.figure()

plt.plot(x, siny, c = 'r', label = 'sin(x)', linewidth = 1)
plt.plot(x, y, c = 'g', label = 'sin(x)', linewidth = 1)

plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('')
plt.legend()
plt.show()




