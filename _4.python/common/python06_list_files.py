"""
各種方法的 ls dir

print('ls 測試 os.walk')  # 多層
print('ls 測試 os.listdir')
print('ls 測試 glob.glob') 轉出一層

#os.walk 遞迴搜尋檔案 只能轉出多層
#os.walk 是一個以遞迴方式列出特定路徑下，所有子目錄與檔案的函數

#os.listdir 取得檔案列表
#os.listdir 可以取得指定目錄中所有的檔案與子目錄名稱

轉出一層
轉出多層

"""

import os
import sys
import cv2
import glob
import stat
import time
import datetime

foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test"
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test/_good1/_good4/_good5"
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"  # 較少

print("------------------------------------------------------------")  # 60個
'''
print('取得檔案大小, 2個方法')

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filesize = os.stat(filename).st_size
print("容量 :", filesize, "位元組")
filesize = os.path.getsize(filename)
print("容量 :", filesize, "位元組")

print("------------------------------------------------------------")  # 60個

print("檢查檔案副檔名")

def is_image(filename):
    f = filename.lower()
    return (
        f.endswith(".png")
        or f.endswith(".jpg")
        or f.endswith(".jpeg")
        or f.endswith(".bmp")
        or f.endswith(".gif")
        or ".jpg" in f
        or f.endswith(".svg")
    )

filename1 = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_word/python_docx1.docx'
filename3 = 'C:/_git/vcs/_1.data/______test_files2/output.avi'

for filename in sorted([filename1, filename2, filename3]):
    print(filename)
    print(is_image(filename))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("ls 測試 os.walk ST")
print("------------------------------------------------------------")  # 60個

print("轉出多層 os.walk 1")
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"

total_folders = 0
total_files = 0
total_size = 0
all_files = list()

""" 分開寫
#   資料夾    子資料夾     檔案
for dirName, sub_dirNames, fileNames in os.walk(foldername):
    print("目前工作目錄名稱:   ", dirName)
    print("目前子目錄名稱串列: ", sub_dirNames)
    print("目前檔案名稱串列:   ", fileNames, "\n")
"""

for item in os.walk(foldername):  # 多層
    total_folders += 1
    # item[0]是路徑名稱，item[2]是檔案清單
    # print(item)
    print("資料夾 :", item[0])
    print("子資料夾:", item[1])
    print("檔案:", item[2])
    print("檔案個數:", len(item[2]))
    for fname in item[2]:
        #ffname = item[0] + "/" + fname  # 取出檔名完整路徑 same
        ffname = os.path.join(item[0], fname)  # 取出檔名完整路徑
        print(ffname)
        total_files += 1
        all_files.append(ffname)
        filesize = os.stat(ffname).st_size  # 取出檔案大小
        total_size += filesize
    print("------------------------------")  # 30個

if total_folders > 0:
    total_folders -= 1

print("位置 :", foldername)
print("容量 :", total_size, "位元組")
print("包含 :", total_files, "個檔案,", total_folders, "個資料夾")

print("顯示結果:")
for _ in all_files:
    print(_)
print("總容量 : " + str(total_size) + " 拜")

print("------------------------------------------------------------")  # 60個

print("轉出多層 os.walk 2")
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"
all_files = list()

# foldername 檔案所在資料夾
# subdir     檔案所在位置的其他資料夾
# files      檔案名稱
for foldername, subdir, files in os.walk(foldername):  # 多層
    if "folder_xxxxx" in subdir:  # 某些資料夾下的檔案不要處理
        print("某些資料夾下的檔案不要處理")
        subdir.remove("folder_xxxxx")
    for filename in files:  # 取得所有檔案，存入 all_files 串列中
        # print('檔案所在資料夾 :', foldername)
        # print('檔案所在位置的其他資料夾 :', subdir)
        # print('檔案名稱', filename)
        # all_files.append(foldername + '/' + filename)   #絕對路徑
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑

        all_files.append(long_filename)  # 絕對路徑

print(len(all_files))

if len(all_files) > 0:
    for filename in all_files:
        # print(filename)
        if not os.path.exists(filename):
            print("檔案不存在")
        else:
            abspath = os.path.abspath(filename)
            directory, short_filename = os.path.split(abspath)
            print("全檔名", abspath)
            print("檔案大小", os.stat(abspath).st_size)
            print("資料夾", directory)
            print("短檔名", short_filename)
            # long_filename = os.path.join('新資料夾', short_filename)    # 取得檔案的絕對路徑
            # print('新全檔名', long_filename)
            print()

    # long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
    # print(long_filename)

# 分析
if len(all_files) > 0:
    for filename in all_files:
        # print(filename)
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print("取得圖檔 :", filename)

    for filename in all_files:
        ext = filename.split(".")[-1]
        print("副檔名 :", ext)
        if ext == "png" or ext == "jpg":
            print("取得全檔名 :", filename)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("ls 測試 os.walk SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("ls 測試 os.listdir ST")
print("------------------------------------------------------------")  # 60個

print("轉出一層 os.listdir 1")

# foldername = "."  # 當前目錄
# foldername = "/"  # 根目錄
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"

#filenames = os.listdir(".")  # 搜尋目前工作目錄下的檔案

filenames = os.listdir(foldername)  # 轉出一層, 指定目錄, 若無參數, 就是當前目錄
print("轉出一層(資料夾+檔案)\n", filenames)
print("當前目錄下共有 :", len(filenames), "個項目(資料夾+檔案)")

for filename in filenames:
    print(filename)
    long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
    print(long_filename)
    sub, ext = os.path.splitext(filename)
    print("前檔名", sub, "副檔名", ext)

print("印出 filenames 內特定附檔名之檔案")
zz = [name for name in filenames if name.endswith((".jpg", ".txt"))]
print("*.jpg *.txt files:")
print(zz)

print("------------------------------------------------------------")  # 60個


# 統計資料夾或檔案的大小
def getFolderSize(pathname):
    size = 0

    if not os.path.isfile(pathname):
        lst = os.listdir(pathname)  # 轉出一層
        for subdirectory in lst:
            size += getFolderSize(pathname + "\\" + subdirectory)
    else:  # 是檔案才要統計大小
        size += os.path.getsize(pathname)  # 取出檔案大小
    return size


foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"
totalsizes = getFolderSize(foldername)
print("資料夾大小 : ", totalsizes, "拜")

print("------------------------------------------------------------")  # 60個


def dirTree(foldername, level=0):
    if level > 1:
        return
    for item in os.listdir(foldername):  # 轉出一層
        foldername2 = os.path.join(foldername, item)
        if os.path.isdir(foldername2):
            for i in range(level):
                print("   ", end="")
            print("+--" + item)
            try:
                dirTree(foldername2, level + 1)
            except:
                pass


foldername = "C:/_git/vcs/_1.data/______test_files5"
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"

print("轉出一層 os.listdir 3 看level")
dirTree(foldername)

print("------------------------------------------------------------")  # 60個


def _listFiles(files, foldername):
    for filename in os.listdir(foldername):  # 轉出一層
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        if os.path.isdir(long_filename):
            _listFiles(files, long_filename)
        else:
            files.append(long_filename)


def read_files(foldername):
    print(foldername)

    filelist = []

    # Make dir nice
    basedir = os.path.abspath(foldername)
    print("資料夾 : ", basedir)
    # Check whether it exists
    if not os.path.isdir(basedir):
        raise ValueError("The given path is not a valid directory.")
    # Find files recursively
    _listFiles(filelist, basedir)
    print(filelist)


print("轉出多層 os.listdir 8")
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"
all_series = read_files(foldername)

print("------------------------------------------------------------")  # 60個

print("轉出一層 os.listdir 9")

foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"

for filename in os.listdir(foldername):  # 轉出一層
    print(filename)
    if filename not in (os.curdir, os.pardir):
        print(filename)
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        print(long_filename)
    else:
        print("x")

print("------------------------------------------------------------")  # 60個

print("轉出多層 os.listdir 10")


def list_files4(foldername):
    filenames = os.listdir(foldername)  # 轉出一層
    for filename in filenames:
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        if os.path.isdir(long_filename):  # 資料夾 再找下去
            print("D", long_filename)
            list_files4(long_filename)
        else:  # 檔案
            print("f", long_filename, os.stat(long_filename).st_size)


foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"
list_files4(foldername)

print("------------------------------------------------------------")  # 60個


def list_files5(foldername):
    try:
        names = [n for n in os.listdir(foldername) if n.endswith(".py")]
    except OSError:
        print("Directory not readable: %s" % foldername, file=sys.stderr)
    else:
        for n in names:
            long_filename = os.path.join(foldername, n)  # 取得檔案的絕對路徑
            if os.path.isfile(long_filename):
                output = io.StringIO()
                print("Testing %s" % long_filename)
                try:
                    roundtrip(long_filename, output)
                except Exception as e:
                    print("  Failed to compile, exception is %s" % repr(e))
            elif os.path.isdir(long_filename):
                testdir(long_filename)


foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"
list_files5(foldername)

print("------------------------------------------------------------")  # 60個


def process(filename, listnames):
    print("process : ", filename)
    if os.path.isdir(filename):
        return processdir(filename, listnames)
    try:
        print(filename)
    except IOError as msg:
        sys.stderr.write("Can't open: %s\n" % msg)
        return 1


def processdir(dir, listnames):
    print("processdir : ", dir)
    try:
        names = os.listdir(dir)  # 轉出一層
    except OSError as msg:
        sys.stderr.write("Can't list directory: %s\n" % dir)
        return 1
    filenames = []
    for name in names:
        print(name)
        long_filename = os.path.join(dir, name)  # 取得檔案的絕對路徑
        print(long_filename)
        if os.path.normcase(long_filename).endswith(".py") or os.path.isdir(
            long_filename
        ):
            filenames.append(long_filename)
    filenames.sort(key=os.path.normcase)
    exit = None
    for filename in filenames:
        x = process(filename, listnames)
        exit = exit or x
    return exit


foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"
listnames = 1  # or 1
x = process(foldername, listnames)
print(x)

print("------------------------------------------------------------")  # 60個

stats = {}  # 字典
print(type(stats))


def addstats(ext, key, n):
    d = stats.setdefault(ext, {})
    d[key] = d.get(key, 0) + n


def statdir(dir):
    try:
        names = os.listdir(dir)  # 轉出一層
    except OSError as err:
        sys.stderr.write("Can't list %s: %s\n" % (dir, err))
        return
    for name in sorted(names):
        if name.startswith(".#"):
            continue  # Skip CVS temp files
        if name.endswith("~"):
            continue  # Skip Emacs backup files
        full = os.path.join(dir, name)
        if os.path.islink(full):
            addstats("<lnk>", "links", 1)
        elif os.path.isdir(full):
            statdir(full)
        else:
            statfile(full)


def statfile(filename):
    head, ext = os.path.splitext(filename)
    head, base = os.path.split(filename)
    if ext == base:
        ext = ""  # E.g. .cvsignore is deemed not to have an extension
    ext = os.path.normcase(ext)
    if not ext:
        ext = "<none>"
    addstats(ext, "files", 1)
    try:
        with open(filename, "rb") as f:
            data = f.read()
    except IOError as err:
        sys.stderr.write("Can't open %s: %s\n" % (filename, err))
        addstats(ext, "unopenable", 1)
        return
    addstats(ext, "bytes", len(data))
    if b"\0" in data:
        addstats(ext, "binary", 1)
        return
    if not data:
        addstats(ext, "empty", 1)
    # addstats(ext, "chars", len(data))
    lines = str(data, "latin-1").splitlines()
    addstats(ext, "lines", len(lines))
    del lines
    words = data.split()
    addstats(ext, "words", len(words))


def report():
    exts = sorted(stats)
    # Get the column keys
    columns = {}
    for ext in exts:
        columns.update(stats[ext])
    cols = sorted(columns)
    colwidth = {}
    colwidth["ext"] = max([len(ext) for ext in exts])
    minwidth = 6
    stats["TOTAL"] = {}
    for col in cols:
        total = 0
        cw = max(minwidth, len(col))
        for ext in exts:
            value = stats[ext].get(col)
            if value is None:
                w = 0
            else:
                w = len("%d" % value)
                total += value
            cw = max(cw, w)
        cw = max(cw, len(str(total)))
        colwidth[col] = cw
        stats["TOTAL"][col] = total
    exts.append("TOTAL")
    for ext in exts:
        stats[ext]["ext"] = ext
    cols.insert(0, "ext")

    def printheader():
        for col in cols:
            print("%*s" % (colwidth[col], col), end=" ")
        print()

    printheader()
    for ext in exts:
        for col in cols:
            value = stats[ext].get(col, "")
            print("%*s" % (colwidth[col], value), end=" ")
        print()
    printheader()  # Another header at the bottom


# Show file statistics by extension.

# filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename = "C:/_git/vcs/_1.data/______test_files3/"

if os.path.isdir(filename):
    print("目錄")
    statdir(filename)
elif os.path.isfile(filename):
    statfile(filename)
    print("檔案")
elif os.path.islink(filename):
    print("連結")
    linkto = os.readlink(filename)
    print(linkto)
else:
    print("不詳")

print(type(stats))
print(stats)

report()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("ls 測試 os.listdir SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("ls 測試 glob.glob ST")
print("------------------------------------------------------------")  # 60個

print("轉出一層")
print("轉出一層 指名 檔案格式")

foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"

filenames = glob.glob("*.py")  # 當前目錄下
filenames = glob.glob("python*.*")  # 當前目錄下
filenames = glob.glob(foldername)  # 這樣不可以
filenames = glob.glob(foldername + "/*.*")
filenames = glob.glob(foldername + "/*.jpg") + glob.glob(foldername + "/*.png")
filenames = glob.glob(foldername + "/*.jpg")
filenames = glob.glob(foldername + "/*")
filenames = glob.glob(foldername + "*")

filenames1 = glob.glob(foldername + "/*.jpg")
filenames2 = glob.glob(foldername + "/*.bmp")
filenames3 = glob.glob(foldername + "/*.png")
filenames4 = glob.glob(foldername + "/*.gif")
filenames = filenames1 + filenames2 + filenames3 + filenames4

# 也可以寫在一起
filenames = (
    glob.glob(foldername + "/*.jpg")
    + glob.glob(foldername + "/*.bmp")
    + glob.glob(foldername + "/*.png")
    + glob.glob(foldername + "/*.gif")
)

print("共有", len(filenames), "個檔案")

# 簡單列出
print(filenames)
for filename in filenames:
    print(filename)

# 檢查檔案或資料夾
for filename in filenames:
    print(filename)
    if os.path.isfile(filename):
        print("是一個檔案")
    elif os.path.isdir(filename):
        print("是一個資料夾")
    else:
        print("其他")
    abspath = os.path.abspath(filename)
    directory, short_filename = os.path.split(abspath)
    print("全檔名", abspath)
    print("資料夾", directory)
    print("短檔名", short_filename)
    long_filename = os.path.join("新資料夾", short_filename)  # 取得檔案的絕對路徑
    print("新全檔名", long_filename)
    print()

# 計算檔案容量
total_size = 0
for filename in filenames:
    print(f"{filename} : {os.path.getsize(filename)} bytes")
    print("檔案 : " + filename + ", 大小 : " + str(os.path.getsize(filename)) + " 拜")
    pathname, short_filename = os.path.split(filename)
    print(short_filename)
    total_size += os.path.getsize(filename)  # 取出檔案大小

print("總容量 : " + str(total_size) + " 拜")

# 撈出一層後 檢查是否是需要的附檔名
py = []
for filename in filenames:
    if filename.endswith(".py"):  # 以.py為副檔名
        py.append(filename)  # 加入串列
print(py)

print("------------------------------------------------------------")  # 60個

print("使用萬用字元")

# 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
jpg = glob.glob("C:/_git/vcs/_1.data/______test_files3/DrAP_test6/*.[jJ][pP][gG]")
print(jpg)

print(glob.glob(r"./test/*"))  # 找出所有檔案
print(glob.glob(r"./test/*.txt"))  # 找出所有副檔名為 .txt 的檔案，例如 1.txt、hello.txt
print(glob.glob(r"./test/[0-9].txt"))  # 找出所以名稱為一個數字，副檔名為 .txt 的檔案，例如 1.txt、2.txt
print(glob.glob(r"./test/????.*"))  # 找出所有檔名有四個字元的檔案，例如 test.txt、demo.py
print(glob.glob(r"./test/t*.*"))  # 找出所有 t 開頭的檔案，例如 test.txt、test.py
print(glob.glob(r"./test/*e*.*"))  # 找出所有檔名裡有 e 的檔案，例如 test.txt、hello.py

print("------------------------------------------------------------")  # 60個

print("轉出一層")
count = 1
filenames = glob.glob(foldername + "/*.jpg") + glob.glob(foldername + "/*.bmp")
for filename in filenames:
    print(filename)
    ext = filename.split(".")[-1]
    newfilename = "{}.{}".format(str(count), ext)
    print(newfilename)
    # 重新命名用
    # os.rename(filename, newfilename)
    count += 1

print("------------------------------------------------------------")  # 60個

print("指名pattern的搜尋 glob.glob1 多了一個l")

pattern = "*"
filenames = glob.glob1(foldername, pattern)
print(filenames)

pattern = "*.jpg"
filenames = glob.glob1(foldername, pattern)
print(filenames)

pattern = "*.bmp"
filenames = glob.glob1(foldername, pattern)
print(filenames)

print("------------------------------------------------------------")  # 60個

print("對一個資料夾內的所有圖檔做處理")
from PIL import Image

# filenames = glob.glob("./data/*.jpg")  # 取得 data 資料夾內所有的圖片
filenames = glob.glob(
    "./data/*.[jJ][pP][gG]"
)  # 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
for i in filenames:
    print("取得檔案 :", i)
    im = Image.open(i)  # 開啟圖片檔案
    size = im.size  # 取得圖片尺寸
    print(size)
    name = i.split("/")[::-1][0]  # 取出檔名

    # 轉存檔案格式
    name = i.lower().split("/")[::-1][0]  # 將檔名換成小寫 ( 避免 JPG 與 jpg 干擾 )
    png = name.replace("jpg", "png")  # 取出圖片檔名，將 jpg 換成 png
    # im.save(f"./data/png/{png}", "png")  # 轉換成 png 並存檔

    # 改變檔案品質
    # im.save(f"./data/jpg/{name}", quality=65, subsampling=0)  # 設定參數並存檔

    # 改變圖片大小
    im2 = im.resize((200, 200))  # 調整圖片尺寸為 200x200
    # im2.save(f"./data/resize/{name}")  # 調整後存檔到 resize 資料夾

print("------------------------------------------------------------")  # 60個

foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"
font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"

from PIL import Image, ImageFont, ImageDraw

imgs = glob.glob(
    "C:/_git/vcs/_1.data/______test_files3/DrAP_test6/*.jpg"
)  # 讀取資料夾裡所有的圖片

for i in imgs:
    print(i)
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    print(name)
    img = Image.open(i)  # 開啟圖片
    w, h = img.size
    font = ImageFont.truetype(font_filename, 100)
    text = Image.new(mode="RGBA", size=(400, 100), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(text)
    draw.text((0, 0), "PIG", fill=(255, 255, 255), font=font)
    text = text.rotate(30, expand=1)  # 逆時針旋轉30度

    img2 = Image.open(i)
    img2.paste(text, (50, 0), text)
    img2.convert("RGBA")
    img2.putalpha(150)
    img.paste(img2, (0, 0), img2)
    print(name)
    # img.save(f"./test/{name}")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("ls 測試 glob.glob SP")
print("------------------------------------------------------------")  # 60個

sys.exit()
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

foldername = "C:/_git/vcs/_1.data/______test_files5"
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"

for entry in os.scandir(foldername):
    info = entry.stat()
    # epoch timestamp轉換成日期字串
    da = datetime.datetime.utcfromtimestamp(info.st_mtime)
    dstr = da.strftime("%Y年%m月%d日, %H:%M:%S")

    if entry.is_dir():
        print("資料夾：", entry.name, "最後存取時間：", dstr)
    elif entry.is_file():
        print("檔案：", entry.name, "最後存取時間：", dstr)

print("時間差了8小時")

print("------------------------------------------------------------")  # 60個

foldername = "C:/_git/vcs/_1.data/______test_files5"
# foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'

for entry in os.scandir(foldername):
    info = entry.stat()
    da = datetime.datetime.utcfromtimestamp(info.st_mtime)
    dstr = da.strftime("%d/%m/%Y")
    if entry.is_file():
        size = int(os.path.getsize(entry.name) / 1024)  # 取出檔案大小
        ext = os.path.splitext(entry.name)
        print(
            entry.name,
            "\t" + str(size) + "KB\t",
            str(ext[-1].replace(".", "")) + "\t",
            dstr,
        )
    elif entry.is_dir():
        print(entry.name, "\t\t\t<DIR>\t", dstr)

"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


filename = "python04_string.py"
print("取得檔案 :", filename, " 的絕對路徑")
fullpath = os.path.abspath(filename)
print(fullpath)

print("os.path.basename:", os.path.basename(fullpath))
print("os.path.dirname:", os.path.dirname(fullpath))
print("os.path.getatime:", os.path.getatime(fullpath))
print("os.path.getmtime:", os.path.getmtime(fullpath))
print("os.path.getctime:", os.path.getctime(fullpath))

print("os.path.splitdrive:", os.path.splitdrive(fullpath))
print()
print("os.path.split:", os.path.split(fullpath))
directory, short_filename = os.path.split(fullpath)
print("長資料夾名 :", directory)
print("短檔名 :", short_filename)

print("os.path.splitext:", os.path.splitext(fullpath))
head, ext = os.path.splitext(fullpath)
print("前檔名 :", head)
print("副檔名 :", ext)

print("------------------------------------------------------------")  # 60個

#os.path.realpath 取得檔案的絕對路徑

print("取得目前python檔案的絕對路徑")
realpath = os.path.realpath(__file__)
print(realpath)

filename = "python04_string.py"
print("取得檔案 :", filename, " 的絕對路徑")
realpath = os.path.realpath(filename)
print(realpath)

print("長檔名 :", realpath)
p = os.path.dirname(realpath)
print("長資料夾名 :", p)
f = os.path.basename(realpath)
print("短檔名 : ", f)

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

short_filename = os.path.basename(filename)

print("長檔名 :", filename)
print("短檔名 :", short_filename)

cache_dir = os.path.dirname(filename)
print("長資料夾名 :", cache_dir)

head, tail = short_filename[:-3], short_filename[-3:]
print("主檔名 :", head)
print("副檔名 :", tail)

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
canonic = os.path.normcase(filename)
print("長檔名 :", canonic, "\t小寫磁碟機名")

print("------------------------------------------------------------")  # 60個

print("-------")
print(os.curdir)
print("-------")
print(os.pardir)
print("-------")

print("------------------------------------------------------------")  # 60個

for envname in "TMPDIR", "TEMP", "TMP":
    dirname = os.getenv(envname)
    print("cccccc", dirname)
    # print(dirname)

print("------------------------------------------------------------")  # 60個

def getuser():
    for name in ("LOGNAME", "USER", "LNAME", "USERNAME"):
        print(name)
        user = os.environ.get(name)
        if user:
            print(user)
            return user


print("get user name")
ccc = getuser()
print(ccc)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print('取得目前目錄至C:\的相對路徑')
print(os.path.relpath('C:\\'))

print('取得目前目錄至特定path的相對路徑')
print(os.path.relpath('C:\\_git\\ttttt1'))

print('取得目前檔案至C:\的相對路徑')
print(os.path.relpath('C:\\', 'python04_string.py'))

print('列出目前目錄的絕對路徑')
print(os.path.abspath('.'))

print('列出上一層目錄的絕對路徑')
print(os.path.abspath('..'))

print('列出檔案的絕對路徑')
print(os.path.abspath('python04_string.py'))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
new_filename = time.strftime("%Y%m%d_%H%M%S_") + filename.split('/')[-1]
print(new_filename)

print("------------------------------------------------------------")  # 60個

cwd = os.getcwd()

print("os.mkdir, 建立資料夾, 不能重複建立資料夾")
print("在當前目錄下, 建立資料夾")
os.mkdir(cwd+"/tmp_mkdir_1111")

print("改名資料夾")
os.rename(cwd+"/tmp_mkdir_1111",cwd+"/tmp_mkdir_2222")

print("刪除資料夾")
os.rmdir(cwd+"/tmp_mkdir_2222")

print("------------------------------------------------------------")  # 60個

#mkdir多一層保護
foldername = "ttttttttttttttttttt"
try:
    os.mkdir(foldername).exit
    print("已建立資料夾 :", foldername)
except OSError as msg:
    print('%s: 建立資料夾失敗 (%s)' % (foldername, str(msg)))

print("------------------------------------------------------------")  # 60個

#建立資料夾
mydir = 'tmp_my_dir'
# 如果mydir不存在就建立此資料夾
if os.path.exists(mydir):
    print(f"{mydir} 已經存在")
else:
    os.mkdir(mydir)
    print(f"建立 {mydir} 資料夾成功")

print("------------------------------------------------------------")  # 60個

#刪除資料夾
mydir = 'tmp_my_dir'
# 如果mydir存在就刪除此資料夾
if os.path.exists(mydir):
    os.rmdir(mydir)
    print(f"刪除 {mydir} 資料夾成功")
else:
    print(f"{mydir} 資料夾不存在")

print("------------------------------------------------------------")  # 60個
"""

foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"

currentdir = os.getcwd()
print("列出目前工作資料夾 ", currentdir)

# 如果foldername不存在就建立此資料夾
if os.path.exists(foldername):
    print("已經存在 %s " % foldername)
else:
    os.mkdir(foldername)
    print("建立 %s 資料夾成功" % foldername)

# 將目前工作資料夾改至foldername
os.chdir(foldername)
print("列出最新工作資料夾 ", os.getcwd())

# 將目前工作資料夾返回
os.chdir(currentdir)
print("列出返回工作資料夾 ", currentdir)

print("------------------------------------------------------------")  # 60個

print("測試 os.path.join")

files = ["filename1.py", "filename2.py", "filename3.py"]
for file in files:
    print(os.path.join("C:\\_git\\vcs\\_1.data\\______test_files3\\DrAP_test6", file))


print("4個參數")
print(os.path.join("C:\\", "_git", "ttttt1", "python04_string.py"))

print("3個參數")
print(os.path.join("C:\\_git", "ttttt1", "python04_string.py"))

print("2個參數")
print(os.path.join("C:\\_git\\ttttt1", "python04_string.py"))

foldername = "C:/_git/vcs/_1.data/______test_files1"
filename = "picture1.jpg"

print(foldername)
print(filename)
r = os.path.join(foldername, filename)
print("os.path.join(foldername, filename) =", r)

foldername1 = "C:/_git/vcs/_1.data/______test_files1"
foldername2 = "new_folder"
filename = "picture1.jpg"

print(foldername1)
print(foldername2)
print(filename)
r = os.path.join(foldername1, foldername2)
r = os.path.join(r, filename)

print("os.path.join(foldername, filename) =", r)

print("------------------------------------------------------------")  # 60個

print("用 os.path.getsize 取得 檔案 大小")
filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
print(filename, ":", os.path.getsize(filename))  # 取出檔案大小

print("用 os.path.getsize 取得 資料夾 大小, fail, 所以不能用這個方法取得資料夾大小")
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"
print(foldername, ":", os.path.getsize(foldername))  # 取出檔案大小 FAIL

print("------------------------------------------------------------")  # 60個


print("判斷真假 ST")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"

print("判斷檔案或資料夾存在 = ", os.path.exists(filename))
print("判斷檔案或資料夾存在 = ", os.path.exists(foldername))

if os.path.exists(filename):
    print(filename, "檔案存在")
else:
    print(filename, "檔案不存在")

if os.path.exists(foldername):
    print(foldername, "資料夾存在")
else:
    print(foldername, "資料夾不存在")

if os.path.isdir(foldername):
    print("是資料夾")
else:
    print("不是資料夾")


filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test6"

print("os.path.isabs:", os.path.isabs(filename))
print("os.path.isfile:", os.path.isfile(filename))
print("os.path.isdir:", os.path.isdir(filename))

print("是絕對路徑 = ", os.path.isabs("ch14_4.py"))
print("是絕對路徑 = ", os.path.isabs("C:\\_git\\vcs\\_1.data\\______test_files3\\ch14_4.py"))

print("是資料夾 = ", os.path.isdir("C:\\_git\\vcs\\_1.data\\______test_files3\\ch14_4.py"))
print("是資料夾 = ", os.path.isdir("C:\\_git\\vcs\\_1.data\\______test_files3"))

print("是檔案 = ", os.path.isfile("C:\\_git\\vcs\\_1.data\\______test_files3\\ch14_4.py"))
print("是檔案 = ", os.path.isfile("C:\\_git\\vcs\\_1.data\\______test_files3"))

print("判斷真假 SP")

print("------------------------------------------------------------")  # 60個


""" 新進待測試
新進 未整理  
檔案操作
檔名處理

    if filename.startswith("filen") and filename.endswith(".jpg"):
        #if remove_prefix:
        #    filename = filename[4:]
        fix_names.append(filename[:-3])

print("------------------------------------------------------------")  # 60個

srcfilename = input("請輸入來源檔案 : ")
dstfilename = input("請輸入目的檔案 : ")        
with open(srcfilename) as src_Obj:        # 用預設mode=r開啟檔案,傳回檔案物件src_Obj
    data = src_Obj.read()           # 讀取檔案到變數data

with open(dstfilename, 'w') as dst_Obj:   # 開啟檔案mode=w
    dst_Obj.write(data)             # 將data輸出到檔案

print("------------------------------------------------------------")  # 60個

os.path.exists() os.path.abspath()

cwd = os.getcwd()
print("當前工作目錄", cwd)

for item in items:
    print(os.path.abspath(item))

print("------------------------------------------------------------")  # 60個

cwd = os.getcwd()
print("當前工作目錄", cwd)

print('改變當前路徑')
os.chdir(foldername)

cwd = os.getcwd()
print("當前工作目錄", cwd)

print("------------------------------------------------------------")  # 60個

print('資料夾 增刪查改 範例, 檔案或目錄操作')
os.mkdir("目錄路徑")
os.rmdir("目錄路徑")
os.revmoe("檔案路徑")
os.rename("舊目錄路徑", "新目錄路徑")

#其實 rename 就是 move
filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/picture1.airi.jpg"
filename3 = filename2.replace("______test_files1", "______test_files5")  # 取出圖片檔名，將 jpg 換成 png
cc = os.rename(filename1, filename2)
cc = os.rename(filename2, filename3)
print(cc)

if filename.lower().endswith(".py"):
if filename.endswith('.jpg'):

if os.path.normcase(filename[-3:]) == ".py":

if filename.lower().endswith(".py"):

if filename.endswith('.c'):

print("------------------------------------------------------------")  # 60個

#time = os.path.getmtime(filename)
#print(time)

print("------------------------------------------------------------")  # 60個

def usage(msg):
    sys.stdout = sys.stderr
    print("Error:", msg)
    print("Use ``%s -h'' for help" % sys.argv[0])

prefix = 'aaaa'
exec_prefix = 'bbbb'
binlib = 'kkkk'
incldir = 'qqqq'

check_dirs = [prefix, exec_prefix, binlib, incldir]
for dir in check_dirs:
    if not os.path.exists(dir):
        usage('needed directory %s not found' % dir)
    if not os.path.isdir(dir):
        usage('%s: not a directory' % dir)

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
    
base = os.path.basename(filename)
base, ext = os.path.splitext(base)

dirname = os.path.dirname(filename)
print(dirname)



os.readlink(long_filename))
os.path.islink(long_filename)
os.path.isdir(file)
os.path.isdir(foldername)
os.path.exists(name):

print(type(stats))
print(stats)
"""


"""
檔名操作

"""

import stat

print("------------------------------------------------------------")  # 60個


# python import module : sys, os
# python import module : DDF 磁碟檔案資料夾操作

import shutil

cur_path = os.path.dirname(__file__)  # 取得目前路徑
print("現在路徑：" + cur_path)

"""
#拷貝檔案
destfile = 'C:/_git/vcs/_1.data/______test_files2/' + "ccccc.py"
print("拷貝檔案 " + destfile)
shutil.copy("test10_new12_file2.py",destfile )  # 檔案複製

print("拷貝檔案 " + destfile)
destfile = 'C:/_git/vcs/_1.data/______test_files2/' + "ccccc2.py"
shutil.copyfile('test10_new12_file2.py', destfile)  # 檔案複製
"""

# 目錄拷貝
import shutil

source_dir = "C:/_git/vcs/_1.data/______test_files1/__pic/_book"
dest_dir = "C:/_git/vcs/_1.data/______test_files2/_book"
print("cp -r " + source_dir + " " + dest_dir)
# shutil.copytree(source_dir, dest_dir)  # 目錄複製

"""
print("刪除目錄, 直接刪除, 不會放入資源回收筒")
import shutil
shutil.rmtree("C:\\dddddddddd\\aaa" )  # 刪除目錄
"""

# 重新命名檔案
# os.rename("foo.txt", "foo2.txt")
# 刪除檔案
# os.remove("foo2.txt");

print("mkdir")
# os.mkdir("test_python_dir")

print("chdir")
# os.chdir("test_python_dir")

filename_r = "C:/_git/vcs/_1.data/______test_files1/article2.txt"
print("檔案名稱 : ", os.path.getmtime(filename_r))

import os.path

filesize = os.path.getsize(filename_r)  # 取出檔案大小
print("filesize : ", filesize)

print("檔案時間 : ", os.path.getmtime(filename_r))

print("檔案時間 : ", time.ctime(os.path.getmtime(filename_r)))

print("檔案是否存在 : ", os.path.isfile(filename_r))

filename = os.path.abspath("test10_new10.py")
if os.path.exists(filename):  # 檢查檔案是否存在
    print("完整路徑名稱：" + filename)
    print("檔案大小：", os.path.getsize(filename))  # 取出檔案大小


"""
print("測試mkdir")

foldername = '__temp/tmpDir'
if os.path.exists(foldername):
    os.rmdir(foldername)
else:
    print(foldername + "目錄未建立, 建立之")
    os.mkdir(foldername)  # 建立目錄

foldername = "__temp/tmpDir"
if not os.path.exists(foldername):
    os.mkdir(foldername)
else:
    print(foldername + "已經存在!")   
"""

filename = "myFile.txt"
if os.path.exists(filename):
    os.remove(filename)
else:
    print(filename + "檔案未建立!")

import os.path

print("目前檔案:", __file__)

cur_path = os.path.dirname(__file__)  # 取得目前目錄路徑
print("現在目錄路徑:", cur_path)

filename = os.path.abspath("ospath.py")
filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

if os.path.exists(filename):
    print("完整路徑名稱:", filename)
    print("檔案大小:", os.path.getsize(filename))  # 取出檔案大小

    basename = os.path.basename(filename)
    print("最後的檔案或路徑名稱:", basename)

    dirname = os.path.dirname(filename)
    print("目前檔案目錄路徑:", dirname)

    print("是否為目錄:", os.path.isdir(filename))

    fullpath, fname = os.path.split(filename)
    print("目錄路徑:", fullpath)
    print("檔名:", fname)

    Drive, fpath = os.path.splitdrive(filename)
    print("磁碟機:", Drive)
    print("路徑名稱:", fpath)

    fullpath = os.path.join(fullpath + "\\" + fname)
    print("組合路徑: ", fullpath)
else:
    print("檔案不存在")


if os.path.exists(filename + ".png"):
    ans = input("此檔案已存在，要覆寫嗎？(y/n)")
    if ans != "y" and ans != "Y":
        exit(1)


"""
filename = '__temp/tmppic_new'

filename, ext = filename.split('.')
if os.path.exists(filename+'_wm.png'):
    ans = input('此檔案已存在，要覆寫嗎？(y/n)')
    if ans != 'y' and ans != 'Y':
        exit(1)
"""

print("拷貝檔案")

imageno = 1
for f in all_files:
    print("全檔名 : " + f)
    dirname, filename = f.split("\\")
    print("資料夾 : " + dirname)
    print("簡檔名 : " + filename)

    mainname, extname = filename.split(".")

    print("前檔名 : " + mainname)
    print("副檔名 : " + extname)

    targetfolder = "C:/_git/vcs/_1.data/______test_files2"
    targetfile = targetfolder + "/" + str(imageno) + "." + extname

    print("新檔名 : " + targetfile)

    shutil.copyfile(f, targetfile)  # 會直接覆蓋舊檔
    imageno += 1


"""
target_dir = source_dir + "output"

print("目標資料夾 : " + target_dir)

if os.path.exists(target_dir):
  print("目的資料夾已存在")
  exit(1)

split用法 TBD
os.mkdir(target_dir)
imageno = 0
for f in all_files:
  dirname, filename = f.split('/')
  mainname, extname = filename.split('.')
  targetfile = target_dir + '/' + str(imageno) + '.' + extname
  shutil.copyfile(f, targetfile)
  imageno += 1
"""


"""
import os
#異常處理
#刪除目錄
try:
    os.rmdir("aaaaa");
    print("remove directory aaaaa OK")
except IOError:
   print("Error: can't find file or read data")
else:
    print("remove directory aaaaa fail")

if not os.path.exists(source_dir):
	print("I can't find the specified directory.")
	exit(1)

"""


print(os.curdir)


"""
dirname = 'New Folder'
try:
  os.mkdir(dirname)
except OSError as dirname:
  print("can't make slave directory", dirname, ":", dirname)
"""

"""
dirname = 'New Foldercccc'
print('如果資料夾不存在  建立之')
## Create the win32com\gen_py directory.
#make_dir = os.path.join(lib_dir, "win32com", "gen_py")
if not os.path.isdir(dirname):
    print('建立資料夾 : ', dirname)
    os.mkdir(dirname)
else:
    print('資料夾已存在, 無法再建立')
"""


import os

testfiles = os.listdir("C:/_git/vcs/_1.data/______test_files1/__RW/_dicom")

# 簡檔名
testfiles = [x for x in testfiles if x.endswith("dcm")]

# 全檔名
testfiles = [
    os.path.join("C:/_git/vcs/_1.data/______test_files1/__RW/_dicom", x)
    for x in testfiles
]

for dcmfile in testfiles:
    print(dcmfile)


import os

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

file, ext = os.path.splitext(filename)

print(file)
print(ext)

base = os.path.basename(filename)
print(base)

fnfilter = os.path.basename
print(fnfilter)

# os.rename(filename, backup)

import os

this_dir = os.path.dirname(__file__)
print(__file__)
print(this_dir)

cwd = os.getcwd()
print(cwd)

aa = os.chdir(cwd)
print(aa)

dirname = "C:/_git/vcs/_4.python"
cc = os.chdir(dirname)
print(cc)

isympy_path = os.path.abspath(__file__)
isympy_dir = os.path.dirname(isympy_path)
sympy_top = os.path.split(isympy_dir)[0]
sympy_dir = os.path.join(sympy_top, "sympy")

if os.path.isdir(sympy_dir):
    # sys.path.insert(0, sympy_top)
    print("is dir")

# print(__path__[0])


print("取得目前python檔案的絕對路徑")
realpath = os.path.realpath(__file__)

# print(os.listdir(cache.dirname))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import re
import platform
import shutil


print("---- 基本設定 --------------------------------------------------------")  # 60個

filename = __file__
print("本檔長檔名", __file__)
print("本檔長檔名 : ", filename)

foldername = "C:/_git/vcs/_1.data/______test_files2/"

print(
    "---- 判斷檔案或資料夾 is exists --------------------------------------------------------"
)  # 60個

file_or_folder_name = filename  # 檔案或資料夾皆可

if os.path.exists(file_or_folder_name):
    print("檔案或資料夾 : ", filename, "存在")
else:
    print("檔案或資料夾 : ", filename, "不 存在")

if not os.path.exists(file_or_folder_name):
    print("檔案或資料夾 : ", filename, "不 存在")
else:
    print("檔案或資料夾 : ", filename, "存在")

if os.path.isdir(file_or_folder_name):
    print(filename, "是 資料夾")

if not os.path.isdir(file_or_folder_name):
    print("資料夾不存在")

if os.path.isfile(file_or_folder_name):
    print(filename, "是 檔案")

if os.path.islink(file_or_folder_name):
    print(filename, "是 連結")

# --------------------- new

"""
    os.remove(file)
    os.rmdir(dir)
    os.remove(file)
    os.mkdir(dir)
    os.mkdir("fb-photos")
    os.mkdir(pathdir)

 os.unlink(installer_name)





installer_name = os.path.abspath(installer_name)

        test = os.path.join(dir, "test")
        
            # Add the "test" directory to PYTHONPATH.
            sys.path = sys.path + [test]

    


"""


print(
    "---- 長檔名 轉 短檔名 basename() --------------------------------------------------------"
)  # 60個

print("長檔名 轉 短檔名 basename()")
short_filename = os.path.basename(filename)
print("短檔名 : ", short_filename)

print("副檔名", short_filename[-3:])

print(
    "---- 取得檔案/資料夾的絕對位置 abspath() --------------------------------------------------------"
)  # 60個

print("取得檔案/資料夾的絕對位置 abspath()")
long_filename = os.path.abspath(filename)
print("長檔名(絕對位置)", long_filename)

print("取得檔案/資料夾的絕對位置 abspath()")
long_foldername = os.path.abspath(foldername)
print("長資料夾名(絕對位置)", long_foldername)

print("取得檔案/資料夾的絕對位置 abspath()")
long_foldername = os.path.abspath("../..")
print("本檔長資料夾(絕對位置)", long_foldername)

"""
補兩個狀況

filename = 'xxx.py'
long_filename = os.path.abspath(filename)
print('長檔名(絕對位置)', long_filename)

filename = '../../xxxx/xxx.py'
long_filename = os.path.abspath(filename)
print('長檔名(絕對位置)', long_filename)


"""

print(
    "---- 取得所在的資料夾 dirname() --------------------------------------------------------"
)  # 60個

print("取得所在的資料夾 dirname()")
long_foldername = os.path.dirname(filename)
print("本檔長資料夾(絕對位置)", long_foldername)

print(
    "---- 連結資料夾 join(A, B) --------------------------------------------------------"
)  # 60個

print("------------------------------------------------------------")  # 60個


excecdir = "aaaaaa"
executable = os.path.join("ppppp", "Python")
print(executable)

print("join")
resdir = os.path.join("bbbb", "Resources")
print(resdir)

print("join")
libdir = os.path.join("aaaa", "Frameworks")
print(libdir)

mainprogram = os.path.join(resdir, "idlemain.py")
print(mainprogram)


fpath = "aaaaaaaaaaa"
correctfile = os.path.join(os.getcwd(), fpath)

correctfile = os.path.normpath(correctfile)

ccc = os.path.join(os.getcwd(), "ziptest2dir")
print(ccc)


# filename = os.path.join(dir, prog)

# os.chdir(os.path.join(ROOT, TK, "win"))


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DIRS = os.path.join(BASE_DIR, "templates")
NAME = os.path.join(BASE_DIR, "db.sqlite3")
AAAA = os.path.join(BASE_DIR, "static")

print(DIRS)
print(NAME)
print(AAAA)


print("------------------------------------------------------------")  # 60個


print("---- 混和應用 --------------------------------------------------------")  # 60個

major = 3
minor = 8
dll_file = "python%s%s.dll" % (major, minor)

dll_path = os.path.join(foldername, "new_dll", dll_file)
print("新建dll完整路徑 : ", dll_path)

print("------------------------------------------------------------")  # 60個

current_version = "%s.%s.%s" % (major, minor, int(time.time() / 3600 / 24))
full_current_version = current_version
print("新建版本完整路徑 : ", full_current_version)

print("------------------------------------------------------------")  # 60個

PATH = "/".join(os.path.abspath(filename).split("/")[:-2])
print(PATH)

print("------------------------------------------------------------")  # 60個

print("取得所在的資料夾 dirname()")
here = os.path.abspath(os.path.dirname(filename))
print(here)
par = os.path.pardir
print(par)

print("取得檔案的絕對位置 abspath()")
ROOT = os.path.abspath(os.path.join(here, par, par))
print(ROOT)


print("------------------------------------------------------------")  # 60個

head, tail = os.path.split(filename)
print("頭", head)
print("尾", tail)
tempname = os.path.join(head, "@" + tail)
print(tempname)

print("------------------------------------------------------------")  # 60個

print("依分隔號區切分 : ")
path_split = filename.split(os.sep)
print(path_split)

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

retval = filename[:-4]
print("長資料夾 + 前檔名", retval)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

filename = "python-%s%s.msi" % (full_current_version, "ccccc")
print(filename)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


def get_header_version_info(srcdir):
    print()
    print(srcdir)
    print()

    patchlevel_h = os.path.join(srcdir, "..", "Include", "patchlevel.h")
    print(patchlevel_h)


def get_sys_version_info():
    major, minor, micro, level, serial = sys.version_info
    release = version = "%s.%s" % (major, minor)
    release += ".%s" % micro
    if level != "final":
        release += "%s%s" % (level[0], serial)
    return version, release


def get_version_info():
    try:
        return get_header_version_info(".")
    except (IOError, OSError):
        version, release = get_sys_version_info()
        print >> sys.stderr, "Can't get version info from Include/patchlevel.h, " "using version of this interpreter (%s)." % release
        return version, release


get_header_version_info(".")
print("aaa", get_sys_version_info())
print("bbb", get_version_info())


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

string = "this is a lion"
print(string)

string = string.replace("lion", "mouse")
print(string)

print("------------------------------------------------------------")  # 60個


"""
os.chdir(os.path.expanduser('~/Documents'))

"""
print("------------------------------------------------------------")  # 60個


def cmp(f1, f2):
    bufsize = 1024 * 8
    with open(f1, "rb") as fp1, open(f2, "rb") as fp2:
        while True:
            b1 = fp1.read(bufsize)
            b2 = fp2.read(bufsize)
            if b1 != b2:
                return False
            if not b1:
                return True


def copy(src, dst):
    if os.path.isfile(dst) and cmp(src, dst):
        return
    shutil.copy(src, dst)


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


def copy(src, dst, mkdirs=0):
    """Copy a file or a directory."""
    if mkdirs:
        makedirs(os.path.dirname(dst))
    if os.path.isdir(src):
        shutil.copytree(src, dst, symlinks=1)
    else:
        shutil.copy2(src, dst)


def copytodir(src, dstdir):
    """Copy a file or a directory to an existing directory."""
    dst = pathjoin(dstdir, os.path.basename(src))
    copy(src, dst)


def makedirs(dir):
    """Make all directories leading up to 'dir' including the leaf
    directory. Don't moan if any path element already exists."""
    try:
        os.makedirs(dir)
    except OSError as why:
        if why.errno != errno.EEXIST:
            raise


def buildLibraries():
    """
    Build our dependencies into $WORKDIR/libraries/usr/local
    """
    print("")
    print("Building required libraries")
    print("")
    universal = os.path.join(WORKDIR, "libraries")
    os.mkdir(universal)
    os.makedirs(os.path.join(universal, "usr", "local", "lib"))
    os.makedirs(os.path.join(universal, "usr", "local", "include"))

    for recipe in library_recipes():
        buildRecipe(recipe, universal, ARCHLIST)


def buildPythonDocs():
    curDir = os.getcwd()
    os.chdir(buildDir)

    runCommand("make clean")
    runCommand("make html")
    os.chdir(curDir)
    if not os.path.exists(docdir):
        os.mkdir(docdir)
    os.rename(os.path.join(buildDir, "build", "html"), docdir)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("顯示目前 PATH")
print(sys.path)
print(sys.path[0])

pathlist = os.environ["PATH"].split(os.pathsep)
print(pathlist)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("預設用法 : ")

curdir = [os.curdir]
print("目前目錄 : ", curdir)

pardir = [os.pardir]
print("上層目錄 : ", pardir)

pwd = os.getcwd()

print("目前位置 : ", pwd)


# getcwd()方法顯示當前的工作目錄。
cur_path = os.getcwd()  # 取得目前路徑
print("現在路徑：" + cur_path)

"""
cur_path = os.getcwd() # 取得目前路徑
file=cur_path + "\dir2\copyfile.py" 
os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔
"""

print(os.sep)
print(os.altsep)


ADDRESS = r"\\.\pipe\_test_pipe-%s" % os.getpid()
print(ADDRESS)


"""
未整理
os.chdir(foldername2)


----


user = os.getlogin()
print(user)

font_file = os.path.join(os.path.dirname(__file__), "OpenFlame.ttf")
print(font_file)


os.remove(fname)
os.rename(temp_fname, fname)

no_asm = int(platform.release().split(".")[0]) < 9
print(no_asm)


"""

"""
print('取得檔案的絕對位置 abspath()')
dest = os.path.abspath(os.path.join(foldername, "..", name + "Upd"))
print(dest)
"""

# -------

# os.makedirs(dest)

"""
for name in os.listdir(foldername):
    path, ext = os.path.splitext(name)

    filename = os.path.normpath(os.path.join(foldername, name))
    destname = os.path.normpath(os.path.join(dest, name))
    #print("%s -> %s" % (filename, destname))
"""
"""

shutil.rmtree(foldername2)

os.makedirs(foldername2)

#未知用意
#os.symlink('python', os.path.join(foldername2, 'python.exe'))

"""


"""
import os

dirname = os.path.dirname(__file__)

os.path.basename(script):



os.chdir(dir)
os.rename(fn, ','+fn)

if os.path.normcase(fn).endswith(".py")


        

os.remove(os.path.join(lib_dir, "win32", "dbi.pyd.old"))



import os

開啟外部程式
#rc = os.system("nasm -f win64 -DNEAR -Ox -g ms\\uptable.asm")

rc = os.system('calc')

os.system('cls') #在cmd視窗下清除螢幕

os.system('cls' if os.name == 'nt' else 'clear')




TEST_SUPPORT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_HOME_DIR = os.path.dirname(TEST_SUPPORT_DIR)
self._environ = os.environ

self.procfile = '/proc/{pid}/statm'.format(pid=os.getpid())



import os

dir = "myDir"


cur_path = os.path.dirname(__file__) # 取得目前路徑



import os

cur_path=os.path.dirname(__file__) # 取得目前路徑  
os.system("cls")  # 清除螢幕
os.system("mkdir dir2")  # 建立 dir2 目錄
os.system("copy ossystem.py dir2\copyfile.py") # 複製檔案 
file=cur_path + "\dir2\copyfile.py" 
os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔


cur_path = os.path.dirname(__file__) # 取得目前路徑

sys.path.insert(0, "../src")

       filename = img['source'].split('/')[-1].split('?')[0]
       print(filename)

dirname = os.path.dirname(__file__)"




filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
directory = os.path.dirname(filename) or '.'




"""

import ctypes


def genwincodec():
    import platform

    code = ''' """Python Character Mapping Codec %s generated on Windows:
%s with the command:
  python Tools/unicode/genwincodec.py %s
"""  # "
''' % (
        "cp950",
        " ".join(platform.win32_ver()),
        950,
    )

    print(code)


genwincodec()

# Get the list of available locales.
if platform.system() == "Windows":
    print("Windows")
else:
    print("Not Windows")

    os_name = platform.system().lower()
    if "windows" in os_name:
        system("cls")
    else:
        system("clear")


print(sys.platform)


print(os.path.expanduser("~"))
history = os.path.join(os.path.expanduser("~"), ".python_history")
print(history)

print(sys.platform)
print(sys.platform[:4])

from os.path import pardir, realpath

_PY_VERSION = sys.version.split()[0]
_PY_VERSION_SHORT = sys.version[:3]
_PY_VERSION_SHORT_NO_DOT = _PY_VERSION[0] + _PY_VERSION[2]
_PREFIX = os.path.normpath(sys.prefix)
_BASE_PREFIX = os.path.normpath(sys.base_prefix)
_EXEC_PREFIX = os.path.normpath(sys.exec_prefix)
_BASE_EXEC_PREFIX = os.path.normpath(sys.base_exec_prefix)
_CONFIG_VARS = None
_USER_BASE = None


def get_platform():
    """Return a string that identifies the current platform.

    This is used mainly to distinguish platform-specific build directories and
    platform-specific built distributions.  Typically includes the OS name
    and version and the architecture (as supplied by 'os.uname()'),
    although the exact information included depends on the OS; eg. for IRIX
    the architecture isn't particularly important (IRIX only runs on SGI
    hardware), but for Linux the kernel version isn't particularly
    important.

    Examples of returned values:
       linux-i586
       linux-alpha (?)
       solaris-2.6-sun4u
       irix-5.3
       irix64-6.2

    Windows will return one of:
       win-amd64 (64bit Windows on AMD64 (aka x86_64, Intel64, EM64T, etc)
       win-ia64 (64bit Windows on Itanium)
       win32 (all others - specifically, sys.platform is returned)

    For other non-POSIX platforms, currently just returns 'sys.platform'.
    """
    if os.name == "nt":
        # sniff sys.version for architecture.
        prefix = " bit ("
        i = sys.version.find(prefix)
        if i == -1:
            return sys.platform
        j = sys.version.find(")", i)
        look = sys.version[i + len(prefix) : j].lower()
        if look == "amd64":
            return "win-amd64"
        if look == "itanium":
            return "win-ia64"
        return sys.platform

    if os.name != "posix" or not hasattr(os, "uname"):
        # XXX what about the architecture? NT is Intel or Alpha
        return sys.platform

    # Set for cross builds explicitly
    if "_PYTHON_HOST_PLATFORM" in os.environ:
        return os.environ["_PYTHON_HOST_PLATFORM"]

    # Try to distinguish various flavours of Unix
    osname, host, release, version, machine = os.uname()

    # Convert the OS name to lowercase, remove '/' characters
    # (to accommodate BSD/OS), and translate spaces (for "Power Macintosh")
    osname = osname.lower().replace("/", "")
    machine = machine.replace(" ", "_")
    machine = machine.replace("/", "-")

    if osname[:5] == "linux":
        # At least on Linux/Intel, 'machine' is the processor --
        # i386, etc.
        # XXX what about Alpha, SPARC, etc?
        return "%s-%s" % (osname, machine)
    elif osname[:5] == "sunos":
        if release[0] >= "5":  # SunOS 5 == Solaris 2
            osname = "solaris"
            release = "%d.%s" % (int(release[0]) - 3, release[2:])
            # We can't use "platform.architecture()[0]" because a
            # bootstrap problem. We use a dict to get an error
            # if some suspicious happens.
            bitness = {2147483647: "32bit", 9223372036854775807: "64bit"}
            machine += ".%s" % bitness[sys.maxsize]
        # fall through to standard osname-release-machine representation
    elif osname[:4] == "irix":  # could be "irix64"!
        return "%s-%s" % (osname, release)
    elif osname[:3] == "aix":
        return "%s-%s.%s" % (osname, version, release)
    elif osname[:6] == "cygwin":
        osname = "cygwin"
        import re

        rel_re = re.compile(r"[\d.]+")
        m = rel_re.match(release)
        if m:
            release = m.group()
    elif osname[:6] == "darwin":
        import _osx_support

        osname, release, machine = _osx_support.get_platform_osx(
            get_config_vars(), osname, release, machine
        )

    return "%s-%s-%s" % (osname, release, machine)


def get_python_version():
    return _PY_VERSION_SHORT


print("")
print("")
print('Platform: "%s"' % get_platform())
print("")
print('Python version: "%s"' % get_python_version())


"""
pybuilddir = 'build/lib.%s-%s' % (get_platform(), sys.version[:3])

# Try to distinguish various flavours of Unix
osname, host, release, version, machine = os.uname()

# Convert the OS name to lowercase, remove '/' characters
# (to accommodate BSD/OS), and translate spaces (for "Power Macintosh")
osname = osname.lower().replace('/', '')
machine = machine.replace(' ', '_')
machine = machine.replace('/', '-')

print(osname)
print(machine)
"""

frame = sys._getframe()
print(frame)

from pathlib import Path

cc = os.path.realpath(__file__)
print("目前檔案 :", cc)

cc = [str(Path(cc).parent)]
print("父資料夾 :", cc)

cc = __file__

print(cc)


import os

print(os.getcwd())
print(os.path.relpath("C:\\"))  # 列出目前工作目錄至C:\的相對路徑
print(os.path.relpath("C:\\___small\\Dropresize"))  # 列出目前工作目錄至特定path的相對路徑
print(os.path.relpath("C:\\", "*.py"))  # 列出目前檔案至D:\的相對路徑

import os

print(os.path.abspath("."))  # 列出目前工作目錄的絕對路徑
print(os.path.abspath(".."))  # 列出上一層工作目錄的絕對路徑
print(os.path.abspath("*.py"))  # 列出目前檔案的絕對路徑


import os

print(os.path.join("D:\\", "Python", "ch14", "ch14_9.py"))  # 4個參數
print(os.path.join("D:\\Python", "ch14", "ch14_9.py"))  # 3個參數
print(os.path.join("D:\\Python\\ch14", "ch14_9.py"))  # 2個參數


print("------------------------------------------------------------")  # 60個

import os
import os.path as path

fpath = os.getcwd() + "\\temp"
if path.exists(fpath + "\\ball0.jpg"):
    print("存在!")
if path.isdir(fpath + "\\test"):
    print("是目錄!")
if path.isfile(fpath + "\\ball0.jpg"):
    print("是檔案!")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import os

path = os.getcwd() + "\\temp"
os.chdir(path)
print(path)
print(os.listdir(path))


print("------------------------------------------------------------")  # 60個

import os

path = os.getcwd() + "\\temp"
print("目前工作路徑: ", os.getcwd())
print(path)
os.chdir(path)
print("chdir(): ", os.getcwd())
os.mkdir("newDir")
print("mkdir(): ", os.listdir(path))

print("------------------------------------------------------------")  # 60個

import os

path = os.getcwd() + "\\temp"
os.chdir(path)
os.rename("newDir", "newDir2")
print("rename(): ", os.listdir(path))

print("------------------------------------------------------------")  # 60個

import os

path = os.getcwd() + "\\temp"
os.chdir(path)
os.rmdir("newDir2")
fp = open("aa.txt", "w")
fp.close()
print("rmdir(): ", os.listdir(path))
os.remove("aa.txt")
print("remove(): ", os.listdir(path))

print("------------------------------------------------------------")  # 60個

import os.path as path

fname = path.realpath("ch9-2-2.py")
print(fname)
r = path.split(fname)
print("os.path.split() =", r)
r = path.splitext(fname)
print("os.path.splitext() =", r)

print("------------------------------------------------------------")  # 60個

import os.path as path

fname = path.realpath("ch9-2-2.py")
print(fname)
p = path.dirname(fname)
print("p = os.path.dirname() =", p)
f = path.basename(fname)
print("f = os.path.basename() =", f)


print("------------------------------------------------------------")  # 60個

import os.path as path

p = "C:\Python\ch09"
f = "ch9-2-2.py"
print(p, f)
r = path.join(p, f)
print("os.path.join(p,f) =", r)

print("------------------------------------------------------------")  # 60個

import os
import os.path as path

fpath = os.getcwd() + "\\temp"
if path.exists(fpath + "\\ball0.jpg"):
    print("存在!")
if path.isdir(fpath + "\\test"):
    print("是目錄!")
if path.isfile(fpath + "\\ball0.jpg"):
    print("是檔案!")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""
print("touch 一個檔案")
import pathlib
pathlib.Path("work_test1.py").touch()
"""

print("------------------------------------------------------------")  # 60個


import os


def getSize(path):
    size = 0  # Store the total size of all files

    if not os.path.isfile(path):
        lst = os.listdir(path)  # All files and subdirectories
        for subdirectory in lst:
            size += getSize(path + "\\" + subdirectory)
    else:  # Base case, it is a file
        size += os.path.getsize(path)  # Accumulate file size

    return size


# 找 檔案 或 資料夾 的大小
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
foldername = "C:/_git/vcs/_1.data/______test_files3"

path = foldername

# Display the size
try:
    print(getSize(path), "bytes")
except:
    print("Directory or file does not exist")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


"""
import pathlib

print('touch當前目錄下所有檔案')
files = glob.glob("*.*") 
for filename in files:
    print(filename)
    pathlib.Path(filename).touch()
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 建立資料夾
target_dir = "tmp_test_create_folder"
# 準備輸出資料夾 若不存在, 則建立
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    # os.makedirs(target_dir, exist_ok = True)
else:
    print("資料夾已存在")

print("------------------------------------------------------------")  # 60個


def recursedown(dirname):
    try:
        names = os.listdir(dirname)  # 轉出一層
        # print(names)
    except OSError as msg:
        err("%s: cannot list directory: %r\n" % (dirname, msg))
        return 1
    names.sort()
    subdirs = []
    for name in names:
        if name in (os.curdir, os.pardir):
            print("skip")
            continue
        fullname = os.path.join(dirname, name)
        if os.path.islink(fullname):
            print("是一個link")
            pass
        elif os.path.isdir(fullname):
            print("是一個資料夾")
            subdirs.append(fullname)
        else:
            # print("a")
            pass
    bad = 0
    for fullname in subdirs:
        if recursedown(fullname):
            bad = 1
    print(subdirs)
    return bad


foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test"

cc = recursedown(foldername)
print(cc)
'''
print("------------------------------------------------------------")  # 60個

