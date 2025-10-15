"""
查詢歷史資料 範例
https://rate.bot.com.tw/xrt/all/2023-03-20


https://rate.bot.com.tw/

(台銀牌告匯率)
https://rate.bot.com.tw/xrt?Lang=zh-TW

"""

import requests
from bs4 import BeautifulSoup


def get_html_data1(url):
    print("取得網頁資料: ", url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("查詢中央銀行匯率")

url = "https://rate.bot.com.tw/xrt/all/day"
# https://rate.bot.com.tw/xrt?Lang=zh-TW  另一個網址
html_data = get_html_data1(url)

soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())  # prettify()這個函數可以將DOM tree以比較美觀的方式印出。

# print('多重條件選擇')
cells = soup.select("table tr td")  # 尋找talbe標籤裡面的tr標籤裡面的td標籤 三者都要符合的抓出來
print(type(cells))
print("符合條件的資料", len(cells), "筆")
print(cells)

print("------------------------------")  # 30個

i = 0
for cell in cells:
    print(i)
    print(cell.text.strip())
    i = i + 1

print("------------------------------")  # 30個

print("顯示 幣別")
print("多重條件選擇")
dnames = soup.select("table tr td[data-table=幣別] div.visible-phone")
# print(type(dnames))
print("符合條件的資料", len(dnames), "筆")
# print(dnames)
names = list()
for dname in dnames:
    names.append(dname.text.strip())
print(names)

print("------------------------------")  # 30個

print("顯示 本行即期買入")
print("多重條件選擇")
buyingrate = soup.select("table tr td[data-table=本行即期買入]")
print(type(buyingrate))
print("符合條件的資料", len(buyingrate), "筆")
print(buyingrate)
i = 0
for price in buyingrate:
    print(i)
    print(price.text.strip())
    i = i + 1

print("------------------------------")  # 30個

prices = list()
for price in buyingrate:
    prices.append(price.text.strip())
print(prices)

print("------------------------------")  # 30個

print(names)
print(prices)
rates = zip(names, prices)
for rate in rates:
    print(rate)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" fail
from lxml import html

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
response = requests.get(url)
tree = html.fromstring(response.text)

print("美金：" + str(tree.xpath("//html/body/div[1]/main/div[3]/table/tbody/tr[1]/td[3]/text()")[0]))
print("日圓：" + str(tree.xpath("//html/body/div[1]/main/div[3]/table/tbody/tr[8]/td[3]/text()")[0]))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("台灣銀行 匯率查詢")

url = "https://rate.bot.com.tw/xrt/flcsv/0/day"  # 牌告匯率 CSV 網址

response = requests.get(url)  # 爬取網址內容
response.encoding = "utf-8"  # 網頁編碼模式  # 調整回應訊息編碼為 utf-8，避免編碼不同造成亂碼
rt = response.text  # 以文字模式讀取內容
rts = rt.split("\n")  # 使用「換行」將內容拆分成串列
for i in rts:  # 讀取串列的每個項目
    try:  # 使用 try 避開最後一行的空白行
        a = i.split(",")  # 每個項目用逗號拆分成子串列
        print(a[0] + ": " + a[12])  # 取出第一個 ( 0 ) 和第十三個項目 ( 12 )
    except:
        break


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


import requests
from bs4 import BeautifulSoup

"""
url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
csvfile = "tmp_xrt.csv"
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
            lst.append(cell.text.replace("\n","").replace("\r",""))
        writer.writerow(lst)

print("------------------------------")  # 30個

def split_name(name):
    pos = name.find(')')
    return pd.Series({
        '"幣別"': name[0:pos].strip() + ")"
    }) 
df = pd.read_csv("tmp_xrt.csv",encoding="big5")
df = df.drop(df.index[[0,1]])
df = df.iloc[:,0:5]
df.columns = ["幣別","現金(買)",
               "現金(賣)","即期(買)",
               "即期(賣)"]
df["幣別"] = df["幣別"].apply(split_name)
df.to_csv("tmp_xrt2.csv",index=False,encoding="big5")
print(df.head())     

print("------------------------------------------------------------")  # 60個
print('------------------------------------------------------------')	#60個

import requests 
from bs4 import BeautifulSoup

base_url = "https://www.cbc.gov.tw/tw/"
url = base_url + "lp-645-1.html"
csvfile = "tmp_USxrt.csv"
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

print("------------------------------")  # 30個

csvfile = "tmp_USxrt.csv"
df = pd.read_csv(csvfile)
df.drop_duplicates(keep=False, inplace=True)
df.to_csv('tmp_USxrt2.csv',index=False,encoding="utf8")
print(df.head(5))

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("查詢台銀牌告匯率")

from bs4 import BeautifulSoup  # 解析網頁
from time import localtime, strftime  # 處理時間
from os.path import exists  # 台銀匯率網站

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")  # 回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml")  # 解析網頁，建立bs物件
for single_tr in (
    bsObj.find("table", {"title": "牌告匯率"}).find("tbody").findAll("tr")
):  # 針對匯率表格分析
    cell = single_tr.findAll("td")  # 找到每一個表格
    currency_name = (
        cell[0].find("div", {"class": "visible-phone"}).contents[0]
    )  # 找到表格中幣別
    currency_name = currency_name.replace("\r", "")  # 取代不需要的字元
    currency_name = currency_name.replace("\n", "")
    currency_name = currency_name.replace(" ", "")
    currency_rate = cell[2].contents[0]  # 找到幣別匯率
    print(currency_name, currency_rate)
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime())  # 記錄目前時間
    data = [["時間", "匯率"], [now_time, currency_rate]]  # 準備寫入檔案資料
    print("寫入資料 :", data)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
csvfile = "tmp_xrt.csv"
r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.select_one("#ie11andabove > div > table")
rows = tag_table.find_all("tr")
with open(csvfile, "w+", newline="", encoding="big5") as fp:
    writer = csv.writer(fp)
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n", "").replace("\r", "").strip())
        writer.writerow(lst)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


# 3030
print("------------------------------")  # 30個
