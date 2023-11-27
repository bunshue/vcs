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
import matplotlib.pyplot as plt

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  

mpl.rcParams['axes.unicode_minus'] = False 

df=pd.read_excel('1129-0900.xlsx') #2018/11/29日早上9點00分的資料

df.plot()

plt.show()


cc = df.info()
print(cc)

cc = df.describe()
print(cc)

sns.pairplot(df)

plt.show()

sns.pairplot(df, vars=['PM2.5', 'AQI','WindSpeed'],kind='reg')

plt.show()


cc = df.corr()
print(cc)


pic=df.plot(kind = 'scatter', x = 'WindSpeed', y = 'PM2.5', title = '風速與PM2.5之關係') #風速越小，PM2.5指數越高
plt.show()

pic=df.plot(kind = 'scatter', x = 'WindSpeed', y = 'AQI', title = '風速與AQI之關係')
plt.show()

pic=df.plot(kind = 'scatter', x = 'PM2.5', y = 'AQI', title = 'PM2.5指數與AQI之關係') #PM2.5指數與AQI似乎出現正相關
plt.show()

df.plot(kind='kde')
plt.show()

plt.scatter(df['WindSpeed'],df['PM2.5'],color='red')
plt.show()


plt.scatter(df['WindSpeed'],df['AQI'],color='blue')
plt.show()

plt.scatter(df['WindSpeed'],df['PM2.5'],color='red')
plt.show()

plt.scatter(df['WindSpeed'],df['AQI'],color='blue')
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

