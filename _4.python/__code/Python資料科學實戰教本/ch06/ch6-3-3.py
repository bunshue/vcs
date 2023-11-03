import requests 
from bs4 import BeautifulSoup
import csv

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
csvfile = "xrt.csv"
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
            lst.append(cell.text.replace("\n","").
                       replace("\r","").
                       strip())
        writer.writerow(lst)
