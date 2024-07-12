"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
'''

import requests

url ='https://www.dcard.tw/f/stock/p/237123381'
response = requests.get(url)
print(response.text)


print('chap7-02a')
import requests
url ='https://www.dcard.tw/f/stock/p/237123381'
res = requests.get(url)
print(res.text)

#chap7-01b
import requests
url ='http://jigsaw.w3.org/HTTP/connection.html'
response = requests.get(url)
#print(response.text)

#在<HEAD></HEAD>區塊中取得包圍網頁標題的指定字串<TITLE></TITLE>所在的位置
#stripe()去除字串頭尾的'\n'(換行)、'\t'(跳格)、' '(空白)
datapos1=response.text.find("<TITLE>")
datapos2=response.text.find("</TITLE>")
data=response.text[datapos1+7:datapos2]
data=data.strip()
print("網頁的<TITLE> :", data)
#在<BODY></BODY>區塊中取得包圍內容標題的指定字串<H1></H1>所在的位置
datapos1=response.text.find("<H1>")
datapos2=response.text.find("</H1>")
data=response.text[datapos1+4:datapos2]
#將設定斜體的HTML語法<I></I>移除
data=data.replace("<I>","")
data=data.replace("</I>","")
data=data.strip()
print("<網頁的H1的資料(去掉<I>)> :", data)


datapos1=response.text.find("<CODE>")
datapos2=response.text.find("</CODE>")
data=response.text[datapos1+7:datapos2]
data=data.strip()
print("網頁的<CODE> :", data)



print("------------------------------------------------------------")  # 60個

print('chap7-02b')
import requests
from bs4 import BeautifulSoup
url ='https://www.dcard.tw/f/stock/p/237123381'
response = requests.get(url)
#指定html.parser作為解析器
soup = BeautifulSoup(response.text, 'html.parser') 
#把排版後的html印出來，因為未排版前有很多網頁語法缺乏換行符號，不易閱讀
#必須借助於Beautiful Shop套件
print(soup.prettify())

print("------------------------------------------------------------")  # 60個

print('chap7-02c')
import requests
from bs4 import BeautifulSoup
url = 'https://www.dcard.tw/f/stock/p/237123381'


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36" #使用者代理
    }

#response = requests.get(url="https://example.com", headers=headers)
response = requests.get(url, headers=headers)
#指定html.parser作為解析器
soup = BeautifulSoup(response.text, 'html.parser') 
#把排版後的html印出來
#print(soup.prettify())
a_tags = soup.find_all('h1')
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print("\n")

print("------------------------------------------------------------")  # 60個

print('chap7-02d')

import requests
from bs4 import BeautifulSoup
url = 'https://www.dcard.tw/f/stock/p/237123381'
res = requests.get(url)
#指定html.parser作為解析器
soup = BeautifulSoup(res.text, 'html.parser') 
#把排版後的html印出來
#print(soup.prettify()) 
a_tags = soup.find_all('h1')
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print("\n")
a_tags = soup.find_all('div',limit=1)
a_tag=a_tags[0]
cc=""
for b in a_tag.contents:
  if str(b).find("gFINpq")>=0:  
    b=str(b).replace('\n','').replace('\r','')
    cc=cc+b
print(cc.strip())

print("------------------------------------------------------------")  # 60個

print('chap7-02e')

import requests
from bs4 import BeautifulSoup
url = 'https://www.dcard.tw/f/stock/p/237123381'
res = requests.get(url)
#指定html.parser作為解析器
soup = BeautifulSoup(res.text, 'html.parser') 
#把排版後的html印出來
#print(soup.prettify()) 
a_tags = soup.find_all('h1')
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print()
a_tags = soup.find_all('div',limit=1)
a_tag=a_tags[0]
cc=""
for b in a_tag.contents:
  if str(b).find("gFINpq")>=0:  
    b=str(b)
    cc=cc+b
cc=cc.strip()
data=">>>>>原Po文章\n"
#尋找前四筆，第一個是原Po文章，後三個則為熱門留言
for j in range(4):
  #尋找最附近的<div class>有gFINpq
  datapos1=cc.find("gFINpq")
  #只保留這個字串以後的文字
  cc=cc[datapos1:] 
  while True:
    #尋找最附近的<span
    datapos1=cc.find("<span")
    #只保留<span以後的文字
    cc=cc[datapos1:]
    #尋找最附近的>
    datapos1=cc.find(">")
    #尋找最附近的</span> 
    datapos2=cc.find("</span>")
    #如果<span></span>中間出現了enUbOQ，表示這個步驟該結束了 
    if cc[:datapos2].find("enUbOQ")>=0:
      break   
    #如果<span></span>有資料，就合併在data字串裡 
    if datapos1+1<datapos2:
      #但是<span></span>的資料，如果還有span就不行了
      if cc[datapos1+1:datapos2].find("span")<0:       
        data=data+cc[datapos1+1:datapos2]+"\n" 
    #只保留</span>之後的文字    
    cc=cc[datapos2+7:]
  #後三個是熱門留言
  if j<3:
    data=data+"\n*******熱門留言"+str(j+1)+":\n"  
print(data)

print("------------------------------------------------------------")  # 60個

print('chap7-02f')

import requests
import json
import pandas as pd
postid = '237123381'
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data=res.json() #方法2
#查看有哪些欄位
print(data.keys())
#因為只有一欄，而且沒有欄位名稱
#否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data,orient="index")
#查看有哪些內容
print(df)

print("------------------------------------------------------------")  # 60個

print('chap7-02g')

import requests
import json
import pandas as pd
postid = '237123381'
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data=res.json() #方法2
#因為只有一欄，而且沒有欄位名稱
#否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data,orient="index")
#取出title、content內容
print(">>>>>文章標題")
print(df.loc["title",0])
print()
print(">>>>>原Po文章")
print(str(df.loc["content",0]).strip())
print("------------------------------------------------------------")  # 60個

print('chap7-02h')

import requests
import json
import pandas as pd
from datetime import datetime
postid = '237123381'
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data = res.json() #方法2
#因為只有一欄，而且沒有欄位名稱
#否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data,orient="index")
#取出title、content內容
print(">>>>>文章標題")
print(df[0]["title"])
print()
print(">>>>>原Po文章\n")
print(str(df[0]["content"]).strip())
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid+'/comments?popular=True'
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data = res.json() #方法2
#因為有欄位名稱
#只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
#取出前3筆資料
for i in range(3):
  print("*******熱門留言"+str(i)+":")
  print(df.loc[i,"content"])
  #將最後修改文字日期轉換成日期  
  updatedate=datetime.fromisoformat(str(df.loc[i,"updatedAt"]).replace("Z",""))
  #計算現在和最後修改日期的時間差
  datediff=datetime.today()-updatedate
  #顯示幾天前有最新留言
  print(datediff.days,"天前")
  print()
#若要查看有哪些欄位
print((df.keys()))
#也可以透過df.info()查看
df.info()
#也可以直接看前幾列
df.head(3)

print("------------------------------------------------------------")  # 60個

print('chap7-02i')

import requests
import json
import pandas as pd
from datetime import datetime
postid = '237123381'
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data = res.json() #方法2
#因為只有一欄，而且沒有欄位名稱
#否則只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame.from_dict(data,orient="index")
#取出title、content內容
print(">>>>>文章標題")
print(df[0]["title"])
print()
print(">>>>>原Po文章\n")
print(str(df[0]["content"]).strip())
url = 'https://www.dcard.tw/service/api/v2/posts/'+postid+'/comments'
res = requests.get(url)
#有兩種方法，下面兩行任選一種都可以
#data = json.loads(res.text) #方法1
data = res.json() #方法2
#因為有欄位名稱
#只要 df = pd.DataFrame(data) 即可
df = pd.DataFrame(data)
#除了updatedAt, content, likeCount三個欄位以外，全部刪除
#刪除欄依定要指定axis=1 
#inplace=True真實刪除
df.drop(['id', 'anonymous', 'postId', 'createdAt', 'floor',
    'withNickname', 'hiddenByAuthor', 'meta',
    'gender', 'school', 'host', 'reportReason', 'mediaMeta', 'hidden',
    'inReview', 'reportReasonText', 'isSuspiciousAccount', 'isModerator',
    'doorplate', 'edited', 'postAvatar', 'activityAvatar', 'verifiedBadge',
    'memberType', 'enablePrivateMessage', 'department'],inplace=True,axis=1)
#依據likeCout內容排序，以降序排列
df.sort_values(by='likeCount', inplace=True, ascending=False)
#要記得重設index，這樣df.loc[]的結果才會正確
df = df.reset_index(drop=True)
#取出前3筆資料
for i in range(3):
  print("*******熱門留言"+str(i)+":")
  print(df.loc[i,"content"])
  #將最後修改文字日期轉換成日期  
  updatedate=datetime.fromisoformat(str(df.loc[i,"updatedAt"]).replace("Z",""))
  #計算現在和最後修改日期的時間差
  datediff=datetime.today()-updatedate
  #顯示幾天前有最新留言
  print(datediff.days,"天前")
  print()
#若要查看有哪些欄位
print((df.keys()))
#也可以透過df.info()查看
df.info()
#也可以直接看前幾列
df.head(3)
'''

print("------------------------------------------------------------")  # 60個

print('chap7-02j')

import requests
import csv
import pandas as pd
#如果要將csv擋下載後讀取要 import io
#from io import StringIO
county="屏東縣"
url = 'https://data.epa.gov.tw/api/v1/aqx_p_432?limit=1000&api_key=keykeykey&sort=ImportDate%20desc&format=csv'
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

