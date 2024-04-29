
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

df = pd.read_csv("200811-201811.csv")

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  

# 指定默認字形：解決plot不能顯示中文問題

mpl.rcParams['axes.unicode_minus'] = False

print(df.head(10))

cc = len(df)
print(cc)

cc = df.describe()
print(cc)

cc = df.nlargest(3,'PM25')
print(cc)

cc = df.nsmallest(3,'PM25')
print(cc)

df = df.drop(labels=['SO2','CO'],axis='columns') #刪除SO2和CO這兩個欄位

cc = df.head()
print(cc)

dfSort=df.sort_values(by='PM25',ascending=False)
cc = dfSort.head(20)
print(cc)

df[['WindSpeed','TEMP']]#顯示Columns(列)為AQI及WindSpeed的數據

cc = df[df.O3<15]
print(cc)

cc = df[(df.PM25 < 30)&(df.TEMP>30)] #列出PM2.5值大於30且溫度大於30的數值
print(cc)

df.plot(kind = 'scatter', x = 'TEMP', y = 'PM25', title = '溫度與PM2.5之關係')

plt.show()

#df.to_csv('New_Data.csv',encoding='utf8')  #存檔至New_Data.csv中
#df.to_excel('New_Data.xlsx', encoding='utf8')#存檔至New_Data.xlsx

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

