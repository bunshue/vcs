"""

pathlib --- 物件導向檔案系統路徑


"""

import os
import sys
import pathlib

print("------------------------------------------------------------")  # 60個

print("HOME :", pathlib.Path.home())
print("CWD  :", pathlib.Path.cwd())
print("CWD  :", pathlib.Path(".").resolve())  # 取出絕對路徑檔名

cc = pathlib.Path.cwd() / "tmp_newfolder"
print("NEW  :", cc)

print("列出目前目錄 :")
file = pathlib.Path(".")
print("相對路徑 :", file)
print("絕對路徑 :", file.resolve())  # 取出絕對路徑檔名

print("在當前目錄樹下列出 Python 原始碼檔案：")
cc = list(file.glob("**/*.py"))
print(cc)

print("瀏覽目錄樹內部：")

foldername = "D:/_git/vcs/_1.data"
file = pathlib.Path(foldername)
q = file / "______test_files3" / "_excel"
print(q)

print("絕對路徑 :", q.resolve())  # 取出絕對路徑檔名

print("查詢路徑屬性：")
print("q.exists()", q.exists())
print("q.is_dir()", q.is_dir())


foldername = "D:/_git/vcs/_4.python/_data/"
file = pathlib.Path(foldername)
q = file / "article2.txt"
print(q)

print("絕對路徑 :", q.resolve())  # 取出絕對路徑檔名

# filename = 'D:/_git/vcs/_4.python/_data/article2.txt'

# 開啟檔案：

with q.open() as f:
    cc = f.readline()
    print(cc)

print("------------------------------------------------------------")  # 60個

foldername = "D:/_git/vcs/_4.python/_data/"

cc = pathlib.PureWindowsPath(foldername).drive

print("所在的磁碟機 : ", cc)

cc = pathlib.PureWindowsPath(foldername).root

print("所在的root : ", cc)


file = pathlib.PureWindowsPath("C:/AA/BB/CC/DD/EE/FF/GG/HH/II/JJ/kk.py")
print(file.parents[0])
print(file.parents[1])
print(file.parents[2])
print(file.parents[3])
print(file.parents[4])
print(file.parents[5])

file = pathlib.PurePath("C:/AA/BB/CC/DD/EE/FF/GG/HH/II/JJ/kk.py")
print(file.parent)  # 邏輯上的父路徑

filename = "D:/_git/vcs/_1.data/______test_files1/picture1.jpg"

file = pathlib.Path(filename)

print(file.stat().st_mode)

print(file.chmod(0o444))

print(file.stat().st_mode)

