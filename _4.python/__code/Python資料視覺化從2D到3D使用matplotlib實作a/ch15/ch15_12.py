# ch15_12.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
plt.pie(people,labels=area,autopct="%1.2f%%",
        wedgeprops={'edgecolor':'w'})
plt.title('使用 wedgeprops 字典',fontsize=16,color='b')
plt.show()


      
