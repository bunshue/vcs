# ch6_16.py
import matplotlib.pyplot as plt
import numpy as np

# 建立子圖 1
x1 = np.linspace(0, 2*np.pi, 300)
ax1 = plt.subplot(211)              
ax1.plot(x1, np.sin(2*np.pi*x1))
ax1.tick_params('x',labelbottom=False)  # 取消顯示刻度標籤
# 建立子圖 2
x2 = np.linspace(0, 3*np.pi, 300)
ax2 = plt.subplot(212, sharex=ax1)      # 共享 x 軸
ax2.plot(x2, np.sin(4*np.pi*x2))
plt.show()



