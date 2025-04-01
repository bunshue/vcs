# plotly 集合 3

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

import plotly

print('------------------------------------------------------------')	#60個


"""
import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots

"""
print('------------------------------------------------------------')	#60個
'''
from plotly.graph_objs import Scatter, Layout

x = [1, 2, 3, 4]
y = [4, 3, 2, 1]
plotly.offline.plot({
    "data": [Scatter(x=x, y=y)],
    "layout": Layout(title="hello world")
})


print('------------------------------------------------------------')	#60個


from plotly.graph_objs import Scatter

plotly.offline.init_notebook_mode(connected=True)

data = [Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67,89,72,95])]
plotly.offline.plot({
    "data": data
}) 


print("------------------------------------------------------------")  # 60個

from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

data = [Scatter(
    x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67,89,72,95], 
    text = ['1號', '2號', '3號', '4號'],
    textposition="top center",
    #mode='markers')]
    #mode='lines')]
    mode='markers+lines+text')]
plotly.offline.plot({
    "data": data,
    "layout": Layout(title='二年甲班成績單')
}) 

print("------------------------------------------------------------")  # 60個

from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

data = [
    Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67,89,72,95], name='國文'), #第1個圖形
    Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[82,56,91,73], name='數學'), #第2個圖形
    Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[92,80,93,85], name='英文')  #第3個圖形
]
plotly.offline.plot({
    "data": data,
    "layout": Layout(title='二年甲班成績單')
}) 

print("------------------------------------------------------------")  # 60個

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

import csv
import json
import requests

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
plotly.offline.plot({  #以plotly繪圖
    "data": data,
    "layout": Layout(title='2017年個股統計圖')
}) 

print("------------------------------------------------------------")  # 60個

from plotly.graph_objs import Scatter

#plotly.offline.init_notebook_mode(connected=True)

data = [Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67,89,72,95])]
plotly.offline.plot({
    "data": data
})

print("------------------------------------------------------------")  # 60個

from plotly.graph_objs import Scatter

plotly.offline.init_notebook_mode(connected=True)

data = [Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67,89,72,95])]
plotly.offline.iplot({
    "data": data
}) 

print("------------------------------------------------------------")  # 60個

from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

data = [Scatter(
    x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67,89,72,95], 
    text = ['1號', '2號', '3號', '4號'],
    textposition="top center",
    #mode='markers')]
    #mode='lines')]
    mode='markers+lines+text')]
plotly.offline.iplot({
    "data": data,
    "layout": Layout(title='二年甲班成績單')
}) 

print("------------------------------------------------------------")  # 60個

from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

data = [
    Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67,89,72,95], name='國文'), #第1個圖形
    Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[82,56,91,73], name='數學'), #第2個圖形
    Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[92,80,93,85], name='英文')  #第3個圖形
]
plotly.offline.iplot({
    "data": data,
    "layout": Layout(title='二年甲班成績單')
}) 


print("------------------------------------------------------------")  # 60個

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
import json
import csv
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
'''
print("------------------------------------------------------------")  # 60個

from plotly.graph_objs import Scatter

plotly.offline.init_notebook_mode(connected=True)

data = [Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67, 89, 72, 95])]
plotly.offline.iplot({"data": data})


from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

data = [
    Scatter(
        x=["林大明", "陳聰明", "黃美麗", "熊小娟"],
        y=[67, 89, 72, 95],
        text=["1號", "2號", "3號", "4號"],
        textposition="top center",
        # mode='markers')]
        # mode='lines')]
        mode="markers+lines+text",
    )
]
plotly.offline.iplot({"data": data, "layout": Layout(title="二年甲班成績單")})


from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

data = [
    Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[67, 89, 72, 95], name="國文"),  # 第1個圖形
    Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[82, 56, 91, 73], name="數學"),  # 第2個圖形
    Scatter(x=["林大明", "陳聰明", "黃美麗", "熊小娟"], y=[92, 80, 93, 85], name="英文"),  # 第3個圖形
]
plotly.offline.iplot({"data": data, "layout": Layout(title="二年甲班成績單")})


def twodigit(n):  # 將數值轉為二位數字串
    if n < 10:
        retstr = "0" + str(n)
    else:
        retstr = str(n)
    return retstr


def convertDate(date):  # 轉捔民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  # 取出民國年
    realyear = str(int(yearstr) + 1911)  # 轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  # 組合日期
    return realdate


import requests
import json
import csv
from plotly.graph_objs import Scatter, Layout

plotly.offline.init_notebook_mode(connected=True)

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

urlbase = (
    "http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2017"  # 網址前半
)
urltail = "01&stockNo=2317&_=1521363562193"  # 網址後半
filepath = "tmp_stockyear2017.csv"

if not os.path.isfile(filepath):  # 如果檔案不存在就建立檔案
    for i in range(1, 13):  # 取1到12數字
        url_twse = urlbase + twodigit(i) + urltail  # 組合網址
        res = requests.get(url_twse)  # 回傳為json資料
        jdata = json.loads(res.text)  # json解析

        outputfile = open(filepath, "a", newline="", encoding="utf-8")  # 開啟儲存檔案
        outputwriter = csv.writer(outputfile)  # 以csv格式寫入檔案
        if i == 1:  # 若是1月就寫入欄位名稱
            outputwriter.writerow(jdata["fields"])
        for dataline in jdata["data"]:  # 逐月寫入資料
            outputwriter.writerow(dataline)
        time.sleep(0.5)  # 延遲0.5秒,否則有時會有錯誤
    outputfile.close()  # 關閉檔案

pdstock = pd.read_csv(filepath, encoding="utf-8")  # 以pandas讀取檔案
for i in range(len(pdstock["日期"])):  # 轉換日期式為西元年格式
    pdstock["日期"][i] = convertDate(pdstock["日期"][i])
pdstock["日期"] = pd.to_datetime(pdstock["日期"])  # 轉換日期欄位為日期格式
data = [
    Scatter(x=pdstock["日期"], y=pdstock["收盤價"], name="收盤價"),
    Scatter(x=pdstock["日期"], y=pdstock["最低價"], name="最低價"),
    Scatter(x=pdstock["日期"], y=pdstock["最高價"], name="最高價"),
]
plotly.offline.iplot({"data": data, "layout": Layout(title="2017年個股統計圖")})  # 以plotly繪圖

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import csv
import json
import requests
from plotly.graph_objs import Scatter, Layout



def twodigit(n):  #將數值轉為二位數字串
    if(n < 10):
        retstr = '0' + str(n)
    else:
        retstr = str(n)
    return retstr

def convertDate(date):  #轉換民國日期為西元:106/03/02->20170302
    str1 = str(date)
    yearstr = str1[:3]  #取出民國年
    realyear = str(int(yearstr) + 1911)  #轉為西元年
    realdate = realyear + str1[4:6] + str1[7:9]  #組合日期
    return realdate

plotly.offline.init_notebook_mode(connected=True)

pd.options.mode.chained_assignment = None  #取消顯示pandas資料重設警告

urlbase = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2017'  #網址前半
urltail = '01&stockNo=2317&_=1521363562193'  #網址後半
filepath = 'tmp_stockyear2017b.csv'

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

plt.show() 

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

