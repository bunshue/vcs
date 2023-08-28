# ch22_4.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
np.random.seed(10)
# 建立 3 組隨機數
data1 = np.random.randint(1, 100, size=100)     
data2 = np.random.randint(1, 100, size=100)     
data3 = np.random.randint(1, 100, size=100)
dataset = [data1, data2, data3]     # 3 組數據組成 dataset 
# 建立圖表物件
fig = plt.figure()
ax = fig.gca()                      # 獲得目前圖表物件
vio = plt.violinplot(dataset)       # 建立小提琴圖
for body in vio['bodies']:          # 小提琴圖區塊
    body.set_facecolor('cyan')      # 內部顏色是 cyan
    body.set_edgecolor('m')         # 邊線顏色是 magenta
    body.set_alpha(0.8)             # 透明度 0.8
ax.set_title('3 組均勻分布的小提琴圖',fontsize=16,color='b')
plt.show()


      
