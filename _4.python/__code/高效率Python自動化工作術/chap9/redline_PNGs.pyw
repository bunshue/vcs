import PySimpleGUI as sg
#--------------------vvv
#【1. import函式庫】
from pathlib import Path
from PIL import Image
from PIL import ImageDraw

#【2. 設定於應用程式顯示的字串】
title = "在圖片畫斜線，再轉存為PNG圖檔（資料夾之內的文字檔）"
infolder = "testfolder"
label1, value1 = "轉存資料夾", "outputfolder3"
extlist = ["*.jpg","*.png"]

#【3.函數: 儲存png檔案】
def savepng(readfile, savefolder):
    try:
        img = Image.open(readfile)            #載入圖片檔
        #-----------------------------------
        draw = ImageDraw.Draw(img)
        draw.line((0, 0, img.width, img.height), fill="RED", width=8)
        #-----------------------------------
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)            #建立轉存資料夾
        filename = Path(readfile).stem+".png"   #建立檔案名稱
        img.save(savedir.joinpath(filename), format="PNG")  #以png格式轉存
        msg = "在"+savefolder + "轉存" + filename + "了喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【函數: 處理資料夾之內的圖片檔】
def savefiles(infolder, savefolder):
    msg = ""
    for ext in extlist:                     #以多個副檔名調查
        filelist = []
        for p in Path(infolder).glob(ext):  #將這個資料夾的檔案
            filelist.append(str(p))         #新增至列表
        for filename in sorted(filelist):   #再替每個檔案排序
            msg += savepng(filename, savefolder)
    return msg
#--------------------^^^
def execute():
    infolder = values["infolder"]
    value1 = values["input1"]
    #--------------------vvv
    #【4.執行函數】
    msg = savefiles(infolder, value1)
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
