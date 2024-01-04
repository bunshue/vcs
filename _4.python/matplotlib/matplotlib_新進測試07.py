# 新進測試07

import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

"""
正弦函數 s=sin(x) 
餘弦函數 c=cos(x)
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
s, c=np.sin(x), np.cos(x)
plt.plot(x, s)
plt.plot(x, c)
plt.xticks([-2*np.pi,-np.pi,0, np.pi, 2*np.pi],['-$2\pi$', '-$\pi$','0', '$\pi$', '$2\pi$'])
plt.legend(['sin','cos'])

plt.show()



print("------------------------------------------------------------")  # 60個

"""
正弦函數 s=sin(x) 
餘弦函數 c=cos(x)
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
s, c=np.sin(x), np.cos(x)

plt.plot(x, s)
plt.plot(x, c)
plt.xticks([-2*np.pi,-np.pi,0, np.pi, 2*np.pi],['-$2\pi$', '-$\pi$','0', '$\pi$', '$2\pi$'])
plt.legend(['sin','cos'],loc=3,fontsize='xx-large',edgecolor='y',facecolor='r')

plt.show()


print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch12\barCharDouble.py

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x=['上學期', '下學期']
s1,s2,s3,s4 = [96.2, 87.1], [88.9, 95.2], [85.1, 91.5], [95.2, 96.7]

index = np.arange(len(x)) 
width=0.15
plt.bar(index - 1.5*width, s1, width, color='b')
plt.bar(index - 0.5*width, s2, width, color='r')
plt.bar(index + 0.5*width, s3, width, color='y')
plt.bar(index + 1.5*width, s4, width, color='g')

plt.xticks(index, x)
plt.legend(['2017年','2018年','2019年','2020年'])

plt.ylabel('平均分數,取到小數點第一位')
plt.title('大學四年各學期平均成績比較表')

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch12\barChart.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.bar(x, s)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch12\barChart01.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.bar(x, s,width=0.5, align='edge', color='r', ec='y',lw=2)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch12\barhCharMinus.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['axes.unicode_minus']=False

x = ['第一季', '第二季', '第三季', '第四季']
s = [20000,15000,17000, -8000]
plt.barh(x, s,color='red')
plt.ylabel('季別')
plt.xlabel('損益金額')
plt.title('今年度營業獲利的概況')

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch12\barhChart.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.barh(x, s)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch12\hist.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=18

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100],edgecolor = 'r') 
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch12\hist01.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size']=15

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

n, b, p=plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100], edgecolor = 'r') 

for i in range(len(n)):
    plt.text(b[i]+10, n[i], int(n[i]), ha='center', va='bottom', fontsize=12)
  
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')
plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch12\pie.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

x = [26,12,21,25,35]
labels = '高雄','花蓮','台中','澎湖','宜蘭'
explode = (0.2, 0, 0, 0,0)
plt.pie(x,labels=labels, explode=explode, autopct='%.1f%%',
        shadow=True)

plt.show()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch12\subplot.py

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

#折線圖
def lineChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.plot(x, s, marker='.')

#長條圖
def barChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.bar(x, s)

#橫條圖
def barhChart(s,x):
    plt.barh(x, s)

#圓餅圖
def pieChart(s,x):	 
    plt.pie(s,labels=x, autopct='%.2f%%')

#要繪圖的數據
x = ['第一季', '第二季', '第三季', '第四季']
s = [13.2, 20.1, 11.9, 14.2]

#定義子圖
plt.figure(1, figsize=(8, 6),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(2,2,1)
pieChart(s,x)

x = ['程式設計概論', '多媒體概論', '計算機概論', '網路概論']
s = [3560, 4000, 4356, 1800]
plt.subplot(2,2,2)
barhChart(s,x)

x = ['新北市', '台北市', '高雄市', '台南市','桃園市','台中市']
s = [0.2, 0.3, 0.15, 0.23,0.19, 0.27]
plt.subplot(223)
lineChart(s,x)

plt.subplot(224)
barChart(s,x)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

