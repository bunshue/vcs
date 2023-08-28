# ch15_8.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]
exp = [0.0,0.0,0.1,0.0,0.0,0.1]
piecolors = ['aqua','g','pink','yellow','m','salmon']
patches, texts, autotexts = plt.pie(people,labels=area,
        explode=exp,autopct="%1.2f%%",colors=piecolors)
for txt in texts:               # 設定標籤顏色
    txt.set_color('m')
plt.title('五月份國外旅遊調查表',fontsize=16,color='b')
plt.show()


      
