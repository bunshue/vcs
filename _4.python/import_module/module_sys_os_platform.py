import re
import os
import sys
import time
import platform
import shutil

''' OK
print(platform)

print(platform.uname())

print('---- 作業系統 --------------------------------------------------------')	#60個

print('作業系統 : ', platform.system())
print('作業系統版本 : ', platform.platform())
print('作業系統版本 : ', platform.platform(aliased=0, terse=0))
print('作業系統版本 : ', platform.release())
print('作業系統版本 : ', platform.version())

print('---- 硬體 --------------------------------------------------------')	#60個

print('CPU : ', platform.processor())
print('機器 : ', platform.machine())
print('機器名稱 : ', platform.node())

print('---- Python --------------------------------------------------------')	#60個

print('Python版本 : ', platform._sys_version(sys_version = None))
print('Python版本 : ', platform.python_implementation())
print('Python版本 : ', platform.python_version())
print('Python版本 : ', platform.python_version_tuple())
print('Python建立編號 : ', platform.python_build())
print('Python建立編號 : ', platform.python_build()[0])
print('Python分支版本 : ', platform.python_branch())
print('Python版本 : ', platform.python_revision())
print('Python編譯器 : ', platform.python_compiler())

print('------------------------------------------------------------')	#60個

print('ccccc', platform.release().split(".")[0])

# Processor identification often has repeated spaces
cpu = ' '.join(platform.processor().split())
print("== %s %s on '%s' ==" % (
    platform.machine(),
    platform.system(),
    cpu,
))

print('------------------------------------------------------------')	#60個

print('* using %s %s' % (
    getattr(platform, 'python_implementation', lambda:'Python')(),
    ' '.join(sys.version.split())))

print('------------------------------------------------------------')	#60個

from distutils.util import get_platform

PLAT_SPEC = "%s-%s" % (get_platform(), sys.version[0:3])
src = os.path.join("build", "lib.%s" % PLAT_SPEC)
#sys.path.append(src)
print(src)

print('------------------------------------------------------------')	#60個

from bs4 import BeautifulSoup

import bs4
print(bs4.__version__)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
'''

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

