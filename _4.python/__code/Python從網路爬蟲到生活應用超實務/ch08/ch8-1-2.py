import requests 
from bs4 import BeautifulSoup
import csv

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