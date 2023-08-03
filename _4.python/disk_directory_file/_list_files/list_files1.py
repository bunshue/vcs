'''
print('ls 測試 os.walk')
print('ls 測試 os.listdir')
print('ls 測試 glob.glob')

#os.walk 遞迴搜尋檔案
#os.walk 是一個以遞迴方式列出特定路徑下，所有子目錄與檔案的函數

#os.listdir 取得檔案列表
#os.listdir 可以取得指定目錄中所有的檔案與子目錄名稱，以下是一個簡單的範例：


'''
import os
import glob

import sys
import shutil

import stat
import time
import hashlib

import ast
import tokenize
import io

foldername = 'C:/_git/vcs/_1.data/______test_files4'

print('----------------------------------------------------------------------')	#70個
print('ls 測試 os.walk')
print('搜尋路徑：', foldername)
filenames = os.walk(foldername)
print(type(filenames))  #很奇怪的結構
print(filenames)
for root, dirs, filenames in filenames:
    print('路徑：', root)
    print('路徑下之目錄：', dirs)   
    print('路徑下之檔案：', filenames)
    print()

print('------------------------------')  #30個

print('撈出資料夾下所有檔案, 多層')
foldername = 'C:/_git/vcs/_1.data/______test_files5/'

print('搜尋路徑：', foldername)
for root, dirs, filenames in os.walk(foldername):
    print('路徑：', root)
    print('路徑下之目錄：', dirs)
    print('路徑下之檔案：', filenames)
    print()

print('------------------------------')  #30個
  
# 遞迴列出所有檔案的絕對路徑
for root, dirs, filenames in os.walk(foldername):
    for filename in filenames:
        print(filename)
        long_filename = os.path.join(root, filename)  # 取得檔案的絕對路徑
        print(long_filename)

print('----------------------------------------------------------------------')	#70個
print('ls 測試 os.listdir')

print('當前目錄下之ls (單層)')
filenames = os.listdir()
print(type(filenames))
print(filenames)

print('------------------------------')  #30個

print('當前目錄下之ls (單層)')
filenames = os.listdir('.')
print(type(filenames))
print(filenames)

print('------------------------------')  #30個

print('根目錄下之ls (單層)')
filenames = os.listdir('/')
print(type(filenames))
print(filenames)

print('------------------------------')  #30個
zz = [name for name in filenames if name.endswith(('.jpg', '.h'))]
print('*.jpg *.h files:')
print(zz)


print('------------------------------')  #30個


filename = os.listdir(foldername)
for sub in filename:
    sub, ext = os.path.splitext(sub)
    fullname = 'aaaa' + "." + sub
    print(fullname)

print('------------------------------')  #30個



print('指定目錄下之ls (單層)')
filenames = os.listdir(foldername)    #單層
print(type(filenames))
print(filenames)
for filename in filenames:
    print(filename)
    long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
    print(long_filename)

print('排序印出')
for filename in sorted(filenames):
    print(filename)

print('------------------------------')  #30個

print('指定目錄下之ls (單層)')
filenames = os.listdir(foldername)    #單層
print(filenames)
for filename in filenames:
    print(filename)

filelist = []
for filename in filenames:
    long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
    print(long_filename)

filelist.sort(key = os.path.normcase)

print('------------------------------')  #30個

print('撈出資料夾下所有檔案, 多層')
def list_files1(foldername, callback):
    for filename in os.listdir(foldername):    #單層
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
            print('Skipping %s' % long_filename)

def visitfile(file):
    print('visiting', file)

list_files1(foldername, visitfile)

print('------------------------------')  #30個

def _listFiles(files, foldername):

    for filename in os.listdir(foldername):
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        if os.path.isdir(long_filename):
            _listFiles(files, long_filename)
        else:
            files.append(long_filename)

def read_files(foldername, showProgress = False, readPixelData=False, force=False):
    print(foldername)

    filelist = []

    # Make dir nice
    basedir = os.path.abspath(foldername)
    print('資料夾 : ', basedir)
    # Check whether it exists
    if not os.path.isdir(basedir):
        raise ValueError('The given path is not a valid directory.')
    # Find files recursively
    _listFiles(filelist, basedir)
    print(filelist)

print('撈出資料夾下所有檔案, 多層')

'''
find_files(foldername)
'''
all_series = read_files(foldername, True, False, False)

print('------------------------------')  #30個

print('撈出資料夾下所有檔案, 單層')
def list_files3(foldername):
    for filename in os.listdir(foldername):
        print(filename)
        if filename not in (os.curdir, os.pardir):
            print(filename)
            long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
            print(long_filename)
        else:
            print('x')

list_files3(foldername)

print('------------------------------')  #30個

print('撈出資料夾下所有檔案, 多層')

def list_files4(foldername):
    filenames = os.listdir(foldername)
    for filename in filenames:
        long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
        if os.path.isdir(long_filename): #資料夾 再找下去
            print('D', long_filename)
            list_files4(long_filename)
        else:   #檔案
            print('f', long_filename, os.stat(long_filename).st_size)

list_files4(foldername)
print('------------------------------')  #30個

def list_files5(foldername):
    try:
        names = [n for n in os.listdir(foldername) if n.endswith('.py')]
    except OSError:
        print("Directory not readable: %s" % foldername, file=sys.stderr)
    else:
        for n in names:
            long_filename = os.path.join(foldername, n)  # 取得檔案的絕對路徑
            if os.path.isfile(long_filename):
                output = io.StringIO()
                print('Testing %s' % long_filename)
                try:
                    roundtrip(long_filename, output)
                except Exception as e:
                    print('  Failed to compile, exception is %s' % repr(e))
            elif os.path.isdir(long_filename):
                testdir(long_filename)

