# -*- coding: utf-8 -*- 
 
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
