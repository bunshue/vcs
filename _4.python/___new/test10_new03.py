import sys

'''
print("------------------------------------------------------------")  # 60個

""" fail
import time as t

timestart = t.clock()
for i in range (0,1000):
    for j in range (0,1000):
        n = i * j
timeend = t.clock()
print("執行一百萬次整數運算的時間：" + str(timeend-timestart) + " 秒")
"""

print("------------------------------------------------------------")  # 60個

import time as t

week = ["一", "二", "三", "四", "五", "六", "日"]
dst = ["無日光節約時間", "有日光節約時間"]
time1 = t.localtime()
show = "現在時刻：中華民國 " + str(int(time1.tm_year)-1911) +" 年 "
show += str(time1.tm_mon) + " 月 " + str(time1.tm_mday) + " 日 "
show += str(time1.tm_hour) + " 點 " + str(time1.tm_min) + " 分 "
show += str(time1.tm_sec) + " 秒 星期" + week[time1.tm_wday] + "\n"
show += "今天是今年的第 " + str(time1.tm_yday) + " 天，此地" + dst[time1.tm_isdst]
print(show)

print("------------------------------------------------------------")  # 60個

import time as t

timestart = t.perf_counter() 
for i in range (0,1000):
    for j in range (0,1000):
        n = i * j
timeend = t.perf_counter() 
print("執行一百萬次整數運算的時間：" + str(timeend-timestart) + " 秒")

print("------------------------------------------------------------")  # 60個

"""
import time as t

timestart = t.clock()
for i in range (0,1000):
    for j in range (0,1000):
        n = float(i) * float(j)
timeend = t.clock()
print("執行一百萬次浮點數運算的時間：" + str(timeend-timestart) + " 秒")
"""
print("------------------------------------------------------------")  # 60個

date1 = "2017-8-23"
date1 = "西元 " + date1
date1 = date1.replace("-", " 年 ", 1)
date1 = date1.replace("-", " 月 ", 1)
date1 += " 日"
print(date1)

print("------------------------------------------------------------")  # 60個

import time as t

time1 = t.localtime()
show = "今天是今年的第 " + str(time1.tm_yday) + " 天，屬於"
if time1.tm_yday < 184 : show += "上半年。"
else :  show += "下半年。"
print(show)

print("------------------------------------------------------------")  # 60個

"""
import time as t

timestart = t.perf_counter() ()
for i in range (0,1000):
    for j in range (0,1000):
        n = float(i) * float(j)
timeend = t.perf_counter() ()
print("執行一百萬次浮點數運算的時間：" + str(timeend-timestart) + " 秒")
"""
print("------------------------------------------------------------")  # 60個

time1 = "10:23:41"
time1 = time1.replace(":", " 點 ", 1)
time1 = time1.replace(":", " 分 ", 1)
time1 += " 秒"
print(time1)

print("------------------------------------------------------------")  # 60個

import random

list1 = random.sample(range(1,50), 7)
special = list1.pop()
list1.sort()
print("本期大樂透中獎號碼為：", end="")
for i in range(0,6):
    if i == 5:    print(str(list1[i]))
    else:    print(str(list1[i]), end=", ")
print("本期大樂透特別號為：" + str(special))

print("------------------------------------------------------------")  # 60個

import time as t

time1 = t.localtime()
show = "現在時刻："
if time1.tm_hour < 12: 
    show += "上午 "
    hour = time1.tm_hour
else:
    show += "下午 "
    hour = time1.tm_hour - 12
show += str(hour) + " 點 " + str(time1.tm_min) + " 分 "
show += str(time1.tm_sec) + " 秒"
print(show)

print("------------------------------------------------------------")  # 60個

dict1 = {"A":"內向穩重", "B":"外向樂觀", "O":"堅強自信", "AB":"聰明自然"}
name = "O"
blood = dict1.get(name)
if blood == None:  
    print("沒有「" + name + "」血型！")
else:  
    print(name + " 血型的個性為：" + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

person = 7
apple = 52
ret = divmod(apple, person)
print("每個學生可分得蘋果 " + str(ret[0]) + " 個")
print("蘋果剩餘 " + str(ret[1]) + " 個")

print("------------------------------------------------------------")  # 60個

listname = ["林大明", "陳阿中", "張小英"]
listchinese = [100, 74, 82]
listmath = [87, 88, 65]
listenglish = [79, 100, 8]
print("姓名     座號  國文  數學  英文")
for i in range(0,3):
    print(listname[i].ljust(5), str(i+1).rjust(3), str(listchinese[i]).rjust(5), str(listmath[i]).rjust(5), str(listenglish[i]).rjust(5))

print("------------------------------------------------------------")  # 60個

def disp_data(): # 顯示串列的自訂程序
    for item in datas:
        print(item,end=" ")
    print()        

# 主程式
datas=[3,5,2,1]  
print("排序前：",end=" ")
disp_data() # 顯示排序前串列
n=len(datas)-1 # 串列長度-1

for i in range(0,n): 
    for j in range(0,n-i):         
        if (datas[j]>datas[j+1]): # 由小到大排序
            datas[j],datas[j+1]=datas[j+1],datas[j] # 兩數互換

print("排序後：",end=" ")  
disp_data()  # 顯示排序後串列 

print("------------------------------------------------------------")  # 60個

def disp_data(): # 顯示串列的自訂程序
    for item in datas:
        print(item,end=" ")
    print()        

# 主程式
datas=[3,5,2,1]  
print("排序前：",end=" ")
disp_data() # 顯示排序前串列
n=len(datas)-1 # 串列長度-1

for i in range(0,n): 
    for j in range(0,n-i):      
        print("i=%d j=%d" %(i,j))
        if (datas[j]>datas[j+1]): # 由大到小排序
            print("%d,%d 互換後" %(datas[j],datas[j+1]) ,end="：")
            datas[j],datas[j+1]=datas[j+1],datas[j] # 兩數互換
        print(datas)

print("排序後：",end=" ")  
disp_data()  # 顯示排序後串列 

print("------------------------------------------------------------")  # 60個

dict1 = {"春季":"暖和", "夏季":"炎熱", "秋季":"涼爽", "冬季":"寒冷"}
name = "春季"
feeling = dict1.get(name)
if feeling == None:  
    print("沒有「" + name + "」季節！")
else:  
    print(name + "的天氣為 " + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

dict1 = {"電視":15000, "冰箱":23000, "冷氣":28000}
name = "冰箱"
if name in dict1:  
    print(name + "的價格為 " + str(dict1[name]))
else:  
    price = input("輸入電器價格：")
    dict1[name] = price
    print("字典內容：" + str(dict1))

print("------------------------------------------------------------")  # 60個

dict1 = {"水瓶座":"活潑善變", "雙魚座":"迷人保守", "白羊座":"天生勇者", "金牛座":"熱情敏感"}
item1 = dict1.items()
for name, nature in item1:
    print("%s 的性格特癥為 %s" % (name, nature))

print("------------------------------------------------------------")  # 60個

dict1 = {"水瓶座":"活潑善變", "雙魚座":"迷人保守", "白羊座":"天生勇者", "金牛座":"熱情敏感"}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("%s 的性格特癥為 %s" % (listkey[i], listvalue[i]))

print("------------------------------------------------------------")  # 60個

ret = divmod(10000, 350)
print("可維持生活 " + str(ret[0]) + " 天")
print("生活費剩餘 " + str(ret[1]) + " 元")

print("------------------------------------------------------------")  # 60個

listname = ["鍾明達", "鄭廣月", "何美麗"]
list1 = [34210, 23600, 145000, 54300]
list2 = [9000, 23900, 83400, 132000]
list3 = [186500, 127800, 100000, 45000]
list4 = [78900, 125000, 90000, 8000]
print("姓名       第一季  第二季  第三季   第四季")
for i in range(0,3):
    print(listname[i].ljust(5), str(list1[i]).rjust(7), str(list2[i]).rjust(7), str(list3[i]).rjust(7), str(list4[i]).rjust(7))

print("------------------------------------------------------------")  # 60個

import random

list1 = random.sample(range(0,10), 4)
list1.sort()
print("本期四星彩中獎號碼為：", end="")
for i in range(0,4):
    if i == 3:    print(str(list1[i]))
    else:    print(str(list1[i]), end=", ")

print("------------------------------------------------------------")  # 60個

def disp_data(): # 顯示串列的自訂程序
    for item in datas:
        print(item,end=" ")
    print()        

# 主程式
datas=datas=[2,3,5,7,1]  
print("排序前：",end=" ")
disp_data() # 顯示排序前串列
n=len(datas)-1 # 串列長度-1

for i in range(0,n): 
    for j in range(0,n-i):         
        if (datas[j]<datas[j+1]): # 由大到小排序
            datas[j],datas[j+1]=datas[j+1],datas[j] # 兩數互換

print("排序後：",end=" ")  
disp_data()  # 顯示排序後串列 

print("------------------------------------------------------------")  # 60個

monthname = {1:'JAN', 2:'FEB', 3:'MAR', 4:'APR', 5:'MAY', 6:'JUN', 7:'JUL', 8:'AUG', 9:'SEP', 10:'OCT', 11:'NOV', 12:'DEC'}
m = 3
print("{}月份的英文簡寫為 {}：".format(m, monthname[m]))

print("------------------------------------------------------------")  # 60個

cnum = {0:"零", 1:"壹", 2:"貮", 3:"參", 4:"肆", 5:"伍", 6:"陸", 7:"柒", 8:"捌", 9:"玖"}
num = "1234"
for n in num:
    print(cnum[int(n)], end="")

print("------------------------------------------------------------")  # 60個

dict1 = {"台北市":6, "新北市":2, "桃園市":5, "台中市":8, "台南市":3, "高雄市":9}
name = "新北市"
PM25 = dict1.get(name)
if PM25 == None:  
    print("六都中沒有「" + name + "」城市！")
else:  
    print(name + " 今天的 PM2.5 值為：" + str(dict1[name]))

print("------------------------------------------------------------")  # 60個

dict1 = {"鼠":"親切和藹", "牛":"保守努力", "虎":"熱情大膽", "兔":"溫柔仁慈"}
for name, nature in dict1.items():
    print("生肖屬 %s 的性格特癥為 %s" % (name, nature))

print("------------------------------------------------------------")  # 60個

rate = {'USD':28.02, 'JPY':0.2513, 'CNY':4.24}
TWD = float("123.456")
print("台幣{:.2f}元等於美金{:.2f}元, 日幣{:.2f}元, 人民幣{:.2f}元".format(TWD, TWD/rate['USD'], TWD/rate['JPY'], TWD/rate['CNY']))

print("------------------------------------------------------------")  # 60個

import random
print("產生N個 從 MIN 到 MAX 不重複的整數(包含頭尾)")
N = 7
MIN = 1
MAX = 50
list1 = random.sample(range(MIN, MAX), N)
print(type(list1))
print(list1)
list1 = random.sample(range(MIN, MAX), N)
print(list1)
list1 = random.sample(range(MIN, MAX), N)
print(list1)
list1 = random.sample(range(MIN, MAX), N)
print(list1)
list1 = random.sample(range(MIN, MAX), N)
print(list1)

print("------------------------------------------------------------")  # 60個

N = 10
MIN = 80
MAX = 100
scores = random.sample(range(MIN, MAX), N)
print("原成績：", scores)

print("人數：%d" % len(scores))
print("最高分為：%d" % max(scores))
print("最低分為：%d" % min(scores))
print("總分為：%d" % sum(scores))
print("平均為：%6.2f" % (sum(scores)/N))

scores2=sorted(scores,reverse=True) # 由大到小排序
print("成績由大到小排序：",scores2)

scores2=sorted(scores,reverse=False) # 由小到大排序
print("成績由小到大排序：",scores2) 

print("------------------------------------------------------------")  # 60個

N = 10
MIN = 80
MAX = 100
scores = random.sample(range(MIN, MAX), N)

def disp_scores(): # 顯示串列的自訂程序
    for score in scores:
        print(score,end=" ")
    print()

print("排序前：",end=" ")
disp_scores()   # 顯示排序前串列

n=len(scores)-1 # 串列長度-1

for i in range(0,n): 
    for j in range(0,n-i):         
        if (scores[j]<scores[j+1]): # 由大到小排序
            scores[j],scores[j+1]=scores[j+1],scores[j] # 兩數互換    

print("成績由大到小排序：",end="") 
disp_scores() # 顯示排序後串列

print("------------------------------------------------------------")  # 60個


sys.exit()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

animals = ["鼠","牛","虎","兔","龍"]

print("動物有：", animals)

animal = "豬"
n = animals.count(animal) 
if (n>0):  # 串列元素存在
    p=animals.index(animal)
    print("%s 在串列中的第 %d 項" %(animal,p+1))
    animals.remove(animal)
else:
    print(animal,"不在串列中!, 加入此動物")
    animals.append(animal)

print("動物有：", animals)

print("------------------------------------------------------------")  # 60個

dict1={"金牌":26, "銀牌":34, "銅牌":30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("得到的 %s 數目為 %d 面" % (listkey[i], listvalue[i]))


print("------------------------------------------------------------")  # 60個

names=["David","Lily","Chiou","Bear","Shantel","Cynthia"]

n=len(names)-1 # 串列長度-1
for i in range(0,n): 
    for j in range(0,n-i):         
        if (names[j]>names[j+1]): # 由小到大排序
            names[j],names[j+1]=names[j+1],names[j] # 互換  
print("------------------------------------------------------------")  # 60個

print("姓名    成績")
print("%-4s  %3d" % (name1, score1))
print("%-4s  %3d" % (name2, score2))

'''
print("------------------------------------------------------------")  # 60個

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("------------------------------------------------------------")  # 60個

