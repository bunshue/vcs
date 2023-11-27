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

pd.set_option("display.max_rows", 1000)  #設定最大能顯示1000rows

pd.set_option("display.max_columns", 1000)  #設定最大能顯示1000columns

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 指定默認字形：解決plot不能顯示中文問題

mpl.rcParams['axes.unicode_minus'] = False

sns.set_context('notebook')

df=pd.read_excel('2017_PM25.xlsx')

cc = df.head(12)
print(cc)

print(df.dtypes)

print(df.describe())

print(df.corr())

df.plot(x='監測月份', y=['PM25'],title='2017年度鳳山區PM2.5變化圖')
plt.show()

df.plot(x='監測月份', y=['PM10'],title='2017年度鳳山區PM10變化圖')
plt.show()

df.plot(x='監測月份', y=['SO2'],title='2017年度鳳山區SO2變化圖')
plt.show()

df.plot(x='監測月份', y=['CO'],title='2017年度鳳山區CO變化圖')
plt.show()

df.plot(x='監測月份', y=['O3'],title='2017年度鳳山區O3變化圖')
plt.show()

df.plot(kind='scatter',x='PM10', y='PM25',title='PM2.5與PM10的關係')
plt.show()

df.plot(kind='scatter',x='NO', y='PM25',title='PM2.5與NO的關係')
plt.show()

df.plot(kind='scatter',x='NO2', y='PM25',title='PM2.5與NO2的關係')
plt.show()

df.plot(kind='scatter',x='O3', y='PM25',title='PM2.5與O3的關係')
plt.show()

df.plot(kind='scatter',x='CO', y='PM25',title='PM2.5與CO的關係')
plt.show()

df.plot(kind='scatter',x='SO2', y='PM25',title='PM2.5與SO2的關係')
plt.show()

df.plot(kind='scatter',x='TEMP', y='PM25',title='PM2.5與溫度的關係')
plt.show()

df.plot(kind='scatter',x='RAIN', y='PM25',title='PM2.5與降雨的關係')
plt.show()

df.plot(kind='scatter',x='Humidity', y='PM25',title='PM2.5與濕度的關係')
plt.show()

df.plot(kind='scatter',x='WIND_SPEED', y='PM25',title='PM2.5與風速的關係')
plt.show()

#正相關 PM10和PM2.5
sns.lmplot(x='PM10',y='PM25',data=df)
plt.title('正相關 PM10和PM2.5')
plt.show()

#正相關 NO和PM2.5
sns.lmplot(x='NO',y='PM25',data=df)
plt.title('正相關 NO和PM2.5')
plt.show()

#正相關 NO2和PM2.5
sns.lmplot(x='NO2',y='PM25',data=df)
plt.title('正相關 NO2和PM2.5')
plt.show()

#正相關 O3和PM2.5
sns.lmplot(x='O3',y='PM25',data=df)
plt.title('正相關 O3和PM2.5')
plt.show()

#正相關 CO和PM2.5
sns.lmplot(x='CO',y='PM25',data=df)
plt.title('正相關 CO和PM2.5')
plt.show()

#正相關 SO2和PM2.5
sns.lmplot(x='SO2',y='PM25',data=df)
plt.title('正相關 SO2和PM2.5')
plt.show()

#NOX,THC,NMCH,CH4和PM2.5皆呈現正相關

#正相關 NOX和PM2.5
sns.lmplot(x='Nox',y='PM25',data=df)
plt.title('正相關 NOX和PM2.5')
plt.show()

#正相關 THC和PM2.5
sns.lmplot(x='THC',y='PM25',data=df)
plt.title('正相關 THC和PM2.5')
plt.show()

#正相關 NMHC和PM2.5
sns.lmplot(x='NMHC',y='PM25',data=df)
plt.title('正相關 NMHC和PM2.5')
plt.show()

#正相關 CH4和PM2.5
sns.lmplot(x='CH4',y='PM25',data=df)
plt.title('正相關 CH4和PM2.5')
plt.show()

#負相關 溫度和PM2.5
sns.lmplot(x='TEMP',y='PM25',data=df)
plt.title('負相關 溫度和PM2.5')
plt.show()

#負相關 雨量和PM2.5
sns.lmplot(x='RAIN',y='PM25',data=df)
plt.title('負相關 雨量和PM2.5')
plt.show()

#負相關 濕度和PM2.5
sns.lmplot(x='Humidity',y='PM25',data=df)
plt.title('負相關 濕度和PM2.5')
plt.show()

#負相關 風速和PM2.5
sns.lmplot(x='WIND_SPEED',y='PM25',data=df)
plt.title('負相關 風速和PM2.5')
plt.show()

#負相關 降雨量和PM2.5
sns.lmplot(x='RAIN_COND',y='PM25',data=df)
plt.title('負相關 降雨量和PM2.5')
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

