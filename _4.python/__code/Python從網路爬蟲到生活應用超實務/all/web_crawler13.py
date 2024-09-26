import requests 
from bs4 import BeautifulSoup
import csv
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

print("------------------------------------------------------------")  # 60個

import pandas as pd

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

import requests 
from bs4 import BeautifulSoup
import csv, time

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

print("------------------------------------------------------------")  # 60個

import pandas as pd

csvfile = "tmp_USxrt.csv"
df = pd.read_csv(csvfile)
df.drop_duplicates(keep=False, inplace=True)
df.to_csv('tmp_USxrt2.csv',index=False,encoding="utf8")
print(df.head(5))
"""
print("------------------------------------------------------------")  # 60個

import twder

print(twder.currencies()) 
 

print("------------------------------------------------------------")  # 60個

import pandas as pd
import twder

df = pd.DataFrame(twder.now_all()).transpose()
df.columns = ["時間","現金(買)","現金(賣)",
              "即期(買)","即期(賣)"]
print(df.head())

print("------------------------------------------------------------")  # 60個

import pandas as pd
import twder

print(twder.now("USD")) 
print(twder.now("JPY"))

df = pd.DataFrame(twder.past_day("USD"))
df.columns = ["時間","現金(買)","現金(賣)",
              "即期(買)","即期(賣)"]
df.set_index("時間" , inplace=True)
print(df.head())

print("------------------------------------------------------------")  # 60個
""" NG
import pandas as pd
import twder

usd = twder.specify_month("USD", 2020, 6) 
df = pd.DataFrame(usd)
df.columns = ["時間","現金(買)","現金(賣)",
              "即期(買)","即期(賣)"]
df.set_index("時間" , inplace=True)
print(df.head())
"""
print("------------------------------------------------------------")  # 60個

import pandas as pd
import twder

usd = twder.past_six_month("USD") 
df = pd.DataFrame(usd)
df.columns = ["時間","現金(買)","現金(賣)",
              "即期(買)","即期(賣)"]
df.set_index("時間" , inplace=True)
print(df.head())

print("------------------------------------------------------------")  # 60個

import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
"""
url = "https://jsjustweb.jihsun.com.tw/z/zc/zcp/zcp_2330.djhtm"
csvfile = "tmp_BalanceSheet.csv"
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
"""
print("------------------------------------------------------------")  # 60個

import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
"""
url = "https://jsjustweb.jihsun.com.tw/z/zc/zcp/zcp.djhtm?a=2330&b=3&c=Q"
csvfile = "tmp_CashFlow.csv"
ua = UserAgent()
user_agent = ua.random
headers = {'User-Agent': user_agent}
r = requests.get(url, headers=headers,verify=False)
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
"""

print("------------------------------------------------------------")  # 60個

import requests 
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import csv
"""
url = "https://jsjustweb.jihsun.com.tw/z/zc/zcp/zcp.djhtm?a=2330&b=2&c=Q"
csvfile = "tmp_IncomeStatement.csv"
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
"""
print("------------------------------------------------------------")  # 60個

"""
公開資訊觀測站
https://mops.twse.com.tw/mops/web/index

