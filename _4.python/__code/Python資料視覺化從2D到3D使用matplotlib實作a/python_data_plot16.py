"""

# plot 集合
第16章：箱線圖

"""

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


#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch16\ch16_0.py

# ch16_0.py
import numpy as np

x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35,
     38, 38, 41, 42, 43, 46, 46, 48, 52, 70]
rtn = np.percentile(x,np.arange(0,100,25))
Q1 = rtn[1]
mean = rtn[2]
Q3 = rtn[3]
IQR = Q3 - Q1
print(f"回傳值 = {rtn}")
print(f"最小值 = {Q1-1.5*IQR}")
print(f"  Q1   = {Q1}")
print(f" mean  = {mean}")
print(f"  Q3   = {Q3}")
print(f"最大值 = {Q3+1.5*IQR}")





      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch16\ch16_3.py

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data1 = np.random.normal(80, 30, 250) 
data2 = np.random.normal(90, 50, 250) 
data3 = np.random.normal(100, 20, 250) 
data4 = np.random.normal(75, 40, 250) 
data5 = np.random.normal(60, 35, 250)
data = [data1, data2, data3, data4, data5] 
labels = ['data1','data2','data3','data4','data5']
plt.boxplot(data,labels=labels)
plt.title("5 組數據的箱線圖",fontsize=16,color='b')

plt.show() 
      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch16\ch16_4.py

# ch16_4.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data1 = np.random.normal(80, 30, 250) 
data2 = np.random.normal(90, 50, 250) 
data3 = np.random.normal(100, 20, 250) 
data4 = np.random.normal(75, 40, 250) 
data5 = np.random.normal(60, 35, 250)
data = [data1, data2, data3, data4, data5] 
labels = ['data1','data2','data3','data4','data5']
plt.boxplot(data,labels=labels,sym='b',patch_artist=True)
plt.title("5 組數據的箱線圖",fontsize=16,color='b')
plt.show() 



      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch16\ch16_5.py

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data1 = np.random.normal(80, 30, 250) 
data2 = np.random.normal(90, 50, 250) 
data3 = np.random.normal(100, 20, 250) 
data4 = np.random.normal(75, 40, 250) 
data5 = np.random.normal(60, 35, 250)
data = [data1, data2, data3, data4, data5] 
labels = ['data1','data2','data3','data4','data5']
my_mark = dict(markerfacecolor='r',marker='o')
plt.boxplot(data,labels=labels,flierprops=my_mark)
plt.title("5 組數據的箱線圖",fontsize=16,color='b')

plt.show() 
     

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch16\ch16_6.py

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data1 = np.random.normal(80, 30, 250) 
data2 = np.random.normal(90, 50, 250) 
data3 = np.random.normal(100, 20, 250) 
data4 = np.random.normal(75, 40, 250) 
data5 = np.random.normal(60, 35, 250)
data = [data1, data2, data3, data4, data5] 
labels = ['data1','data2','data3','data4','data5']
my_mark = dict(markeredgecolor='g',markerfacecolor='g',marker='*')
plt.boxplot(data,labels=labels,flierprops=my_mark)
plt.title("5 組數據的箱線圖",fontsize=16,color='b')
plt.show() 



      

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch16\ch16_14.py

# ch16_14.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10) 
data1 = np.random.randn(1000) 
data2 = np.random.randn(1000) 
data3 = np.random.randn(1000) 
data = [data1, data2, data3] 
labels = ['data1','data2','data3']
plt.boxplot(data,labels=labels,notch=True)
plt.title("notch=True 的箱線圖",fontsize=16,color='b')
plt.show() 



      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch16\ch16_15.py

# ch16_15.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10)
# 建立 3 組數據
data = [np.random.randn(1000) for x in range(1,4)]
labels = ['x1','x2','x3']
# 建立子圖
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(9,5))
# 建立正常的箱形圖盒子
box1 = ax[0].boxplot(data,
                     patch_artist=True, # 含顏色
                     labels=labels)     # x 軸標記
ax[0].set_title('預設箱線圖盒子')
# 建立缺口箱線圖盒子
box2 = ax[1].boxplot(data,
                     notch=True,        # 缺口
                     patch_artist=True, # 含顏色
                     labels=labels)     # x 軸標記
ax[1].set_title('缺口箱線圖盒子')
# 箱線盒填上顏色
colors = ['lightgreen', 'yellow', 'aqua']
for box in (box1,box2):
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
# 建立水平軸線
for ax in [ax[0], ax[1]]:
    ax.yaxis.grid(True)
    ax.set_xlabel('3 組數據')
    ax.set_ylabel('觀察值')
plt.show() 


      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch16\ch16_18.py

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(20) 
x1 = np.random.randn(1000) 
x2 = np.random.randn(1000) 
x3 = np.random.randn(1000) 
x4 = np.random.randn(1000) 
x = [x1, x2, x3, x4]
# 建立箱線圖
bp = plt.boxplot(x,patch_artist=True,notch ='True') 
colors = ['green','m','yellow','b'] 
# 設定盒子
for patch, color in zip(bp['boxes'],colors):
    patch.set_facecolor(color) 
# 更改晶鬚樣式 
for whisker in bp['whiskers']:
    whisker.set(color ='g',linewidth=2,linestyle =":") 
# 更改帽子樣式 
for cap in bp['caps']:
    cap.set(color ='b', linewidth = 2) 
# 更改中位數樣式 
for median in bp['medians']:
    median.set(color ='g', linewidth = 3) 
# 更改異常值樣式 
for flier in bp['fliers']:
    flier.set(marker='D',markerfacecolor='g',markeredgecolor='g') 
plt.title("使用回傳物件更新樣式") 
plt.show()

  
      

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


