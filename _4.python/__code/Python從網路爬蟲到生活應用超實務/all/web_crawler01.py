import csv

print("------------------------------------------------------------")  # 60個

# 共同
import re
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

from image_downloader.image_downloader import download_csv_file_images

download_csv_file_images("欲抓圖片網址清單.csv")

print("------------------------------------------------------------")  # 60個

from image_downloader.image_downloader import download_csv_file_images

df = pd.read_csv("imgur_dog.csv")
print(df.head())
df.columns = ["imgur-src"]
df.to_csv("imgur_dog2.csv", index=False)

download_csv_file_images("imgur_dog2.csv")

print("------------------------------------------------------------")  # 60個

from image_downloader.image_downloader import download_csv_file_images
from apscheduler.schedulers.blocking import BlockingScheduler

csvfile = "tmp_ptt_beauty.csv"


def task(file):
    download_csv_file_images(file)


scheduler = BlockingScheduler()
run_date = "2020-9-6 14:40:00"
scheduler.add_job(task, "date", run_date=run_date, args=[csvfile])
print("自動排程在", run_date, "下載 ", csvfile, " 的圖檔...")
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
url = "https://www.msn.com/zh-tw/weather/forecast?iso=TW"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find("span", class_="current")
print(span.text)
print(span.get("aria-label"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver

url = "https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=65"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
span = soup.select_one("span.tem-C.is-active")
print(span.text)
driver.quit()

print("------------------------------------------------------------")  # 60個

url = "https://movies.yahoo.com.tw/movieinfo_main/復仇者聯盟-終局之戰-avengers-endgame-9728"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
div_p = soup.find("div", class_="table")
img = div_p.find("div", class_="movie_intro_info_l").find("img")
print("劇照:", img.get("src"))
div_info = div_p.find("div", class_="movie_intro_info_r")
title_cht = div_info.find("h1")
print("中文片名:", title_cht.text)
title_en = div_info.find("h3")
print("英文片名:", title_en.text)
date = div_info.find("span")
print(date.text)
length = date.find_next()
print(length.text)
company = length.find_next()
print(company.text)

print("------------------------------------------------------------")  # 60個

url = "https://zh.wikipedia.org/wiki/漫威漫畫"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tag_table = soup.find("table", class_="infobox")
tag_trs = tag_table.find_all("tr")
tag_trs = tag_trs[2:]
for tr in tag_trs:
    th = tr.find("th")
    td = tr.find("td")
    print(th.text, ":", td.text.strip())

print("------------------------------------------------------------")  # 60個

url = "https://www.railway.gov.tw/tra-tip-web/tip/tip004/tip421/restCode?RestNo=A110"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
lst = soup.find("ul", class_="shop-item")
items = lst.find_all("li")
print(len(items))
for item in items:
    title = item.find("div", class_="pro-title")
    print("便當名稱:", title.text)
    price = item.find("strong")
    print("便當價格:", price.text)
    print("-------------------------------")

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

url = "https://rent.housefun.com.tw/region/�x�_��/?cid=0000"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")
div = soup.find("div", id="SearchContent")
items = div.find_all("article")
print(len(items))
for item in items:
    title = item.find("h3", class_="title").find("a")
    if title:
        print(title.text)
    address = item.find("address", class_="addr")
    if address:
        print(address.text.strip())
    price = item.find("span", class_="infos num")
    if price:
        print(price.text)
    print("-------------------")
driver.quit()

print("------------------------------------------------------------")  # 60個

from fake_useragent import UserAgent
import re

URL = "https://movies.yahoo.com.tw/movie_intheaters.html/?page={0}"
ua = UserAgent()
headers = {"user-agent": ua.random}


def format_date(date_str):  # 取出上映日期
    pattern = "\d+-\d+-\d+"
    match = re.search(pattern, date_str)
    if match is None:
        return date_str
    else:
        return match.group(0)


all_movies = [["中文片名", "英文片名", "期待度", "海報圖片", "上映日"]]
for page in range(1, 11):
    url = URL.format(page)
    print("抓取: 第" + str(page) + "頁 網路資料中...")
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, "lxml")
        movies = []
        tag_ul = soup.find("ul", class_="release_list")
        rows = tag_ul.find_all("li")
        for row in rows:
            name_div = row.find("div", class_="release_movie_name")
            cht_n = name_div.find("a").text
            eng_n = name_div.find("div", class_="en").find("a").text
            expect = row.find("div", class_="leveltext").find("span").text
            photo_div = row.find("div", class_="release_foto")
            poster_url = photo_div.find("img")["src"]
            date = row.find("div", class_="release_movie_time")
            release_date = format_date(date.text)
            movie = [
                cht_n.strip(),
                eng_n.strip(),
                expect.strip(),
                poster_url,
                release_date,
            ]
            movies.append(movie)
        all_movies = all_movies + movies
        if soup.find("li", class_="nexttxt disabled"):
            break  # 已經沒有下一頁
        print("等待5秒鐘...")
        time.sleep(5)
    else:
        print("HTTP請求錯誤...")

with open("movies.csv", "w+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in all_movies:
        writer.writerow(item)

print("------------------------------------------------------------")  # 60個

from fake_useragent import UserAgent
import re

url = "https://movies.yahoo.com.tw/movie_intheaters.html/?page=1"
ua = UserAgent()
headers = {"user-agent": ua.random}


def format_date(date_str):  # 取出上映日期
    pattern = "\d+-\d+-\d+"
    match = re.search(pattern, date_str)
    if match is None:
        return date_str
    else:
        return match.group(0)


all_movies = [["中文片名", "英文片名", "期待度", "海報圖片", "上映日"]]
page = 1
while True:
    print("抓取: 第" + str(page) + "頁 網路資料中...")
    page = page + 1
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, "lxml")
        movies = []
        tag_ul = soup.find("ul", class_="release_list")
        rows = tag_ul.find_all("li")
        for row in rows:
            name_div = row.find("div", class_="release_movie_name")
            cht_n = name_div.find("a").text
            eng_n = name_div.find("div", class_="en").find("a").text
            expect = row.find("div", class_="leveltext").find("span").text
            photo_div = row.find("div", class_="release_foto")
            poster_url = photo_div.find("img")["src"]
            date = row.find("div", class_="release_movie_time")
            release_date = format_date(date.text)
            movie = [
                cht_n.strip(),
                eng_n.strip(),
                expect.strip(),
                poster_url,
                release_date,
            ]
            movies.append(movie)
        all_movies = all_movies + movies
        if soup.find("li", class_="nexttxt disabled"):
            break  # 已經沒有下一頁
        nextPage = soup.find("li", class_="nexttxt")
        if nextPage:
            url = nextPage.find("a")["href"]
        print("等待5秒鐘...")
        time.sleep(5)
    else:
        print("HTTP請求錯誤...")

with open("movies2.csv", "w+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in all_movies:
        writer.writerow(item)

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
import json

url = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=nike NBA&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)

items = []
count = 1
page = 1
while True:
    print("抓取: 第" + str(page) + "頁 網路資料中...")
    page = page + 1
    soup = BeautifulSoup(driver.page_source, "lxml")
    tag_ul = soup.select_one("div.listArea > ul")
    tag_lis = tag_ul.find_all("li")
    for tag_li in tag_lis:
        title = tag_li.find("h3", class_="prdName")
        price = tag_li.find("span", class_="price").find("b")
        items.append({"id": count, "title": title.text, "price": price.text})
        print("已經擷取:", count, "筆")
        count = count + 1

    btn_css = "div.pageArea.topPage > dl > dd > a"
    button = driver.find_elements_by_css_selector(btn_css)
    if button[len(button) - 1].text == "下一頁":
        button[len(button) - 1].click()
    else:
        break
    time.sleep(10)
driver.quit()

with open("momo_items.json", "w", encoding="utf-8") as fp:
    json.dump(items, fp, indent=2, sort_keys=True, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

csvfile = "TaiwanRailway.csv"
url = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime"
post_data = {
    "startStation": "1000-臺北",
    "endStation": "1100-中壢",
    "transfer": "ONE",
    "rideDate": "2020/08/20",
    "startOrEndTime": "true",
    "startTime": "00:00",
    "endTime": "23:59",
    "trainTypeList": "ALL",
    "query": "查詢",
}

r = requests.post(url, data=post_data)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find("table", class_="itinerary-controls")
title_row = tag_table.find("tr")
rows = tag_table.find_all("tr", class_="trip-column")
rows.insert(0, title_row)

with open(csvfile, "w+", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n", "").replace("\r", ""))
        writer.writerow(lst)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

print(
    "開眼電影網 台北週末票房排行榜------------------------------------------------------------"
)  # 60個

url = "http://app2.atmovies.com.tw/boxoffice/"

r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find("table")
rows = tag_table.find_all("tr")
items = []
for row in rows:
    item = []
    for cell in row.find_all("td"):
        item.append(cell.text.replace("\n", "").replace("\r", "").strip())
    if item and item[0] != "more":
        items.append(item)

print(items)

print("------------------------------------------------------------")  # 60個

"""
url = "https://movies.yahoo.com.tw/chart.html"
csvfile = "yahoomovies.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find("div", class_="rank_list") 
rows = soup.find_all('div', class_='tr')
colname = list(rows.pop(0).stripped_strings)
items = []
for row in rows:
    tds = row.find_all("div", class_="td")
    item = []
    item.append(tds[0].text)
    item.append(tds[2].text)
    title = tds[3].text.strip()
    if "\n" in title:
        x = title.split("\n")
        title = x[0]
    item.append(title)
    item.append(tds[4].text.strip())
    item.append(tds[5].text.strip())
    item.append(tds[6].text.strip())
    items.append(item)

with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(colname)
    for item in items:
        writer.writerow(item)
"""

print("愛食記------------------------------------------------------------")  # 60個

url = "https://ifoodie.tw/explore/台北市/list?sortby=rating"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
item_lst = soup.find("div", class_="item-list")
items = item_lst.find_all("div", class_="restaurant-item")
print(len(items))
for index in range(5):
    item = items[index]
    title = item.find("a", class_="title-text")
    if title:
        print(title.text)
    address = item.find("div", class_="address-row")
    if address:
        print(address.text)
    avg_price = item.find("div", class_="avg-price")
    if avg_price:
        print(avg_price.text[2:])
    message = item.find("div", class_="message-text")
    if message:
        print(message.text)
    print("-------------------")

print("博客來 全站熱銷榜------------------------------------------------------------")  # 60個

from fake_useragent import UserAgent

csvfile = "books.csv"
url = "http://www.books.com.tw/web/sys_hourstop/home?loc=P_003_001"
ua = UserAgent()
headers = {"user-agent": ua.random}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")
tag_ul = soup.find("ul", class_="clearfix")
rows = tag_ul.find_all("li", class_="item")
print(len(rows))
items = []
for row in rows:
    item = []
    top = row.find("strong", class_="no")
    item.append(top.text.strip())
    title = row.find("h4")
    item.append(title.text.strip())
    item.append(title.find("a").get("href"))
    img = row.find("img", class_="cover")
    item.append(img.get("src"))
    price = row.find("ul", class_="msg").find("li", class_="price_a")
    item.append(price.text.strip())
    items.append(item)

with open(csvfile, "w+", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(["排名", "名稱", "網址", "圖片", "價格"])
    for item in items:
        writer.writerow(item)

print("Google趨勢------------------------------------------------------------")  # 60個

import re
import json
import datetime
from fake_useragent import UserAgent

URL = "https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed={}&geo=TW&ns=15"

ua = UserAgent()
enddate = datetime.datetime.today()
startdate = enddate - datetime.timedelta(days=29)
all_items = []
start = datetime.datetime.strftime(startdate, "%Y%m%d")
end = datetime.datetime.strftime(enddate, "%Y%m%d")
for i in pd.date_range(start=start, end=end, freq="1D"):
    url = URL.format(datetime.datetime.strftime(i, "%Y%m%d"))
    print(url)
    headers = {"user-agent": ua.random}
    r = requests.get(url, headers=headers)
    json_str = re.sub("\)\]\}',\n", "", r.text)
    data = json.loads(json_str)
    results = data["default"]["trendingSearchesDays"][0]["trendingSearches"]
    items = []
    rank = 1
    for item in results:
        dic = item["title"]
        dic["rank"] = rank
        items.append(dic)
        rank = rank + 1
    df = pd.DataFrame(items)
    df["date"] = datetime.datetime.strftime(i, "%Y-%m-%d")
    print(df.head())
    all_items.append(df)

df = pd.concat(all_items, ignore_index=True)
df.to_csv("trends.csv", index=False)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute("href")
    if href:
        links.append(href)
        print(href)
print(len(links))
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tags = soup.select("#video-title")
links = []
for tag in tags:
    href = tag["href"]
    if href:
        links.append(href)
        print(href)
print(len(links))
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute("href")
    links.append(href)
print(len(links))

wait = WebDriverWait(driver, 10)
for link in links:
    driver.get(link)
    num = link.strip("https://www.youtube.com/watch?v=")
    title = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#container > h1"))
    ).text
    description = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#description"))
    ).text
    print("編號:", num)
    print("名稱:", title.strip())
    print("描述:", description.strip())
    print("---------------------------")
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)

for x in range(5):
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)
    time.sleep(5)

