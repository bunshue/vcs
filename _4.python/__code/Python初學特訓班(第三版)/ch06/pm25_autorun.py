import sqlite3,ast,requests,os
from bs4 import BeautifulSoup

cur_path=os.path.dirname(__file__) # 取得目前路徑
conn = sqlite3.connect(cur_path + '/' + 'DataBasePM25.sqlite') # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

# 建立一個資料表
sqlstr='''
CREATE TABLE IF NOT EXISTS TablePM25 ("no" INTEGER PRIMARY KEY AUTOINCREMENT 
NOT NULL UNIQUE ,"SiteName" TEXT NOT NULL ,"PM25" INTEGER)
'''
cursor.execute(sqlstr)

url = "http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json"
# 讀取網頁原始碼
html=requests.get(url).text.encode('utf-8-sig')

print('資料已更新...')    
sp=BeautifulSoup(html,'html.parser')    
# 將網頁內轉換為 list,list 中的元素是 dict 
jsondata = ast.literal_eval(sp.text)
# 刪除資料表內容
conn.execute("delete from TablePM25")
conn.commit()

n=1
for site in jsondata:
    SiteName=site["SiteName"]
    if site["PM2.5"] == "ND":
        continue    
    PM25=0 if site["PM2.5"] == "" else int(site["PM2.5"])     
    print("站名:{}   PM2.5={}".format(SiteName,PM25))
    # 新增一筆記錄
    sqlstr="insert into TablePM25 values({},'{}',{})" .format(n,SiteName,PM25)
    cursor.execute(sqlstr)
    n+=1
    conn.commit() # 主動更新  

conn.close()  # 關閉資料庫連線  