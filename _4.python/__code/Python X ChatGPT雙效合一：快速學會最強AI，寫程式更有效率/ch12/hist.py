# -*- coding: utf-8 -*- 
 
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=18

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100],edgecolor = 'b') 
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')
plt.show()