tags = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for tag in tags:
    href = tag.get_attribute("href")
    if href:
        links.append(href)
print(len(links))

df = pd.DataFrame(columns=["id", "title", "description"])
wait = WebDriverWait(driver, 10)
for link in links:
    driver.get(link)
    num = link.strip("https://www.youtube.com/watch?v=")
    title = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#container > h1"))
    ).text
    description = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#description"))
    ).text
    df.loc[len(df)] = [num, title, description]

print(df.head())
df.to_csv("YouTube.csv", index=False, encoding="utf-8")
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

url = "https://fchart.github.io/img/Butterfly.png"
path = "Butterfly.png"

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(path, "wb") as fp:
        for chunk in response:
            fp.write(chunk)
    print("圖檔已經下載")
else:
    print("錯誤! HTTP請求失敗...")

print("------------------------------------------------------------")  # 60個

url = "https://fchart.github.io/"
os.makedirs("fchart", exist_ok=True)
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
for img in soup.find_all("img"):
    try:
        imgUrl = url + img.get("src").replace("\\", "/")
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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import json

URL = "https://www.ptt.cc"
url = URL + "/bbs/NBA/index.html"


def get_resource(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/63.0.3239.132 Safari/537.36"
    }
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
        if tag.find("div", class_="date").text.strip() == date:
            push_count = 0  # 取得推文數
            push_str = tag.find("div", class_="nrec").text
            if push_str:
                try:
                    push_count = int(push_str)  # 轉換成數字
                except ValueError:  # 轉換失敗，可能是'爆'或 'X1','X2'
                    if push_str == "爆":
                        push_count = 99
                    elif push_str.startswith("X"):
                        push_count = -10
            # 取得貼文的超連結和標題文字
            if tag.find("a"):  # 有超連結，表示文章存在
                href = tag.find("a")["href"]
                title = tag.find("a").text
                author = tag.find("div", class_="author").string
                articles.append(
                    {
                        "title": title,
                        "href": href,
                        "push_count": push_count,
                        "author": author,
                    }
                )

    return articles, prev_url


