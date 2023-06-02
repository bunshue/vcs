# Python 測試 BeautifulSoup
#解讀 遠端 網頁資料, 都是使用 html.parser 解析器

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import re
import os
import sys
import csv
import time
import json
import urllib
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)    # 用 requests 的 get 方法把網頁抓下來

    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

def get_soup_from_url(url):
    html_data = get_html_data1(url)
    if html_data == None:
        print('無法取得網頁資料')
        sys.exit(1)	#立刻退出程式

    html_data.encoding = 'UTF-8' # 或是 unicode 也可, 指定編碼方式
    soup = BeautifulSoup(html_data.text, "html.parser")  # 解析原始碼
    #soup = BeautifulSoup(html_data.text, "lxml") # 指定 lxml 作為解析器
    #print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
    print("取得網頁標題", soup.title)
    return soup
    
print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 1')


# Python 測試 BeautifulSoup Yahoo電影 台北票房榜

import ssl
from urllib import request, parse

#urlopen https時需要驗證一次SSL證書，
#當網站目標使用自簽名的證書時就會跳出錯誤
#使用SSL module把證書驗證改成不需要驗證
#context = ssl._create_unverified_context()

url = 'https://movies.yahoo.com.tw/chart.html'
req_obj = request.Request(url)

''' 有問題
#with request.urlopen(req_obj,context=context) as res_obj:
with request.urlopen(req_obj) as res_obj:
    html_data = res_obj.read()
    html_data = html_data.decode('utf-8')
    print(html_data)
    soup = BeautifulSoup(html_data, 'html.parser')
    print(soup.prettify())
    
    rows = soup.find_all('div', class_ = 'tr')

    colname = list(rows.pop(0).stripped_strings)
    contents = []
    for row in rows:
        thisweek_rank = row.find_next('div' , attrs={'class' : 'td'})
        updown = thisweek_rank.find_next('div')
        lastweek_rank = updown.find_next('div')

        if thisweek_rank.string == str(1):
            movie_title = lastweek_rank.find_next('h2')
        else:
            movie_title = lastweek_rank.find_next('div' , attrs={'class' : 'rank_txt'})

        release_date = movie_title.find_next('div' , attrs={'class' : 'td'})
        trailer = release_date.find_next('div' , attrs={'class' : 'td'})

        if trailer.find('a') is None:
            trailer_address = ''
        else:
            trailer_address = trailer.find('a')['href']

        starts = row.find('h6' , attrs={'class' : 'count'})
        lastweek_rank = lastweek_rank.string if lastweek_rank.string else ''

        c = [thisweek_rank.string , lastweek_rank , movie_title.string , release_date.string , trailer_address , starts.string]
        print('加入: ', c)
        contents.append(c)

print(contents)
'''

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 2')

filename = 'C:/_git/vcs/_1.data/______test_files2/kkbox_songs.csv'

# KKBOX華語新歌日榜
url = "https://kma.kkbox.com/charts/api/v1/daily?category=390&lang=tc&limit=50&terr=tw&type=newrelease"

# 取得歌曲資訊json檔
html_data = requests.get(url)
# print(html_data.status_code)
# print(html_data.text)

# 將json字串轉為Python的字典型態
data = json.loads(html_data.text)
song_list = data["data"]["charts"]["newrelease"]

#印10筆資料就好
cnt = 0
with open(filename, 'w', newline = '', encoding = "big5") as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    # 寫入一列資料
    writer.writerow(["排名", "歌名", "作者", "發行日期", "連結"])
    # 取得每首歌的排名、曲名、連結、作者、時間
    for song in song_list:
        song_rank = song["rankings"]["this_period"]
        song_name = song["song_name"]
        song_url = song["song_url"]
        song_artist = song["artist_name"]
        song_timestamp = int(song["release_date"])
        # 從timestamp轉為日期格式
        song_date = time.strftime("%Y-%m-%d", time.localtime(song_timestamp))

        print("排名:", song_rank)
        print("歌名:", song_name)
        print("作者:", song_artist)
        print("發行日期:", song_date)
        print("連結:", song_url)

        writer.writerow([song_rank, song_name, song_artist.encode('utf-8'), song_date, song_url])

        # # 從歌曲連結取得歌詞
        # song_response = requests.get(song_url)
        # soup = BeautifulSoup(song_response.text, "html.parser")
        # lyric = soup.find("div", class_="lyrics").text
        # print("歌詞:", lyric)

        print("-" * 30)
        cnt += 1
        if cnt == 10:
            break;

print('將資料寫入檔案 : ' + filename)
print('OK')



print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 3')


# Python 測試 BeautifulSoup 好樂迪 K歌排行
import ssl
from urllib import request, parse
import pandas as pd

#urlopen https時需要驗證一次SSL證書，
#當網站目標使用自簽名的證書時就會跳出錯誤
#使用SSL module把證書驗證改成不需要驗證
#context = ssl._create_unverified_context()
# 使用 ssl 模組，避免遇到 CERTIFICATE_VERIFY_FAILED 錯誤
context = ssl._create_unverified_context()

