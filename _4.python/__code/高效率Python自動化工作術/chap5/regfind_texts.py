from pathlib import Path
import re

infolder = "testfolder"
value1 = ".個是"
value2 = "*.txt"

#【函數：利用正規表示法搜尋文字檔】
def findfile(readfile, findword):
    try:
        msg = ""
        ptn = re.compile(findword)          #建立搜尋模式
        p = Path(readfile)                  #文字檔的
        text = p.read_text(encoding="UTF-8") #載入文字
        cnt = len(re.findall(ptn, text))    #搜尋字串
        if cnt > 0:                         #找到的話
            msg = readfile+"："+"找到" + str(cnt)+"個喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【函數：以正規表示法搜尋資料夾與子資料夾的所有文字檔】
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
