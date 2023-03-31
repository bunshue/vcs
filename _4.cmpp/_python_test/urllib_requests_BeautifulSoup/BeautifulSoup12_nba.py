    
'''
參考 https://ithelp.ithome.com.tw/articles/10186119

BeautifulSoup 套件 是 Python 上的 網頁解析工具
requests 套件允許我們發送與接收有機及草飼的 HTTP/1.1 請求（這真的是美式幽默。）
'''

import requests
import requests as rq
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

url = "https://www.ptt.cc/bbs/NBA/index.html" # PTT NBA 板

print('01. 印出網頁資料')
response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器
print(soup.prettify()) # 把排版後的 html 印出來

print('02. 一些 BeautifulSoup 的屬性或方法')
response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
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
response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(type(soup.a))
print("---")
print(soup.a.name) # 抓標籤名 a
print("---")
print(soup.a['id']) # 抓<a></a>的 id 名稱

print('04. 標籤中的內容（NavigableString）')

response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(type(soup.a.string))
print("---")
soup.a.string

print('05. BeautifulSoup')

response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, 'lxml') # 指定 lxml 作為解析器

type(soup)

print('06. 爬樹')

#DOM（Document Object Model）的樹狀結構觀念在使用 BeautifulSoup 扮演至關重要的角色，所以我們也要練習爬樹。
print('06a. 往下爬')
#從標籤中回傳更多資訊。

response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(soup.body.a.contents)
print(list(soup.body.a.children))
print(soup.body.a.string)

print('06b. 往上爬')
#回傳上一階層的標籤。

response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(soup.title)
print("---")
print(soup.title.parent)

print('06c. 往旁邊爬')
#回傳同一階層的標籤。

response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
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

response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(soup.find("a")) # 第一個 <a></a>
print("---")
print(soup.find_all("a")) # 全部 <a></a>

print('07b. 可以在第二個參數 class_= 加入 CSS 的類別。')

response = rq.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

print(soup.find("div", class_= "r-ent"))

print('08.')
#BeautifulSoup 牛刀小試

'''
大略照著官方文件練習了前面的內容之後，我們參考Tutorial of PTT crawler來應用 BeautifulSoup 把 PTT NBA 版首頁資訊包含推文數，作者 id，文章標題與發文日期搜集下來。

我們需要的資訊都放在 CSS 類別為 r-ent 的 <div></div> 中。
'''
response = rq.get(url)
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

posts = soup.find_all("div", class_ = "r-ent")
print(posts)
type(posts)


#注意這個 posts 物件是一個 ResultSet，一般我們使用迴圈將裡面的每一個元素再抓出來，先練習一下作者 id。

print('09.')

response = rq.get(url)
html_doc = response.text # text 屬性就是 html 檔案
soup = BeautifulSoup(response.text, "lxml") # 指定 lxml 作為解析器

author_ids = [] # 建立一個空的 list 來放置作者 id
posts = soup.find_all("div", class_ = "r-ent")
for post in posts:
    author_ids.extend(post.find("div", class_ = "author"))

print(author_ids)

print('10. #接下來我們把推文數，文章標題與發文日期一起寫進去。')

response = rq.get(url)
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

response = rq.get(url)
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
import requests
from bs4 import BeautifulSoup

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
