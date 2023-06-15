'''
查詢台銀牌告匯率
'''

import requests #匯入套件
from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"): #針對匯率表格分析
    cell = single_tr.findAll("td") #找到每一個表格
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] #找到表格中幣別
    currency_name = currency_name.replace("\r","") #取代不需要的字元
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate = cell[2].contents[0] #找到幣別匯率
    print(currency_name, currency_rate)
    filename = "bankRate" + currency_name + ".csv" #每種幣別存一個檔案
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime()) #記錄目前時間
    if not exists(filename):
        data = [['時間', '匯率'], [now_time, currency_rate]] #準備寫入檔案資料
    else:
        data = [[now_time, currency_rate]]
    f = open(filename, "a") #開啟檔案
    w = csv.writer(f) #建立寫入CSV物件
    w.writerows(data) #寫入資料
    f.close()
    


