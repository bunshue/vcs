# ch6_20.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 建立子圖 1
x1 = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(221)              
ax1.plot(x1, np.sin(2*np.pi*x1))
# 建立子圖 2
x2 = np.linspace(0, 3*np.pi, 300)
ax2 = plt.subplot(222, sharex=ax1, sharey=ax1)  # 共享x和y軸
ax2.plot(x2, np.sin(4*np.pi*x2))
# 建立子圖 3
x3 = np.linspace(0, 2*np.pi, 300)
ax3 = plt.subplot(223, sharex=ax1, sharey=ax1)  # 共享x和y軸        
ax3.plot(x3, np.sin(x3**2),'b')
# 建立子圖 4
ax4 = plt.subplot(224, sharex=ax1, sharey=ax1)  # 共享x和y軸    
ax4.plot(x3, 1+np.sin(x3**2),'g--')
plt.suptitle("共享 x 和 y 軸")
plt.show()



