'''
print('ls 測試 os.walk')
print('ls 測試 os.listdir')
print('ls 測試 glob.glob')

'''
import os
import glob

import sys
import shutil

from stat import *

import stat
import time
import hashlib

foldername = 'C:/_git/vcs/_1.data/______test_files4'

print('----------------------------------------------------------------------')	#70個
print('ls 測試 os.walk')

filenames = os.walk(foldername)
print(type(filenames))  #很奇怪的結構
print(filenames)
for dirname, subdir, files in filenames:
    print('資料夾路徑：', dirname)
    print('\t資料夾串列：', subdir)   
    print('\t檔案串列：', files)
    print()

print('------------------------------')  #30個

print('撈出資料夾下所有檔案, 多層')
for root, dirs, files in os.walk(foldername):
    for filename in files:
        #if not (filename.endswith('.c') or filename.endswith('.h')):
        #    continue
        print(filename)
        path = os.path.join(root, filename)
        print(path)

print('------------------------------')  #30個


print('----------------------------------------------------------------------')	#70個
print('ls 測試 os.listdir')

print('當前目錄下之ls (單層)')
filenames = os.listdir()
print(type(filenames))
print(filenames)

print('根目錄下之ls (單層)')
filenames = os.listdir('/')
print(type(filenames))
print(filenames)

print('指定目錄下之ls (單層)')
filenames = os.listdir(foldername)    #單層
print(type(filenames))
print(filenames)

filenames = os.listdir(foldername)    #單層
print(filenames)
for filename in filenames:
    print(filename, end = '')
    if os.path.isdir(filename):
        print('資料夾', end = '')
    if os.path.islink(filename):
        print('連結', end = '')
    print()

filelist = []
for filename in filenames:
    fn = os.path.join(foldername, filename)
    print(fn, end = '\t')
    if os.path.isdir(fn):
        print('資料夾')
    else:
        print('檔案')

filelist.sort(key = os.path.normcase)

print('------------------------------')  #30個

print('撈出資料夾下所有檔案, 多層')
def walktree(foldername, callback):
    for filename in os.listdir(foldername):    #單層
        pathname = os.path.join(foldername, filename)
        mode = os.lstat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting', file)

walktree(foldername, visitfile)

print('------------------------------')  #30個

def _listFiles(files, path):
    """List all files in the directory, recursively. """

    for filename in os.listdir(path):
        filename = os.path.join(path, filename)
        if os.path.isdir(filename):
            _listFiles(files, filename)
        else:
            files.append(filename)

def read_files(path, showProgress = False, readPixelData=False, force=False):
    print(path)

    filelist = []

    # Make dir nice
    basedir = os.path.abspath(path)
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
def lll(dirname):
    for filename in os.listdir(dirname):
        print(filename)
        if filename not in (os.curdir, os.pardir):
            print(filename)
            full = os.path.join(dirname, filename)
            if os.path.islink(full):    #尋找link
                print('link')
                print(filename, '->', os.readlink(full))
            else:
                print('f')
        else:
            print('x')

lll(foldername)

print('------------------------------')  #30個

print('撈出資料夾下所有檔案, 多層')