"""
Path.is_dir()
Path.is_file()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

path = pathlib.Path("test10_new06.py")
print("絕對路徑 :", path.resolve())  # 取出絕對路徑檔名

new_path = str(abs_path) + ".old"
print(new_path)

path = pathlib.Path(os.pardir)
print(path)
print("絕對路徑 :", path.resolve())  # 取出絕對路徑檔名

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filepath = "檔案操作_新進1.py"
file = pathlib.Path(filepath)
print("檔案路徑　　　 = " + str(file))
print("檔案名稱　　　　 = " + file.name)
print("檔案副檔名　　 = " + file.suffix)
print("檔案副檔名以外 = " + file.stem)
print("資料夾名稱　　　　 = " + file.parent.name)
print("檔案大小　　 = " + str(file.stat().st_size) + "位元組")

print("------------------------------------------------------------")  # 60個

file = pathlib.Path(".")
file = file.joinpath("tmp_newfolder")
file.mkdir(exist_ok=True)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("pathlib.Path.glob()  搜尋所有檔案 單層 ST")
print("pathlib.Path.rglob() 搜尋所有檔案 多層 遞迴 ST")
print("------------------------------------------------------------")  # 60個

foldername = "D:/_git/vcs/_1.data"
foldername = "testfolder"
foldername = "."
ext = "*.py"

file = pathlib.Path(foldername)
print(file)

print("列出子目錄：")
filenames = pathlib.Path(foldername).glob(ext)  # 撈出單層
filenames = pathlib.Path(foldername).glob("**/*.py")  # 撈出單層

print(list(filenames))
for filename in filenames:
    print(filename)

size = 0
for text_path in filenames:
    if not text_path.is_symlink():
        size += text_path.stat().st_size
print(size)

print("------------------------------------------------------------")  # 60個

filelist = []
for filename in pathlib.Path(foldername).glob(ext):  # 撈出單層
    print(filename)  # 取出絕對路徑檔名
    print(filename.absolute())  # 取出絕對路徑檔名
    print("絕對路徑 :", filename.resolve())  # 取出絕對路徑檔名
    filelist.append(str(filename))  # 新增至列表

for filename in sorted(filelist):  # 排序
    print(filename)

print("------------------------------------------------------------")  # 60個

# 撈出一層
foldername = "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_angry_bird"

extlist = ["*.jpg", "*.png"]

msg = ""
for ext in extlist:  # 以多個副檔名調查
    filelist = []
    for filename in pathlib.Path(foldername).glob(ext):  # 撈出單層
        filelist.append(str(filename))  # 新增至列表
    for filename in sorted(filelist):  # 排序
        msg += filename + "\n"
print(msg)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

foldername = "testfolder"
foldername = "."
ext = "*.py"
filelist = []
count = 0
total_size = 0

for filename in pathlib.Path(foldername).rglob(ext):  # 撈出多層
    # print(filename)
    filelist.append(str(filename))  # 新增至列表
    count += 1
    total_size += filename.stat().st_size  # filename.stat().st_size 就是檔案大小（位元組）

allsize = 0
for filename in sorted(filelist):  # 排序
    size = pathlib.Path(filename).stat().st_size
    print(filename + " = " + str(size) + "位元組")
    allsize += size

print(f"檔案數量 : {count}")
print(f"總容量   : {total_size:,} Bytes")

print("------------------------------")  # 30個

# 先把結果存成 list, 這樣之後還可以重複使用 files
filenames = list(pathlib.Path(foldername).rglob(ext))  # 撈出多層
count = len(filenames)
total_size = sum(filename.stat().st_size for filename in filenames)

print(f"檔案數量 : {count}")
print(f"總容量   : {total_size:,} Bytes")
print(f"總容量   : {total_size / 1024:.2f} KB")
print(f"總容量   : {total_size / 1024 / 1024:.2f} MB")

for filename in filenames[:10]:
    print(filename)

print("------------------------------------------------------------")  # 60個

# show file size

foldername = "D:/_git/vcs/_1.data/______test_files1"
file_type = "*.bmp"


# 【函數：以最佳單位傳回檔案容量】
def format_bytes(size):
    units = ["位元組", "KB", "MB", "GB", "TB", "PB", "EB"]
    n = 0
    while size > 1024:
        size = size / 1024.0
        n += 1
    return str(int(size)) + " " + units[n]


# 【函數：加總資料夾與子資料夾所有檔案的檔案容量】
def foldersize(foldername, file_type):
    msg = ""
    allsize = 0
    filelist = []
    for filename in pathlib.Path(foldername).rglob(file_type):  # 撈出多層
        if filename.name[0] != ".":  # 沒有隱藏檔案的話
            filelist.append(str(filename))  # 新增至列表
    for filename in sorted(filelist):  # 排序
        size = pathlib.Path(filename).stat().st_size
        msg += filename + " : " + format_bytes(size) + "\n"
        allsize += size
    filesize = "檔案容量總和 = " + format_bytes(allsize) + "\n"
    filesize += "檔案個數 = " + str(len(filelist)) + "\n"
    msg = filesize + msg
    return msg


msg = foldersize(foldername, file_type)
print(msg)

print("------------------------------------------------------------")  # 60個

# show file list

foldername = "D:/_git/vcs/_1.data/______test_files1"
file_type = "*.bmp"


# 【函數：建立檔案列表】
def listfiles(foldername, file_type):
    msg = ""
    filelist = []
    for filename in pathlib.Path(foldername).rglob(file_type):  # 撈出多層
        filelist.append(str(filename))  # 新增至列表
    for filename in sorted(filelist):  # 排序
        msg += filename + "\n"
    msg = "檔案個數 = " + str(len(filelist)) + "\n" + msg
    return msg


msg = listfiles(foldername, file_type)
print(msg)

print("------------------------------------------------------------")  # 60個

# find filename

print("搜尋資料夾內所有檔名符合特定字串的檔案")

foldername = "D:/_git/vcs/_1.data/______test_files1"
value1 = "vcs_R"


# 【函數：確認在資料夾的檔案名稱是否包含特定字串】
def findfilename(foldername, findword):
    cnt = 0
    msg = ""
    filelist = []
    for filename in pathlib.Path(foldername).rglob("*.*"):  # 撈出多層
        if filename.name[0] != ".":  # 沒有隱藏檔案的話
            filelist.append(str(filename))  # 新增至列表
    for filename in sorted(filelist):  # 排序
        if filename.count(findword) > 0:  # 如果找到1個以上的特定字串
            msg += filename + "\n"
            cnt += 1
    msg = "檔案個數 = " + str(cnt) + "\n" + msg
    return msg


msg = findfilename(foldername, value1)
print(msg)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("pathlib.Path.glob()  搜尋所有檔案 單層 SP")
print("pathlib.Path.rglob() 搜尋所有檔案 多層 遞迴 SP")
print("------------------------------------------------------------")  # 60個

foldername = "D:/_git/vcs/_1.data/______test_files5"

msg = ""
pathlib.Path(foldername).mkdir(exist_ok=True)  # 建立轉存檔案的資料夾

name = "tmp_AAAA"
newfolder = pathlib.Path(foldername).joinpath(name)
newfolder.mkdir(exist_ok=True)  # 建立資料夾
msg = "在" + foldername + "建立了" + name + "了。"
print(msg)

name = "tmp_BBBB"
newfolder = pathlib.Path(foldername).joinpath(name)
newfolder.mkdir(exist_ok=True)  # 建立資料夾
msg = "在" + foldername + "建立了" + name + "了。"
print(msg)

name = "tmp_CCCC"
newfolder = pathlib.Path(foldername).joinpath(name)
newfolder.mkdir(exist_ok=True)  # 建立資料夾
msg = "在" + foldername + "建立了" + name + "了。"
print(msg)

print("------------------------------------------------------------")  # 60個
"""
all_files = sorted(os.listdir("system"))  # 排序

for i, _ in enumerate(all_files[:-1]):  # 跳過最後一個
    print(i, _)
"""
print("------------------------------------------------------------")  # 60個

HERE = pathlib.Path(__file__).resolve().parent  # 取出絕對路徑檔名
print(HERE)

cc = pathlib.Path
print(cc)

print("------------------------------------------------------------")  # 60個

filename = "test10_new07.py"
filename = "D:/_git/vcs/_4.python/_data/蘇軾_念奴嬌_赤壁懷古.txt"

try:
    filename = pathlib.Path(filename)  # 文字檔案的
    text = filename.read_text(encoding="UTF-16")  # 載入文字
    print(text)  # 顯示
except:
    print("程式執行失敗。")  # 出現錯誤時

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


# 6060
print("------------------------------------------------------------")  # 60個
# 3030
print("------------------------------")  # 30個
# 1515
print("---------------")  # 15個
