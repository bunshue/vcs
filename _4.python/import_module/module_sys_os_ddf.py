# python import module : sys, os
# python import module : DDF 磁碟檔案資料夾操作

import os,shutil
cur_path = os.path.dirname(__file__) # 取得目前路徑
print("現在路徑："+cur_path)

'''
#拷貝檔案
destfile = 'C:/_git/vcs/_1.data/______test_files2/' + "ccccc.py"
print("拷貝檔案 " + destfile)
shutil.copy("test10_new12_file2.py",destfile )  # 檔案複製

print("拷貝檔案 " + destfile)
destfile = 'C:/_git/vcs/_1.data/______test_files2/' + "ccccc2.py"
shutil.copyfile('test10_new12_file2.py', destfile)  # 檔案複製
'''

#目錄拷貝
import shutil
source_dir = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
dest_dir = 'C:/_git/vcs/_1.data/______test_files2/source_pic'
print('cp -r ' + source_dir + ' ' + dest_dir)
#shutil.copytree(source_dir, dest_dir)  # 目錄複製

'''
print("刪除目錄, 直接刪除, 不會放入資源回收筒")
import shutil
shutil.rmtree("C:\\dddddddddd\\aaa" )  # 刪除目錄
'''


import os
filenames = os.listdir('.')
print("列出所有檔案", filenames)

zz = [name for name in filenames if name.endswith(('.jpg', '.h'))]
print('*.jpg *.h files:')
print(zz)

#重新命名檔案
#os.rename("foo.txt", "foo2.txt")
#刪除檔案
#os.remove("foo2.txt");

print("mkdir")
#os.mkdir("test_python_dir")

print("chdir")
#os.chdir("test_python_dir")

filename_r = 'C:/_git/vcs/_1.data/______test_files1/article2.txt'
print("檔案名稱 : ", os.path.getmtime(filename_r))

import os.path
filesize = os.path.getsize(filename_r)
print("filesize : " , filesize)

print("檔案時間 : ", os.path.getmtime(filename_r))
import time
print("檔案時間 : ", time.ctime(os.path.getmtime(filename_r)))


print("檔案是否存在 : ", os.path.isfile(filename_r))



import os
filename = os.path.abspath("test10_new10.py")
if os.path.exists(filename): #檢查檔案是否存在
    print("完整路徑名稱：" + filename)
    print("檔案大小：" , os.path.getsize(filename))



    
import os, shutil, glob

print("單層資料夾內所有檔案容量")

source_dir = 'C:/_git/vcs/_1.data/______test_files1/__pic/_peony1/'

pngfiles = glob.glob(source_dir + "*.png")
jpgfiles = glob.glob(source_dir + "*.jpg")
giffiles = glob.glob(source_dir + "*.gif")
bmpfiles = glob.glob(source_dir + "*.bmp")
allfiles = pngfiles + jpgfiles + giffiles + bmpfiles

allfilesize = 0
for f in allfiles:
    allfilesize += os.path.getsize(f)
    print("檔案 : " + f + ", 大小 : " + str(os.path.getsize(f)) + " 拜")

print("總容量 : " + str(allfilesize) + " 拜")






'''
print("測試mkdir")
import os
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
'''

import os
filename = "myFile.txt"
if os.path.exists(filename):
    os.remove(filename)
else:
    print(filename + "檔案未建立!")   

import os
filename=os.path.abspath("ospath.py")
if os.path.exists(filename):   
    basename=os.path.basename(filename)
    print("最後的檔案或路徑名稱：" + basename)
    
    dirname=os.path.dirname(filename)
    print("目前檔案目錄路徑：" + dirname) 
    
    print("是否為目錄：",os.path.isdir(filename))
    
    fullpath,fname=os.path.split(filename)
    print("目錄路徑：" + fullpath)
    print("檔名：" + fname)
    
    Drive,fpath=os.path.splitdrive(filename)
    print("磁碟機：" + Drive)
    print("路徑名稱：" + fpath)   
    
    fullpath = os.path.join(fullpath + "\\" + fname)
    print("組合路徑= " + fullpath)







if os.path.exists(filename+'.png'):
    ans = input('此檔案已存在，要覆寫嗎？(y/n)')
    if ans != 'y' and ans != 'Y':
        exit(1)
   
    
