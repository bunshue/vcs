"""
檔名操作

"""


import os
import glob

import sys
import stat




print('------------------------------------------------------------')	#60個



# python import module : sys, os
# python import module : DDF 磁碟檔案資料夾操作

import os
import shutil
cur_path = os.path.dirname(__file__) # 取得目前路徑
print("現在路徑：" + cur_path)

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

import os.path

print('目前檔案:', __file__)

cur_path=os.path.dirname(__file__) # 取得目前目錄路徑
print('現在目錄路徑:', cur_path)

filename=os.path.abspath("ospath.py")
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

if os.path.exists(filename):   
    print('完整路徑名稱:', filename)
    print('檔案大小:', os.path.getsize(filename))

    basename=os.path.basename(filename)
    print('最後的檔案或路徑名稱:', basename)
    
    dirname=os.path.dirname(filename)
    print('目前檔案目錄路徑:', dirname) 
    
    print('是否為目錄:', os.path.isdir(filename))
    
    fullpath,fname=os.path.split(filename)
    print('目錄路徑:', fullpath)
    print('檔名:', fname)
    
    Drive,fpath=os.path.splitdrive(filename)
    print('磁碟機:', Drive)
    print('路徑名稱:', fpath)   
    
    fullpath = os.path.join(fullpath + "\\" + fname)
    print('組合路徑: ', fullpath)
else:
    print('檔案不存在')




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



import os

testfiles = os.listdir('C:/_git/vcs/_1.data/______test_files1/__RW/_dicom')

#簡檔名
testfiles = [x for x in testfiles if x.endswith('dcm')]

#全檔名
testfiles = [os.path.join('C:/_git/vcs/_1.data/______test_files1/__RW/_dicom', x) for x in testfiles]

for dcmfile in testfiles:
    print(dcmfile)



import os

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

file, ext = os.path.splitext(filename)

print(file)
print(ext)

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








print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

import re
import os
import sys
import time
import platform
import shutil


print('---- 基本設定 --------------------------------------------------------')	#60個

filename = __file__
print('本檔長檔名', __file__)
print('本檔長檔名 : ', filename)

foldername = 'C:/_git/vcs/_1.data/______test_files2/'

print('---- 判斷檔案或資料夾 is exists --------------------------------------------------------')	#60個

file_or_folder_name = filename  #檔案或資料夾皆可

if os.path.exists(file_or_folder_name):
    print('檔案或資料夾 : ', filename, '存在')
else:
    print('檔案或資料夾 : ', filename, '不 存在')

if not os.path.exists(file_or_folder_name):
    print('檔案或資料夾 : ', filename, '不 存在')
else:
    print('檔案或資料夾 : ', filename, '存在')

if os.path.isdir(file_or_folder_name):
    print(filename, '是 資料夾')

if not os.path.isdir(file_or_folder_name):
    print('資料夾不存在')

if os.path.isfile(file_or_folder_name):
    print(filename, '是 檔案')

if os.path.islink(file_or_folder_name):
    print(filename, '是 連結')

#--------------------- new

'''
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

    


'''


print('---- 長檔名 轉 短檔名 basename() --------------------------------------------------------')	#60個

print('長檔名 轉 短檔名 basename()')
short_filename = os.path.basename(filename)
print('短檔名 : ', short_filename)

print('副檔名', short_filename[-3:])

print('---- 取得檔案/資料夾的絕對位置 abspath() --------------------------------------------------------')	#60個

print('取得檔案/資料夾的絕對位置 abspath()')
long_filename = os.path.abspath(filename)
print('長檔名(絕對位置)', long_filename)

print('取得檔案/資料夾的絕對位置 abspath()')
long_foldername = os.path.abspath(foldername)
print('長資料夾名(絕對位置)', long_foldername)

print('取得檔案/資料夾的絕對位置 abspath()')
long_foldername = os.path.abspath("../..")
print('本檔長資料夾(絕對位置)', long_foldername)

'''
補兩個狀況

filename = 'xxx.py'
long_filename = os.path.abspath(filename)
print('長檔名(絕對位置)', long_filename)

filename = '../../xxxx/xxx.py'
long_filename = os.path.abspath(filename)
print('長檔名(絕對位置)', long_filename)


'''

print('---- 取得所在的資料夾 dirname() --------------------------------------------------------')	#60個

print('取得所在的資料夾 dirname()')
long_foldername = os.path.dirname(filename)
print('本檔長資料夾(絕對位置)', long_foldername)

