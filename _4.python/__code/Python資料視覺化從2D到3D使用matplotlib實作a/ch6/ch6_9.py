# ch6_9.py
import matplotlib.pyplot as plt

plt.subplot(1,2,1)      # 建立子圖表 1,2,1
plt.text(0.15,0.5,'subplot(1,2,1)',fontsize='16',c='b')
plt.subplot(2,2,2)      # 建立子圖表 2,2,2
plt.text(0.15,0.5,'subplot(2,2,2)',fontsize='16',c='m')
plt.subplot(2,2,4)      # 建立子圖表 2,2,4
plt.text(0.15,0.5,'subplot(2,2,4)',fontsize='16',c='m')
plt.show()



