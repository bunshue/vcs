"""

print('ls 測試 os.walk')
print('ls 測試 os.listdir')
print('ls 測試 glob.glob')

#os.walk 遞迴搜尋檔案
#os.walk 是一個以遞迴方式列出特定路徑下，所有子目錄與檔案的函數

#os.listdir 取得檔案列表
#os.listdir 可以取得指定目錄中所有的檔案與子目錄名稱

各種方法的 ls dir

撈出一層

撈出全部

"""

import os
import sys
import glob
import stat
import datetime

foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test"
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test/_good1/_good4/_good5"

print("------------------------------------------------------------")  # 60個

print(
    "ls 測試 os.walk ST------------------------------------------------------------"
)  # 60個

print("撈出資料夾下所有檔案, 多層1")
print("搜尋路徑：", foldername)
filenames = os.walk(foldername)
print(type(filenames))  # 很奇怪的結構
# print(filenames)

allfiles = []

# foldername 檔案所在資料夾
# subdir     檔案所在位置的其他資料夾
# files      檔案名稱
for foldername, subdir, files in filenames:
    if "folder_xxxxx" in subdir:  # 某些資料夾下的檔案不要處理
        print("某些資料夾下的檔案不要處理")
        subdir.remove("folder_xxxxx")
    for filename in files:  # 取得所有檔案，存入 allfiles 串列中
        # print('檔案所在資料夾 :', foldername)
        # print('檔案所在位置的其他資料夾 :', subdir)
        # print('檔案名稱', filename)
        # allfiles.append(foldername + '/' + filename)   #絕對路徑
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        filesize = os.stat(long_filename).st_size

        allfiles.append(long_filename)  # 絕對路徑

print(len(allfiles))

if len(allfiles) > 0:
    for filename in allfiles:
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

print("------------------------------------------------------------")  # 60個

# 分析
if len(allfiles) > 0:
    for filename in allfiles:
        # print(filename)
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print("取得圖檔 :", filename)

    for filename in allfiles:
        ext = filename.split(".")[-1]
        print("副檔名 :", ext)
        if ext == "png" or ext == "jpg":
            print("取得全檔名 :", filename)


print(
    "ls 測試 os.walk SP------------------------------------------------------------"
)  # 60個


print(
    "ls 測試 os.listdir ST------------------------------------------------------------"
)  # 60個

print("指定目錄下之ls (單層)")

# filenames = os.listdir()   #無參數, 當前目錄

folder = "."  # 當前目錄
folder = "/"  # 根目錄
folder = foldername  # 指定目錄

filenames = os.listdir(folder)  # 單層
print(type(filenames))
print(filenames)

for filename in filenames:
    print(filename)
    long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
    print(long_filename)
    sub, ext = os.path.splitext(filename)
    print("前檔名", sub, "後檔名", ext)

print("排序印出")
for filename in sorted(filenames):
    print(filename)

print("印出 filenames 內特定附檔名之檔案")
zz = [name for name in filenames if name.endswith((".jpg", ".txt"))]
print("*.jpg *.txt files:")
print(zz)

print("------------------------------------------------------------")  # 60個

print("指定目錄下之ls (單層)")
filenames = os.listdir(foldername)  # 單層
print(filenames)
for filename in filenames:
    print(filename)

filelist = []
for filename in filenames:
    long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
    print(long_filename)

filelist.sort(key=os.path.normcase)

print("------------------------------------------------------------")  # 60個

print("指定目錄下之ls (單層)")

filenames = os.listdir(foldername)
filenames.sort()

for filename in filenames:
    long_filename = os.path.join(foldername, filename)
    print(long_filename)

print("------------------------------------------------------------")  # 60個

fix_names = []
for filename in sorted(os.listdir(foldername)):
    if filename.startswith("fix_") and filename.endswith(".py"):
        if remove_prefix:
            filename = filename[4:]
        fix_names.append(filename[:-3])

print(fix_names)