foldername = 'C:/_git/vcs/_1.data/______test_files5'
list_files5(foldername)

print('------------------------------')  #30個

def getFolderSize(foldername):
    size = 0 # Store the total size of all files

    if not os.path.isfile(foldername):
        lst = os.listdir(foldername) # All files and subdirectories
        for subdirectory in lst:
            size += getFolderSize(foldername + "\\" + subdirectory) 
    else: # Base case, it is a file
        size += os.path.getsize(foldername) # Accumulate file size 
    return size

foldername = 'C:/_git/vcs/_1.data/______test_files5'
folder_size = getFolderSize(foldername)

print('資料夾大小 : ', folder_size, '拜')

print('------------------------------')  #30個


print('----------------------------------------------------------------------')	#70個
print('ls 測試 glob.glob')

print('資料夾: ' + foldername)

print('Processing: {}'.format(foldername))

#撈出資料夾下所有檔案

#單層
filenames = glob.glob(foldername + '/*.jpg') + glob.glob(foldername + '/*.png')
print(filenames)

for target_image in filenames:
    pathname, filename = os.path.split(target_image)
    print(filename)
    '''
    im = Image.open(target_image)
    w, h = im.size
    '''
print("完成")




foldername = 'C:/_git/vcs/_1.data/______test_files5/'
filenames = glob.glob(foldername)

for filename in filenames:
    print(filename)

print('------------------------------')  #30個

os.chdir(foldername)
curdir = os.getcwd()

print('當前目錄', curdir)

filenames = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt")

for filename in filenames:
    print(filenames)

print('------------------------------')  #30個


print('------------------------------')  #30個

#尋找檔案
print('尋找目前目錄下之 *.py *.txt')
filenames = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt") 
for filename in filenames:
    print(filename)

count = 1
filenames = glob.glob('*.jpg') + glob.glob('*.png')
for filename in filenames:
    print(filename)
    ext = filename.split('.')[-1]
    newfilename = "{}.{}".format(str(count), ext)
    print(newfilename)
    #os.rename(filename, newfilename)
    count += 1
print("完成...")

filenames = glob.glob('*.jpg') + glob.glob('*.png')

allmd5s = dict()
for filename in filenames:
    print(filename + " is processing...")
    img_md5 = hashlib.md5(open(filename,'rb').read()).digest()
    if img_md5 in allmd5s:
        print("---------------")
        print("以下為重覆的檔案：")
        #print(os.path.abspath(filename))
        #print(allmd5s[img_md5])
        os.system("open " + os.path.abspath(filename))
        os.system("open " + allmd5s[img_md5])
    else:
        allmd5s[img_md5] = os.path.abspath(filename) 

print('------------------------------')  #30個

print('kkkkkkkkkkkkkkkkkkkkk')
print('撈出一層資料 .jpg檔  FAIL')
#filenames = glob.glob('data\*.jpg')
filenames = glob.glob('C:\_git\vcs\_1.data\______test_files1\__pic\_angry_bird\*.jpg')
print(filenames)

# FAIL

for filename in filenames:
    print(filename)
    if os.path.isfile(filename):
        print('是一個檔案')
    else:
        print('不是一個檔案')
        
    time = os.path.getmtime(filename)
    print(time)

    if not os.path.exists(filename):
        print('檔案不存在')
    else:
        abspath = os.path.abspath(filename)
        directory, short_filename = os.path.split(abspath)
        print('全檔名', abspath)
        print('資料夾', directory)
        print('短檔名', short_filename)
        long_filename = os.path.join('新資料夾', short_filename)    # 取得檔案的絕對路徑
        print('新全檔名', long_filename)
        print()

print('------------------------------')  #30個

print('指名pattern的搜尋')
foldername = 'C:/_git/vcs/_1.data/______test_files5'

pattern = '*'

filenames = glob.glob1(foldername, pattern)
print(filenames)

for filename in glob.glob1(foldername, "*.dll"):
    print(filename)

for filename in glob.glob1(foldername, "*.pyd"):
    print(filename)

print('------------------------------')  #30個
    
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


print('------------------------------')  #30個






print('------------------------------')  #30個

def process(filename, listnames):
    print('process : ', filename)
    if os.path.isdir(filename):
        return processdir(filename, listnames)
    try:
        print(filename)
    except IOError as msg:
        sys.stderr.write("Can't open: %s\n" % msg)
        return 1

def processdir(dir, listnames):
    print('processdir : ', dir)
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
        if os.path.normcase(long_filename).endswith(".py") or os.path.isdir(long_filename):
            filenames.append(long_filename)
    filenames.sort(key = os.path.normcase)
    exit = None
    for filename in filenames:
        x = process(filename, listnames)
        exit = exit or x
    return exit

foldername = 'C:/_git/vcs/_1.data/______test_files5'
listnames = 1  # or 1
x = process(foldername, listnames)
print(x)




print('------------------------------')  #30個


print('新進未整理------------------------------')  #30個

print('------------------------------')  #30個


print('------------------------------')  #30個

print('------------------------------')  #30個
    
print('------------------------------')  #30個


'''
# 新進未整理





mkdir多一層保護
        try:
            os.mkdir(odir)
            print("Created output directory", odir)
        except OSError as msg:
            usage('%s: mkdir failed (%s)' % (odir, str(msg)))



        #if not (filename.endswith('.c') or filename.endswith('.h')):
        #    continue


            if os.path.islink(long_filename):    #尋找link
                print('link')
                print(filename, '->', os.readlink(long_filename))
            else:
                print('f')


'''



'''
    def glob(self, pattern, exclude = None):
        """Add a list of files to the current component as specified in the
        glob pattern. Individual files can be excluded in the exclude list."""
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

'''
