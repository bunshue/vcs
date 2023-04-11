# Python 測試 BeautifulSoup

import sys
import requests
from bs4 import BeautifulSoup


import ssl
from urllib import request, parse
from bs4 import BeautifulSoup
import pandas as pd

# 使用 ssl 模組，避免遇到 CERTIFICATE_VERIFY_FAILED 錯誤
context = ssl._create_unverified_context()
# 給好樂迪的網址建立 Request
url = 'https://www.holiday.com.tw/SongInfo/SongList.aspx'
req_obj = request.Request(url)

song_list = []
# 發送 request
with request.urlopen(req_obj,context=context) as res_obj:
       # 將 response 讀回並用 utf8 decode 
	resp = res_obj.read().decode('utf-8')
        # 使用 html.parser
	soup = BeautifulSoup(resp , 'html.parser')
        # 用 find 找到 id 為 ctl00_ContentPlaceHolder1_dgSong 的 table 標籤，並回傳 table 內所有的 tr 內容
	rank_table = soup.find('table',id='ctl00_ContentPlaceHolder1_dgSong').find_all('tr')

        #由於要避開 table 的第一列 tr 資料以及最後一列 tr 資料，所以取 [1:-2] 
	for rt in rank_table[1:-2]:
               # 找到所有的 td 並取得第 5 個 td(index 是 4)
		song_name = rt.find_all('td')[4]
               # 找到第一個 a 這個標籤，因為只有歌手的資料被 a tag 包住
		singer = rt.find('a')
        # 把歌曲跟歌手的資料轉成 string 並去前後空白塞到一個 song_list
	song_list.append([song_name.string.strip(),singer.string.strip()])

# 把 song_list 使用 pandas 模組轉成 dataframe 用於後面資料分析
df = pd.DataFrame(song_list,columns=['song','singer'])
print(df)

print('BeautifulSoup 測試 作業完成')

