import requests
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent

csvfile = "books.csv"
url = "http://www.books.com.tw/web/sys_hourstop/home?loc=P_003_001"
ua = UserAgent()
headers = {'user-agent' : ua.random}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
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
    price = row.find("ul", class_="msg").find("li",class_="price_a")
    item.append(price.text.strip())
    items.append(item)

with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["排名","名稱","網址","圖片","價格"])
    for item in items:
        writer.writerow(item)