import PySimpleGUI as sg

#【2. 設定於應用程式顯示的字串】
title = "以正規表示法搜尋文字檔（資料夾與子資料夾）"
infolder = "."
label1, value1 = "要搜尋的字串", ".個是"
label2, value2 = "副檔名", "*.txt"

def execute():
    infolder = values["infolder"]
    value1 = values["input1"]
    value2 = values["input2"]

    msg = '你按了 執行 按鈕\n'
    msg += '取得' + infolder+"\n"
    msg += '取得' + value1+"\n"
    msg += '取得' + value2+"\n"
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

