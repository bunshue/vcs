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
