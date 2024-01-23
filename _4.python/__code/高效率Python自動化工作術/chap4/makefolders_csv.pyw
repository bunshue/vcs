import PySimpleGUI as sg
#--------------------vvv
#【1. import函式庫】
from pathlib import Path
import csv

#【2. 設定於應用程式顯示的字串】
title = "利用名冊的CSV檔案建立資料夾"
infile = "namelist.csv"
label1, value1 = "轉存的資料夾", "outputfolder"

#【3.函數：根據CSV的內容建立資料夾】
def makefolders(readfile, savefolder):
  try:
    msg = ""
    Path(savefolder).mkdir(exist_ok=True)   #建立轉存檔案的資料夾
    f = Path(infile).open(encoding="UTF-8") #開啟檔案
    csvdata = csv.reader(f)                 #載入CSV的資料
    for row in csvdata:                     #取得每一列資料
      for foldername in row:              #逐次取得元素
        newfolder = Path(savefolder).joinpath(foldername)
        newfolder.mkdir(exist_ok=True)  #建立資料夾
        msg += "在" + savefolder + "建立了" + foldername + "了。\n"
    return msg
  except:
    return readfile + "：無法載入檔案。"
#--------------------^^^
def execute():
    infile = values["infile"]
    value1 = values["input1"]
    #--------------------vvv
    #【4.執行函數】
    msg = makefolders(infile, value1)
    #--------------------^^^
    window["text1"].update(msg)
#應用程式的介面
layout = [[sg.Text("要載入的檔案", size=(14,1)),
           sg.Input(infile, key="infile"), sg.FileBrowse("選取")],
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