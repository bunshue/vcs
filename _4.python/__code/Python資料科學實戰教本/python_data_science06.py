import sys
import json 
import requests

print("------------------------------------------------------------")  # 60個

url = "https://www.googleapis.com/books/v1/volumes?maxResults=5&q=Python&projection=lite"
jsonfilename = "tmp_GoogleBooks.json"
r = requests.get(url)
r.encoding = "utf8"
json_data = json.loads(r.text)
with open(jsonfilename, 'w') as fp:
    json.dump(json_data, fp)
    print('json 存檔完成, 檔案 :', jsonfilename)

print("------------------------------------------------------------")  # 60個

import requests

""" momo 網站 無 headers, 不可抓取
URL = "https://www.momoshop.com.tw/search/"

r = requests.get(URL+"searchShop.jsp?keyword=NBA")
if r.status_code == requests.codes.ok:
    r.encoding = "big5"
    print(r.text)        
else:
    print("HTTP請求錯誤..." + URL)

"""
print("------------------------------------------------------------")  # 60個

import requests

print('使用 headers 抓取 momo 網站')

URL="https://www.momoshop.com.tw/search/"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
           'AppleWebKit/537.36 (KHTML, like Gecko)'
           'Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get(URL+"searchShop.jsp?keyword=NBA", headers=headers)
if r.status_code == requests.codes.ok:
    r.encoding = "big5"    
    print(r.text)        
else:
    print("HTTP請求錯誤..." + URL)

print("------------------------------------------------------------")  # 60個

""" webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL="https://www.momoshop.com.tw/search/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(URL+"searchShop.jsp?keyword=NBA")
print("-----------------------------")
print(driver.title)
html = driver.page_source
fp = open("tmp_NBA.html", "w", encoding="utf8")
fp.write(html)
print("寫入檔案tmp_NBA.html...")
fp.close()
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

""" wait long
import time
import requests

URL = "http://www.majortests.com/word-lists/word-list-0{0}.html"

for i in range(1, 10):
    url = URL.format(i) 
    r = requests.get(url)
    print(r.status_code)
    print("等待5秒鐘... i = ", i)
    time.sleep(5) 
"""

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

URL = "https://www.ptt.cc/bbs/NBA/index6503.html"
DELETED = BeautifulSoup("<a href='Deleted'>本文已刪除</a>", "lxml").a

r = requests.get(URL)
if r.status_code == requests.codes.ok:
    r.encoding = "utf8"
    soup = BeautifulSoup(r.text, "lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        tag_a = tag.find("a") or DELETED
        print(tag_a["href"])
        print(tag_a.text)
        print(tag.find("div", class_="author").string)
else:
    print("HTTP請求錯誤..." + URL)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

URL = "https://www.ptt.cc/bbs/Gossiping/index.html"

r = requests.get(URL, cookies={"over18": "1"})
if r.status_code == requests.codes.ok:
    r.encoding = "utf8"
    soup = BeautifulSoup(r.text, "lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        if tag.find('a'): # 是否有<a>標籤
            tag_a = tag.find("a")
            print(tag_a["href"])
            print(tag_a.text)
            print(tag.find("div", class_="author").string)
else:
    print("HTTP請求錯誤..." + URL)

print("------------------------------------------------------------")  # 60個

from urllib.parse import urljoin

URL = "http://www.majortests.com/word-lists/word-list-01.html"
PTT = "https://wwww.ptt.cc/bbs/movie/index.html"

catalog = ["movie", "NBA", "Gossiping"]

for i in range(1, 5):
    url = urljoin(URL, "world-list-0{0}.html".format(i)) 
    print(url)
print("-----------------")
for item in catalog:
    url = urljoin(PTT, "../{0}/index.html".format(item))
    print(url)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
import csv, re

URL = "https://movies.yahoo.com.tw/movie_intheaters.html"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
           "AppleWebKit/537.36 (KHTML, like Gecko)"
           "Chrome/63.0.3239.132 Safari/537.36"}

def format_date(date):  # 取出上映日期
    if not date: return "N/A"
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date.text)
    if match is None:
        return date.text
    else:
        return match.group(0)    

def get_text(tag):
    if tag:
        return tag.text.strip()
    else:
        return "N/A"
 
def get_attrib(tag, attrib):
    if tag:
        return tag[attrib].strip()
    else:
        return "N/A"

""" fail    
movies = [["中文片名","英文片名","期待度","海報圖片","上映日"]]
r = requests.get(URL, headers=headers)
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'lxml')
    tag_ul = soup.find("ul", class_="release_list")
    rows = tag_ul.find_all("li")
    for row in rows:
        name_div = row.find("div",class_="release_movie_name")
        cht_n = get_text(name_div.find("a"))
        eng_n = get_text(name_div.find("div",class_="en").find("a"))
        expect = get_text(row.find("div",class_="leveltext").find("span"))
        photo_div = row.find("div",class_="release_foto")
        poster_url = get_attrib(photo_div.find("img"),"data-src")
        date = row.find('div',class_='release_movie_time')
        release_date = format_date(date)
        movie= [cht_n,eng_n,expect,poster_url,release_date]
        movies.append(movie)