all_articles = []
print("抓取網路資料中...")
soup = get_resource(url)
if soup:
    # 取得今天日期, 去掉開頭'0'符合PTT的日期格式
    today = time.strftime("%m/%d").lstrip("0")
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
    json.dump(all_articles, fp, indent=2, sort_keys=True, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個

URL = "https://www.ptt.cc"
url = URL + "/bbs/beauty/index.html"


def get_resource(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        "AppleWebKit/537.36 (KHTML, like Gecko)"
        "Chrome/63.0.3239.132 Safari/537.36"
    }
    r = requests.get(url, headers=headers, cookies={"over18": "1"})
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
        if tag.find("div", class_="date").text.strip() == date:
            push_count = 0  # 取得推文數
            push_str = tag.find("div", class_="nrec").text
            if push_str:
                try:
                    push_count = int(push_str)  # 轉換成數字
                except ValueError:  # 轉換失敗，可能是'爆'或 'X1','X2'
                    if push_str == "爆":
                        push_count = 99
                    elif push_str.startswith("X"):
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
                        articles.append([title, href, push_count, author, url_photo])

    return articles, prev_url


all_articles = []
print("抓取網路資料中...")
soup = get_resource(url)
if soup:
    # 取得今天日期, 去掉開頭'0'符合PTT的日期格式
    today = time.strftime("%m/%d").lstrip("0")
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
    writer.writerow(["title", "href", "push_count", "author", "photo-src"])
    for article in all_articles:
        writer.writerow(article)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def task(text):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務1...", text)


scheduler = BlockingScheduler()


run_date = datetime.date(2020, 9, 4)
scheduler.add_job(task, "date", run_date=run_date, args=["工作1"])
run_date = datetime.datetime(2020, 9, 4, 14, 10, 0)
scheduler.add_job(task, "date", run_date=run_date, args=["工作2"])
run_date = "2020-9-4 14:15:00"
scheduler.add_job(task, "date", run_date=run_date, args=["工作3"])

""" NG
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from apscheduler.schedulers.blocking import BlockingScheduler


def task(text):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務2...", text)


scheduler = BlockingScheduler()
scheduler.add_job(task, "interval", minutes=1, args=["工作1"])
start_date = "2020-09-04 14:25:00"
end_date = "2020-09-04 14:28:00"
scheduler.add_job(
    task,
    "interval",
    minutes=1,
    seconds=30,
    start_date=start_date,
    end_date=end_date,
    args=["工作2"],
)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()

print("------------------------------------------------------------")  # 60個

from telegram import Bot

bot = Bot("<API�v��>")
print(bot.getMe())

print("------------------------------------------------------------")  # 60個

from telegram import Bot

bot = Bot("<API�v��>")
updates = bot.getUpdates()
print(updates[0].update_id)
print(updates[0].message)


print("------------------------------------------------------------")  # 60個

from telegram.ext import Updater, CommandHandler

token = "<API權杖>"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher


def hello(update, context):
    from_user = update.message.from_user
    name = from_user.last_name + from_user.first_name
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id, text="你好! {}".format(name))


def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id, text="已經停止Telegram Bot 歡迎機器人")
    updater.stop()


dispatcher.add_handler(CommandHandler("hello", hello))
dispatcher.add_handler(CommandHandler("stop", stop))
print("Telegram Bot 歡迎機器人啟動中...")
updater.start_polling()
updater.idle()

print("------------------------------------------------------------")  # 60個

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

token = "<API權杖>"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id, text="已經停止Telegram Bot 鸚鵡機器人")
    updater.stop()


dispatcher.add_handler(CommandHandler("stop", stop))
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
print("Telegram Bot 鸚鵡機器人啟動中...")
updater.start_polling()
updater.idle()

print("------------------------------------------------------------")  # 60個

from telegram.ext import Updater, CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton

token = "<API權杖>"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    buttons = [
        [
            InlineKeyboardButton("IFTTT", callback_data="1"),
            InlineKeyboardButton("LINE Notify", callback_data="2"),
        ],
        [InlineKeyboardButton("Telegram Bot", callback_data="3")],
    ]
    markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text("請選擇: ", reply_markup=markup)


def answer(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text("你的選擇是: " + query.data)


def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id, text="已經停止Telegram Bot 選單機器人")
    updater.stop()


dispatcher.add_handler(CommandHandler("stop", stop))
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(answer))
print("Telegram Bot 選單機器人啟動中...")
updater.start_polling()
updater.idle()

print("------------------------------------------------------------")  # 60個

from telegram.ext import Updater, CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
from random import randint

token = "<API權杖>"
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher


def math_add(update, context):
    a, b = randint(1, 100), randint(1, 100)
    buttons = []
    for s in range(a + b - randint(1, 3), a + b + randint(1, 3)):
        data = "{} {} {}".format(a, b, s)
        buttons.append(InlineKeyboardButton(str(s), callback_data=data))

    text = "{} + {} = ?".format(a, b)
    markup = InlineKeyboardMarkup([buttons])
    update.message.reply_text(text, reply_markup=markup)


def check_answer(update, context):
    a, b, s = [int(x) for x in update.callback_query.data.split()]
    if a + b == s:
        update.callback_query.edit_message_text("答對了!")
    else:
        update.callback_query.edit_message_text("答錯囉!")


def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id, text="已經停止Telegram Bot 加法測驗機器人")
    updater.stop()


dispatcher.add_handler(CommandHandler("stop", stop))
dispatcher.add_handler(CommandHandler("add", math_add))
dispatcher.add_handler(CallbackQueryHandler(check_answer))
print("Telegram Bot 加法測驗機器人啟動中...")
updater.start_polling()
updater.idle()

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

api_key = "<API金鑰>"


def email_alert(first, second=None, third=None):
    URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
    event_name = "web_scraping"
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    requests.get(url)


def task():
    url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    span = soup.find("span", class_="current")
    temp = span.text
    summary = span.get("aria-label")
    email_alert(temp, summary)


scheduler = BlockingScheduler()
scheduler.add_job(task, "interval", minutes=2)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()

print("------------------------------------------------------------")  # 60個

from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler

api_key = "<API金鑰>"
token = "<API權杖>"


def email_alert(first, second=None, third=None):
    URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
    event_name = "web_scraping"
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    requests.get(url)


def task():
    url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    span = soup.find("span", class_="current")
    temp = span.text
    summary = span.get("aria-label")
    email_alert(temp, summary)


scheduler = BackgroundScheduler()
scheduler.add_job(task, "interval", minutes=2)

updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id, text="已經啟動Email排程天氣通知")
    scheduler.start()


def shutdown(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id, text="已經停止Email排程天氣通知")
    scheduler.shutdown()


def stop(update, context):
    bot = context.bot
    bot.send_message(chat_id=update.effective_chat.id, text="已經停止Telegram Bot 管家機器人")
    updater.stop()


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("shutdown", shutdown))
dispatcher.add_handler(CommandHandler("stop", stop))
print("Telegram Bot 管家機器人啟動中...")
updater.start_polling()
updater.idle()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from apscheduler.schedulers.blocking import BlockingScheduler


def task():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務3...")


scheduler = BlockingScheduler()
scheduler.add_job(task, "interval", seconds=3)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

"""
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
            lst.append(cell.text.replace("\n","").replace("\r",""))
        writer.writerow(lst)

print("------------------------------------------------------------")  # 60個

def split_name(name):
    pos = name.find(')')
    return pd.Series({
        '"幣別"': name[0:pos].strip() + ")"
    }) 
df = pd.read_csv("tmp_xrt.csv",encoding="big5")
df = df.drop(df.index[[0,1]])
df = df.iloc[:,0:5]
df.columns = ["幣別","現金(買)",
               "現金(賣)","即期(買)",
               "即期(賣)"]
df["幣別"] = df["幣別"].apply(split_name)
df.to_csv("tmp_xrt2.csv",index=False,encoding="big5")
print(df.head())     

print("------------------------------------------------------------")  # 60個
print('------------------------------------------------------------')	#60個

import requests 
from bs4 import BeautifulSoup

base_url = "https://www.cbc.gov.tw/tw/"
url = base_url + "lp-645-1.html"
csvfile = "tmp_USxrt.csv"
items = []
next_page = True;

while next_page:
    print(url)
    r = requests.get(url)
    r.encoding = "utf8"
    soup = BeautifulSoup(r.text, "lxml")
    tag_table = soup.find("table", class_="rwd-table")  # 找到<table>
    rows = tag_table.find_all("tr")   # 找出所有<tr>
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").replace("\r",""))
        items.append(lst)
    # 找尋下一頁按鈕的<a>標籤
    tag_li = soup.find("li", class_="next")
    if tag_li:
        next_page = True
        url = base_url + tag_li.find("a").get("href")
        time.sleep(2)
    else:
        next_page = False        
       
with open(csvfile,'w+', newline='',encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in items:
        writer.writerow(item)

print("------------------------------------------------------------")  # 60個

csvfile = "tmp_USxrt.csv"
df = pd.read_csv(csvfile)
df.drop_duplicates(keep=False, inplace=True)
df.to_csv('tmp_USxrt2.csv',index=False,encoding="utf8")
print(df.head(5))
"""
print("------------------------------------------------------------")  # 60個

import twder

print(twder.currencies())

print("------------------------------------------------------------")  # 60個

import twder

df = pd.DataFrame(twder.now_all()).transpose()
df.columns = ["時間", "現金(買)", "現金(賣)", "即期(買)", "即期(賣)"]
print(df.head())

print("------------------------------------------------------------")  # 60個

import twder

print(twder.now("USD"))
print(twder.now("JPY"))

df = pd.DataFrame(twder.past_day("USD"))
df.columns = ["時間", "現金(買)", "現金(賣)", "即期(買)", "即期(賣)"]
df.set_index("時間", inplace=True)
print(df.head())

print("------------------------------------------------------------")  # 60個
""" NG
import twder

usd = twder.specify_month("USD", 2020, 6) 
df = pd.DataFrame(usd)
df.columns = ["時間","現金(買)","現金(賣)",
              "即期(買)","即期(賣)"]
df.set_index("時間" , inplace=True)
print(df.head())
"""
print("------------------------------------------------------------")  # 60個

import twder

usd = twder.past_six_month("USD")
df = pd.DataFrame(usd)
df.columns = ["時間", "現金(買)", "現金(賣)", "即期(買)", "即期(賣)"]
df.set_index("時間", inplace=True)
print(df.head())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

"""
url = "https://jsjustweb.jihsun.com.tw/z/zc/zcp/zcp_2330.djhtm"
csvfile = "tmp_BalanceSheet.csv"
ua = UserAgent()
user_agent = ua.random
headers = {'User-Agent': user_agent}
r = requests.get(url,headers=headers,verify=False)
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one("#oMainTable")  # 找到<table>
rows = tag_table.find_all("tr")   # 找出所有<tr>
# 開啟CSV檔案寫入截取的資料
with open(csvfile,'w+',newline='',encoding="big5") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").replace("\r",""))
        writer.writerow(lst)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

"""
url = "https://jsjustweb.jihsun.com.tw/z/zc/zcp/zcp.djhtm?a=2330&b=3&c=Q"
csvfile = "tmp_CashFlow.csv"
ua = UserAgent()
user_agent = ua.random
headers = {'User-Agent': user_agent}
r = requests.get(url, headers=headers,verify=False)
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one("#oMainTable")  # 找到<table>
rows = tag_table.find_all("tr")   # 找出所有<tr>
# 開啟CSV檔案寫入截取的資料
with open(csvfile,'w+',newline='',encoding="big5") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").replace("\r",""))
        writer.writerow(lst)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

"""
url = "https://jsjustweb.jihsun.com.tw/z/zc/zcp/zcp.djhtm?a=2330&b=2&c=Q"
csvfile = "tmp_IncomeStatement.csv"
ua = UserAgent()
user_agent = ua.random
headers = {'User-Agent': user_agent}
r = requests.get(url,headers=headers,verify=False)
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one("#oMainTable")  # 找到<table>
rows = tag_table.find_all("tr")   # 找出所有<tr>
# 開啟CSV檔案寫入截取的資料
with open(csvfile,'w+',newline='',encoding="big5") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").replace("\r",""))
        writer.writerow(lst)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
公開資訊觀測站
https://mops.twse.com.tw/mops/web/index
"""

import requests
from fake_useragent import UserAgent
from io import StringIO


def get_monthly_report(s_type, year, month, delay=5):
    if year > 1990:
        year -= 1911
    URL = "https://mops.twse.com.tw/nas/t21/{}/"
    stock_type = ["sii", "otc", "rotc"]
    URL = URL.format(stock_type[s_type])
    url = URL + "t21sc03_{0}_{1}.html".format(str(year), str(month))
    ua = UserAgent()
    user_agent = ua.random
    headers = {"User-Agent": user_agent}
    r = requests.get(url, headers=headers)
    r.encoding = "big5"
    dfs = pd.read_html(StringIO(r.text), encoding="big5")
    items = []
    for item in dfs:
        if item.shape[1] <= 11 and item.shape[1] >= 10:
            items.append(item)
    df = pd.concat(items)
    if "levels" in dir(df.columns):
        df.columns = df.columns.get_level_values(1)
    df["當月營收"] = pd.to_numeric(df["當月營收"], "coerce")
    df = df[~df["當月營收"].isnull()]
    df = df[df["公司代號"] != "合計"]
    time.sleep(delay)

    return df


"""
df = get_monthly_report(0, 109, 1)
print(df.shape)
print(df.head())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

"""
base_url = "https://www.twse.com.tw"
url = base_url + "/zh/brokerService/brokerServiceAudit"
# https://www.twse.com.tw/brokerService/brokerServiceAudit?showType=list&stkNo=1020&focus=6
csvfile = "tmp_BrokerBranchs.csv"
items = []
print("爬取總公司: ", url)
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one(".grid")  # 找到<table>
rows = tag_table.find_all("tr")       # 找出所有<tr>
for row in rows:
    item = []
    for cell in row.find_all(["td"]):
        txt = cell.text.replace("\n","").replace("\r","").strip()        
        if txt == "明細":
            new_url = base_url + cell.find("a").get("href")
            print("爬取分公司: ", new_url)
            r2 = requests.get(new_url)
            r2.encoding = "utf8"
            soup2 = BeautifulSoup(r2.text, "lxml")
            tag_table2 = soup2.select_one(".grid.links")  # 找到<table>
            rows2 = tag_table2.find_all("tr")   # 找出所有<tr>
            for row2 in rows2:
                item_branch = []
                for cell2 in row2.find_all("td"):
                    txt = cell2.text.replace("\n","").replace("\r","").strip()
                    item_branch.append(txt)
                if item_branch and len(item_branch) == 5:
                    items.append(item_branch)   # 新增分公司
        else:
            item.append(txt)
    if item and len(item) == 5: 
        items.append(item)                 # 新增總公司
    time.sleep(1)                

print("券商總數(總公司+分公司):", len(items))
# 開啟CSV檔案寫入截取的資料
with open(csvfile,"w+",newline="",encoding="utf8") as fp:
    writer = csv.writer(fp)
    writer.writerow(["證券商代號", "證券商名稱", "開業日", "地址", "電話"])
    for item in items:
        writer.writerow(item)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import datetime

# from monthlyReport import get_monthly_report

data = []
now = datetime.datetime.now()
year = now.year
month = now.month - 1
if month == 0:
    month = 12
    year -= 1
"""
for i in range(12):
    print("爬取月營收的月份: ", year,"/", month)
    try:
        key = "%d-%d-01"%(year, month)
        m_df = get_monthly_report(0, year, month)
        m_df.index = m_df["公司代號"]
        item_df = pd.DataFrame({key: m_df["當月營收"]}).transpose()
        data.append(item_df) 
    except Exception:
        print("錯誤: 月營收資料爬取錯誤...")
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    time.sleep(10)

df = pd.concat(data)
df.index = pd.to_datetime(df.index)
df = df.sort_index()
print(df.head())
df.to_csv("tmp_monthlysales.csv")

print("------------------------------")  # 30個

df = pd.read_csv("tmp_monthlysales.csv", index_col=0)
df.index = pd.to_datetime(df.index)
print(df["2330"])
df["2330"].plot(kind="line", title="台積電月營收")

print("------------------------------")  # 30個

df = pd.read_csv("tmp_monthlysales.csv", index_col=0)
df.index = pd.to_datetime(df.index)
tsmc = df["2330"]
print(tsmc/tsmc.shift()-1)
(tsmc/tsmc.shift()-1).plot(kind="line", title="台積電營收成長率")

print("------------------------------")  # 30個

df = pd.read_csv("tmp_monthlysales.csv", index_col=0)
df.index = pd.to_datetime(df.index)

df1 = df.iloc[-3:].mean() > df.iloc[-12:].mean()
print(df1[df1 == True].index)
print("------------------------------")
df2 = df.rolling(window=3, min_periods=2).mean()
df2 = (df2 > df2.shift()).iloc[-6:].sum()
print(df2[df2 == 6].head())
print("------------------------------")
df3 = df.iloc[-1] == df.iloc[-12:].max()
print(df3[df3 == True].index)
print("------------------------------")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
公開資訊觀測站
https://mops.twse.com.tw/mops/web/index
"""

import requests
from fake_useragent import UserAgent
from io import StringIO


def get_monthly_report(s_type, year, month, delay=5):
    if year > 1990:
        year -= 1911
    URL = "https://mops.twse.com.tw/nas/t21/{}/"
    stock_type = ["sii", "otc", "rotc"]
    URL = URL.format(stock_type[s_type])
    url = URL + "t21sc03_{0}_{1}.html".format(str(year), str(month))
    ua = UserAgent()
    user_agent = ua.random
    headers = {"User-Agent": user_agent}
    r = requests.get(url, headers=headers)
    r.encoding = "big5"
    dfs = pd.read_html(StringIO(r.text), encoding="big5")
    items = []
    for item in dfs:
        if item.shape[1] <= 11 and item.shape[1] >= 10:
            items.append(item)
    df = pd.concat(items)
    if "levels" in dir(df.columns):
        df.columns = df.columns.get_level_values(1)
    df["當月營收"] = pd.to_numeric(df["當月營收"], "coerce")
    df = df[~df["當月營收"].isnull()]
    df = df[df["公司代號"] != "合計"]
    time.sleep(delay)

    return df


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
import re
from selenium import webdriver

"""
url = "https://www.bloomberg.com/quote/SPX:IND"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
regex = re.compile('^companyName.*')
name_box = soup.find("h1", class_= regex)
name = name_box.text
print(name)
price_box = soup.find("span", attrs={"class":re.compile("^priceText.*")})
price = price_box.text
print(price)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import requests
from fake_useragent import UserAgent

dates = [20200601, 20200701, 20200801]
stockNo = 2330
url = (
    "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"
)
ua = UserAgent()

for date in dates:
    print(date, stockNo)
    headers = {"User-Agent": ua.random}
    r = requests.get(url.format(date, stockNo), headers=headers)
    csvfile = "tmp_{}_{}.csv".format(stockNo, date)

    data = pd.read_html(r.text)[0]
    data.columns = data.columns.droplevel(0)
    data.to_csv(csvfile, index=False)
    time.sleep(5)

print("------------------------------------------------------------")  # 60個

import pandas_datareader as pdr

""" NG
df = pdr.DataReader("2330.TW", "yahoo")

print(df.shape)
print(df.head())
"""

print("------------------------------------------------------------")  # 60個

import datetime
import pandas_datareader as pdr

start = datetime.datetime.now() - datetime.timedelta(days=60)
end = datetime.date.today()
""" NG
df = pdr.DataReader("2330.TW", "yahoo", start, end)
print(df.shape)
print(df.head())
"""
print("------------------------------------------------------------")  # 60個

import requests

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=json&date={}&selectType=ALL"
r = requests.get(url.format(date))
content = r.content
csv_file = open("tmp_three_major1.json", "wb")
csv_file.write(content)
csv_file.close()

print("------------------------------------------------------------")  # 60個

import requests

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=csv&date={}&selectType=ALL"
r = requests.get(url.format(date))
content = r.content
csv_file = open("tmp_three_major2.csv", "wb")
csv_file.write(content)
csv_file.close()

print("------------------------------------------------------------")  # 60個

import requests
import json

date = "20200820"
url = "https://www.twse.com.tw/fund/T86?response=json&date={}&selectType=ALL"
r = requests.get(url.format(date))
if r.status_code == requests.codes.ok:
    print("成功爬取資料...")
    """# NG
    data = r.json() 
    df = pd.read_json(json.dumps(data["data"]))
    df.columns = data["fields"]
    print(df.head())
    df.to_csv("tmp_three_major3.csv", index=False)
    """
else:
    print("HTTP請求錯誤...")

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
import re
from selenium import webdriver

"""
url = "https://www.bloomberg.com/quote/CCMP:IND"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
regex = re.compile('^companyName.*')
name_box = soup.find("h1", class_= regex)
name = name_box.text
print(name)
price_box = soup.find("span", attrs={"class":re.compile("^priceText.*")})
price = price_box.text
print(price)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Hello World!"


@app.route("/callback")
def callback():
    return "Callback"


@app.route("/user/<username>")
def user(username):
    return "使用者名稱: " + str(username)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def main():
    return jsonify({"name": "Joe Chen", "email": "hueyan@ms2.hinet.net"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify

url = "https://ifoodie.tw/explore/台北市/list?sortby=rating"


def getTop(limit=5):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    item_lst = soup.find("div", class_="item-list")
    items = item_lst.find_all("div", class_="restaurant-item", limit=limit)
    outputs = []
    for item in items:
        title = item.find("a", class_="title-text")
        title_txt = title.text if title else "N/A"
        address = item.find("div", class_="address-row")
        address_txt = address.text if address else "N/A"
        price = item.find("div", class_="avg-price")
        price_txt = price.text[2:] if price else "N/A"
        result = {"title": title_txt, "address": address_txt, "price": price_txt}
        outputs.append(result)
    return outputs


app = Flask(__name__)


@app.route("/")
def main():
    return jsonify(getTop(5))


@app.route("/top/<limit>")
def top(limit):
    return jsonify(getTop(int(limit)))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

channel_token = "<Channel access token>"
channel_secret = "<Channel secret>"

app = Flask(__name__)
line_bot_api = LineBotApi(channel_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text=event.message.text)
    )


if __name__ == "__main__":
    app.run(port=8080)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
import requests
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

channel_token = "<Channel access token>"
channel_secret = "<Channel secret>"
url = "https://ifoodie.tw/explore/台北市/list?sortby=rating"


def getTop(limit=5):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    item_lst = soup.find("div", class_="item-list")
    items = item_lst.find_all("div", class_="restaurant-item", limit=limit)
    output = ""
    index = 1
    for item in items:
        title = item.find("a", class_="title-text")
        title_txt = title.text if title else "N/A"
        address = item.find("div", class_="address-row")
        address_txt = address.text if address else "N/A"
        price = item.find("div", class_="avg-price")
        price_txt = price.text[2:] if price else "N/A"
        output += str(index) + ": \n名稱: " + title_txt
        output += "\n地址: " + address_txt
        output += "\n價格: " + price_txt
        output += "\n"
        index += 1
    return output


app = Flask(__name__)
line_bot_api = LineBotApi(channel_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    if "美食" in text or "food" in text or "Food" in text:
        reply_msg = getTop(3)
    else:
        reply_msg = text
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_msg))


if __name__ == "__main__":
    app.run(port=8080)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from telegram import Bot, Update
from telegram.ext import Dispatcher
from telegram.ext import MessageHandler, Filters
from flask import Flask
from flask import request

token = "<API權杖>"
webhook_URL = "https://8eaa46651097.ngrok.io/callback"
app = Flask(__name__)

bot = Bot(token)
dispatcher = Dispatcher(bot, None, workers=0)


def echo(update, context):
    text = context.message.text
    bot.send_message(context.message.chat_id, text=text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


@app.route("/callback", methods=["POST", "GET"])
def callback():
    if (request.method == "POST") or (request.method == "GET"):
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
        return "OK"
    else:
        return "ERROR"


@app.route("/setwebhook", methods=["GET", "POST"])
def set_webhook():
    s = bot.setWebhook(webhook_URL)
    if s:
        return "成功完成 Webhook URL 設定:" + webhook_URL
    else:
        return "Webhook URL 設定失敗!"


@app.route("/deletewebhook", methods=["GET", "POST"])
def delete_webhook():
    s = bot.deleteWebhook()
    if s:
        return "成功刪除 Webhook URL 設定!"
    else:
        return "刪除 Webhook URL 設定失敗!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
import requests
from telegram import Bot, Update
from telegram.ext import Dispatcher
from telegram.ext import MessageHandler, Filters
from flask import Flask
from flask import request

token = "<API權杖>"
webhook_URL = "https://212370c3399b.ngrok.io/callback"
url = "https://ifoodie.tw/explore/台北市/list?sortby=rating"


def getTop(limit=5):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    item_lst = soup.find("div", class_="item-list")
    items = item_lst.find_all("div", class_="restaurant-item", limit=limit)
    output = ""
    index = 1
    for item in items:
        title = item.find("a", class_="title-text")
        title_txt = title.text if title else "N/A"
        address = item.find("div", class_="address-row")
        address_txt = address.text if address else "N/A"
        price = item.find("div", class_="avg-price")
        price_txt = price.text[2:] if price else "N/A"
        output += str(index) + ": \n名稱: " + title_txt
        output += "\n地址: " + address_txt
        output += "\n價格: " + price_txt
        output += "\n"
        index += 1
    return output


app = Flask(__name__)

bot = Bot(token)
dispatcher = Dispatcher(bot, None, workers=0)


def handle_msg(update, context):
    text = context.message.text
    if "美食" in text or "food" in text or "Food" in text:
        reply_msg = getTop(3)
    else:
        reply_msg = text
    bot.send_message(context.message.chat_id, text=reply_msg)


msg_handler = MessageHandler(Filters.text & (~Filters.command), handle_msg)
dispatcher.add_handler(msg_handler)


@app.route("/callback", methods=["POST", "GET"])
def callback():
    if (request.method == "POST") or (request.method == "GET"):
        update = Update.de_json(request.get_json(force=True), bot)
        print(update.message)
        dispatcher.process_update(update)
        return "OK"
    else:
        return "ERROR"


@app.route("/setwebhook", methods=["GET", "POST"])
def set_webhook():
    s = bot.setWebhook(webhook_URL)
    if s:
        return "成功完成 Webhook URL 設定:" + webhook_URL
    else:
        return "Webhook URL 設定失敗!"


@app.route("/deletewebhook", methods=["GET", "POST"])
def delete_webhook():
    s = bot.deleteWebhook()
    if s:
        return "成功刪除 Webhook URL 設定!"
    else:
        return "刪除 Webhook URL 設定失敗!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from apscheduler.schedulers.blocking import BlockingScheduler

message = "Welcome to the United States"


def do_task(mesg):
    # do_something(mesg)
    print("Say :", mesg)
    print("Say :", mesg)
    print("Say :", mesg)
    print("Say :", mesg)


scheduler = BlockingScheduler()
run_date = "2024-9-27 16:54:00"
scheduler.add_job(do_task, "date", run_date=run_date, args=[message])
print("自動排程在", run_date, ", 訊息 :", message)

try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
