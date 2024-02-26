"""

做一個檔案/資料夾的瀏覽公版程式 GUI介面

tk
pysimplegui

選取檔案/資料夾後 關閉此GUI介面 後續進行處理
ex: 圖片處理 圖片裁切縮放 檔案處理 播放......


"""

import os
import sys
import time
import random


import PySimpleGUI as sg

title = "選取檔案/資料夾"
infile = "test.txt"

def execute():
    print("執行")
    infile = values["infile"]

    mesg = "檔案名稱 = " + infile

    window["text1"].update(mesg)
    print(mesg)

#應用程式的介面
layout = [[sg.Text("載入的檔案", size=(14,1)),
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

print('選取檔案/資料夾 後, 做後續的處理.....')


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