print('test start')

TB = 1024 * 1024 * 1024 * 1024  # 定義TB的計算常量
GB = 1024 * 1024 * 1024  # 定義GB的計算常量
MB = 1024 * 1024  # 定義MB的計算常量
KB = 1024  # 定義KB的計算常量


def ByteConversionTBGBMBKB(size):
    if size < 0:
        return "不合法的數值"
    elif size / TB >= 1024:  # 如果目前Byte的值大於等於1024TB
        return "無法表示"
    elif size / TB >= 1:  # 如果目前Byte的值大於等於1TB
        return format(size / TB, ".2f") + " TB"  # 將其轉換成TB
    elif size / GB >= 1:  # 如果目前Byte的值大於等於1GB
        return format(size / GB, ".2f") + " GB"  # 將其轉換成GB
    elif size / MB >= 1:  # 如果目前Byte的值大於等於1MB
        return format(size / MB, ".2f") + " MB"  # 將其轉換成MB
    elif size / KB >= 1:  # 如果目前Byte的值大於等於1KB
        return format(size / KB, ".2f") + " KB"  # 將其轉換成KB
    else:
        return str(size) + " Byte"  # 顯示Byte值


"""
filesize = 123456
print("filesize = ", filesize, "\t檔案大小 : ", ByteConversionTBGBMBKB(filesize))
print("大小:\t", filesize, " 拜")
print("大小:\t", ByteConversionTBGBMBKB(filesize))
"""


