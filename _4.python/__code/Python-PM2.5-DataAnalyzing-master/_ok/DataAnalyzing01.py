

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

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