# 過度擬合 (overfitting)

# 拉格朗日 (Lagrange) 插值法

x = np.linspace(0, 1, 200)
y = -((x - 1) ** 2) + 1
plt.plot(x, y, "lime")

X = np.linspace(0, 1, 20)
Y = -((X - 1) ** 2) + 1 + 0.08 * np.random.randn(20)
plt.scatter(X, Y, c="b", s=50)

z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x), "r")

xmin, xmax, ymin, ymax = 0, 1, 0, 1.5
plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍

plt.show()

print("------------------------------------------------------------")  # 60個

"""
#【秘技】分列 X, Y 的變成點座標

等一下我們會大量的把資料變換形式, 現在我們先熱身。在畫圖時常常用到把 x, y 座標分列。現在我們要合成點要怎麼做呢? 也就是說
X1 <-- [1,2,3,4]
Y1 <-- [5,6,7,8]
希望變成
[[1,5], [2,6], [3,7], [4,8]]
"""

X1 = np.array([1, 2, 3, 4])
Y1 = np.array([5, 6, 7, 8])

# NumPy 有個神奇的方式會幫我們做!

ccc = np.c_[X1, Y1]
print(ccc)

"""
【重要插播】meshgrid 用法

為了用 contourf (填充型的等高線) 呈現我們成果, 我們要介紹一個初學有點難理解、meshgrid 的概念。

meshgrid 是產生格點的方式, 通常是我們要畫 3D 曲面啦、或是等高線的時候要先為我們在 xy 平面上「佈點」, 然後算出每點的高度 Z。

我們要做的是給定 x 方向座標, y 方向座標, 然後就產生格點, 如圖示。
"""


