import sys
import requests
from bs4 import BeautifulSoup

url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
span = soup.find('span', class_="current")
print(span.text)
print(span.get("aria-label"))


sys.exit()
print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch07\ch7-1-2.py

from selenium import webdriver
from bs4 import BeautifulSoup

url = "https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=65"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
soup = BeautifulSoup(driver.page_source, "lxml")
span = soup.select_one("span.tem-C.is-active")
print(span.text)
driver.quit()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch07\ch7-2-1.py

import requests
from bs4 import BeautifulSoup

url = "https://movies.yahoo.com.tw/movieinfo_main/復仇者聯盟-終局之戰-avengers-endgame-9728"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
div_p = soup.find('div', class_="table")
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

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch07\ch7-2-2.py

import requests
from bs4 import BeautifulSoup

url = "https://zh.wikipedia.org/wiki/漫威漫畫"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tag_table = soup.find('table', class_="infobox")
tag_trs = tag_table.find_all("tr")
tag_trs = tag_trs[2:]
for tr in tag_trs:
    th = tr.find("th")
    td = tr.find("td")
    print(th.text,":",td.text.strip())

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch07\ch7-3-1.py

from bs4 import BeautifulSoup
import requests

url = "https://www.railway.gov.tw/tra-tip-web/tip/tip004/tip421/restCode?RestNo=A110"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lst = soup.find("ul", class_="shop-item")
items = lst.find_all("li") 
print(len(items))
for item in items:
    title = item.find("div", class_="pro-title")
    print("便當名稱:", title.text)
    price = item.find("strong")
    print("便當價格:", price.text)
    print("-------------------------------")        



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch07\ch7-3-2.py

from bs4 import BeautifulSoup
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
    if title: print(title.text)
    address = item.find("address", class_="addr")
    if address: print(address.text.strip())
    price = item.find("span", class_="infos num")
    if price: print(price.text)
    print("-------------------")
driver.quit()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch07\ch7-4-1.py

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv, re, time

URL = "https://movies.yahoo.com.tw/movie_intheaters.html/?page={0}"
ua = UserAgent()
headers = {'user-agent' : ua.random}
 
def format_date(date_str):  # 取出上映日期
   pattern = '\d+-\d+-\d+'
   match = re.search(pattern, date_str)
   if match is None:
      return date_str
   else:
      return match.group(0)    
 
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
         cht_n = name_div.find("a").text
         eng_n = name_div.find("div",class_="en").find("a").text
         expect = row.find("div",class_="leveltext").find("span").text
         photo_div = row.find("div",class_="release_foto")
         poster_url = photo_div.find("img")["src"]
         date = row.find('div',class_='release_movie_time')
         release_date = format_date(date.text)
         movie= [cht_n.strip(),eng_n.strip(),expect.strip(),
                 poster_url,release_date]
         movies.append(movie)
      all_movies = all_movies + movies
      if soup.find("li", class_="nexttxt disabled"):
         break   # 已經沒有下一頁
      print("等待5秒鐘...")   
      time.sleep(5) 
   else:
      print("HTTP請求錯誤...")

with open("movies.csv", "w+",newline="",encoding="utf-8") as fp:
   writer = csv.writer(fp)
   for item in all_movies:
      writer.writerow(item)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch07\ch7-4-1a.py

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv, re, time

url = "https://movies.yahoo.com.tw/movie_intheaters.html/?page=1"
ua = UserAgent()
headers = {'user-agent' : ua.random}
 
def format_date(date_str):  # 取出上映日期
   pattern = '\d+-\d+-\d+'
   match = re.search(pattern, date_str)
   if match is None:
      return date_str
   else:
      return match.group(0)    
 
all_movies = [["中文片名","英文片名","期待度","海報圖片","上映日"]]
page = 1
while True:
   print("抓取: 第" + str(page) + "頁 網路資料中...")
   page = page + 1
   r = requests.get(url, headers=headers)
   if r.status_code == requests.codes.ok:
      soup = BeautifulSoup(r.text, 'lxml')
      movies = []
      tag_ul = soup.find("ul", class_="release_list")
      rows = tag_ul.find_all("li")
      for row in rows:
         name_div = row.find("div",class_="release_movie_name")
         cht_n = name_div.find("a").text
         eng_n = name_div.find("div",class_="en").find("a").text
         expect = row.find("div",class_="leveltext").find("span").text
         photo_div = row.find("div",class_="release_foto")
         poster_url = photo_div.find("img")["src"]
         date = row.find('div',class_='release_movie_time')
         release_date = format_date(date.text)
         movie= [cht_n.strip(),eng_n.strip(),expect.strip(),
                 poster_url,release_date]
         movies.append(movie)
      all_movies = all_movies + movies
      if soup.find("li", class_="nexttxt disabled"):
         break   # 已經沒有下一頁
      nextPage = soup.find("li", class_="nexttxt")   
      if nextPage:
         url = nextPage.find("a")["href"] 
      print("等待5秒鐘...")          
      time.sleep(5) 
   else:
      print("HTTP請求錯誤...")

with open("movies2.csv", "w+",newline="",encoding="utf-8") as fp:
   writer = csv.writer(fp)
   for item in all_movies:
      writer.writerow(item)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch07\ch7-4-2.py

from bs4 import BeautifulSoup
from selenium import webdriver
import time, json

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
        items.append({"id": count,
                      "title": title.text,
                      "price": price.text})  
        print("已經擷取:", count, "筆") 
        count = count + 1

    btn_css = "div.pageArea.topPage > dl > dd > a"    
    button = driver.find_elements_by_css_selector(btn_css)
    if button[len(button)-1].text == "下一頁":
        button[len(button)-1].click()
    else:
        break
    time.sleep(10)    
driver.quit()

with open("momo_items.json", "w", encoding="utf-8") as fp:
    json.dump(items,fp,indent=2,sort_keys=True,ensure_ascii=False)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch07\ch7-5.py

from bs4 import BeautifulSoup
import requests
import csv

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
    "query": "查詢" }

r = requests.post(url, data=post_data)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find("table", class_="itinerary-controls") 
title_row = tag_table.find("tr")                       
rows = tag_table.find_all("tr", class_="trip-column")  
rows.insert(0, title_row)

with open(csvfile, 'w+', newline='', encoding="utf-8") as fp:
    writer = csv.writer(fp)    
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").replace("\r",""))
        writer.writerow(lst)

print('------------------------------------------------------------')	#60個

