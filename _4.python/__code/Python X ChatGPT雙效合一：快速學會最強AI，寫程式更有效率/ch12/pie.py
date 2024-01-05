# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

x = [26,12,21,25,35]
labels = '高雄','花蓮','台中','澎湖','宜蘭'
explode = (0.2, 0, 0, 0,0)
plt.pie(x,labels=labels, explode=explode, autopct='%.1f%%',
        shadow=True)

plt.show()