def check_video_filename(filename):
    f = filename.lower()
    return (
        f.endswith(".mp4")
        or f.endswith(".avi")
        or f.endswith(".wmv")
        or f.endswith(".ogg")
        or f.endswith(".ogg")
        or ".ogg" in f
        or f.endswith(".ogg")
    )


print("轉出多層 os.walk 1 AP專用")

#foldername = "D:/內視鏡影片/_ims影片1"
#foldername = "F:/_________AP_kilo_F/__ap0117"
foldername = "D:/內視鏡影片/_ims影片1"
#foldername = f"D:\vcs\astro\_DATA2\_________整理_mp3\_音樂"
foldername = "D:/vcs/astro/_DATA2/_________整理_mp3/_音樂"

total_folders = 0
total_files = 0
total_size = 0
all_files = list()

for item in os.walk(foldername):  # 多層
    total_folders += 1
    for fname in item[2]:
        # ffname = item[0] + "/" + fname  # 取出檔名完整路徑 same
        ffname = os.path.join(item[0], fname)  # 取出檔名完整路徑
        # print(ffname)
        if check_video_filename(ffname) == True:
            total_files += 1
            filesize = os.stat(ffname).st_size  # 取出檔案大小
            total_size += filesize
            #all_files.append(ffname + " " + ByteConversionTBGBMBKB(filesize))
            all_files.append(ffname)
            abspath = os.path.abspath(ffname)
            directory, short_filename = os.path.split(abspath)
            # print("全檔名", ffname)
            # print("全檔名", abspath)
            # print("資料夾", directory)
            # print("短檔名", short_filename)
    print("------------------------------")  # 30個

