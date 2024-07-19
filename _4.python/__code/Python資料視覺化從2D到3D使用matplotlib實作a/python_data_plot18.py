# plot 集合

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch18\ch18_1.py

# ch18_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
days = [1,2,3,4,5,6,7]                  # 設定日期
working = [5,4,6,5,8,4,3]               # 設定每天工作時間
playing =  [2,5,3,4,5,8,6]              # 設定每天玩手機的時間
labels = ['工作','玩手機']
xlabels = ['星期一','星期二','星期三','星期四',
           '星期五','星期六','星期日']
# 繪製堆疊折線圖
plt.stackplot(days,working,playing,labels=labels)
plt.xlabel('日期',fontsize=12,color='b')
plt.ylabel('時數',fontsize=12,color='b')
plt.title('繪製一週工作和玩手機的時間',fontsize=16,color='b')
plt.xticks(days,xlabels)
plt.legend(loc='upper left')
plt.show()





  
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch18\ch18_2.py

# ch18_2.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
days = [1,2,3,4,5,6,7]              # 設定日期
working = [8,8,9,8,8,2,2]           # 設定每天工作時間
playing = [4,5,3,8,6,12,10]         # 設定每天玩手機的時間
eating = [2,2,3,2,3,4,4]            # 設定每天吃飯時間
sleeping = [10,9,9,6,7,6,8]          # 設定每天睡眠時間
labels = ['工作','玩手機','吃飯','睡眠']
xlabels = ['星期一','星期二','星期三','星期四',
           '星期五','星期六','星期日']
colors = ['orange','lightgreen','yellow','lightblue']
# 繪製堆疊折線圖
plt.stackplot(days,working,playing,eating,sleeping,
              labels=labels,colors=colors)
plt.xlabel('日期',fontsize=12,color='b')
plt.ylabel('時數',fontsize=12,color='b')
plt.title('繪製一週時間分配圖',fontsize=16,color='b')
plt.xticks(days,xlabels)
plt.legend()
plt.show()





  
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch18\ch18_3.py

# ch18_3.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
x = np.linspace(0, 10, 10)
y1 = x
y2 = 1.5 * x + 1.5
y3 = 2.0 * x + 2
plt.stackplot(x, y1, y2, y3)
plt.xlim((0, 10))
plt.ylim((0, 60))
plt.title('基礎數學公式的堆疊',fontsize=16,color='b')
plt.show()





  
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch18\ch18_4.py

# ch18_4.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
population = {
    '非洲':[180, 200, 210, 230, 280],
    '歐洲':[300, 310, 340, 370, 410],
    '美洲':[290, 330, 350, 365, 380],
    '亞洲':[1200, 1250, 1300, 1600, 1900],
    '大洋洲':[88, 95, 110, 130, 150]
}
year = ['1980','1990','2000','2010','2020']
plt.stackplot(year,population.values(),labels=population.keys())
plt.legend(loc='upper left')
plt.xlabel('年度',color='b')
plt.ylabel('百萬人',color='b')
plt.title('世界人口統計',fontsize=16,color='b')
plt.show()





  
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch18\ch18_5.py

# ch18_5.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
days = [x for x in range(0, 7)]             # 一週時間    
suspected = [22, 25, 45, 58, 69, 82, 95]    # 疑似病例 
cured = [8, 12, 16, 25, 43, 56, 68]         # 康原病例
deaths = [2, 2, 6, 7, 10, 12, 13]           # 往生人數
colors = ['orange','green','red']
labels = ['疑似病例','康原病例','往生人數']
xlabels = ['星期一','星期二','星期三','星期四',
           '星期五','星期六','星期日']
# 建立堆疊折線圖
plt.stackplot(days, suspected,cured,deaths,colors=colors,
              labels=labels,baseline ='zero') 
plt.legend(loc='upper left') 
plt.title('病例數據統計資料',fontsize=16,color='b')
plt.xlabel('一週時間',fontsize=12,color='b')
plt.ylabel('全部病例數',fontsize=12,color='b')
plt.xticks(days,xlabels)
plt.show()





  
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch18\ch18_6.py

