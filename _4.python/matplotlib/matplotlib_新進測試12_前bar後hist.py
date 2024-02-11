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

print("前bar------------------------------------------------------------")  # 60個


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.barh(x, s)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')

plt.show()


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


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.bar(x, s,width=0.5, align='edge', color='r', ec='y',lw=2)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')
plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

name = ['鼠', '牛', '虎', '兔', '龍']
weight = [3, 48, 33, 8, 38]
plt.bar(name, weight)

plt.ylabel('體重(單位:公斤)')
plt.title('動物體重 使用中文')

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='DFKai-SB'
plt.rcParams['font.size'] = 15  #預設值10.0

name = ['鼠', '牛', '虎', '兔', '龍']
weight = [3, 48, 33, 8, 38]

plt.bar(name, weight, width = 0.8, align = 'edge', color = 'r', ec = 'y', lw = 2)

plt.ylabel('體重(單位:公斤)')
plt.title('動物體重 使用中文')

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

name = ['鼠', '牛', '虎', '兔', '龍']
weight = [3, 48, 33, 8, 38]

plt.bar(name, weight, width = 0.8, align = 'edge', color = 'r', ec = 'y', lw = 2)

plt.ylabel('體重(單位:公斤)')
plt.title('動物體重 使用中文')

plt.show()


print("------------------------------------------------------------")  # 60個



votes = [135, 412, 397]         # 得票數
N = len(votes)                  # 計算長度
x = np.arange(N)                # 長條圖x軸座標
width = 0.35                    # 長條圖寬度
plt.bar(x, votes, width)        # 繪製長條圖

plt.ylabel('得票數')
plt.title('選舉結果')
plt.xticks(x, ('James', 'Peter', 'Norton')) # x 軸刻度
plt.yticks(np.arange(0, 450, 30))           # y 軸刻度
plt.show()

print("------------------------------------------------------------")  # 60個

def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):              
        ranNum = random.randint(1, sides)      # 產生1-6隨機數
        dice.append(ranNum)
def dice_count(sides):
    #計算1-6個出現次數
    for i in range(1, sides+1):
        frequency = dice.count(i)       # 計算i出現在dice串列的次數
        frequencies.append(frequency)

times = 600                             # 擲骰子次數
sides = 6                               # 骰子有幾面
dice = []                               # 建立擲骰子的串列
frequencies = []                        # 儲存每一面骰子出現次數串列
dice_generator(times, sides)            # 產生擲骰子的串列
dice_count(sides)                       # 將骰子串列轉成次數串列                          
x = np.arange(6)                        # 長條圖x軸座標
width = 0.35                            # 長條圖寬度
plt.bar(x, frequencies, width, color='g')   # 繪製長條圖
plt.ylabel('次數')
plt.xlabel('骰子點數')
plt.title('測試 600 次')
plt.xticks(x, ('1', '2', '3', '4', '5', '6'))
plt.yticks(np.arange(0, 150, 15))

plt.show()



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("後hist------------------------------------------------------------")  # 60個

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.rcParams['font.size']=18

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100],edgecolor = 'b') 
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')

plt.show()


print("------------------------------------------------------------")  # 60個

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size']=15

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

n, b, p = plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100], edgecolor = 'r') 

for i in range(len(n)):
    plt.text(b[i]+10, n[i], int(n[i]), ha='center', va='bottom', fontsize=12)
  
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')
plt.show()

print("------------------------------------------------------------")  # 60個



def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):              
        ranNum = random.randint(1, sides)      # 產生1-6隨機數
        dice.append(ranNum)

times = 10000                           # 擲骰子次數
sides = 6                               # 骰子有幾面
dice = []                               # 建立擲骰子的串列
dice_generator(times, sides)            # 產生擲骰子的串列
h = plt.hist(dice,sides)                # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print("------------------------------------------------------------")  # 60個

print('比上面多了 rwidth=0.8')

def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):              
        ranNum = random.randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)

times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列
h = plt.hist(dice,sides,rwidth=0.8)             # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print("------------------------------------------------------------")  # 60個

print('比上面多了 rwidth=0.8 cumulative=True')

def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):              
        ranNum = random.randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)

times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列
h = plt.hist(dice,sides,rwidth=0.5,cumulative=True) # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



