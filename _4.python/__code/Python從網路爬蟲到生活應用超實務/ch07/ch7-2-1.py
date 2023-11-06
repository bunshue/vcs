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