# 給好樂迪的網址建立 Request
url = 'https://www.holiday.com.tw/SongInfo/SongList.aspx'
req_obj = request.Request(url)
''' 有問題
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
'''

print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 4')


    
'''
參考 https://ithelp.ithome.com.tw/articles/10186119

BeautifulSoup 套件 是 Python 上的 網頁解析工具
requests 套件允許我們發送與接收有機及草飼的 HTTP/1.1 請求（這真的是美式幽默。）
'''

import numpy as np
import pandas as pd


url = "https://www.ptt.cc/bbs/NBA/index.html" # PTT NBA 板

print('01. 印出網頁資料')
response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
print(soup.prettify()) # 把排版後的 html 印出來

print('02. 一些 BeautifulSoup 的屬性或方法')
response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
# 一些屬性或方法
print(soup.title) # 把 tag 抓出來
print("---")
print(soup.title.name) # 把 title 的 tag 名稱抓出來
print("---")
print(soup.title.string) # 把 title tag 的內容欻出來
print("---")
print(soup.title.parent.name) # title tag 的上一層 tag
print("---")
print(soup.a) # 把第一個 <a></a> 抓出來
print("---")
print(soup.find_all('a')) # 把所有的 <a></a> 抓出來

#Beautiful Soup 幫我們將 html 檔案轉換為 bs4 的物件，像是標籤（Tag），
#標籤中的內容（NavigableString）與 BeautifulSoup 物件本身。

print('03.')
response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(type(soup.a))
print("---")
print(soup.a.name) # 抓標籤名 a
print("---")
print(soup.a['id']) # 抓<a></a>的 id 名稱

print('04. 標籤中的內容（NavigableString）')

response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(type(soup.a.string))
print("---")
soup.a.string

print('05. BeautifulSoup')

response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, 'lxml') # 指定 lxml 作為解析器

type(soup)

print('06. 爬樹')

#DOM（Document Object Model）的樹狀結構觀念在使用 BeautifulSoup 扮演至關重要的角色，所以我們也要練習爬樹。
print('06a. 往下爬')
#從標籤中回傳更多資訊。

response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(soup.body.a.contents)
print(list(soup.body.a.children))
print(soup.body.a.string)

print('06b. 往上爬')
#回傳上一階層的標籤。

response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(soup.title)
print("---")
print(soup.title.parent)

print('06c. 往旁邊爬')
#回傳同一階層的標籤。

response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

first_a_tag = soup.body.a
next_to_first_a_tag = first_a_tag.next_sibling
print(first_a_tag)
print("---")
print(next_to_first_a_tag)
print("---")
print(next_to_first_a_tag.previous_sibling)

print('07a. 搜尋')
#這是我們主要使用 BeautifulSoup 套件來做網站解析的方法。
#find() 方法
#find_all() 方法

response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(soup.find("a")) # 第一個 <a></a>
print("---")
print(soup.find_all("a")) # 全部 <a></a>

print('07b. 可以在第二個參數 class_= 加入 CSS 的類別。')

response = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(soup.find("div", class_= "r-ent"))

print('08.')
#BeautifulSoup 牛刀小試

'''
大略照著官方文件練習了前面的內容之後，我們參考Tutorial of PTT crawler來應用 BeautifulSoup 把 PTT NBA 版首頁資訊包含推文數，作者 id，文章標題與發文日期搜集下來。

我們需要的資訊都放在 CSS 類別為 r-ent 的 <div></div> 中。
'''
response = requests.get(url)
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

posts = soup.find_all("div", class_ = "r-ent")
print(posts)
type(posts)


#注意這個 posts 物件是一個 ResultSet，一般我們使用迴圈將裡面的每一個元素再抓出來，先練習一下作者 id。

print('09.')

response = requests.get(url)
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

author_ids = [] # 建立一個空的 list 來放置作者 id
posts = soup.find_all("div", class_ = "r-ent")
for post in posts:
    author_ids.extend(post.find("div", class_ = "author"))

print(author_ids)

print('10. #接下來我們把推文數，文章標題與發文日期一起寫進去。')

response = requests.get(url)
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

author_ids = [] # 建立一個空的 list 來放作者 id
recommends = [] # 建立一個空的 list 來放推文數
post_titles = [] # 建立一個空的 list 來放文章標題
post_dates = [] # 建立一個空的 list 來放發文日期

posts = soup.find_all("div", class_ = "r-ent")
for post in posts:
    try:
        author_ids.append(post.find("div", class_ = "author").string)    
    except:
        author_ids.append(np.nan)
    try:
        post_titles.append(post.find("a").string)
    except:
        post_titles.append(np.nan)
    try:
        post_dates.append(post.find("div", class_ = "date").string)
    except:
        post_dates.append(np.nan)

# 推文數藏在 div 裡面的 span 所以分開處理
recommendations = soup.find_all("div", class_ = "nrec")
for recommendation in recommendations:
    try:
        recommends.append(int(recommendation.find("span").string))
    except:
        recommends.append(np.nan)

print(author_ids)
print(recommends)
print(post_titles)
print(post_dates)

