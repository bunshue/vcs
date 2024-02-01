# ch6_18.py
import matplotlib.pyplot as plt
import numpy as np

# 建立子圖 1
x = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(121)          
ax1.plot(x, np.sin(x**2),'b')
# 建立子圖 2
ax2 = plt.subplot(122,sharey=ax1)   # 共享 y 軸    
ax2.plot(x, 1+np.sin(x**2),'g--')
plt.show()



