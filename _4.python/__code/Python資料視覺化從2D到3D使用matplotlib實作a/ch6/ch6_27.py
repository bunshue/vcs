# ch6_27.py
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(nrows=1,ncols=2) # 建立2個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0].plot(x, y,'b')                    # 子圖索引 0 
ax[1].plot(x, y,'g')                    # 子圖索引 1
plt.tight_layout()                      # 緊縮佈局
plt.show()



