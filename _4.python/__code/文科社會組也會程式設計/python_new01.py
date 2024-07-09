
"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個

#chap7-02j

import requests
import csv
import pandas as pd

#如果要將csv擋下載後讀取要 import io
#from io import StringIO
county="屏東縣"

url = 'https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=9e273741-dad9-4c98-86cc-73e75137f66c&sort=ImportDate%20desc&format=csv'
#方法1:下載檔案後儲存，再開啟檔案讀出
#res = requests.get(url)
#open('data.csv','wb').write(res.content)
#df=pd.read_csv('data.csv')
#方法2:直接讀取網站的檔案
df=pd.read_csv(url)
#查看有那些欄位
df.info()
#只保留SiteName、County、AQI、Status四個欄位
df.drop(['SiteId','Longitude','Latitude','PublishTime','SO2_AVG', 'Pollutant', 'SO2', 'CO', 'NO', 'CO_8hr', 'O3', 'O3_8hr', 'PM10', 'PM10_AVG', 'PM2.5', 'PM2.5_AVG', 'NO2', 'NOx', 'WindSpeed', 'WindDirec'],inplace=True,axis=1)
#設定過濾條件
indexNames=df[df['County']!=county].index
#刪除所有不是臺北市的偵測站
df.drop(indexNames,inplace=True)
#重設索引值
df=df.reset_index(drop=True)
#列出該縣市所有偵測站狀態
print(county,"空氣品質狀態")
for i in range(len(df)):
  print(df.loc[i,'SiteName'],'(',df.loc[i,'Status'],")")
indexNames=df[df['Status']=='良好'].index
df.drop(indexNames,inplace=True)
#重設索引值
df=df.reset_index(drop=True)
#列出該縣市所有為達良好之偵測站
print()
print(county,"空氣品質未達良好之偵測站")
for i in range(len(df)):
  print(df.loc[i,'SiteName'],'(',df.loc[i,'Status'],")")


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