"""

import pandas as pd
import requests
from fake_useragent import UserAgent
from io import StringIO
import time

def get_monthly_report(s_type, year, month, delay=5):    
    if year > 1990:
        year -= 1911  
    URL = "https://mops.twse.com.tw/nas/t21/{}/" 
    stock_type = ["sii", "otc", "rotc"]
    URL = URL.format(stock_type[s_type])    
    url = URL + "t21sc03_{0}_{1}.html".format(str(year),str(month))
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    r.encoding = "big5"
    dfs = pd.read_html(StringIO(r.text), encoding="big5")
    items = []    
    for item in dfs:
        if item.shape[1] <= 11 and item.shape[1] >= 10:
            items.append(item)
    df = pd.concat(items)
    if "levels" in dir(df.columns):
        df.columns = df.columns.get_level_values(1)
    df["當月營收"] = pd.to_numeric(df["當月營收"], "coerce")
    df = df[~df["當月營收"].isnull()]
    df = df[df["公司代號"] != "合計"]    
    time.sleep(delay)

    return df
"""
df = get_monthly_report(0, 109, 1)
print(df.shape)
print(df.head())
"""
print("------------------------------------------------------------")  # 60個

import requests 
from bs4 import BeautifulSoup
import csv, time
"""
base_url = "https://www.twse.com.tw"
url = base_url + "/zh/brokerService/brokerServiceAudit"
# https://www.twse.com.tw/brokerService/brokerServiceAudit?showType=list&stkNo=1020&focus=6
csvfile = "tmp_BrokerBranchs.csv"
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
"""
print("------------------------------------------------------------")  # 60個

import datetime
import pandas as pd
import time
#from monthlyReport import get_monthly_report

data = []
now = datetime.datetime.now()
year = now.year
month = now.month - 1
if month == 0: 
    month = 12
    year -= 1
"""
for i in range(12):
    print("爬取月營收的月份: ", year,"/", month)
    try:
        key = "%d-%d-01"%(year, month)
        m_df = get_monthly_report(0, year, month)
        m_df.index = m_df["公司代號"]
        item_df = pd.DataFrame({key: m_df["當月營收"]}).transpose()
        data.append(item_df) 
    except Exception:
        print("錯誤: 月營收資料爬取錯誤...")
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    time.sleep(10)

df = pd.concat(data)
df.index = pd.to_datetime(df.index)
df = df.sort_index()
print(df.head())
df.to_csv("tmp_monthlysales.csv")

print("------------------------------")  # 30個

import pandas as pd

df = pd.read_csv("tmp_monthlysales.csv", index_col=0)
df.index = pd.to_datetime(df.index)
print(df["2330"])
df["2330"].plot(kind="line", title="台積電月營收")

print("------------------------------")  # 30個

import pandas as pd

df = pd.read_csv("tmp_monthlysales.csv", index_col=0)
df.index = pd.to_datetime(df.index)
tsmc = df["2330"]
print(tsmc/tsmc.shift()-1)
(tsmc/tsmc.shift()-1).plot(kind="line", title="台積電營收成長率")

print("------------------------------")  # 30個

import pandas as pd

df = pd.read_csv("tmp_monthlysales.csv", index_col=0)
df.index = pd.to_datetime(df.index)

df1 = df.iloc[-3:].mean() > df.iloc[-12:].mean()
print(df1[df1 == True].index)
print("------------------------------")
df2 = df.rolling(window=3, min_periods=2).mean()
df2 = (df2 > df2.shift()).iloc[-6:].sum()
print(df2[df2 == 6].head())
print("------------------------------")
df3 = df.iloc[-1] == df.iloc[-12:].max()
print(df3[df3 == True].index)
print("------------------------------")
"""
print("------------------------------------------------------------")  # 60個


"""

公開資訊觀測站
https://mops.twse.com.tw/mops/web/index

"""

import pandas as pd
import requests
from fake_useragent import UserAgent
from io import StringIO
import time

def get_monthly_report(s_type, year, month, delay=5):    
    if year > 1990:
        year -= 1911  
    URL = "https://mops.twse.com.tw/nas/t21/{}/" 
    stock_type = ["sii", "otc", "rotc"]
    URL = URL.format(stock_type[s_type])    
    url = URL + "t21sc03_{0}_{1}.html".format(str(year),str(month))
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    r.encoding = "big5"
    dfs = pd.read_html(StringIO(r.text), encoding="big5")
    items = []    
    for item in dfs:
        if item.shape[1] <= 11 and item.shape[1] >= 10:
            items.append(item)
    df = pd.concat(items)
    if "levels" in dir(df.columns):
        df.columns = df.columns.get_level_values(1)
    df["當月營收"] = pd.to_numeric(df["當月營收"], "coerce")
    df = df[~df["當月營收"].isnull()]
    df = df[df["公司代號"] != "合計"]    
    time.sleep(delay)

    return df
   


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

