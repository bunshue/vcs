# ch19_6.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(14)
y = np.sin(x/3)
fig, ax = plt.subplots()
ax.set_title('step() - pre,post,mid參數的使用')
# 繪製階梯圖 
ax.step(x,y+2,where='pre')
ax.step(x,y+1,where='mid')
ax.step(x,y,where='post')
# 繪製直線圖
ax.plot(x,y+2,'D--',color='m',alpha=0.3)
ax.plot(x,y+1,'D--',color='m',alpha=0.3)
ax.plot(x,y,'D--',color='m',alpha=0.3)
labels = ['pre','mid','post']
ax.legend(title='參數 where', labels=labels)
plt.show()


      
