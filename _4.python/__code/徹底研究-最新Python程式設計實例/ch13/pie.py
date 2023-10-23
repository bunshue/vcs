# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

x = [89,58,63,50]
labels = '高雄','台中','宜蘭','花蓮'
explode = (0.1, 0, 0, 0)
plt.pie(x,labels=labels, explode=explode, autopct='%.1f%%', shadow=True)

plt.show()
