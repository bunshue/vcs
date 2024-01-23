import PySimpleGUI as sg
#--------------------vvv
#【1. import函式庫】
from pathlib import Path

#【2. 設定於應用程式顯示的字串】
title = "顯示檔案的檔案容量總和（資料夾與子資料）"
infolder = "."
label1, value1 = "副檔名", "*"

#【3.函數：以最佳單位傳回檔案容量】
def format_bytes(size):
    units = ["位元組","KB","MB","GB","TB","PB","EB"]
    n = 0
    while size > 1024:
        size = size / 1024.0
        n += 1
    return str(int(size)) + " " + units[n]

#【3.函數：加總資料夾與子資料夾所有檔案的檔案容量】
def foldersize(infolder, ext):
    msg = ""
    allsize = 0
    filelist = []
    for p in Path(infolder).rglob(ext):     #將這個資料夾以及子資料夾的所有檔案
        if p.name[0] != ".":                #沒有隱藏檔案的話
            filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):       #再替每個檔案排序
        size = Path(filename).stat().st_size
        msg += filename + " : "+format_bytes(size)+"\n"
        allsize += size
    filesize = "檔案容量總和 = " + format_bytes(allsize) + "\n"
    filesize += "檔案個數 = " + str(len(filelist))+ "\n"
    msg = filesize + msg
    return msg
#--------------------^^^
def execute():
    infolder = values["infolder"]
    value1 = values["input1"]
    #--------------------vvv
    #【4.執行函數】
    msg = foldersize(infolder, value1)
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
