'''
新北市不動產仲介經紀商業同業公會網站
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

file_name = "新北市仲介" + ".csv" #設定csv寫入檔名
f = open(file_name, "w", encoding = 'utf8')
w = csv.writer(f)
httphead = 'http://www.tcr.org.tw/a/table_blogs/index/21654'

# 根據新北市不動產仲介經紀商業同業公會網站會員介紹首頁
# 與其後各頁差異，根據頁面規則涵蓋需要抓取頁面
for i in range(1,17):
    if i==1:
        htmlname=httphead
    else:
        htmlname=httphead+"?page="+str(i)
    html = urlopen(htmlname)
    # 以BeautifulSoup的"lxml"模式解析網頁，設定為bsObj物件
    bsObj = BeautifulSoup(html, "lxml")
    count=0

    for single_tr in bsObj.find("table").find("table").findAll("tr"): #抓取網頁資料
        if count==0:
            cell = single_tr.findAll("th") # 處理表頭
            F0 = cell[0].contents
            F1 = cell[1].contents
            F2 = cell[2].contents
            F3 = cell[3].contents
            F4 = cell[4].contents
        else:
            cell = single_tr.findAll("td") # 處理表格中資料
            # print(cell)
            F0 = cell[0].a.string
            F1 = cell[1].a.string
            F2 = cell[2].a.string
            F3 = cell[3].a.string
            F4 = cell[4].a.string
        print(F0,F1,F2,F3,F4)
        data = [[F0,F1,F2,F3,F4]]
        if i>1 and count>0:
            w.writerows(data) # 逐行寫入csv檔案
        count=count+1

f.close()

