"""

plt.rcParams['font.sans-serif']='DFKai-SB'  # 中文OK

plt.rcParams['font.sans-serif']='mingliu'	#指定為明體字
plt.rcParams['font.sans-serif']='mingliu'  # 中文OK


"""

#bar累計
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='mingliu'

areas=['北部','中部','南部','東部']
data1=[800000,580000,640000,420000]
data2=[750000,460000,680000,340000]
plt.bar(areas,data1,label='上半年')
plt.bar(areas,data2,label='下半年',bottom=data1)

plt.legend()
plt.show()


print("------------------------------------------------------------")  # 60個

#bar並列

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']='mingliu'

areas=['北部','中部','南部','東部']
width=0.4
x1=[x-width/2 for x in range(len(areas))]
x2=[x+width/2 for x in range(len(areas))]
data1=[800000,580000,640000,420000]
data2=[750000,460000,680000,340000]
plt.bar(x1,data1,width,label='上半年')
plt.bar(x2,data2,width,label='下半年')
plt.xticks(range(len(areas)),labels=areas)

plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個


#pie指定顏色
import matplotlib.pyplot as plt

datas=[40, 45, 15]
lbls=['現金', '股票', '債券']
exps=[0.2, 0, 0]
clrs=['pink','lightblue','yellow']
plt.pie(datas, labels=lbls, colors=clrs, explode=exps, autopct='%2.1f%%',startangle=0, shadow=True)

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import random as rnd

plt.rcParams['font.sans-serif']='mingliu'
dices=['1點','2點','3點','4點','5點','6點']
data=[]
times=[]
for i in range(1000):
    data.append(rnd.randint(1,6))

for i in range(1,7):
    times.append(data.count(i))
    
plt.pie(times,labels=dices,autopct='%2.1f%%',explode=[0.1,0.1,0.1,0.1,0.1,0.1],shadow=True)
plt.title('擲骰子機率圖',fontsize=18)
plt.show()