if total_folders > 0:
    total_folders -= 1

print("位置 :", foldername)
print("容量 :", total_size, "位元組")
print("包含 :", total_files, "個檔案,", total_folders, "個資料夾")

"""
print("顯示結果:")
for _ in all_files:
    print(_, end = " ")
"""

string_video_filenames = ""
for _ in all_files:
    string_video_filenames += _+" "

#print("總容量 : ", ByteConversionTBGBMBKB(total_size))


"""
#呼叫 potplayer 播放之
1. 容量 特大/特小 的 影片檔案
2. 格式 特大/特小 的 影片檔案
3. 檔名含有關鍵字 的 影片檔案
4. 將找到的資料存成文字檔
5. 一次播放找到符合條件的影片檔案
"""
"""
# 目前在python使用potplayer, 無法一次播放2個檔案......

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

#os.system("notepad " + filename_r)

all_filename = "D:\vcs\04_能臣之路.rmvb " + "D:\vcs\07_深谋远虑.rmvb " + "D:\vcs\09_一决雌雄.rmvb"

video_player_path_kilo = "xxxx"

video_player_path_sugar = "D:/___backup/PotPlayer/PotPlayerMini64.exe"

cmd = "D:/___backup/PotPlayer/PotPlayerMini64.exe spiderman1.mp4 spiderman2.mp4"
os.system(cmd)

cmd = video_player_path_sugar + " " + video_filename
print(cmd)
os.system(cmd)

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

os.system(video_player_path_sugar+ " " + video_filename)

#os.system(video_player_path_sugar+ " " + string_video_filenames)
#os.system(video_player_path_sugar)

"""
print("------------------------------------------------------------")  # 60個

