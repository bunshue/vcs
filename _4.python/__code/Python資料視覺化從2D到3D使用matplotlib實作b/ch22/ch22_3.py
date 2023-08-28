# ch22_3.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10)
# 建立 200 個均勻分佈的隨機數
uniform = np.arange(-100, 100) 
fig, ax = plt.subplots(nrows=1,ncols=2,figsize =(8,4),sharey=True) 
ax[0].set_title('均勻分佈')
ax[0].set_ylabel('觀察值')
ax[0].violinplot(uniform,showmedians=True)
# 建立 200 個常態分佈的隨機數  
normal = np.random.normal(size = 200)*35  
ax[1].set_title('常態分佈')
ax[1].violinplot(normal,showmedians=True)

plt.show()


      
