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


# 直方圖
x = np.random.rand(50, 2) # 產生共兩組，每組50個隨機數,
plt.hist(x)

plt.show()


print("------------------------------------------------------------")  # 60個


