import requests 
from bs4 import BeautifulSoup

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
        item.append(cell.text.replace("\n","").replace("\r","").strip())
    if item and item[0] != "more":
        items.append(item) 

print(items)
