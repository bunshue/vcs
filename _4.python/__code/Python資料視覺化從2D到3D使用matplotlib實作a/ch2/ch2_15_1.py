# ch2_15_1.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 2*np.pi, 50)   # 建立 50 個點
y = np.sin(x)
plt.plot(x,y,'bo')                  # 繪製 sine wave
plt.xlabel('Angel')
plt.ylabel('Sin')
plt.title('Sine Wave')
plt.show()



