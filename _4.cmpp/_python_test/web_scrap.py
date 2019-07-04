#!/usr/bin/python

#抓取網頁資料
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
#print(html.read(), 'utf-8')

#建立一個csv檔 逗號分隔值(comma-seperated values)
import csv
csvFile = open("F0035CH1aaaaa.CSV", 'w+', newline='')
try:
    writer =csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()
    