# 於是我們再度用我們的 X1, Y1 示範。

X1 = np.array([1, 2, 3, 4])

Y1 = np.array([5, 6, 7, 8])

# 因為 matplotlib 很愛 x, y-座標分開, 經 meshgrid 後也是分開的! 所以我們用 Xm 和 Ym 來接。

Xm, Ym = np.meshgrid(X1, Y1)

# 看一下內容...

print(Xm)
print(Ym)

# 等等, 這什麼啊? 原來 meshgrid 存網格的 x 座標是一列一列存的。
# 同理我們可以理解 Ym 的內容為什麼是這樣了...

print("------------------------------------------------------------")  # 60個

# 01 numpy 的 filter

egg = np.array([3, -5, 10, 23, -5, 11])
idx = egg >= 0
print(idx)
# array([ True, False,  True,  True, False,  True])

print(egg[idx])
# array([ 3, 10, 23, 11])

print(egg[egg >= 0])
# array([ 3, 10, 23, 11])

x = np.linspace(-10, 10, 1000)
y = np.sin(x)
plt.plot(x, y)
plt.scatter(x[y > 0], y[y > 0], c="r")
plt.show()

# 02 Overfitting
Px = np.random.rand(6)
Py = np.random.rand(6)
plt.scatter(Px, Py, c="r", s=50)
plt.show()

