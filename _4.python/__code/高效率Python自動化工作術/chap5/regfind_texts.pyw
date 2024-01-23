import PySimpleGUI as sg
#--------------------vvv
#【1. import函式庫】
from pathlib import Path
import re

#【2. 設定於應用程式顯示的字串】
title = "以正規表示法搜尋文字檔（資料夾與子資料夾）"
infolder = "."
label1, value1 = "要搜尋的字串", ".個是"
label2, value2 = "副檔名", "*.txt"

#【3.函數：利用正規表示法搜尋文字檔】
def findfile(readfile, findword):
    try:
        msg = ""
        ptn = re.compile(findword)          #建立搜尋模式
        p = Path(readfile)                  #文字檔的
        text = p.read_text(encoding="UTF-8") #載入文字
        cnt = len(re.findall(ptn, text))    #搜尋字串
        if cnt > 0:                         #找到的話
            msg = readfile+"："+"找到" + str(cnt)+"個喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【3.函數：以正規表示法搜尋資料夾與子資料夾的所有文字檔】
def findfiles(infolder, findword, ext):
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += findfile(filename, findword)
    return msg
#--------------------^^^
def execute():
    infolder = values["infolder"]
    value1 = values["input1"]
    value2 = values["input2"]
    #--------------------vvv
    #【4.執行函數】
    msg = findfiles(infolder, value1, value2)
    #--------------------^^^
    window["text1"].update(msg)
#應用程式的介面
layout = [[sg.Text("要載入的資料夾", size=(14,1)),
           sg.Input(infolder, key="infolder"),sg.FolderBrowse("選取")],
          [sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
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
