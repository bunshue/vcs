# matplotlib_新進測試12_前bar後hist

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

# 柱圖

data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
plt.bar(list(data.keys()), list(data.values()))
plt.show()

print("------------------------------------------------------------")  # 60個

# 條形圖
data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
error = [3, 4, 2, 7] 
plt.barh(list(data.keys()), list(data.values()), xerr=error, align='center', 
        color='green', ecolor='black')
plt.show()





print("------------------------------------------------------------")  # 60個



# 堆疊圖
y1 = (20, 35, 30, 35, 27)
y2 = (25, 32, 34, 20, 25)
x = np.arange(len(y1))
width = 0.35
p1 = plt.bar(x, y1, width)
p2 = plt.bar(x, y2, width, bottom=y1) # 堆疊圖
plt.show()




print("------------------------------------------------------------")  # 60個



import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['理工學院', '外語學院', '管理學院', '文學院']
s1= [540,2800,1864,1285]
s2=[489,2968,1908,1300]
s=[s1[0]+s2[0],s1[1]+s2[1],s1[2]+s2[2],s1[3]+s2[3]]
print(s)
plt.bar(x, s)
plt.ylabel('總人數(單位:人)')
plt.title('卓越綜合大學通過英檢中高級人數')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='DFKai-SB'
plt.rcParams['font.size'] = 15  #預設值10.0

x = ['理工學院', '外語學院', '管理學院', '文學院']
s1= [540,2800,1864,1285]
s2=[489,2968,1908,1300]
s=[s1[0]+s2[0],s1[1]+s2[1],s1[2]+s2[2],s1[3]+s2[3]]
plt.bar(x, s,width=0.8, align='edge', color='r', ec='y',lw=2)
plt.ylabel('總人數(單位:人)')
plt.title('卓越綜合大學通過英檢中高級人數')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['理工學院', '外語學院', '管理學院', '文學院']
s1= [540,2800,1864,1285]
s2=[489,2968,1908,1300]
s=[s1[0]+s2[0],s1[1]+s2[1],s1[2]+s2[2],s1[3]+s2[3]]
plt.bar(x, s,width=0.8, align='edge', color='r', ec='y',lw=2)
plt.ylabel('總人數(單位:人)')
plt.title('卓越綜合大學通過英檢中高級人數')
plt.show()

print("------------------------------------------------------------")  # 60個

votes = [135, 412, 397]         # 得票數
N = len(votes)                  # 計算長度
x = np.arange(N)                # 長條圖x軸座標
width = 0.35                    # 長條圖寬度

plt.bar(x, votes, width)        # 繪製長條圖

plt.xticks(x, ('James', 'Peter', 'Norton'))
plt.yticks(np.arange(0, 450, 30))
plt.title('x用名稱 y設定範圍刻距')

plt.show()

print("------------------------------------------------------------")  # 60個

def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):              
        ranNum = random.randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)
def dice_count(sides):
    # 計算1-6個出現次數
    for i in range(1, sides+1):
        frequency = dice.count(i)               # 計算i出現在dice串列的次數
        frequencies.append(frequency)
          
times = 600                                     # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
frequencies = []                                # 儲存每一面骰子出現次數串列
dice_generator(times, sides)                    # 產生擲骰子的串列
dice_count(sides)                               # 將骰子串列轉成次數串列                          
x = np.arange(6)                                # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.bar(x, frequencies, width, color='g')       # 繪製長條圖
plt.ylabel('Frequency')
plt.title('丟骰子600次')
plt.xticks(x, ('1', '2', '3', '4', '5', '6'))
plt.yticks(np.arange(0, 150, 15))

plt.show()

print("------------------------------------------------------------")  # 60個

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

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.bar(x, s)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')

plt.show()

print("------------------------------------------------------------")  # 60個

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.bar(x, s,width=0.5, align='edge', color='r', ec='y',lw=2)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')

plt.show()

print("------------------------------------------------------------")  # 60個

x = ['第一季', '第二季', '第三季', '第四季']
s = [20000,15000,17000, -8000]
plt.barh(x, s,color='red')
plt.ylabel('季別')
plt.xlabel('損益金額')
plt.title('今年度營業獲利的概況')

