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

'''
filename = 'AQI_20231124.csv'

df = pd.read_csv(filename)

print(df.head())

print(len(df))

print(df.describe())

print(df['aqi'])

#print(df[(df.aqi < 30)&(df.wind_speed>2)])


#mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 指定默认字体：解决plot不能显示中文问题
#mpl.rcParams['axes.unicode_minus'] = False 
df.plot(x='sitename', y=['aqi'])

plt.show()



print(df['aqi'])


print(df.sort_index(ascending=True).head())


print(df.sort_index(ascending=False).head())

print(df.shape)

print(df.mean())

AQI_filter = df['aqi']>60

YYY=df[AQI_filter]

print(YYY.head())


from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 指定默认字体：解决plot不能显示中文问题

mpl.rcParams['axes.unicode_minus'] = False 

pic=df.plot(kind = 'scatter', x = 'pm10', y = 'aqi', title = 'PM10指數與AQI之關係')

plt.show()

print(pic)

print(df.corr())

print('------------------------------------------------------------')	#60個

filename = 'AQI_20231124b.csv'
df = pd.read_csv(filename)

print(df['pm2.5'])


from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams['axes.unicode_minus'] = False 

#wind_speed有缺資料

pic=df.plot(kind = 'scatter', x = 'wind_speed', y = 'pm2.5',c='aqi',title = 'PM2.5指數與AQI與風速之關係')

plt.show()

print(pic)


from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  
# 指定默認字形：解決plot不能顯示中文問題
mpl.rcParams['axes.unicode_minus'] = False 
pic1=df.plot(kind = 'scatter', x = 'wind_speed', y = 'aqi',title = '風速與AQI與之關係')
print(pic1)

plt.show()
'''
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

filename = 'AQI_20231124.xls'

df = pd.read_excel(filename)


print(df.head(12))

print(df.dtypes)

print(df.describe())

print(df.corr())

#df.plot(x='監測月份', y=['pm2.5'],title='2017年度鳳山區PM2.5變化圖')
#df.plot(x='監測月份', y=['PM10'],title='2017年度鳳山區PM10變化圖')

"""
df.plot(x='監測月份', y=['SO2'],title='2017年度鳳山區SO2變化圖')
df.plot(x='監測月份', y=['CO'],title='2017年度鳳山區CO變化圖')
df.plot(x='監測月份', y=['O3'],title='2017年度鳳山區O3變化圖')


df.plot(kind='scatter',x='PM10', y='pm2.5',title='PM2.5與PM10的關係')
df.plot(kind='scatter',x='NO', y='pm2.5',title='PM2.5與NO的關係')
df.plot(kind='scatter',x='no2', y='pm2.5',title='PM2.5與no2的關係')
df.plot(kind='scatter',x='O3', y='pm2.5',title='PM2.5與O3的關係')
df.plot(kind='scatter',x='CO', y='pm2.5',title='PM2.5與CO的關係')
df.plot(kind='scatter',x='SO2', y='pm2.5',title='PM2.5與SO2的關係')


df.plot(kind='scatter',x='TEMP', y='pm2.5',title='PM2.5與溫度的關係')
df.plot(kind='scatter',x='RAIN', y='pm2.5',title='PM2.5與降雨的關係')
df.plot(kind='scatter',x='Humidity', y='pm2.5',title='PM2.5與濕度的關係')
df.plot(kind='scatter',x='WIND_SPEED', y='pm2.5',title='PM2.5與風速的關係')


"""


#plt.show()



print('------------------------------------------------------------')	#60個

#正相關 PM10和PM2.5

filename = 'AQI_20231124.csv'

df = pd.read_csv(filename)

sns.lmplot(x='pm10',y='pm2.5',data=df)
plt.show()

#正相關 NO和PM2.5
sns.lmplot(x='no',y='pm2.5',data=df)
plt.show()


#正相關 NO2和PM2.5
sns.lmplot(x='no2',y='pm2.5',data=df)
plt.show()

#正相關 O3和PM2.5
sns.lmplot(x='o3',y='pm2.5',data=df)
plt.show()

#正相關 CO和PM2.5
sns.lmplot(x='co',y='pm2.5',data=df)
plt.show()

#正相關 SO2和PM2.5
sns.lmplot(x='so2',y='pm2.5',data=df)
plt.show()

#NOX,THC,NMCH,CH4和PM2.5皆呈現正相關
sns.lmplot(x='nox',y='pm2.5',data=df)
#sns.lmplot(x='THC',y='pm2.5',data=df)
#sns.lmplot(x='NMHC',y='pm2.5',data=df)
#sns.lmplot(x='CH4',y='pm2.5',data=df)

plt.show()


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


