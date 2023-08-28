# ch21_2.py
import matplotlib.pyplot as plt
  
# 事先定義間斷長條圖數據 1 
x_1 = [(2, 4), (9, 6)]
y_1 = (2, 3) 
# 繪製間斷長條圖 1
plt.broken_barh(x_1, y_1, facecolors ='m')
# 事先定義間斷長條圖數據 2  
x_2 = [(5, 1), (8, 3), (12, 6)]
y_2 = (6, 3) 
# 繪製間斷長條圖 2
plt.broken_barh(x_2, y_2, facecolors ='g')
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.title('Broken_barh()',fontsize=16,color='b')
plt.show()


      
