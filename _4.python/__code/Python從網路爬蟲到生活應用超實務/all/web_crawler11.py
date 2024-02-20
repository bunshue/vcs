import os
import requests
from bs4 import BeautifulSoup

print('------------------------------------------------------------')	#60個

url = "https://fchart.github.io/img/Butterfly.png"
path = "Butterfly.png"

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, 'wb') as fp:
        for chunk in response:
            fp.write(chunk)
    print("圖檔已經下載")        
else:
    print("錯誤! HTTP請求失敗...")

print('------------------------------------------------------------')	#60個

url = "https://fchart.github.io/"
os.makedirs("fchart", exist_ok=True)
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
for img in soup.find_all("img"):
    try:
        imgUrl = url + img.get("src").replace('\\','/')
        print("下載:", imgUrl)
        res = requests.get(imgUrl)
    except requests.exceptions.MissingSchema:
        print("圖檔下載錯誤...")
        continue
    
    imgFile = os.path.join("fchart", os.path.basename(imgUrl))
    fp = open(imgFile, "wb")
    for chunk in res.iter_content(100000):
        fp.write(chunk)
    fp.close()
print("結束網頁圖檔下載...")

print('------------------------------------------------------------')	#60個

keyword = "dog"
pathdir = "imgur"
url = "http://imgur.com/search?q=" + keyword
os.makedirs(pathdir, exist_ok=True)
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
images = soup.find_all("a", class_="image-list-link")
print("圖檔數:", len(images))
for img in images:
    try:
        imgUrl = "http:" + img.find("img").get("src")
        print("下載:", imgUrl)
        res = requests.get(imgUrl)
    except requests.exceptions.MissingSchema:
        print("圖檔下載錯誤...")
        continue
    
    imgFile = os.path.join(pathdir, os.path.basename(imgUrl))
    fp = open(imgFile, "wb")
    for chunk in res.iter_content(100000):
        fp.write(chunk)
    fp.close()
print("結束 Imgur 網頁圖檔下載...")

print('------------------------------------------------------------')	#60個

import time
from selenium import webdriver

keyword = "dog"
pathdir = "imgur2"
url = "http://imgur.com/search?q=" + keyword
os.makedirs(pathdir, exist_ok=True)
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
for x in range(3):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)

soup = BeautifulSoup(driver.page_source, "lxml")
images = soup.find_all("a", class_="image-list-link")
print("圖檔數:", len(images))
for img in images:
    try:
        imgUrl = "http:" + img.find("img").get("src")
        print("下載:", imgUrl)
        res = requests.get(imgUrl)
    except requests.exceptions.MissingSchema:
        print("圖檔下載錯誤...")
        continue
    
    imgFile = os.path.join(pathdir, os.path.basename(imgUrl))
    fp = open(imgFile, "wb")
    for chunk in res.iter_content(100000):
        fp.write(chunk)
    fp.close()
print("結束 Imgur 網頁圖檔下載...")
driver.quit()

print('------------------------------------------------------------')	#60個

import time
import json

URL = "https://www.ptt.cc" 
url = URL + "/bbs/NBA/index.html"

def get_resource(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
    r = requests.get(url, headers=headers)
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
            # 取得貼文的超連結和標題文字
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

all_articles = []
print("抓取網路資料中...")
soup = get_resource(url)
if soup:
    # 取得今天日期, 去掉開頭'0'符合PTT的日期格式
    today = time.strftime("%m/%d").lstrip('0') 
    # 取得目前頁面的今日文章清單
    current_articles, prev_url = get_articles(soup, today) 
    while current_articles: 
        all_articles += current_articles
        print("等待2秒鐘...")
        time.sleep(2) 
        # 剖析上一頁繼續尋找是否有今日的文章
        soup = get_resource(URL + prev_url)
        current_articles, prev_url = get_articles(soup, today)

print("今天總共有: " + str(len(all_articles)) + " 篇文章")
with open("ptt_NBA.json", "w", encoding="utf-8") as fp: 
    json.dump(all_articles,fp,indent=2,sort_keys=True,ensure_ascii=False)

print('------------------------------------------------------------')	#60個

import time
import csv

URL = "https://www.ptt.cc" 
url = URL + "/bbs/beauty/index.html"

def get_resource(url):
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
               "AppleWebKit/537.36 (KHTML, like Gecko)"
               "Chrome/63.0.3239.132 Safari/537.36"}
    r = requests.get(url, headers=headers, cookies={"over18":"1"})
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
            # 取得貼文的超連結和標題文字
            if tag.find("a"):  # 有超連結，表示文章存在
                href = tag.find("a")["href"]
                title = tag.find("a").text
                author = tag.find("div", class_="author").string 
                # 抓圖片
                b_soup = get_resource(URL + href)
                b_divs = b_soup.find("div", id="main-content")
                photos = b_divs.find_all("a")
                for photo in photos:
                    url_photo = photo["href"]
                    if url_photo.startswith("https://i.imgur"):
                        articles.append([title,href,push_count,
                                         author,url_photo])
    
    return articles, prev_url

all_articles = []
print("抓取網路資料中...")
soup = get_resource(url)
if soup:
    # 取得今天日期, 去掉開頭'0'符合PTT的日期格式
    today = time.strftime("%m/%d").lstrip('0') 
    # 取得目前頁面的今日文章清單
    current_articles, prev_url = get_articles(soup, today) 
    while current_articles: 
        all_articles += current_articles
        print("等待2秒鐘...")
        time.sleep(2) 
        # 剖析上一頁繼續尋找是否有今日的文章
        soup = get_resource(URL + prev_url)
        current_articles, prev_url = get_articles(soup, today)

print("今天總共爬到: " + str(len(all_articles)) + " 張圖")
with open("ptt_beauty.csv", "w+", newline="", encoding="big5") as fp:
    writer = csv.writer(fp)
    writer.writerow(["title","href","push_count","author","photo-src"])
    for article in all_articles:
        writer.writerow(article)

print('------------------------------------------------------------')	#60個

from image_downloader.image_downloader import download_csv_file_images

download_csv_file_images("ptt_beauty.csv")

print('------------------------------------------------------------')	#60個

import time
import csv
from selenium import webdriver

keyword = "dog"
url = "http://imgur.com/search?q=" + keyword
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
for x in range(3):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)

soup = BeautifulSoup(driver.page_source, "lxml")
images = soup.find_all("a", class_="image-list-link")
print("圖檔數:", len(images))
with open("imgur_dog.csv", "w+", newline="", encoding="big5") as fp:
    writer = csv.writer(fp)
    writer.writerow(["image-href"])
    for img in images:
        imgUrl = "http:" + img.find("img").get("src")
        writer.writerow([imgUrl])

print("成功建立 imgur_dog.csv 檔...")
driver.quit()

print('------------------------------------------------------------')	#60個

from image_downloader.image_downloader import download_csv_file_images
import pandas as pd

df = pd.read_csv("imgur_dog.csv")
print(df.head())
df.columns = ["imgur-src"]
df.to_csv("imgur_dog2.csv",index=False)

download_csv_file_images("imgur_dog2.csv")

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