print('11. ')
#檢查結果都沒有問題之後，那我們就可以把這幾個 list 放進 dictionary 接著轉換成 data frame 了。

response = requests.get(url)
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

author_ids = [] # 建立一個空的 list 來放作者 id
recommends = [] # 建立一個空的 list 來放推文數
post_titles = [] # 建立一個空的 list 來放文章標題
post_dates = [] # 建立一個空的 list 來放發文日期

posts = soup.find_all("div", class_ = "r-ent")
for post in posts:
    try:
        author_ids.append(post.find("div", class_ = "author").string)    
    except:
        author_ids.append(np.nan)
    try:
        post_titles.append(post.find("a").string)
    except:
        post_titles.append(np.nan)
    try:
        post_dates.append(post.find("div", class_ = "date").string)
    except:
        post_dates.append(np.nan)

# 推文數藏在 div 裡面的 span 所以分開處理
recommendations = soup.find_all("div", class_ = "nrec")
for recommendation in recommendations:
    try:
        recommends.append(int(recommendation.find("span").string))
    except:
        recommends.append(np.nan)
        
ptt_nba_dict = {"author": author_ids,
                "recommends": recommends,
                "title": post_titles,
                "date": post_dates
}

ptt_nba_df = pd.DataFrame(ptt_nba_dict)
ptt_nba_df

'''
old

print('BeautifulSoup 測試 4')

url = "https://www.ptt.cc/bbs/NBA/index.html" # PTT NBA 板
html_data = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = html_data.text # text 屬性就是 html 檔案
soup = BeautifulSoup(html_data.text, "lxml") # 指定 lxml 作為解析器
#print(soup.prettify()) # 把排版後的 html 印出來

# 一些屬性或方法
print(soup.title) # 把 tag 抓出來
print("---")
print(soup.title.name) # 把 title 的 tag 名稱抓出來
print("---")
print(soup.title.string) # 把 title tag 的內容欻出來
print("---")
print(soup.title.parent.name) # title tag 的上一層 tag
print("---")
print(soup.a) # 把第一個 <a></a> 抓出來
print("---")
print(soup.find_all('a')) # 把所有的 <a></a> 抓出來



'''







print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 5a')

#文淵閣工作室官網
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"
#print(html.text)   #many

print('BeautifulSoup 測試 5b')
#文淵閣工作室官網
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"

htmllist = html.text.splitlines()   #將網頁資料一行一行地分割成串列
''' many
for row in htmllist:
   print(row)
'''

print('BeautifulSoup 測試 5c')

#文淵閣工作室官網
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"

soup = BeautifulSoup(html.text,"html.parser")
links = soup.find_all("a") # 讀取 <a>
for link in links:
    href = link.get("href") # 讀取 href 屬性內容
    # 判斷內容是否為非 None，並且開頭文字是 http://
    if  href != None and href.startswith("http://"): 
        print(href)







print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 6')

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

print('BeautifulSoup 測試 7')

#url = 'https://pornav.co/'
url = 'https://www.deviantart.com/'

html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, 'html.parser')
        #print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

        print("取得網頁標題", soup.title)

        print('搜尋網頁中的 jpg圖片連結')
        ''' many
        regex = re.compile('.*\.jpg')
        imglist = soup.find_all("img", {"src":regex})
        for img in imglist:
            print(img["src"])
        '''
        
else:
        print('無法取得網頁資料')



print('BeautifulSoup 測試 作業完成')












print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 7')

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

print('#抓中央氣象局的衛星雲圖')


url = 'https://www.cwb.gov.tw/V8/C/W/OBS_Sat.html'

#TBD

'''
html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, 'html.parser')
        print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

        print("取得網頁標題", soup.title)

        print('搜尋網頁中的 jpg圖片連結')
        
        regex = re.compile('.*\.jpg')
        imglist = soup.find_all("img", {"src":regex})
        for img in imglist:
            print(img["src"])
        
else:
        print('無法取得網頁資料')
'''








print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 8')



import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

#某圖庫網站
url = 'https://www.dreamstime.com/free-images_pg1'

html = requests.get(url)
html.encoding="utf-8"

sp = BeautifulSoup(html.text, 'html.parser')

# 建立 images 目錄儲存圖片
images_dir="images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)
    
# 取得所有 <a> 和 <img> 標籤
all_links=sp.find_all(['a','img']) 
for link in all_links:
    # 讀取 src 和　href 屬性內容
    src=link.get('src')
    href = link.get('href')
    attrs=[src,href]
    for attr in attrs:
        # 讀取　.jpg 和　.png 檔
        if attr != None and ('.jpg' in attr or '.png' in attr):
            # 設定圖檔完整路徑
            full_path = attr            
            filename = full_path.split('/')[-1]  # 取得圖檔名
            print(full_path)
            # 儲存圖片
            try:
                image = urlopen(full_path)
                f = open(os.path.join(images_dir,filename),'wb')
                f.write(image.read())
                f.close()
            except:
                print("{} 無法讀取!".format(filename))



print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 9')





print('\n\nBeautifulSoup 測試 作業完成\n')

