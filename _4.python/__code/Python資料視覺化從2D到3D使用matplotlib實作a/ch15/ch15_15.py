# ch15_15.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
plt.pie(people,labels=area,autopct="%1.2f%%")
plt.title('使用 plt.axis() 函數',fontsize=16,color='b')
plt.axis('equal')           # 圓餅圖保持圓形
plt.show()


      
