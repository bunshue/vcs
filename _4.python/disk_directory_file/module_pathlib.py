"""

pathlib --- 物件導向檔案系統路徑


"""

import os
import sys

import pathlib

print("------------------------------------------------------------")  # 60個

print("列出子目錄：")
p = pathlib.Path('.')
print(p)

print("在當前目錄樹下列出 Python 原始碼檔案：")
cc = list(p.glob('**/*.py'))
print(cc)

print("瀏覽目錄樹內部：")

foldername = 'C:/_git/vcs/_1.data'
p = pathlib.Path(foldername)
q = p / '______test_files3' / '_excel'
print(q)

q.resolve()

print("查詢路徑屬性：")

print("q.exists()", q.exists())

print("q.is_dir()", q.is_dir())


foldername = 'C:/_git/vcs/_4.python/_data/'
p = pathlib.Path(foldername)
q = p / 'article2.txt'
print(q)

#q.resolve()

#filename = 'C:/_git/vcs/_4.python/_data/article2.txt'

#開啟檔案：

with q.open() as f:
    cc = f.readline()
    print(cc)

print("------------------------------------------------------------")  # 60個

foldername = 'C:/_git/vcs/_4.python/_data/'

cc = pathlib.PureWindowsPath(foldername).drive

print("所在的磁碟機 : ", cc)

cc = pathlib.PureWindowsPath(foldername).root

print("所在的root : ", cc)


p = pathlib.PureWindowsPath('C:/AA/BB/CC/DD/EE/FF/GG/HH/II/JJ/kk.py')
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])
print(p.parents[4])
print(p.parents[5])

p = pathlib.PurePath('C:/AA/BB/CC/DD/EE/FF/GG/HH/II/JJ/kk.py')
#邏輯上的父路徑：
print(p.parent)


print("CWD :", pathlib.Path.cwd())
print("HOME :", pathlib.Path.home())


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

p = pathlib.Path(filename)

print(p.stat().st_mode)

print(p.chmod(0o444))

print(p.stat().st_mode)

"""
Path.is_dir()
Path.is_file()
"""

print('------------------------------------------------------------')	#60個

path = pathlib.Path('test10_new06.py')
abs_path = path.resolve()
print(abs_path)
new_path = str(abs_path) + ".old"
print(new_path)

print('------------------------------------------------------------')	#60個

filepath = "檔案操作_新進1.py"
p = pathlib.Path(filepath)
print("檔案路徑　　　 = " + str(p))
print("檔案名稱　　　　 = " + p.name)
print("檔案副檔名　　 = " + p.suffix)
print("檔案副檔名以外 = " + p.stem)
print("資料夾名稱　　　　 = " + p.parent.name)
print("檔案大小　　 = " + str(p.stat().st_size) + "位元組")

print("------------------------------------------------------------")  # 60個

p = pathlib.Path(".")
p = p.joinpath("tmp_newfolder")
p.mkdir(exist_ok=True)

print("------------------------------------------------------------")  # 60個

infolder = "testfolder"
ext = "*.txt"
filelist = []
for p in pathlib.Path(infolder).glob(ext):  #將這個資料夾的檔案
    filelist.append(str(p))         #新增至列表
for filename in sorted(filelist):   #再替每個檔案排序
    print(filename)

print("------------------------------------------------------------")  # 60個

infolder = "testfolder"
ext = "*.txt"
filelist = []
for p in pathlib.Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
    filelist.append(str(p))         #新增至列表
for filename in sorted(filelist):   #再替每個檔案排序
    print(filename)

print("------------------------------------------------------------")  # 60個

infolder = "testfolder"
ext = "*.txt"
allsize = 0
filelist = []
for p in pathlib.Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
    filelist.append(str(p))         #新增至列表
for filename in sorted(filelist):   #再替每個檔案排序
    size = pathlib.Path(filename).stat().st_size
    print(filename + " = " + str(size) + "位元組")
    allsize += size
print("allsize = " + str(allsize) + "位元組")

print("------------------------------------------------------------")  # 60個

test_path = pathlib.Path(os.pardir)
print(test_path)
test_path.resolve()

print('------------------------------------------------------------')	#60個

cur_path = pathlib.Path(".")
size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        
print(size)

print('------------------------------------------------------------')	#60個

"""
cur_path = pathlib.Path(".")
new_path = cur_path.joinpath("backup")
size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        text_path.rename(new_path.joinpath(text_path.name))
        
print(size)
"""

print('------------------------------------------------------------')	#60個

"""
cur_path = pathlib.Path(".")
FILE_PATTERN = "*.txt"
path_list = cur_path.glob(FILE_PATTERN)
print(list(path_list))
[PosixPath('item_attributes.txt'), PosixPath('related_items.txt'), PosixPath('item_info.txt')]
"""

print("------------------------------------------------------------")  # 60個

"""
import datetime

FILE_PATTERN = "*.txt"
ARCHIVE = "archive"
if __name__ == '__main__':
    
    date_string = datetime.date.today().strftime("%Y-%m-%d")
    cur_path = pathlib.Path(".")
    new_path = cur_path.joinpath(ARCHIVE, date_string)
    new_path.mkdir()                                    
    paths = cur_path.glob(FILE_PATTERN)
    for path in paths:
        path.rename(new_path.joinpath(path.name))
"""