print("------------------------------------------------------------")  # 60個

print("撈出資料夾下所有檔案, 多層3")


def list_files1(foldername, callback):
    for filename in os.listdir(foldername):  # 單層
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        mode = os.lstat(long_filename).st_mode
        if stat.S_ISDIR(mode):
            # It's a directory, recurse into it
            list_files1(long_filename, callback)
        elif stat.S_ISREG(mode):
            # It's a file, call the callback function
            callback(long_filename)
        else:
            # Unknown file type, print a message
            print("Skipping %s" % long_filename)


def visitfile(file):
    print("visiting", file)


list_files1(foldername, visitfile)

print("------------------------------------------------------------")  # 60個


def _listFiles(files, foldername):
    for filename in os.listdir(foldername):
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        if os.path.isdir(long_filename):
            _listFiles(files, long_filename)
        else:
            files.append(long_filename)


def read_files(foldername, showProgress=False, readPixelData=False, force=False):
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


print("撈出資料夾下所有檔案, 多層4")

# find_files(foldername)

all_series = read_files(foldername, True, False, False)

print("------------------------------------------------------------")  # 60個

print("撈出資料夾下所有檔案, 單層")


def list_files3(foldername):
    for filename in os.listdir(foldername):
        print(filename)
        if filename not in (os.curdir, os.pardir):
            print(filename)
            long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
            print(long_filename)
        else:
            print("x")


list_files3(foldername)

print("------------------------------------------------------------")  # 60個

print("撈出資料夾下所有檔案, 多層5")


def list_files4(foldername):
    filenames = os.listdir(foldername)
    for filename in filenames:
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        if os.path.isdir(long_filename):  # 資料夾 再找下去
            print("D", long_filename)
            list_files4(long_filename)
        else:  # 檔案
            print("f", long_filename, os.stat(long_filename).st_size)


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


list_files5(foldername)

print("------------------------------------------------------------")  # 60個


def getFolderSize(foldername):
    size = 0  # Store the total size of all files

    if not os.path.isfile(foldername):
        lst = os.listdir(foldername)  # All files and subdirectories
        for subdirectory in lst:
            size += getFolderSize(foldername + "\\" + subdirectory)
    else:  # Base case, it is a file
        size += os.path.getsize(foldername)  # Accumulate file size
    return size


folder_size = getFolderSize(foldername)

print("資料夾大小 : ", folder_size, "拜")

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
        names = os.listdir(dir)
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
        names = os.listdir(dir)
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

print(
    "ls 測試 os.listdir SP------------------------------------------------------------"
)  # 60個

print(
    "ls 測試 glob.glob ST------------------------------------------------------------"
)  # 60個

print("撈出資料夾下所有檔案, 單層")
print("資料夾: " + foldername)
print("資料夾: {}".format(foldername))

filenames = glob.glob(foldername + "/*.jpg") + glob.glob(foldername + "/*.png")
print(filenames)

for target_image in filenames:
    pathname, filename = os.path.split(target_image)
    print(filename)

    # im = Image.open(target_image)
    # w, h = im.size

print("------------------------------------------------------------")  # 60個

print("撈出資料夾下所有檔案, 單層")

filenames = glob.glob(foldername)

for filename in filenames:
    print(filename)

print("------------------------------------------------------------")  # 60個

print("撈出資料夾下所有檔案, 單層")
os.chdir(foldername)

filenames = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt")

for filename in filenames:
    print(filenames)

print("------------------------------------------------------------")  # 60個

print("目前目錄下撈出一層 指名 *.py")
filenames = glob.glob("*.py")
for filename in filenames:
    print("檔案 :", filename)

print("------------------------------------------------------------")  # 60個

# 尋找檔案
print("尋找目前目錄下之 *.py *.txt")
filenames = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt")
for filename in filenames:
    print(filename)

count = 1
filenames = glob.glob("*.jpg") + glob.glob("*.png")
for filename in filenames:
    print(filename)
    ext = filename.split(".")[-1]
    newfilename = "{}.{}".format(str(count), ext)
    print(newfilename)
    # os.rename(filename, newfilename)
    count += 1