def get_video_info(video):
    video_info = {}
    
    video_info['width'] = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_info['height'] = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_info['frames'] = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_info['fps'] = video.get(cv2.CAP_PROP_FPS)
    video_info['length'] = video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)
    print(type(video_info))
    return video_info

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'
vid = cv2.VideoCapture(video_filename)

video_info = get_video_info(vid)
print(video_info)


print("------------------------------------------------------------")  # 60個


filesize = 123456
print('filesize = ', filesize , '\t檔案大小 : ', ByteConversionTBGBMBKB(filesize))


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filesize = os.stat(filename).st_size

print('檔案大小:\t', filesize, ' 拜')
print('檔案大小:\t', ByteConversionTBGBMBKB(filesize))

print("------------------------------------------------------------")  # 60個

"""
分析

if file.endswith('.jpg') or file.endswith('.png'):

    for file in files:  # 取得所有 .png .jpg 檔，存入 allfiles 串列中
        ext = file.split('.')[-1]
        if ext == "png" or ext == "jpg":
            allfiles.append(foldername +'/'+file)

      for file in allfiles:  
         filename = file.split('.')[0] #主檔名         

   if basename == target_foldername:  # 輸出資料夾不再重複處理
      continue

"""

print("------------------------------------------------------------")  # 60個