# ch18_6.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
days = [x for x in range(0, 7)]             # 一週時間    
suspected = [22, 25, 45, 58, 69, 82, 95]    # 疑似病例 
cured = [8, 12, 16, 25, 43, 56, 68]         # 康原病例
deaths = [2, 2, 6, 7, 10, 12, 13]           # 往生人數
colors = ['orange','green','red']
labels = ['疑似病例','康原病例','往生人數']
xlabels = ['星期一','星期二','星期三','星期四',
           '星期五','星期六','星期日']
# 建立堆疊折線圖
plt.stackplot(days, suspected,cured,deaths,colors=colors,
              labels=labels,baseline ='sym') 
plt.legend(loc='upper left') 
plt.title('病例數據統計資料',fontsize=16,color='b')
plt.xlabel('一週時間',fontsize=12,color='b')
plt.ylabel('全部病例數',fontsize=12,color='b')
plt.xticks(days,xlabels)
plt.show()





  
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch18\ch18_7.py

# ch18_7.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
days = [x for x in range(0, 7)]             # 一週時間    
suspected = [22, 25, 45, 58, 69, 82, 95]    # 疑似病例 
cured = [8, 12, 16, 25, 43, 56, 68]         # 康原病例
deaths = [2, 2, 6, 7, 10, 12, 13]           # 往生人數
colors = ['orange','green','red']
labels = ['疑似病例','康原病例','往生人數']
xlabels = ['星期一','星期二','星期三','星期四',
           '星期五','星期六','星期日']
# 建立堆疊折線圖
plt.stackplot(days, suspected,cured,deaths,colors=colors,
              labels=labels,baseline ='wiggle') 
plt.legend(loc='upper left') 
plt.title('病例數據統計資料',fontsize=16,color='b')
plt.xlabel('一週時間',fontsize=12,color='b')
plt.ylabel('全部病例數',fontsize=12,color='b')
plt.xticks(days,xlabels)
plt.show()





  
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch18\ch18_8.py

# ch18_8.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
days = [x for x in range(0, 7)]             # 一週時間    
suspected = [22, 25, 45, 58, 69, 82, 95]    # 疑似病例 
cured = [8, 12, 16, 25, 43, 56, 68]         # 康原病例
deaths = [2, 2, 6, 7, 10, 12, 13]           # 往生人數
colors = ['orange','green','red']
labels = ['疑似病例','康原病例','往生人數']
xlabels = ['星期一','星期二','星期三','星期四',
           '星期五','星期六','星期日']
# 建立堆疊折線圖
plt.stackplot(days, suspected,cured,deaths,colors=colors,
              labels=labels,baseline ='weighted_wiggle') 
plt.legend(loc='lower left') 
plt.title('病例數據統計資料',fontsize=16,color='b')
plt.xlabel('一週時間',fontsize=12,color='b')
plt.ylabel('全部病例數',fontsize=12,color='b')
plt.xticks(days,xlabels)
plt.show()





  
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch18\ch18_9.py

# ch18_9.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
months= ['1月','2月','3月','4月','5月','6月',
         '7月','8月','9月','10月','11月','12月']

cost = {
    '房屋貸款':[32000,31500,31000,30500,30000,29500, 
                29000,28500,28000,27500,27000,26500],
    '餐飲支出':[20000,18000,21000,23000,25000,30000, 
                24000,25000,28000,26000,21000,22000],
    '水電費用':[8500,8000,8500,9500,10000,11000, 
                10500,10000,8800,8900,9300,9200],
    '保險支出':[6000,6200,5500,5800,5900,6100, 
                4800,5200,6100,5900,4800,7000]
}
fig, ax = plt.subplots()
ax.set_title("家庭開銷統計",fontsize=16,color='b')
ax.set_xlabel("月份",fontsize=14,color='b')
ax.set_ylabel("費用",fontsize=14,color='b')
# 繪製家庭開銷堆疊折線圖
ax.stackplot(months,cost.values(),labels=cost.keys())
ax.legend()
plt.tight_layout()
plt.show()





  
      

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


