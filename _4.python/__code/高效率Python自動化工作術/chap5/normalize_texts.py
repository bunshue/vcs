from pathlib import Path
import unicodedata

infolder = "testfolder"
value1 = "outputfolder"
value2 = "*.txt"

#【函數：執行unicode正規化】
def normalizefile(readfile, savefolder):
    try:
        msg = ""
        p1 = Path(readfile)                         #將文字檔
        text = p1.read_text(encoding="UTF-8")       #載入
        text = unicodedata.normalize("NFKC", text)  #執行unicode正規化
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)            #建立轉存資料夾
        filename = p1.name
        p2 = Path(savedir.joinpath(filename))
        p2.write_text(text, encoding="UTF-8")   #轉存檔案
        msg = "在"+savefolder+"轉存"+ filename + "了喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【函數: 對資料夾之內的文字檔執行unicode正規化】
def normalizefiles(infolder, savefolder, ext):
    msg = ""
    filelist = []
    for p in Path(infolder).glob(ext):  #將這個資料夾的檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += normalizefile(filename, savefolder)
    return msg

#【執行函數】
msg = normalizefiles(infolder, value1, value2)
print(msg)