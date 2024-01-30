# matplotlib_新進測試13_pie

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
import time
import random

print("------------------------------------------------------------")  # 60個
'''

#派圖
data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
explode = (0, 0.1, 0, 0)  # 向外擴展顯示的區域
plt.pie(data.values(), explode=explode, labels=data.keys(), autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal') # 設置餅圖爲正圓形

plt.show()

print("------------------------------------------------------------")  # 60個

#sorts = ["Travel","Entertainment","Education","Transporation","Food"]
sorts = [u"交通",u"娛樂",u"教育",u"交通",u"餐費"]

fee = [8000,2000,3000,5000,6000]
          
plt.pie(fee,labels=sorts,explode=(0,0.2,0,0,0),
        autopct="%1.2f%%")      # 繪製圓餅圖

plt.show()
'''
print("------------------------------------------------------------")  # 60個

plt.rcParams['font.size']=12

x = [26,12,21,25,35]
labels = '高雄','花蓮','台中','澎湖','宜蘭'   #tuple格式
print(type(labels))
explode = (0.2, 0, 0, 0, 0)
plt.pie(x,labels=labels, explode=explode, autopct='%.1f%%', shadow=True)

plt.show()

print("------------------------------------------------------------")  # 60個


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

count = [1,1,1,1,1,1,1,1,1,1,1,1]
names = '鼠','牛','虎','兔','龍','蛇', '馬','羊','猴','雞','狗','豬'
explode = (0, 0.1, 0, 0.2, 0, 0.3, 0, 0.4, 0, 0.5, 0, 0.6)
plt.pie(count,labels=names, explode=explode, autopct='%.1f%%',
        shadow=True)

plt.show()


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


