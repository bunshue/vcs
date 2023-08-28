# ch15_11.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
patches = plt.pie(people,labels=area,autopct="%1.2f%%")
for edgecolor in patches[0]:
    edgecolor.set_edgecolor('w')        # 設定圓餅邊界線是白色
plt.title('使用 set_edgecolor() 函數',fontsize=16,color='b')
plt.show()


      
