# ch19_7.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(14)
y = np.sin(x/3)
fig, ax = plt.subplots()
ax.set_title('plot() - drawstyle參數的使用')
# 繪製階梯圖 
ax.plot(x,y+2,drawstyle='steps')
ax.plot(x,y+1,drawstyle='steps-mid')
ax.plot(x,y,drawstyle='steps-post')
# 繪製直線圖
ax.plot(x,y+2,'D--',color='m',alpha=0.3)
ax.plot(x,y+1,'D--',color='m',alpha=0.3)
ax.plot(x,y,'D--',color='m',alpha=0.3)
labels = ['steps','steps-mid','steps-post']
ax.legend(title='參數 drawstyle', labels=labels)
plt.show()


      
