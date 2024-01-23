import PySimpleGUI as sg
#--------------------vvv
#【1. import函式庫】
import requests
from bs4 import BeautifulSoup

#【2. 設定於應用程式顯示的字串】
title = "顯示RSS的書名一覽表"
label1, value1 = "RSS URL", "https://www.shoeisha.co.jp/rss/book/index.xml"
label2, value2 = "標籤", "title"

#【3.函數: 取得RSS的標籤】
def readRSSitem(url, tag):
    msg = ""
    r = requests.get(url)                   #取得URL的資料
    r.encoding = r.apparent_encoding        #自動辨識字元編碼
    soup= BeautifulSoup(r.text, "lxml")     #剖析XML資料
    for i, element in enumerate(soup.findAll(tag)):
        msg += str(i) + ":" + element.text + "\n" #新增標籤的元素
    return msg
#--------------------^^^
def execute():
    value1 = values["input1"]
    value2 = values["input2"]
    #--------------------vvv
    #【4.執行函數】
    msg = readRSSitem(value1, value2)
    #--------------------^^^
    window["text1"].update(msg)
#應用程式的介面
layout = [[sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
          [sg.Text(label2, size=(14,1)), sg.Input(value2, key="input2")],
          [sg.Button("執行", size=(20,1), pad=(5,15), bind_return_key=True)],
          [sg.Multiline(key="text1", size=(60,10))]]
#執行應用程式的處理
window = sg.Window(title, layout, font=(None,14))
while True:
    event, values = window.read()
    if event == None:
        break
    if event == "執行":
      execute()
window.close()
