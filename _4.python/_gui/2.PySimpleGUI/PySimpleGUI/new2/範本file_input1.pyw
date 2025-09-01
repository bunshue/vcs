import PySimpleGUI as sg
#--------------------vvv
#【1.import函式庫】

#【2.設定於應用程式顯示的字串】
title = "選取檔案+輸入欄位1個的應用程式"
infile = "test.txt"
label1, value1 = "輸入欄位1", "初始值1"

#【3.函數】
def testfunc(path, word1):
    msg = "檔案名稱 = " + path + "\n"
    msg += "輸入欄位的字串 = " + word1
    return msg
#--------------------^^^
def execute():
    infile = values["infile"]
    value1 = values["input1"]
    #--------------------vvv
    #【4.執行函數】
    msg = testfunc(infile, value1)
    #--------------------^^^
    window["text1"].update(msg)
#應用程式的介面
layout = [[sg.Text("載入的檔案", size=(14,1)),
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