import PySimpleGUI as sg
#--------------------vvv
#【1. import函式庫】
from pathlib import Path

#【2. 設定於應用程式顯示的字串】
title = "搜尋檔案名稱（資料夾與子資料夾）"
infolder = "."
label1, value1 = "要搜尋的字串", "test"

#【3.函數：確認在資料夾的檔案名稱是否包含特定字串】
def findfilename(infolder, findword):
    cnt = 0
    msg = ""
    filelist = []
    for p in Path(infolder).rglob("*.*"):   #將這個資料夾以及子資料夾的所有檔案
        if p.name[0] != ".":                #沒有隱藏檔案的話
            filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):       #再替每個檔案排序
        if filename.count(findword) > 0:    #如果找到1個以上的特定字串
            msg += filename + "\n"
            cnt += 1
    msg = "檔案個數 = " + str(cnt) + "\n" + msg
    return msg
#--------------------^^^
def execute():
    infolder = values["infolder"]
    value1 = values["input1"]
    #--------------------vvv
    #【4.執行函數】
    msg = findfilename(infolder, value1)
    #--------------------^^^
    window["text1"].update(msg)
#應用程式的介面
layout = [[sg.Text("要載入的資料夾", size=(14,1)),
           sg.Input(infolder, key="infolder"),sg.FolderBrowse("選取")],
          [sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
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
