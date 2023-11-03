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

with open("movies.csv", "w+",newline="",encoding="utf-8") as fp:
    writer = csv.writer(fp)
    for item in movies:
        writer.writerow(item)