else:
   print("HTTP請求錯誤...")

with open("tmp_movies.csv", "w+",newline="",encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in movies:
        writer.writerow(item)
"""
print("------------------------------------------------------------")  # 60個

""" webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json

URL = "https://fchart.github.io/Ashion/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(URL)

soup = BeautifulSoup(driver.page_source, "lxml")
sec = soup.find("section", class_="product spad")
items = sec.find_all("div", class_="product__item")
print(len(items))
products=[]
for item in items:
    tag = item.find("h6").find("a")
    title = tag.text.strip() if tag else "N/A"
    tag = item.find("div", class_="product__item__pic")
    img = tag["data-setbg"].strip() if tag else "N/A"
    tag = item.find("div", class_="product__price")
    price = tag.text.strip() if tag else "N/A"
    print(title)
    products.append({
        "title": title,
        "image": URL+img,
        "price": price
    })
driver.quit()
with open("tmp_products.json", "w", encoding="utf-8") as fp: # 寫入JSON檔案
    json.dump(products,fp,indent=2,
              sort_keys=True,
              ensure_ascii=False)
"""

print("------------------------------------------------------------")  # 60個

import requests 
from bs4 import BeautifulSoup
import csv

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
csvfile = "tmp_xrt.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one("#ie11andabove > div > table")
rows = tag_table.find_all("tr")
with open(csvfile,'w+',newline='',encoding="big5") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").
                       replace("\r","").
                       strip())
        writer.writerow(lst)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
import csv, re, time

URL = "https://movies.yahoo.com.tw/movie_intheaters.html/?page={0}"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
           "AppleWebKit/537.36 (KHTML, like Gecko)"
           "Chrome/63.0.3239.132 Safari/537.36"}
 
def format_date(date):  # 取出上映日期
    if not date: return "N/A"
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date.text)
    if match is None:
        return date.text
    else:
        return match.group(0)    

def get_text(tag):
    if tag:
        return tag.text.strip()
    else:
        return "N/A"
 
def get_attrib(tag, attrib):
    if tag:
        return tag[attrib].strip()
    else:
        return "N/A"   
""" fail
all_movies = [["中文片名","英文片名","期待度","海報圖片","上映日"]]
for page in range(1, 11):
    url = URL.format(page)
    print("抓取: 第" + str(page) + "頁 網路資料中...")
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        movies = []
        tag_ul = soup.find("ul", class_="release_list")
        rows = tag_ul.find_all("li")
        for row in rows:
            name_div = row.find("div",class_="release_movie_name")
            cht_n = get_text(name_div.find("a"))
            eng_n = get_text(name_div.find("div",class_="en").find("a"))
            expect = get_text(row.find("div",class_="leveltext").find("span"))
            photo_div = row.find("div",class_="release_foto")
            poster_url = get_attrib(photo_div.find("img"),"data-src")
            date = row.find('div',class_='release_movie_time')
            release_date = format_date(date)
            movie= [cht_n,eng_n,expect,poster_url,release_date]
            movies.append(movie)
        all_movies = all_movies + movies
        if soup.find("li", class_="nexttxt disabled"):
            break   # 已經沒有下一頁
        print("等待5秒鐘...")   
        time.sleep(5) 
    else:
        print("HTTP請求錯誤...")

with open("all_movies.csv", "w+",newline="",encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in all_movies:
        writer.writerow(item)
"""

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
import csv, re, time

URL = "https://movies.yahoo.com.tw/movie_intheaters.html/?page=1"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
           "AppleWebKit/537.36 (KHTML, like Gecko)"
           "Chrome/63.0.3239.132 Safari/537.36"}
 
def format_date(date):  # 取出上映日期
    if not date: return "N/A"
    pattern = '\d+-\d+-\d+'
    match = re.search(pattern, date.text)
    if match is None:
        return date.text
    else:
        return match.group(0)    

def get_text(tag):
    if tag:
        return tag.text.strip()
    else:
        return "N/A"
 
def get_attrib(tag, attrib):
    if tag:
        return tag[attrib].strip()
    else:
        return "N/A"  

""" fail
all_movies = [["中文片名","英文片名","期待度","海報圖片","上映日"]]
page = 1
while True:
    print("抓取: 第" + str(page) + "頁 網路資料中...")
    page = page + 1
    r = requests.get(URL, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'lxml')
        movies = []
        tag_ul = soup.find("ul", class_="release_list")
        rows = tag_ul.find_all("li")
        for row in rows:
            name_div = row.find("div",class_="release_movie_name")
            cht_n = get_text(name_div.find("a"))
            eng_n = get_text(name_div.find("div",class_="en").find("a"))
            expect = get_text(row.find("div",class_="leveltext").find("span"))
            photo_div = row.find("div",class_="release_foto")
            poster_url = get_attrib(photo_div.find("img"),"data-src")
            date = row.find('div',class_='release_movie_time')
            release_date = format_date(date)
            movie= [cht_n,eng_n,expect,poster_url,release_date]
            movies.append(movie)
        all_movies = all_movies + movies
        if soup.find("li", class_="nexttxt disabled"):
            break   # 已經沒有下一頁
        nextPage = soup.find("li", class_="nexttxt")   
        if nextPage:
            URL = nextPage.find("a")["href"] 
            print("等待5秒鐘...")          
            time.sleep(5)
        else:
            break
    else:
        print("HTTP請求錯誤...")

with open("tmp_all_movies2.csv", "w+",newline="",encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in all_movies:
        writer.writerow(item)
"""
print("------------------------------------------------------------")  # 60個

""" webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time, csv

URL="https://fchart.github.io/ML/nba_items.html"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(URL)
pages_remaining = True
page_num = 1
while pages_remaining:
    soup = BeautifulSoup(driver.page_source, "lxml")
    tag_table = soup.select_one("#our-table")
    rows = tag_table.find_all("tr")
    csvfile = "tmp_NBA_Products" + str(page_num) + ".csv"
    with open(csvfile, 'w+', newline='', encoding="utf8") as fp:
        writer = csv.writer(fp)
        for row in rows:
            lst = []
            for cell in row.find_all(["td", "th"]):
                lst.append(cell.text.replace("\n","").
                           replace("\r","").
                           strip())
            writer.writerow(lst)
    print("儲存頁面:", page_num)
    try:   
        next_link = driver.find_element(By.CLASS_NAME, "nextbtn")
        if next_link:
            next_link.click()
            time.sleep(5)
            page_num = page_num + 1
        else:
            pages_remaining = False
    except Exception:
        pages_remaining = False        
driver.close()
"""
print("------------------------------------------------------------")  # 60個

import time
import requests
import json
from bs4 import BeautifulSoup

# 目標URL網址
URL = "https://www.ptt.cc"
MAX_PUSH = 50
# TOPIC = "Gossiping"
TOPIC = "NBA" 

def get_resource(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
    return requests.get(url, headers=headers, cookies={"over18":"1"})

def parse_html(r):
    if r.status_code == requests.codes.ok:
        r.encoding = "utf8"
        soup = BeautifulSoup(r.text, "lxml")        
    else:
        print("HTTP請求錯誤..." + url)
        soup = None
    
    return soup    

def get_articles(soup, date):
    articles = []  
    # 取得上一頁的超連結
    paging_div = soup.find("div", class_="btn-group btn-group-paging")
    paging_a = paging_div.find_all("a", class_="btn")
    prev_url = paging_a[1]["href"]

    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        # 判斷文章的日期
        if tag.find("div",class_="date").text.strip() == date:
            push_count = 0    # 取得推文數
            push_str = tag.find("div", class_="nrec").text
            if push_str:
                try:
                    push_count = int(push_str)  # 轉換成數字
                except ValueError:  # 轉換失敗，可能是'爆'或 'X1','X2'
                    if push_str == '爆':
                        push_count = 99
                    elif push_str.startswith('X'):
                        push_count = -10
            # 取得貼章的超連結和標題文字
            if tag.find("a"):  # 有超連結，表示文章存在
                href = tag.find("a")["href"]
                title = tag.find("a").text
                author = tag.find("div", class_="author").string 
                articles.append({
                    "title": title,
                    "href": href,
                    "push_count": push_count,
                    "author": author
                })
    
    return articles, prev_url

def save_to_json(articles, file):
    print("今天總共有: " + str(len(articles)) + " 篇文章")
    threshold = MAX_PUSH
    print("熱門文章(> %d 推): " % (threshold))
    for item in articles:   # 顯示熱門文章清單
        if int(item["push_count"]) > threshold:
            print(item["title"], item["href"], item["author"])    
    with open(file, "w", encoding="utf-8") as fp: # 寫入JSON檔案
        json.dump(articles,fp,indent=2,sort_keys=True,ensure_ascii=False)

def web_scraping_bot(url):
    articles = []
    print("抓取網路資料中...")
    soup = parse_html(get_resource(url))
    if soup:
        # 取得今天日期, 去掉開頭'0'符合PTT的日期格式
        today = time.strftime("%m/%d").lstrip('0') 
        # 取得目前頁面的今日文章清單
        current_articles, prev_url = get_articles(soup, today) 
        while current_articles: 
            articles += current_articles
            print("等待2秒鐘...")
            time.sleep(2) 
             # 剖析上一頁繼續尋找是否有今日的文章
            soup = parse_html(get_resource(URL + prev_url))
            current_articles, prev_url = get_articles(soup, today)

    return articles

if __name__ == '__main__':
    url = URL + "/bbs/" + TOPIC + "/index.html"
    print(url)
    articles = web_scraping_bot(url)
    for item in articles:
        print(item)
    save_to_json(articles, "tmp_articles.json")
 

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