'''
filename = '__temp/tmppic_new'

filename, ext = filename.split('.')
if os.path.exists(filename+'_wm.png'):
    ans = input('此檔案已存在，要覆寫嗎？(y/n)')
    if ans != 'y' and ans != 'Y':
        exit(1)
'''

print('拷貝檔案')

imageno = 1
for f in allfiles:
  print('全檔名 : ' + f)
  dirname, filename = f.split('\\')
  print('資料夾 : ' + dirname)
  print('簡檔名 : ' + filename)

  mainname, extname = filename.split('.')

  print('前檔名 : ' + mainname)
  print('副檔名 : ' + extname)

  targetfolder = 'C:/_git/vcs/_1.data/______test_files2'
  targetfile = targetfolder + '/' + str(imageno) + '.' + extname

  print('新檔名 : ' + targetfile)
  
  shutil.copyfile(f, targetfile)  #會直接覆蓋舊檔
  imageno += 1



'''
target_dir = source_dir + "output"

print("目標資料夾 : " + target_dir)

if os.path.exists(target_dir):
  print("目的資料夾已存在")
  exit(1)

split用法 TBD
os.mkdir(target_dir)
imageno = 0
for f in allfiles:
  dirname, filename = f.split('/')
  mainname, extname = filename.split('.')
  targetfile = target_dir + '/' + str(imageno) + '.' + extname
  shutil.copyfile(f, targetfile)
  imageno += 1
'''





'''
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

'''




print(os.curdir)



foldername = 'C:/_git/vcs/_1.data/______test_files2'

filenames = os.listdir(foldername)
print(filenames)
for filename in filenames:
    print(filename, end = '')
    if os.path.isdir(filename):
        print('資料夾', end = '')
    if os.path.islink(filename):
        print('連結', end = '')
    print()

'''
dirname = 'New Folder'
try:
  os.mkdir(dirname)
except OSError as dirname:
  print("can't make slave directory", dirname, ":", dirname)
'''

'''
dirname = 'New Foldercccc'
print('如果資料夾不存在  建立之')
## Create the win32com\gen_py directory.
#make_dir = os.path.join(lib_dir, "win32com", "gen_py")
if not os.path.isdir(dirname):
    print('建立資料夾 : ', dirname)
    os.mkdir(dirname)
else:
    print('資料夾已存在, 無法再建立')
'''    


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

foldername = 'C:/_git/vcs/_1.data/______test_files2'
testdir(foldername)




import os

testfiles = os.listdir('C:/_git/vcs/_1.data/______test_files1/__RW/_dicom')

#簡檔名
testfiles = [x for x in testfiles if x.endswith('dcm')]

#全檔名
testfiles = [os.path.join('C:/_git/vcs/_1.data/______test_files1/__RW/_dicom', x) for x in testfiles]

for dcmfile in testfiles:
    print(dcmfile)



import os

filename = 'C:/_git/vcs/_1.data/______test_files1/human1.jpg'

file, ext = os.path.splitext(filename)

print(file)
print(ext)









filename = 'C:/_git/vcs/_1.data/______test_files1/human1.jpg'
import os
from stat import ST_MTIME
from stat import ST_CTIME

st = os.stat(filename)

print(st)

print(st[ST_MTIME])
print(st[ST_CTIME])

base = os.path.basename(filename)
print(base)

fnfilter = os.path.basename
print(fnfilter)

#os.rename(filename, backup)

import os
this_dir = os.path.dirname(__file__)
print(__file__)
print(this_dir)

cwd = os.getcwd()
print(cwd)

aa = os.chdir(cwd)
print(aa)

dirname = 'C:/_git/vcs/_4.python'
cc = os.chdir(dirname)
print(cc)

import os
import sys

isympy_path = os.path.abspath(__file__)
isympy_dir = os.path.dirname(isympy_path)
sympy_top = os.path.split(isympy_dir)[0]
sympy_dir = os.path.join(sympy_top, 'sympy')

if os.path.isdir(sympy_dir):
    #sys.path.insert(0, sympy_top)
    print('is dir')

#print(__path__[0])

tmp = os.path.realpath(__file__)
print(tmp)

#print(os.listdir(cache.dirname))





