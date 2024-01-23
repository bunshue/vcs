import PySimpleGUI as sg
#--------------------vvv
#【1. import函式庫】
from pathlib import Path
from pdfminer.high_level import extract_text

#【2. 設定於應用程式顯示的字串】
title = "從PDF擷取文字"
infile = "test.pdf"

#【3.函數: 從PDF檔案擷取Text函數】
def extracttext(readfile):
  try:
    text = extract_text(readfile)
    return text
  except:
    return readfile + "：程式執行失敗。"
#--------------------^^^
def execute():
    infile = values["infile"]
    #--------------------vvv
    #【4.執行函數】
    msg = extracttext(infile)
    #--------------------^^^
    window["text1"].update(msg)
#應用程式的介面
layout = [[sg.Text("要載入的檔案", size=(14,1)),
           sg.Input(infile, key="infile"), sg.FileBrowse("選取")],
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