import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(20) 
x1 = np.random.randn(1000) 
x2 = np.random.randn(1000) 
x3 = np.random.randn(1000) 
x4 = np.random.randn(1000) 
x = [x1, x2, x3, x4]
# 建立箱線圖
bp = plt.boxplot(x,patch_artist=True,notch ='True') 
colors = ['green','m','yellow','b'] 
# 設定盒子
for patch, color in zip(bp['boxes'],colors):
    patch.set_facecolor(color) 
# 更改晶鬚樣式 
for whisker in bp['whiskers']:
    whisker.set(color ='g',linewidth=2,linestyle =":") 
# 更改帽子樣式 
for cap in bp['caps']:
    cap.set(color ='b', linewidth = 2) 
# 更改中位數樣式 
for median in bp['medians']:
    median.set(color ='g', linewidth = 3) 
# 更改異常值樣式 
for flier in bp['fliers']:
    flier.set(marker='D',markerfacecolor='g',markeredgecolor='g') 
plt.title("使用回傳物件更新樣式") 
plt.show()

  
      
