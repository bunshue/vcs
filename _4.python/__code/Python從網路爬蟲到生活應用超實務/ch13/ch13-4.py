import requests 
from bs4 import BeautifulSoup
import csv, time

base_url = "https://www.twse.com.tw"
url = base_url + "/zh/brokerService/brokerServiceAudit"
# https://www.twse.com.tw/brokerService/brokerServiceAudit?showType=list&stkNo=1020&focus=6
csvfile = "BrokerBranchs.csv"
items = []
print("爬取總公司: ", url)
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one(".grid")  # 找到<table>
rows = tag_table.find_all("tr")       # 找出所有<tr>
for row in rows:
    item = []
    for cell in row.find_all(["td"]):
        txt = cell.text.replace("\n","").replace("\r","").strip()        
        if txt == "明細":
            new_url = base_url + cell.find("a").get("href")
            print("爬取分公司: ", new_url)
            r2 = requests.get(new_url)
            r2.encoding = "utf8"
            soup2 = BeautifulSoup(r2.text, "lxml")
            tag_table2 = soup2.select_one(".grid.links")  # 找到<table>
            rows2 = tag_table2.find_all("tr")   # 找出所有<tr>
            for row2 in rows2:
                item_branch = []
                for cell2 in row2.find_all("td"):
                    txt = cell2.text.replace("\n","").replace("\r","").strip()
                    item_branch.append(txt)
                if item_branch and len(item_branch) == 5:
                    items.append(item_branch)   # 新增分公司
        else:
            item.append(txt)
    if item and len(item) == 5: 
        items.append(item)                 # 新增總公司
    time.sleep(1)                

print("券商總數(總公司+分公司):", len(items))
# 開啟CSV檔案寫入截取的資料
with open(csvfile,"w+",newline="",encoding="utf8") as fp:
    writer = csv.writer(fp)
    writer.writerow(["證券商代號", "證券商名稱", "開業日", "地址", "電話"])
    for item in items:
        writer.writerow(item)