print("完成...")

filenames = glob.glob("*.jpg") + glob.glob("*.png")
print(filenames)

print("------------------------------------------------------------")  # 60個

print("kkkkkkkkkkkkkkkkkkkkk")
print("撈出一層資料 .jpg檔  FAIL")
# filenames = glob.glob('data\*.jpg')
filenames = glob.glob("C:\_git\vcs\_1.data\______test_files1\__pic\_angry_bird\*.jpg")
print(filenames)

# FAIL

for filename in filenames:
    print(filename)
    if os.path.isfile(filename):
        print("是一個檔案")
    else:
        print("不是一個檔案")

    time = os.path.getmtime(filename)
    print(time)

    if not os.path.exists(filename):
        print("檔案不存在")
    else:
        abspath = os.path.abspath(filename)
        directory, short_filename = os.path.split(abspath)
        print("全檔名", abspath)
        print("資料夾", directory)
        print("短檔名", short_filename)
        long_filename = os.path.join("新資料夾", short_filename)  # 取得檔案的絕對路徑
        print("新全檔名", long_filename)
        print()

print("------------------------------------------------------------")  # 60個

print("指名pattern的搜尋")

pattern = "*"

filenames = glob.glob1(foldername, pattern)
print(filenames)

for filename in glob.glob1(foldername, "*.dll"):
    print(filename)

for filename in glob.glob1(foldername, "*.pyd"):
    print(filename)

print("------------------------------------------------------------")  # 60個

print("單層資料夾內所有檔案容量")

pngfiles = glob.glob(foldername + "*.png")
jpgfiles = glob.glob(foldername + "*.jpg")
giffiles = glob.glob(foldername + "*.gif")
bmpfiles = glob.glob(foldername + "*.bmp")
filenames = pngfiles + jpgfiles + giffiles + bmpfiles

allfilesize = 0
for filename in filenames:
    allfilesize += os.path.getsize(filename)
    print("檔案 : " + filename + ", 大小 : " + str(os.path.getsize(filename)) + " 拜")

print("總容量 : " + str(allfilesize) + " 拜")

