def twodigit(n):  #將數值轉為二位數字串
    if(n < 10):
        retstr = '0' + str(n)
    else:
        retstr = str(n)
    return retstr

def convertDate(date):  #轉捔民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  #取出民國年
    realyear = str(int(yearstr) + 1911)  #轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  #組合日期
    return realdate

import requests
import json, csv
import pandas as pd
import os
import time
import plotly
from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

pd.options.mode.chained_assignment = None  #取消顯示pandas資料重設警告

urlbase = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2017'  #網址前半
urltail = '01&stockNo=2317&_=1521363562193'  #網址後半
filepath = 'stockyear2017.csv'

if not os.path.isfile(filepath):  #如果檔案不存在就建立檔案
    for i in range(1, 13):  #取1到12數字
        url_twse = urlbase + twodigit(i) + urltail  #組合網址
        res = requests.get(url_twse)  #回傳為json資料
        jdata = json.loads(res.text)  #json解析
        
        outputfile = open(filepath, 'a', newline='', encoding='utf-8')  #開啟儲存檔案
        outputwriter = csv.writer(outputfile)  #以csv格式寫入檔案
        if i==1:  #若是1月就寫入欄位名稱
            outputwriter.writerow(jdata['fields'])
        for dataline in (jdata['data']):  #逐月寫入資料
            outputwriter.writerow(dataline)
        time.sleep(0.5)  #延遲0.5秒,否則有時會有錯誤
    outputfile.close()  #關閉檔案

pdstock = pd.read_csv(filepath, encoding='utf-8')  #以pandas讀取檔案
for i in range(len(pdstock['日期'])):  #轉換日期式為西元年格式
    pdstock['日期'][i] = convertDate(pdstock['日期'][i])
pdstock['日期'] = pd.to_datetime(pdstock['日期'])  #轉換日期欄位為日期格式
data = [
    Scatter(x=pdstock['日期'], y=pdstock['收盤價'], name='收盤價'),
    Scatter(x=pdstock['日期'], y=pdstock['最低價'], name='最低價'),
    Scatter(x=pdstock['日期'], y=pdstock['最高價'], name='最高價')
]
plotly.offline.iplot({  #以plotly繪圖
    "data": data,
    "layout": Layout(title='2017年個股統計圖')
}) 
