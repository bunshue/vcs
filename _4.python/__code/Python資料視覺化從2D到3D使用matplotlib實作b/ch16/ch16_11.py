# ch16_11.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data = np.random.randn(500) 
labels = ['data']
whisker_line = dict(linestyle='--',
                   linewidth=2.5,
                   color='m')
plt.boxplot(data,labels=labels,vert=False,whiskerprops=whisker_line)
plt.title("設計水平箱線圖的晶鬚線",fontsize=16,color='b')
plt.show() 



      