print(
    "ls 測試 glob.glob SP------------------------------------------------------------"
)  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("---- 新進未整理 --------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("-------")
print(os.curdir)
print("-------")
print(os.pardir)
print("-------")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("新進------------------------------------------------------------")  # 60個


"""
     
檔案操作

os.readlink(long_filename))
os.path.islink(long_filename)
os.path.isdir(file)
os.path.isdir(foldername):
os.path.exists(name):

mkdir多一層保護
        try:
            os.mkdir(odir)
            print("Created output directory", odir)
        except OSError as msg:
            usage('%s: mkdir failed (%s)' % (odir, str(msg)))

if filename.lower().endswith(".py"):
if filename.endswith('.jpg'):

if os.path.normcase(filename[-3:]) == ".py":

if filename.lower().endswith(".py"):

if filename.endswith('.c'):

----------------------------------------------------------------
    def glob(self, pattern, exclude = None):
        #Add a list of files to the current component as specified in the
        #glob pattern. Individual files can be excluded in the exclude list.
        files = glob.glob1(self.absolute, pattern)
        for f in files:
            if exclude and f in exclude: continue
            self.add_file(f)
        return files

            filenames = glob.glob(name)
            filename_list = []
            for filename in filenames:
                filename_list.extend(getFilesForName(filename))
            return filename_list
"""

print("------------------------------------------------------------")  # 60個

import stat

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

st = os.lstat(filename)

anytime = st[stat.ST_MTIME]
size = st[stat.ST_SIZE]
print("檔案大小 :", size, "拜")


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

canonic = os.path.abspath(filename)
print("長檔名 :", canonic, "\t大寫磁碟機名")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
canonic = os.path.normcase(filename)
print("長檔名 :", canonic, "\t小寫磁碟機名")

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
head, ext = os.path.splitext(filename)
print("前檔名 :", head)
print("副檔名 :", ext)
head, base = os.path.split(filename)
print("長資料夾名 :", head)
print("短檔名 :", base)

print("------------------------------------------------------------")  # 60個

# 撈出一層 至 list

cc = os.listdir()  # 沒有參數就是當前目錄
print(type(cc))
# print(cc)

print("當前目錄下共有 :", len(cc), "個項目(資料夾+檔案)")

print("------------------------------------------------------------")  # 60個

print("轉出多層")
# foldername = 'C:/_git/vcs/_1.data/______test_files5'
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test"

total_folders = 0
total_files = 0
total_size = 0
all_files = list()
for item in os.walk(foldername):
    total_folders += 1
    # print(item)
    print("資料夾 :", item[0])
    print("子資料夾:", item[1])
    print("檔案:", item[2])
    total_files += len(item[2])
    for _ in item[2]:
        file = item[0] + "/" + _
        filesize = os.stat(file).st_size
        # print(filesize)
        total_size += filesize
        all_files.append(file)
    print("------------------------------------------------------------")  # 60個

if total_folders > 0:
    total_folders -= 1

print("位置 :", foldername)
print("容量 :", total_size, "位元組")
print("包含 :", total_files, "個檔案,", total_folders, "個資料夾")

print()
for _ in all_files:
    print(_)

print("------------------------------------------------------------")  # 60個

foldername = "C:/_git/vcs/_1.data/______test_files5"
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test"

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


def dirTree(path, level=0):
    if level > 1:
        return
    for item in os.listdir(path):
        path2 = os.path.join(path, item)
        if os.path.isdir(path2):
            for i in range(level):
                print("   ", end="")
            print("+--" + item)
            try:
                dirTree(path2, level + 1)
            except:
                pass


foldername = "C:/_git/vcs/_1.data/______test_files5"
foldername = "C:/_git/vcs/_1.data/______test_files3/DrAP_test"

dirTree(foldername)

print("------------------------------------------------------------")  # 60個

foldername = "C:/_git/vcs/_1.data/______test_files5"
# foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'

for entry in os.scandir(foldername):
    info = entry.stat()
    da = datetime.datetime.utcfromtimestamp(info.st_mtime)
    dstr = da.strftime("%d/%m/%Y")
    if entry.is_file():
        size = int(os.path.getsize(entry.name) / 1024)
        ext = os.path.splitext(entry.name)
        print(
            entry.name,
            "\t" + str(size) + "KB\t",
            str(ext[-1].replace(".", "")) + "\t",
            dstr,
        )
    elif entry.is_dir():
        print(entry.name, "\t\t\t<DIR>\t", dstr)

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

from PIL import Image, ImageFont, ImageDraw

imgs = glob.glob("./demo/*.jpg")  # 讀取 demo 資料夾裡所有的圖片

for i in imgs:
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    img = Image.open(i)  # 開啟圖片
    w, h = img.size
    font = ImageFont.truetype("Teko-Regular.ttf", 100)
    text = Image.new(mode="RGBA", size=(400, 100), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(text)
    draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)
    text = text.rotate(30, expand=1)
    img2 = Image.open(i)
    img2.paste(text, (50, 0), text)
    img2.convert("RGBA")
    img2.putalpha(150)
    img.paste(img2, (0, 0), img2)
    img.save(f"./test/{name}")

print("------------------------------------------------------------")  # 60個

jpg = glob.glob("./demo/*.[jJ][pP][gG]")  # 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
print(jpg)
"""
['./demo/pic-001.jpg', './demo/pic-002.jpg', './demo/pic-003.jpg',
'./demo/pic-004.jpg', './demo/pic-005.jpg', './demo/pic-006.jpg',
'./demo/pic-007.jpg', './demo/pic-008.jpg', './demo/pic-009.jpg',
'./demo/pic-010.jpg']
"""

images = glob.glob("./demo/*")
print(images)

print("------------------------------------------------------------")  # 60個

curdir = os.getcwd()
print("當前目錄", curdir)


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""
image_foldername = 'tmp_images'
html_filename = 'tmp_countryfood2222.html'
if os.path.exists(html_filename):  
    os.remove(html_filename)     # 若有 tmp_countryfood.html 網頁即刪除
if os.path.exists(image_foldername): 
    shutil.rmtree(image_foldername)    # 若有images目錄即刪除
else:
    os.mkdir(image_foldername)        # 若無images目錄即刪除
"""

print("------------------------------------------------------------")  # 60個

print("顯示資料夾內的特定格式的檔案")


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


def find_similar_images(foldername):
    image_filenames = []
    image_filenames += [
        os.path.join(foldername, path)
        for path in os.listdir(foldername)
        if is_image(path)
    ]
    for img in sorted(image_filenames):
        print(img)


foldername = "C:/_git/vcs/_1.data/______test_files2"
find_similar_images(foldername)

print("------------------------------------------------------------")  # 60個

""" os 模組
directory = os.getcwd()

os.mkdir(directory+"/example")  #建立資料夾
os.mkdir(directory+"/doc")  #建立資料夾
directory_listdir=os.listdir( directory )
print("資料夾裡的文件與資料夾:{}".format(directory_listdir))

os.rename(directory+"/example",directory+"/sample") #更名
directory_listdir=os.listdir( directory )
print("資料夾裡的文件與資料夾:{}".format(directory_listdir))

os.rmdir(directory+"/doc")
directory_listdir=os.listdir( directory )
print("資料夾裡的文件與資料夾:{}".format(directory_listdir))
"""

print("------------------------------------------------------------")  # 60個


items = os.listdir()
print(os.path.exists("myprime.py"))
for item in items:
    print(os.path.abspath(item))

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

fullpath = os.path.abspath(filename)
print(fullpath)

print("os.path.basename:", os.path.basename(fullpath))
print("os.path.dirname:", os.path.dirname(fullpath))
print("os.path.getatime:", os.path.getatime(fullpath))
print("os.path.getmtime:", os.path.getmtime(fullpath))
print("os.path.getctime:", os.path.getctime(fullpath))
print("os.path.getsize:", os.path.getsize(fullpath))
print("os.path.isabs:", os.path.isabs(fullpath))
print("os.path.isfile:", os.path.isfile(fullpath))
print("os.path.isdir:", os.path.isdir(fullpath))
print("os.path.split:", os.path.split(fullpath))
print("os.path.splitdrive:", os.path.splitdrive(fullpath))
print("os.path.splitext:", os.path.splitext(fullpath))


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

for envname in "TMPDIR", "TEMP", "TMP":
    dirname = os.getenv(envname)
    print("cccccc", dirname)
    # print(dirname)


print("------------------------------------------------------------")  # 60個

import os.path as path

fname = path.realpath("ch11-2-2.py")
print(fname)
r = path.split(fname)
print("os.path.split() =", r)
r = path.splitext(fname)
print("os.path.splitext() =", r)

print("------------------------------------------------------------")  # 60個

import os.path as path

fname = path.realpath("ch11-2-2.py")
print(fname)
p = path.dirname(fname)
print("p = os.path.dirname() =", p)
f = path.basename(fname)
print("f = os.path.basename() =", f)

print("------------------------------------------------------------")  # 60個

import os.path as path

p = "D:\PythonChatGPT\ch11"
f = "ch11-2-2.py"
print(p, f)
r = path.join(p, f)
print("os.path.join(p,f) =", r)


print("------------------------------------------------------------")  # 60個

"""
print('檔案或目錄操作')
os.mkdir("目錄路徑")
os.rmdir("目錄路徑")
os.revmoe("檔案路徑")


shutil.copytree
shutil.rmtree
shutil.copyfile
shutil.move


"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
