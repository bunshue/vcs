from pathlib import Path
import re

infolder = "testfolder"
value1 = ".個是"
value2 = "那個是"
value3 = "outputfolder"
ext = "*.txt"

#【函數：以正規表示法置換文字檔的內容】
def replacefile(readfile, findword, newword, savefolder):
    try:
        msg = ""
        ptn = re.compile(findword)          #建立搜尋模式
        p1 = Path(readfile)                 #文字檔的
        text = p1.read_text(encoding="UTF-8") #載入文字
        text = re.sub(ptn, newword, text)   #置換
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)            #建立轉存資料夾
        filename = p1.name
        p2 = Path(savedir.joinpath(filename))
        p2.write_text(text, encoding="UTF-8")   #轉存檔案
        msg = "在" + savefolder+"轉存"+ filename + "了。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【函數：置換資料夾之內的文字檔】
def replacefiles(infolder, findword, newword, savefolder):
    msg = ""
    filelist = []
    for p in Path(infolder).glob(ext):  #將這個資料夾的檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += replacefile(filename, findword, newword, savefolder)
    return msg

#【執行函數】
msg = replacefiles(infolder, value1, value2, value3)
print(msg)  #顯示結果