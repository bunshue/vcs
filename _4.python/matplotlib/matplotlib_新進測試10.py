import os
import sys
import time
import random

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

import matplotlib.pyplot as plt

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

import matplotlib.pyplot as plt

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

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y)
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y, lw=8, ls='-.')
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y, marker='*')
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y, marker='D',ms=10, mfc='y', mec='r')
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y)
plt.plot(x, y, color='y')
#plt.plot(x, y, color=(1,1,0))  #RGB
#plt.plot(x, y, color='# FFFF00')  #HEX
#plt.plot(x, y, color='yellow')  #英文全名
#plt.plot(x, y, color='0.5')
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

x = [89,58,63,50]
labels = '高雄','台中','宜蘭','花蓮'
explode = (0.1, 0, 0, 0)
plt.pie(x,labels=labels, explode=explode, autopct='%.1f%%', shadow=True)

plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

#橫條圖
def diagram_1(s,x):
	plt.barh(x, s)

#圓餅圖
def diagram_2(s,x):	 
	plt.pie(s,labels=x, autopct='%.2f%%')
#折線圖+長條圖

def diagram_4(s,x):
    plt.plot(x, s, marker='.')
    plt.bar(x, s, alpha=0.5)	

#長條圖
def diagram_3(s,x):
	plt.bar(x, s)	

#要繪圖的數據
x = ['高雄','台中','宜蘭','花蓮']
s = [89,58,63,50]

#設定子圖
plt.figure(1, figsize=(8, 8),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(221)
diagram_1(s,x)

plt.subplot(222)
diagram_2(s,x)

plt.subplot(223)
diagram_3(s,x)

plt.subplot(2,2,4)
diagram_4(s,x)

plt.show()

