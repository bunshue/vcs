# ch13_4.py
import requests, bs4
import csv

fn = "out13_4.csv"
tablelist = []                                              # 利率表串列
headlist = []
ratelist = []
url = 'http://www.taiwanrate.com/'
htmlfile = requests.get(url)
htmlfile.encoding = 'utf-8'                                 # 轉成utf-8
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
ratetable = objSoup.find_all('table')
# 列印表格欄位名稱
lefttop = ratetable[4].find('tr').find('tr').find('td')     # 第4個表格
headlist.append(lefttop.text)                               # 加入欄位名稱串列                
ratehead = ratetable[4].find('tr').find_all('a', 'bodytablehead')
for head in ratehead:
    headlist.append(head.text)                              # 加入欄位名稱串列
tablelist.append(headlist)                                  # 
# 以上是列印表格欄位名稱
# 以下是列印各銀行利率, 先找出第一個class='bodytabletr1'
ratetd = ratetable[4].find('tr', 'bodytabletr1')            # 找出第一筆利率   
for row in ratetd:
    ratelist.append(row.text)
tablelist.append(ratelist)                                  # 將第一筆銀行利率加入
while ratetd.find_next_sibling('tr'):                       # 找出其他銀行利率
    ratetd = ratetd.find_next_sibling('tr')
    ratelist = []
    for row in ratetd:
        ratelist.append(row.text)
    tablelist.append(ratelist)                              # 加入其它家銀行利率

with open(fn, 'w', newline = '') as csvFile:                # 寫入out13_4.csv
    csvWriter = csv.writer(csvFile)
    for row in tablelist:
        csvWriter.writerow(row)                             # 一次寫一筆













