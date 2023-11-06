import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv

url = "https://jsjustweb.jihsun.com.tw/z/zc/zcp/zcp_2330.djhtm"
csvfile = "BalanceSheet.csv"
ua = UserAgent()
user_agent = ua.random
headers = {'User-Agent': user_agent}
r = requests.get(url,headers=headers,verify=False)
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one("#oMainTable")  # 找到<table>
rows = tag_table.find_all("tr")   # 找出所有<tr>
# 開啟CSV檔案寫入截取的資料
with open(csvfile,'w+',newline='',encoding="big5") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").replace("\r",""))
        writer.writerow(lst)