plt.show()

print("------------------------------------------------------------")  # 60個

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.barh(x, s)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')

plt.show()


print("------------------------------------------------------------")  # 60個

print('Bar圖')

money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]

def millions(x, pos):
    """The two args are the value and tick position."""
    return '${:1.1f}M'.format(x * 1e-6)

fig, ax = plt.subplots()
# Use automatic FuncFormatter creation
ax.yaxis.set_major_formatter(millions)
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money,label = 'data1', align = 'edge')
ax.set_title('Bar chart')
ax.set_xlabel('Name')
ax.set_ylabel('Money')
ax.legend(loc = 2)

plt.show()

print("------------------------------------------------------------")  # 60個


# from basic_units import cm, inch

cm = 1
inch = cm*0.039

fig, ax = plt.subplots()
N = 5
ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
men_means = [150*cm, 160*cm, 146*cm, 172*cm, 155*cm]
men_std = [20*cm, 30*cm, 32*cm, 10*cm, 20*cm]
ax.bar(x = ind, height = men_means, width = width, bottom = 0*cm, yerr = men_std, label = 'Men')
women_means = (145*cm, 149*cm, 172*cm, 165*cm, 200*cm)
women_std = (30*cm, 25*cm, 20*cm, 31*cm, 22*cm)
ax.bar(x = ind + width, height = women_means, width = width, bottom = 0*cm, yerr = women_std,label = 'Women')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()
ax.yaxis.set_units(inch)
ax.autoscale_view()

plt.show()

print('------------------------------------------------------------')	#60個

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(N) # the x locations for the groups
width = 0.35
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(ind, menMeans, width, color = 'r')
ax.bar(ind, womenMeans, width,bottom = menMeans, color = 'b')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
ax.set_yticks(np.arange(0, 81, 10))
ax.legend(labels = ['Men', 'Women'])

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


















print("------------------------------------------------------------")  # 60個


# 直方圖
x = np.random.rand(50, 2) # 產生共兩組，每組50個隨機數,
plt.hist(x)

plt.show()


print("------------------------------------------------------------")  # 60個

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size']=15

score = [800,750,450,680,802,630,710,450,250,320,610,670,815,\
         870,900,650,450,730,840,675,795,585,870,960,190]

plt.hist(score, bins = [10,255,405,605,785,905,990],edgecolor = 'k') 
plt.title('多益成績分布直方圖')
plt.xlabel('成績')
plt.ylabel('人數')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size']=15

score = [800,750,450,680,802,630,710,450,250,320,610,670,815,870,900,650,450,730,840,675,795,585,870,960,190]
n, b, p=plt.hist(score, bins = [10,255,405,605,785,905,990], edgecolor = 'k')

for i in range(len(n)):
    plt.text(b[i]+10, n[i], int(n[i]), ha='center', va='bottom', fontsize=10)
plt.title('多益成績分布直方圖')
plt.xlabel('成績')
plt.ylabel('人數')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams['font.size']=18

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100],edgecolor = 'r') 
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')

plt.show()

print("------------------------------------------------------------")  # 60個

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

print("Hist圖")

fig, ax = plt.subplots(1, 3, figsize=(10, 8))

normal_samples = np.random.normal(
    size=100000
)  # 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
uniform_samples = np.random.uniform(size=100000)  # 生成 100000 組介於 0 與 1 之間均勻分配隨機變數
exp_samples = np.random.exponential(scale=2, size=100000)

ax[0].hist(x=normal_samples, bins=1000, label="Normal distribution")
ax[1].hist(x=uniform_samples, bins=1000, label="Uniform distribution")
ax[2].hist(x=exp_samples, bins=1000, label="Exponential distribution")
ax[0].legend()
ax[1].legend()
ax[2].legend()

plt.show()

print("------------------------------------------------------------")  # 60個

#繪製直方圖

plt.subplot(121)
np.random.seed(0)
data = np.random.randn(10000)
plt.hist(data, bins = 'auto')

plt.subplot(122)
np.random.seed(0)
data = np.random.randn(10000)
plt.hist(data, bins = 'auto', density = True)   #y軸改成密度

plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