x = np.linspace(0, 1, 1000)
y = 0.5 * np.sin(x) + 0.5
plt.scatter(Px, Py, c="r", s=50)
plt.plot(x, y)
plt.show()


def myplot(n=1):
    y = 0.5 * np.sin(n * x) + 0.5
    plt.scatter(Px, Py, c="r", s=50)
    plt.plot(x, y)


myplot(3)
plt.show()


print("------------------------------------------------------------")  # 60個


# 要平均值 μ, 標準差 σ 的時候呢?

μ = 87

σ = 2.5

eggs = np.random.randn(100) * σ + μ

# 我們來檢查這樣生出的平均值、標準差是不是我們想的那樣。

print("平均值 :", eggs.mean())

# 87.3032349761459

print("標準差 :", eggs.std())

# 2.411544933383249

import seaborn as sns

sns.distplot(eggs)
plt.show()


print("------------------------------------------------------------")  # 60個


# lambda: 臨時要使用的函數
currency = 32.1357851  # 1美元 = 32.13台幣    台灣銀行 現金賣出價

price = [100, 500, 1000]  # 美元

ll = list(map(lambda x: currency * x, price))
print("換算成台幣 :", ll)

usb2twd = lambda x: currency * x

print(usb2twd(1000))


# print(f"1 美元合台幣 {c:.2f} 元。")
# print(f"1 美元合台幣 {c:10.2f} 元。")

print("------------------------------------------------------------")  # 60個


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, s, r):
        self.suit = s
        self.rank = r

    def show(self):
        print(self.SUITS[self.suit] + self.RANKS[self.rank])


card01 = Card(2, 3)
card01.show()

print("------------------------------------------------------------")  # 60個

"""
import matplotlib as mpl
import matplotlib.font_manager as fm

for f in mpl.font_manager.fontManager.ttflist:
    print(f.name)

#[f.name for f in mpl.font_manager.fontManager.ttflist]

print('matplotlib 真的「看到的」字型')
for f in fm.fontManager.ttflist:
    print(f.name)
"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
