import pathlib
import unicodedata

search_folder = "testfolder"
value1 = "outputfolder"
search_file_type = "*.txt"

#【函數：執行unicode正規化】
def normalizefile(readfile, savefolder):
    try:
        msg = ""
        p1 = pathlib.Path(readfile)                         #將文字檔
        text = p1.read_text(encoding="UTF-8")       #載入
        text = unicodedata.normalize("NFKC", text)  #執行unicode正規化
        savedir = pathlib.Path(savefolder)
        savedir.mkdir(exist_ok=True)            #建立轉存資料夾
        filename = p1.name
        p2 = pathlib.Path(savedir.joinpath(filename))
        p2.write_text(text, encoding="UTF-8")   #轉存檔案
        msg = "在"+savefolder+"轉存"+ filename + "了喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"

#【函數: 對資料夾之內的文字檔執行unicode正規化】
def normalizefiles(search_folder, savefolder, ext):
    msg = ""
    filelist = []
    for p in pathlib.Path(search_folder).glob(ext):  #將這個資料夾的檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += normalizefile(filename, savefolder)
    return msg

#【執行函數】
msg = normalizefiles(search_folder, value1, search_file_type)
print(msg)
