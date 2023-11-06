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