print('---- 連結資料夾 join(A, B) --------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


excecdir = 'aaaaaa'
executable = os.path.join('ppppp', "Python")
print(executable)

print('join')
resdir = os.path.join('bbbb', "Resources")
print(resdir)

print('join')
libdir = os.path.join('aaaa', "Frameworks")
print(libdir)

mainprogram = os.path.join(resdir, "idlemain.py")
print(mainprogram)


fpath = 'aaaaaaaaaaa'
correctfile = os.path.join(os.getcwd(), fpath)

correctfile = os.path.normpath(correctfile)

ccc = os.path.join(os.getcwd(), 'ziptest2dir')
print(ccc)





#filename = os.path.join(dir, prog)

#os.chdir(os.path.join(ROOT, TK, "win"))


import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



DIRS = os.path.join(BASE_DIR, 'templates')
NAME = os.path.join(BASE_DIR, 'db.sqlite3')
AAAA = os.path.join(BASE_DIR, 'static')

print(DIRS)
print(NAME)
print(AAAA)


print('------------------------------------------------------------')	#60個


print('---- 混和應用 --------------------------------------------------------')	#60個

major = 3
minor = 8
dll_file = "python%s%s.dll" % (major, minor)

dll_path = os.path.join(foldername, 'new_dll', dll_file)
print('新建dll完整路徑 : ', dll_path)

print('------------------------------------------------------------')	#60個

current_version = "%s.%s.%s" % (major, minor, int(time.time()/3600/24))
full_current_version = current_version
print('新建版本完整路徑 : ', full_current_version)

print('------------------------------------------------------------')	#60個

PATH = "/".join(os.path.abspath(filename).split("/")[:-2])
print(PATH)

print('------------------------------------------------------------')	#60個

print('取得所在的資料夾 dirname()')
here = os.path.abspath(os.path.dirname(filename))
print(here)
par = os.path.pardir
print(par)

print('取得檔案的絕對位置 abspath()')
ROOT = os.path.abspath(os.path.join(here, par, par))
print(ROOT)



print('------------------------------------------------------------')	#60個

head, tail = os.path.split(filename)
print('頭', head)
print('尾', tail)
tempname = os.path.join(head, '@' + tail)
print(tempname)

print('------------------------------------------------------------')	#60個

print('依分隔號區切分 : ')
path_split = filename.split(os.sep)
print(path_split)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

retval = (filename[:-4])
print('長資料夾 + 前檔名', retval)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

filename = "python-%s%s.msi" % (full_current_version, 'ccccc')
print(filename)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




def get_header_version_info(srcdir):
    print()
    print(srcdir)
    print()
    
    patchlevel_h = os.path.join(srcdir, '..', 'Include', 'patchlevel.h')
    print(patchlevel_h)

def get_sys_version_info():
    major, minor, micro, level, serial = sys.version_info
    release = version = '%s.%s' % (major, minor)
    release += '.%s' % micro
    if level != 'final':
        release += '%s%s' % (level[0], serial)
    return version, release

def get_version_info():
    try:
        return get_header_version_info('.')
    except (IOError, OSError):
        version, release = get_sys_version_info()
        print >>sys.stderr, 'Can\'t get version info from Include/patchlevel.h, ' \
              'using version of this interpreter (%s).' % release
        return version, release

get_header_version_info('.')
print('aaa', get_sys_version_info())
print('bbb', get_version_info())



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

string = 'this is a lion'
print(string)

string = string.replace('lion', 'mouse')
print(string)

print('------------------------------------------------------------')	#60個


'''
os.chdir(os.path.expanduser('~/Documents'))

'''
print('------------------------------------------------------------')	#60個

def cmp(f1, f2):
    bufsize = 1024 * 8
    with open(f1, 'rb') as fp1, open(f2, 'rb') as fp2:
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


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


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
    universal = os.path.join(WORKDIR, 'libraries')
    os.mkdir(universal)
    os.makedirs(os.path.join(universal, 'usr', 'local', 'lib'))
    os.makedirs(os.path.join(universal, 'usr', 'local', 'include'))

    for recipe in library_recipes():
        buildRecipe(recipe, universal, ARCHLIST)

def buildPythonDocs():
    curDir = os.getcwd()
    os.chdir(buildDir)

    runCommand('make clean')
    runCommand('make html')
    os.chdir(curDir)
    if not os.path.exists(docdir):
        os.mkdir(docdir)
    os.rename(os.path.join(buildDir, 'build', 'html'), docdir)





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('顯示目前 PATH')
print(sys.path)
print(sys.path[0])

pathlist = os.environ['PATH'].split(os.pathsep)
print(pathlist)


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個

print('預設用法 : ')

curdir = [os.curdir]
print('目前目錄 : ', curdir)

pardir = [os.pardir]
print('上層目錄 : ', pardir)

pwd = os.getcwd()

print('目前位置 : ', pwd)


#getcwd()方法顯示當前的工作目錄。
cur_path = os.getcwd() # 取得目前路徑
print("現在路徑："+cur_path)

'''
cur_path = os.getcwd() # 取得目前路徑
file=cur_path + "\dir2\copyfile.py" 
os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔
'''

print(os.sep)
print(os.altsep)


ADDRESS = r'\\.\pipe\_test_pipe-%s' % os.getpid()
print(ADDRESS)



'''
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


'''

'''
print('取得檔案的絕對位置 abspath()')
dest = os.path.abspath(os.path.join(foldername, "..", name + "Upd"))
print(dest)
'''

#-------

#os.makedirs(dest)

'''
for name in os.listdir(foldername):
    path, ext = os.path.splitext(name)

    filename = os.path.normpath(os.path.join(foldername, name))
    destname = os.path.normpath(os.path.join(dest, name))
    #print("%s -> %s" % (filename, destname))
'''
'''

shutil.rmtree(foldername2)

os.makedirs(foldername2)

#未知用意
#os.symlink('python', os.path.join(foldername2, 'python.exe'))

'''


'''
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


import sys

sys.path.insert(0, "../src")


       filename = img['source'].split('/')[-1].split('?')[0]
       print(filename)

dirname = os.path.dirname(__file__)"




filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
directory = os.path.dirname(filename) or '.'




'''

import ctypes

def genwincodec():
    import platform
    code = '''\
"""Python Character Mapping Codec %s generated on Windows:
%s with the command:
  python Tools/unicode/genwincodec.py %s
"""#"
''' % ('cp950', ' '.join(platform.win32_ver()), 950
      )

    print(code)

import sys
genwincodec()

# Get the list of available locales.
if platform.system() == 'Windows':
    print('Windows')
else:
    print('Not Windows')

    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


print(sys.platform)




print(os.path.expanduser('~'))
history = os.path.join(os.path.expanduser('~'), '.python_history')
print(history)

print(sys.platform)
print(sys.platform[:4])




import os
import sys
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
    if os.name == 'nt':
        # sniff sys.version for architecture.
        prefix = " bit ("
        i = sys.version.find(prefix)
        if i == -1:
            return sys.platform
        j = sys.version.find(")", i)
        look = sys.version[i+len(prefix):j].lower()
        if look == 'amd64':
            return 'win-amd64'
        if look == 'itanium':
            return 'win-ia64'
        return sys.platform

    if os.name != "posix" or not hasattr(os, 'uname'):
        # XXX what about the architecture? NT is Intel or Alpha
        return sys.platform

    # Set for cross builds explicitly
    if "_PYTHON_HOST_PLATFORM" in os.environ:
        return os.environ["_PYTHON_HOST_PLATFORM"]

    # Try to distinguish various flavours of Unix
    osname, host, release, version, machine = os.uname()

    # Convert the OS name to lowercase, remove '/' characters
    # (to accommodate BSD/OS), and translate spaces (for "Power Macintosh")
    osname = osname.lower().replace('/', '')
    machine = machine.replace(' ', '_')
    machine = machine.replace('/', '-')

    if osname[:5] == "linux":
        # At least on Linux/Intel, 'machine' is the processor --
        # i386, etc.
        # XXX what about Alpha, SPARC, etc?
        return  "%s-%s" % (osname, machine)
    elif osname[:5] == "sunos":
        if release[0] >= "5":           # SunOS 5 == Solaris 2
            osname = "solaris"
            release = "%d.%s" % (int(release[0]) - 3, release[2:])
            # We can't use "platform.architecture()[0]" because a
            # bootstrap problem. We use a dict to get an error
            # if some suspicious happens.
            bitness = {2147483647:"32bit", 9223372036854775807:"64bit"}
            machine += ".%s" % bitness[sys.maxsize]
        # fall through to standard osname-release-machine representation
    elif osname[:4] == "irix":              # could be "irix64"!
        return "%s-%s" % (osname, release)
    elif osname[:3] == "aix":
        return "%s-%s.%s" % (osname, version, release)
    elif osname[:6] == "cygwin":
        osname = "cygwin"
        import re
        rel_re = re.compile(r'[\d.]+')
        m = rel_re.match(release)
        if m:
            release = m.group()
    elif osname[:6] == "darwin":
        import _osx_support
        osname, release, machine = _osx_support.get_platform_osx(
                                            get_config_vars(),
                                            osname, release, machine)

    return "%s-%s-%s" % (osname, release, machine)


def get_python_version():
    return _PY_VERSION_SHORT


print('')
print('')
print('Platform: "%s"' % get_platform())
print('')
print('Python version: "%s"' % get_python_version())




'''
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
'''





import sys

frame = sys._getframe()
print(frame)





