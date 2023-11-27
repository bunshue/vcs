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

print('各國PM2.5與溫度比較')

print('北京')

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_excel('BeijingPM20100101_20151231.xlsx')

cc = df.head()
print(cc)

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']  
mpl.rcParams['axes.unicode_minus'] = False

x=df['TEMP']
y=df['PM25']

plt.xlabel("溫度")                   #X軸名稱
plt.ylabel("PM2.5")                   #Y軸名稱
plt.title("北京PM2.5與溫度比較")                    #標題
plt.scatter(x,y)
plt.show()

print('瀋陽')

df=pd.read_excel('ShenyangPM20100101_20151231.xlsx')

x=df['TEMP']
y=df['PM25']

plt.xlabel("溫度")                   #X軸名稱
plt.ylabel("PM2.5")                   #Y軸名稱
plt.title("瀋陽PM2.5與溫度比較")                    #標題
plt.scatter(x,y)
plt.show()

""" fail
print('伊朗大不里士')

df=pd.read_excel('Abrasan.xlsx')

cc = df.head()
print(cc)

x=df['TEMP']
y=df['PM25']

plt.xlabel("溫度")                   #X軸名稱
plt.ylabel("PM2.5")                   #Y軸名稱
plt.title("大不里士PM2.5與溫度比較")                    #標題
plt.scatter(x,y)
plt.shop()
"""

"""
結論
綜合日本長崎大學的研究，以及所能蒐集到的數據來看，也許溫度與PM2.5呈現正相關，但是每個國家的情況不同，並沒有一個絕對的基準。
例如印度大部分地區溫度也都蠻高的，但是空汙也相當嚴重，這部分可能又須考量到當地的產業結構等相關問題。
"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

