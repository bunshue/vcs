import pathlib
import unicodedata
import re
from pathlib import Path

print("------------------------------------------------------------")  # 60個
print("find_texts")
print("------------------------------------------------------------")  # 60個

search_folder = "testfolder"
search_pattern = "這個是"
search_file_type = "*.txt"

# 【函數：搜尋文字檔】
def findfile(readfile, findword):
    print("讀取檔案 :", readfile)
    try:
        msg = ""
        p = pathlib.Path(readfile)  # 文字檔的
        text = p.read_text(encoding="UTF-8")  # 載入文字
        cnt = text.count(findword)  # 搜尋字串
        if cnt > 0:  # 找到的話
            msg = "檔案 : " + readfile + ", 找到" + str(cnt) + "個。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"


# 【函數: 搜尋資料夾與子資料夾的文字檔】
def findfiles(search_folder, findword, ext):
    msg = ""
    filelist = []
    for p in pathlib.Path(search_folder).rglob(ext):  # 將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))  # 新增至列表
    for filename in sorted(filelist):  # 再替每個檔案排序
        msg += findfile(filename, findword)
    return msg


# 【執行函數】
msg = findfiles(search_folder, search_pattern, search_file_type)
print(msg)

print("------------------------------------------------------------")  # 60個
print("regreplace_texts")
print("------------------------------------------------------------")  # 60個

infolder = "testfolder"
value1 = ".個是"
value2 = "那個是"
value3 = "outputfolder"
ext = "*.txt"


# 【函數：以正規表示法置換文字檔的內容】
def replacefile(readfile, findword, newword, savefolder):
    try:
        msg = ""
        ptn = re.compile(findword)  # 建立搜尋模式
        p1 = Path(readfile)  # 文字檔的
        text = p1.read_text(encoding="UTF-8")  # 載入文字
        text = re.sub(ptn, newword, text)  # 置換
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)  # 建立轉存資料夾
        filename = p1.name
        p2 = Path(savedir.joinpath(filename))
        p2.write_text(text, encoding="UTF-8")  # 轉存檔案
        msg = "在" + savefolder + "轉存" + filename + "了。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"


# 【函數：置換資料夾之內的文字檔】
def replacefiles(infolder, findword, newword, savefolder):
    msg = ""
    filelist = []
    for p in Path(infolder).glob(ext):  # 將這個資料夾的檔案
        filelist.append(str(p))  # 新增至列表
    for filename in sorted(filelist):  # 再替每個檔案排序
        msg += replacefile(filename, findword, newword, savefolder)
    return msg


# 【執行函數】
msg = replacefiles(infolder, value1, value2, value3)
print(msg)  # 顯示結果


print("------------------------------------------------------------")  # 60個
# regfind_texts.py
print("------------------------------------------------------------")  # 60個

infolder = "testfolder"
value1 = ".個是"
value2 = "*.txt"


# 【函數：利用正規表示法搜尋文字檔】
def findfile(readfile, findword):
    try:
        msg = ""
        ptn = re.compile(findword)  # 建立搜尋模式
        p = Path(readfile)  # 文字檔的
        text = p.read_text(encoding="UTF-8")  # 載入文字
        cnt = len(re.findall(ptn, text))  # 搜尋字串
        if cnt > 0:  # 找到的話
            msg = readfile + "：" + "找到" + str(cnt) + "個\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"


# 【函數：以正規表示法搜尋資料夾與子資料夾的所有文字檔】
def findfiles(infolder, findword, ext):
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext):  # 將這個資料夾以及子資料夾的所有檔案
        print("p :", p)
        filelist.append(str(p))  # 新增至列表
    for filename in sorted(filelist):  # 再替每個檔案排序
        print("filename :", filename)
        msg += findfile(filename, findword)
    return msg


print('尋找檔案')
msg = findfiles(infolder, value1, value2)
print(msg)


print("------------------------------------------------------------")  # 60個
# replace_texts
print("------------------------------------------------------------")  # 60個

infolder = "testfolder"
value1 = "這個是"
value2 = "那個是"
value3 = "outputfolder"
ext = "*.txt"


# 【函數: 置換文字檔】
def replacefile(readfile, findword, newword, savefolder):
    try:
        msg = ""
        p1 = Path(readfile)  # 將文字檔
        text = p1.read_text(encoding="UTF-8")  # 載入
        text = text.replace(findword, newword)  # 置換
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)  # 建立轉存資料夾
        filename = p1.name
        p2 = Path(savedir.joinpath(filename))
        p2.write_text(text, encoding="UTF-8")  # 轉存檔案
        msg = "在" + savefolder + "轉存了" + filename + " 喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"


# 【函數：置換資料夾之內的文字檔】
def replacefiles(infolder, findword, newword, savefolder):
    msg = ""
    filelist = []
    for p in Path(infolder).glob(ext):  # 將這個資料夾的檔案
        filelist.append(str(p))  # 新增至列表
    for filename in sorted(filelist):  # 再替每個檔案排序
        msg += replacefile(filename, findword, newword, savefolder)
    return msg


# 【執行函數】
msg = replacefiles(infolder, value1, value2, value3)
print(msg)

print("------------------------------------------------------------")  # 60個
# normalize_texts.py
print("------------------------------------------------------------")  # 60個

search_folder = "testfolder"
value1 = "outputfolder"
search_file_type = "*.txt"


# 【函數：執行unicode正規化】
def normalizefile(readfile, savefolder):
    try:
        msg = ""
        p1 = pathlib.Path(readfile)  # 將文字檔
        text = p1.read_text(encoding="UTF-8")  # 載入
        text = unicodedata.normalize("NFKC", text)  # 執行unicode正規化
        savedir = pathlib.Path(savefolder)
        savedir.mkdir(exist_ok=True)  # 建立轉存資料夾
        filename = p1.name
        p2 = pathlib.Path(savedir.joinpath(filename))
        p2.write_text(text, encoding="UTF-8")  # 轉存檔案
        msg = "在" + savefolder + "轉存" + filename + "了喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"


# 【函數: 對資料夾之內的文字檔執行unicode正規化】
def normalizefiles(search_folder, savefolder, ext):
    msg = ""
    filelist = []
    for p in pathlib.Path(search_folder).glob(ext):  # 將這個資料夾的檔案
        filelist.append(str(p))  # 新增至列表
    for filename in sorted(filelist):  # 再替每個檔案排序
        msg += normalizefile(filename, savefolder)
    return msg


# 【執行函數】
msg = normalizefiles(search_folder, value1, search_file_type)
print(msg)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


