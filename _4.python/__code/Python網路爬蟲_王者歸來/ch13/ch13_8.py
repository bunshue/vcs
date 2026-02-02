# ch13_8.py
import requests, bs4
import csv

fn = 'out13_8.csv'
tablelist = []
headlist = []
url = 'https://www.moneydj.com/funddj/ya/YP401000.djhtm'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')      # 取得物件
fundtable = objSoup.find('table', id='oMainTable')
# 抓標題
objhead = fundtable.find('tr', id='oScrollMenu')
heads = objhead.find_all('th')
for head in heads:                                      # 輸出基金表格標題
    headlist.append(head.text)
tablelist.append(headlist)
# 抓基金表格資料
objtable = fundtable.find('tbody')
tables = objtable.find_all('tr')
for table in tables:                                    # 輸出各基金績效
    rowtext = table.text.strip()
    txt = rowtext.split('\n')                           # 將字串轉成串列
    tablelist.append(txt)
# 寫入csv    
with open(fn, 'w', newline = '') as csvFile:            # 寫入out13_8.csv
    csvWriter = csv.writer(csvFile)
    for row in tablelist:
        csvWriter.writerow(row)                         # 一次寫一筆
    
    
    