def test_get_filename(foldername):

    #foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'

    print('------------------------------------------------------------')	#60個
    print('ls 測試 os.walk')
    print('------------------------------------------------------------')	#60個

    print('撈出資料夾下所有檔案, 多層1')
    print('搜尋路徑：', foldername)
    filenames = os.walk(foldername)
    print(type(filenames))  #很奇怪的結構
    #print(filenames)

    allfiles = []

    #foldername 檔案所在資料夾
    #subdir     檔案所在位置的其他資料夾
    #files      檔案名稱
    for foldername, subdir, files in filenames:
        if 'folder_xxxxx' in subdir:  #某些資料夾下的檔案不要處理
            print('某些資料夾下的檔案不要處理')
            subdir.remove('folder_xxxxx')
        for filename in files:  # 取得所有檔案，存入 allfiles 串列中
            #print('檔案所在資料夾 :', foldername)
            #print('檔案所在位置的其他資料夾 :', subdir)
            #print('檔案名稱', filename)
            #allfiles.append(foldername + '/' + filename)   #絕對路徑
            long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
            filesize = os.stat(long_filename).st_size
            
            allfiles.append(long_filename)   #絕對路徑
            
            

    print(len(allfiles))

    if len(allfiles) > 0:
        for filename in allfiles:
            #print(filename)
            if not os.path.exists(filename):
                print('檔案不存在')
            else:
                abspath = os.path.abspath(filename)
                directory, short_filename = os.path.split(abspath)
                print('全檔名', abspath)
                print('檔案大小', os.stat(abspath).st_size)
                print('資料夾', directory)
                print('短檔名', short_filename)
                #long_filename = os.path.join('新資料夾', short_filename)    # 取得檔案的絕對路徑
                #print('新全檔名', long_filename)
                print()

        #long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        #print(long_filename)


