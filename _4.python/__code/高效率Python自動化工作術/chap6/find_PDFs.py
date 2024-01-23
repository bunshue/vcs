from pathlib import Path
from pdfminer.high_level import extract_text

infolder = "testfolder"
value1 = "這個是"
value2 = "*.pdf"

#【函數：搜尋文字檔】
def findfile(readfile, findword):
    try:
        msg = ""
        text = extract_text(readfile)   #擷取文字
        cnt = text.count(findword)      #搜尋字串
        if cnt > 0:                     #找到的話
            msg = readfile+"："+"找到" + str(cnt)+"個了。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【函數: 搜尋資料夾與子資料夾的文字檔】
def findfiles(infolder, findword, ext):
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += findfile(filename, findword)
    return msg

#【執行函數】
msg = findfiles(infolder, value1, value2)
print(msg)
