from pathlib import Path
from PIL import Image

infolder = "testfolder"
value1 = "outputfolder1"
extlist = ["*.jpg","*.png"]

#【函數: 儲存png檔案】
def savepng(readfile, savefolder):
    try:
        img = Image.open(readfile)              #載入圖片檔
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

#【執行函數】
msg = savefiles(infolder, value1)
print(msg)