# -*- coding: utf-8 -*- 

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
