import PySimpleGUI as sg
#--------------------vvv
#【1. import函式庫】
from pathlib import Path

#【2. 設定於應用程式顯示的字串】
title = "置換文字檔（資料夾之內的文字檔）"
infolder = "."
label1, value1 = "要搜尋的字串", "這個是"
label2, value2 = "置換字串", "那個是"
label3, value3 = "轉存資料夾", "outputfolder"
ext = "*.txt"

#【3.函數: 置換文字檔】
def replacefile(readfile, findword, newword, savefolder):
    try:
        msg = ""
        p1 = Path(readfile)                     #將文字檔
        text = p1.read_text(encoding="UTF-8")   #載入
        text = text.replace(findword, newword)  #置換
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)            #建立轉存資料夾
        filename = p1.name
        p2 = Path(savedir.joinpath(filename))
        p2.write_text(text, encoding="UTF-8")   #轉存檔案
        msg = "在" + savefolder+"轉存了"+ filename + " 喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【3.函數：置換資料夾之內的文字檔】
def replacefiles(infolder, findword, newword, savefolder):
    msg = ""
    filelist = []
    for p in Path(infolder).glob(ext):  #將這個資料夾的檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += replacefile(filename, findword, newword, savefolder)
    return msg
#--------------------^^^
def execute():
    infolder = values["infolder"]
    value1 = values["input1"]
    value2 = values["input2"]
    value3 = values["input3"]
    #--------------------vvv
    #【4.執行函數】
    msg = replacefiles(infolder, value1, value2, value3)
    #--------------------^^^
    window["text1"].update(msg)
#應用程式的介面
layout = [[sg.Text("要載入的資料夾", size=(14,1)),
           sg.Input(infolder, key="infolder"),sg.FolderBrowse("選取")],
          [sg.Text(label1, size=(14,1)), sg.Input(value1, key="input1")],
          [sg.Text(label2, size=(14,1)), sg.Input(value2, key="input2")],
          [sg.Text(label3, size=(14,1)), sg.Input(value3, key="input3")],
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
  