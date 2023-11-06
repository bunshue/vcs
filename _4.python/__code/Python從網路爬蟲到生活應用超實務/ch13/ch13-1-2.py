import requests 
from bs4 import BeautifulSoup
import csv, time

base_url = "https://www.cbc.gov.tw/tw/"
url = base_url + "lp-645-1.html"
csvfile = "USxrt.csv"
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

