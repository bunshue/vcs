import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import pandas as pd
import seaborn as sns

print('------------------------------------------------------------')	#60個

plt.style.use('fivethirtyeight')

#空氣盒子數據溫度與空污

#使用三種不同的資料

#df = pd.read_csv("200811-201811.csv")
#df=pd.read_excel('20160101-20190101(Daily).xlsx')
df=pd.read_excel('KH-1982-2018.xlsx')
cc = df.isnull().sum()
print(cc)

cc = df.head()
print(cc)

cc = df.describe()
print(cc)

ax=df.plot(kind='scatter',x='TEMP',y="PM25")

ax.set_title('TEMP v.s. PM25')
plt.show()

cc = df.corr()
print(cc)

print('------------------------------------------------------------')	#60個

""" NG

#pandas-profiling套件測試

#使用pandas_profiling模組分析並輸出成html

#高雄2008年至2018年之資料


import pandas_profiling

plt.style.use('fivethirtyeight')

df = pd.read_csv("200811-201811.csv")

profile = pandas_profiling.ProfileReport(df)

pandas_profiling.ProfileReport(df)

profile.to_file(outputfile="output.html")  #支援輸出html
"""

print('------------------------------------------------------------')	#60個

#空氣盒子數據PM25與各項因子之視覺化散布圖
#高雄1982至2018年之PM25與各氣象因子視覺化散布圖
#高雄2008至2018年之PM25與各氣象因子視覺化散布圖

#高雄1982年至2018年之資料 高雄2008年至2018年之資料

plt.style.use('fivethirtyeight')

#使用三種不同的資料

#df = pd.read_csv("200811-201811.csv")  #高雄2008年至2018年之資料
df=pd.read_excel('KH-1982-2018.xlsx')   #高雄1982年至2018年之資料

cc = df.isnull().sum()
print(cc)

cc = df.head()
print(cc)

cc = df.corr()
print(cc)

ax=df.plot(kind='scatter',x='TEMP',y="PM25")
ax.set_title('TEMP v.s. PM25')
plt.show()


ax=df.plot(kind='scatter',x='Humidity',y="PM25")
ax.set_title('Humidity v.s. PM25')
plt.show()


ax=df.plot(kind='scatter',x='WindSpeed',y="PM25")
ax.set_title('WindSpeed v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='CH4',y="PM25")
ax.set_title('CH4 v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='NMHC',y="PM25")
ax.set_title('NMHC v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='THC',y="PM25")
ax.set_title('THC v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='NO2',y="PM25")
ax.set_title('NO2 v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='NO',y="PM25")
ax.set_title('NO v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='Nox',y="PM25")
ax.set_title('Nox v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='PM25',y="PM25")
ax.set_title('PM25 v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='O3',y="PM25")
ax.set_title('O3 v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='CO',y="PM25")
ax.set_title('CO v.s. PM25')
plt.show()

ax=df.plot(kind='scatter',x='SO2',y="PM25")
ax.set_title('SO2 v.s. PM25')
plt.show()

heatmap = df.corr()
sns.heatmap(heatmap,cmap='coolwarm')
plt.show()

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