"""
foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'
test_get_filename(foldername)
"""

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
print(filename)
filename = os.path.normcase(filename)
print(filename)

print('------------------------------------------------------------')	#60個

filename = 'C:/aaa/bbb/ccc/ddd/eee.jpg'

name = filename.split('/')
print(type(name))
print(len(name))
print(name)


print('------------------------------------------------------------')	#60個


from os.path import abspath

def _basename(path):
    # A basename() variant which first strips the trailing slash, if present.
    # Thus we always get the last component of the path, even for directories.
    sep = os.path.sep + (os.path.altsep or '')
    return os.path.basename(path.rstrip(sep))

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
base_name = _basename(filename)
print(base_name)

src = abspath(base_name)
print(src)

zip_filename = base_name + ".zip"
print(zip_filename)

print('------------------------------------------------------------')	#60個

foldername = 'C:/_git/vcs/_1.data/______test_files2'

normdir = os.path.normcase(foldername)
print(normdir)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('尋找python程式碼的所在地')

module_name = 'pytube'
code_place = os.path.dirname(__import__(module_name).__file__)
print(code_place)


print('取得相對路徑')
foldername = 'C:/_git/vcs/_1.data/______test_files1/'
fn = os.path.relpath(foldername, code_place)

print(fn)

print('------------------------------------------------------------')	#60個


foldername = 'C:/_git/vcs/_1.data/______test_files5'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

name = os.path.basename(filename)

print(name)


print('------------------------------------------------------------')	#60個


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

if filename.endswith(".jpg"):
    # It is a module -- insert its dir into sys.path and try to
    # import it. If it is part of a package, that possibly
    # won't work because of package imports.
    dirname, filename = os.path.split(filename)
    print(filename[:-3])



print('------------------------------------------------------------')	#60個

print('將主檔名中不合法的字元去除')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

m_filename = ""
for c in filename:
   #print(c)
   if c == " " or c == "." or c == "," or c == "、" or c == "，" or c == "(" or c == ")":
      m_filename += ""  # 去除不合法字元
   else:
      m_filename += c

print(filename)
print(m_filename)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