def add_files_in_folder(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        fullname = os.path.join(dirname, filename)
        if os.path.isdir(fullname): #資料夾 再找下去
            print('D', fullname)
            add_files_in_folder(fullname)
        else:   #檔案
            print('f', fullname, os.stat(fullname).st_size)

add_files_in_folder(foldername)

print('------------------------------')  #30個

filenames = os.listdir('.')
print("列出所有檔案", filenames)

zz = [name for name in filenames if name.endswith(('.jpg', '.h'))]
print('*.jpg *.h files:')
print(zz)

print('------------------------------')  #30個

def testdir(foldername):
    try:
        names = [n for n in os.listdir(foldername) if n.endswith('.py')]
    except OSError:
        print("Directory not readable: %s" % foldername, file=sys.stderr)
    else:
        for n in names:
            fullname = os.path.join(foldername, n)
            if os.path.isfile(fullname):
                output = io.StringIO()
                print('Testing %s' % fullname)
                try:
                    roundtrip(fullname, output)
                except Exception as e:
                    print('  Failed to compile, exception is %s' % repr(e))
            elif os.path.isdir(fullname):
                testdir(fullname)

testdir(foldername)

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

print(getFolderSize(foldername), "bytes")

print('------------------------------')  #30個

files = os.listdir(foldername)
for sub in files:
    sub, ext = os.path.splitext(sub)
    fullname = 'aaaa' + "." + sub
    print(fullname)


print('------------------------------')  #30個




print('----------------------------------------------------------------------')	#70個
print('ls 測試 glob.glob')

'''
    def glob(self, pattern, exclude = None):
        """Add a list of files to the current component as specified in the
        glob pattern. Individual files can be excluded in the exclude list."""
        files = glob.glob1(self.absolute, pattern)
        for f in files:
            if exclude and f in exclude: continue
            self.add_file(f)
        return files

            files = glob.glob(name)
            filelist = []
            for file in files:
                filelist.extend(getFilesForName(file))
            return filelist

'''

print('資料夾: ' + foldername)

print('Processing: {}'.format(foldername))

#單層
allfiles = glob.glob(foldername + '/*.jpg') + glob.glob(foldername + '/*.png')

cnt = 0
for target_image in allfiles:
	pathname, filename = os.path.split(target_image)
	print(filename)
	cnt = cnt + 1
	'''
	im = Image.open(target_image)
	w, h = im.size
	'''

print('cnt = ' + str(cnt))
print("完成")

print('------------------------------')  #30個
	
#撈出資料夾下所有檔案
'''
print('Processing: {}'.format(foldername))

allfiles = glob.glob(foldername + '/*.jpg') + glob.glob(foldername + '/*.png')

print(allfiles)
'''


#尋找檔案
print('尋找目前目錄下之 *.py *.txt')
files = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt") 
for file in files:
    print(file)


allfiles = glob.glob('*.jpg') + glob.glob('*.png')
count = 1
for afile in allfiles:
	print(afile)
	ext = afile.split('.')[-1]
	newfilename = "{}.{}".format(str(count), ext)
	os.rename(afile, newfilename)
	count += 1
print("完成...")

allfiles = glob.glob('*.jpg') + glob.glob('*.png')

allmd5s = dict()
for imagefile in allfiles:
	print(imagefile + " is processing...")
	img_md5 = hashlib.md5(open(imagefile,'rb').read()).digest()
	if img_md5 in allmd5s:
		print("---------------")
		print("以下為重覆的檔案：")
		#print(os.path.abspath(imagefile))
		#print(allmd5s[img_md5])
		os.system("open " + os.path.abspath(imagefile))
		os.system("open " + allmd5s[img_md5])
	else:
		allmd5s[img_md5] = 	os.path.abspath(imagefile) 




print('------------------------------')  #30個

print('撈出一層資料 .jpg檔')
files = glob.glob('data\*.jpg')
for file in files:
    print(file)
    if os.path.isfile(file):
        print('是一個檔案')
    else:
        print('不是一個檔案')
    time = os.path.getmtime(file)
    print(time)

    if not os.path.exists(file):
        print('檔案不存在')
    else:
        abspath = os.path.abspath(file)
        directory, filename = os.path.split(abspath)
        print('全檔名', abspath)
        print('資料夾', directory)
        print('短檔名', filename)
        new_filename = os.path.join('新資料夾', filename)
        print('新全檔名', new_filename)
        print()




print('------------------------------')  #30個
    
print("單層資料夾內所有檔案容量")

pngfiles = glob.glob(foldername + "*.png")
jpgfiles = glob.glob(foldername + "*.jpg")
giffiles = glob.glob(foldername + "*.gif")
bmpfiles = glob.glob(foldername + "*.bmp")
allfiles = pngfiles + jpgfiles + giffiles + bmpfiles

allfilesize = 0
for f in allfiles:
    allfilesize += os.path.getsize(f)
    print("檔案 : " + f + ", 大小 : " + str(os.path.getsize(f)) + " 拜")

print("總容量 : " + str(allfilesize) + " 拜")


print('------------------------------')  #30個






print('------------------------------')  #30個






print('------------------------------')  #30個


print('新進未整理------------------------------')  #30個




import glob
import sys

foldername = 'C:/_git/vcs/_1.data/______test_files2/'
files = glob.glob(foldername)

for file in files:
    print('aaaa')
    output(file)


'''

foldername = 'C:/_git/vcs/_1.data/______test_files2'

for cursrc, dirs, files in os.walk(foldername):
    print('----------------')
    print(cursrc, dirs, files)
    print('----------------')
'''







'''
foldername = 'C:/_git/vcs/_1.data/______test_files2/'

for root, dirs, files in os.walk(foldername):
    for fn in files:
        #fn = join(root, fn)
        print(fn)
'''