print('------------------------------------------------------------')	#60個

#撈出一層

infolder = "C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird"

extlist = ["*.jpg","*.png"]

msg = ""
for ext in extlist:                     #以多個副檔名調查
    filelist = []
    for p in pathlib.Path(infolder).glob(ext):  #將這個資料夾的檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += filename + "\n"
print(msg)

print('------------------------------------------------------------')	#60個

#show file size

foldername = 'C:/_git/vcs/_1.data/______test_files1'
file_type = "*.bmp"

#【函數：以最佳單位傳回檔案容量】
def format_bytes(size):
    units = ["位元組","KB","MB","GB","TB","PB","EB"]
    n = 0
    while size > 1024:
        size = size / 1024.0
        n += 1
    return str(int(size)) + " " + units[n]

#【函數：加總資料夾與子資料夾所有檔案的檔案容量】
def foldersize(foldername, file_type):
    msg = ""
    allsize = 0
    filelist = []
    for p in pathlib.Path(foldername).rglob(file_type):     #將這個資料夾以及子資料夾的所有檔案
        if p.name[0] != ".":                #沒有隱藏檔案的話
            filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):       #再替每個檔案排序
        size = pathlib.Path(filename).stat().st_size
        msg += filename + " : "+format_bytes(size)+"\n"
        allsize += size
    filesize = "檔案容量總和 = " + format_bytes(allsize) + "\n"
    filesize += "檔案個數 = " + str(len(filelist))+ "\n"
    msg = filesize + msg
    return msg

#【執行函數】
msg = foldersize(foldername, file_type)
print(msg)

print('------------------------------------------------------------')	#60個

#show file list

foldername = 'C:/_git/vcs/_1.data/______test_files1'
file_type = "*.bmp"

#【函數：建立檔案列表】
def listfiles(foldername, file_type):
    msg = ""
    filelist = []
    for p in pathlib.Path(foldername).rglob(file_type): #將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        msg += filename + "\n"
    msg = "檔案個數 = " + str(len(filelist)) + "\n" + msg
    return msg

#【執行函數】
msg = listfiles(foldername, file_type)
print(msg)


print('------------------------------------------------------------')	#60個

# find filename

print("搜尋資料夾內所有檔名符合特定字串的檔案")

foldername = 'C:/_git/vcs/_1.data/______test_files1'
value1 = "vcs_R"

#【函數：確認在資料夾的檔案名稱是否包含特定字串】
def findfilename(foldername, findword):
    cnt = 0
    msg = ""
    filelist = []
    for p in pathlib.Path(foldername).rglob("*.*"):   #將這個資料夾以及子資料夾的所有檔案
        if p.name[0] != ".":                #沒有隱藏檔案的話
            filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):       #再替每個檔案排序
        if filename.count(findword) > 0:    #如果找到1個以上的特定字串
            msg += filename + "\n"
            cnt += 1
    msg = "檔案個數 = " + str(cnt) + "\n" + msg
    return msg

#【執行函數】
msg = findfilename(foldername, value1)
print(msg)

print('------------------------------------------------------------')	#60個

foldername = 'C:/_git/vcs/_1.data/______test_files5'

msg = ""
pathlib.Path(foldername).mkdir(exist_ok=True)   #建立轉存檔案的資料夾

name = "tmp_AAAA"
newfolder = pathlib.Path(foldername).joinpath(name)
newfolder.mkdir(exist_ok=True)  #建立資料夾
msg = "在" + foldername + "建立了" + name + "了。"
print(msg)

name = "tmp_BBBB"
newfolder = pathlib.Path(foldername).joinpath(name)
newfolder.mkdir(exist_ok=True)  #建立資料夾
msg = "在" + foldername + "建立了" + name + "了。"
print(msg)

name = "tmp_CCCC"
newfolder = pathlib.Path(foldername).joinpath(name)
newfolder.mkdir(exist_ok=True)  #建立資料夾
msg = "在" + foldername + "建立了" + name + "了。"
print(msg)

print('------------------------------------------------------------')	#60個

all_files = sorted(os.listdir('system'))

print(pathlib.Path.cwd())

path1 = pathlib.Path.cwd() / 'system'
print(path1)

for i, _ in enumerate(all_files[:-1]):  #跳過最後一個
    print(i, _)

print("------------------------------------------------------------")  # 60個

HERE = pathlib.Path(__file__).resolve().parent

print(HERE)

cc = pathlib.Path
print(cc)

cc = pathlib.Path.home() / ".pydicom"

print(cc)

print("------------------------------------------------------------")  # 60個

cur_path = pathlib.Path(".")
FILE_PATTERN = "*.txt"
path_list = cur_path.glob(FILE_PATTERN)
print(list(path_list))
# [PosixPath('item_attributes.txt'), PosixPath('related_items.txt'), PosixPath('item_info.txt')]

print("------------------------------------------------------------")  # 60個

filename = "test10_new07.py"
filename = "C:/_git/vcs/_4.python/_data/蘇軾_念奴嬌_赤壁懷古.txt"

try:
    p = pathlib.Path(filename)  # 文字檔案的
    text = p.read_text(encoding="UTF-16")  # 載入文字
    print(text)  # 顯示
except:
    print("程式執行失敗。")  # 出現錯誤時

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個




