import PySimpleGUI as sg
#--------------------vvv
#【1. import函式庫】
from pathlib import Path
from mutagen.mp3 import MP3
import datetime

#【2. 設定於應用程式顯示的字串】
title = "MP3檔案的總播放時間（資料夾與子資料夾）"
infolder = "."
ext = "*.mp3"

#【3.函數: 取得MP3檔案的播放時間】
def getplaytime(readfile):
    try:
        audio = MP3(readfile)   #載入檔案
        sec = audio.info.length #播放時間（秒）
        timestr = str(datetime.timedelta(seconds=sec))  #轉換成時分秒格式
        return sec, readfile + " " + timestr
    except:
        return 0, readfile + "：程式執行失敗。"
#【3.函數：搜尋資料夾與子資料夾MP3檔案】
def findfiles(infolder):
    sec = 0
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        val1, val2 = getplaytime(filename)
        sec += val1
        msg += val2 + "\n"
    totaltimestr = str(datetime.timedelta(seconds=sec))
    msg += "總播放時間 " + totaltimestr
    return msg
#--------------------^^^
def execute():
    infolder = values["infolder"]
    #--------------------vvv
    #【4.執行函數】
    msg = findfiles(infolder)
    #--------------------^^^
    window["text1"].update(msg)
#應用程式的介面
layout = [[sg.Text("要載入的資料夾", size=(14,1)),
           sg.Input(infolder, key="infolder"),sg.FolderBrowse("選取")],
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
