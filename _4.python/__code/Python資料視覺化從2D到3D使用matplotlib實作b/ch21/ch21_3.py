# ch21_3.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 定義間斷長條圖數據 1 
x_1 = [(0, 7), (20, 4)]         # 定義時間
y_1 = (90, 30)                  # 定義車速
plt.broken_barh(x_1, y_1, facecolors ='g')
# 定義間斷長條圖數據 2  
x_2 = [(7, 3), (17, 3)]         # 定義時間
y_2 = (40, 20)                  # 定義車速
plt.broken_barh(x_2, y_2, facecolors ='r')
# 定義間斷長條圖數據 3  
x_3 = [(10, 7)]                 # 定義時間
y_3 = (60, 30)                  # 定義車速
plt.broken_barh(x_3, y_3, facecolors ='b')
plt.xlabel('時間',fontsize=14,color='b')
plt.xticks(np.arange(0,25,step=4))
plt.ylabel('車速',fontsize=14,color='b')
plt.title('每天不同時段行車速度表',fontsize=16,color='b')
plt.show()


      
