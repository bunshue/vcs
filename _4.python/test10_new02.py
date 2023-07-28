print('------------------------------')  #30個


print('字元轉unicode')
string = '你'

print(ord(string))

print(hex(ord(string)))

print('十進位 轉 十六進位')

# Convert a decimal to a hex as a string 
def decimalToHex(decimalValue):
    hex = ""
 
    while decimalValue != 0:
        hexValue = decimalValue % 16 
        hex = toHexChar(hexValue) + hex
        decimalValue = decimalValue // 16
    
    return hex
  
# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

decimalValue = 170
hexValue = decimalToHex(decimalValue)
print('decimal : %d\thex : %s' % (decimalValue, hexValue) )

decimalValue = 65535
hexValue = decimalToHex(decimalValue)
print('decimal : %d\thex : %s' % (decimalValue, hexValue) )

level = 123
levelnum = 170
print(" * PY_RELEASE_LEVEL = %r = %s" % (level, hex(levelnum)))


print('------------------------------')  #30個

print('------------------------------')  #30個



import os
import sys

__version__ = 1, 7, 0


'''
os.remove(fname)
os.rename(temp_fname, fname)

'''

print('list之使用')

llll = ['aa', 'bb', 'cc', 'dd', 'ee']
pppp = llll[2:] #第二項(含)以後的
print(llll)
print(pppp)

table1 = [] #list
table2 = {} #dict
print(type(table1))
print(type(table2))

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
mod = os.path.basename(filename)
print(mod)
print(mod[-3:])

head, tail = os.path.split(filename)
print(head)
print(tail)
tempname = os.path.join(head, '@' + tail)
print(tempname)


curdir = [os.curdir]
print(curdir)

pardir = [os.pardir]
print(pardir)


print('------------------------------')  #30個


a_dict = {}
print(type(a_dict))


a_list = []
print(type(a_list))


target_url = 'https://www.nkust.edu.tw/p/403-1000-12-{}.php'

for page in range(1, 6):
    html = target_url.format(page)
    print(html)


data = list()
for page in range(1, 6):
    pdate = 'aaaa'
    title = 'bbbb'
    link = 'cccc'
    data.append((pdate, link, title))
print(type(data))
print(data)


from bs4 import BeautifulSoup

from platform import python_version
print(python_version())
import bs4
print(bs4.__version__)


contents = list()

for page in range(1, 6):
    content = dict()
    content['link'] = 'aaaaa'
    content['content'] = 'bbbbb'
    content['date'] = 'ccccc'
    content['title'] = 'ddddd'
    contents.append(content)
    
print(contents)


import os
import re
import sys

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


import os
import sys
from distutils.util import get_platform
PLAT_SPEC = "%s-%s" % (get_platform(), sys.version[0:3])
src = os.path.join("build", "lib.%s" % PLAT_SPEC)
#sys.path.append(src)
print(src)

print(sys.argv)

print('------------------------------')  #30個

import platform, subprocess
print(platform.system())

print('------------------------------')  #30個



foldername = 'C:/_git/vcs/_1.data/______test_files2/'

name = os.path.basename(os.path.abspath(foldername))
print(name)
dest = os.path.abspath(os.path.join(foldername, "..", name + "Upd"))
print(dest)
#os.makedirs(dest)

#vs9to10(src, dest)

for name in os.listdir(foldername):
    path, ext = os.path.splitext(name)

    filename = os.path.normpath(os.path.join(foldername, name))
    destname = os.path.normpath(os.path.join(dest, name))
    #print("%s -> %s" % (filename, destname))

old_cd = os.getcwd()

print(old_cd)

print('------------------------------')  #30個

#os.chdir(os.path.join(ROOT, TK, "win"))

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


print('------------------------------')  #30個

import os

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print(filename[:-4])
print(filename[:-4])
retval = os.path.basename(filename[:-4])

print(retval)

import platform
no_asm = int(platform.release().split(".")[0]) < 9
print(no_asm)

print('------------------------------')  #30個



ADDRESS = r'\\.\pipe\_test_pipe-%s' % os.getpid()
print(ADDRESS)


print('------------------------------')  #30個




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


print('------------------------------')  #30個



import os
import sys
import shutil

foldername1 = 'C:/_git/vcs/_1.data/______test_files3'
foldername2 = foldername1 + 'aaaa'
if os.path.exists(foldername2):
    print('rmtree : ', foldername2)
    shutil.rmtree(foldername2)

os.makedirs(foldername2)

print('目前位置 : ', os.getcwd())

os.chdir(foldername2)
print('目前位置 : ', os.getcwd())

#未知用意
#os.symlink('python', os.path.join(foldername2, 'python.exe'))


import time

imagepath = '-%04d-%02d-%02d'%(time.localtime()[:3])
imagepath = imagepath + '.dmg'

print(imagepath)

foldername1 = 'C:/_git/vcs/_1.data/______test_files1'
foldername2 = 'C:/_git/vcs/_1.data/______test_files2'
foldername3 = 'C:/_git/vcs/_1.data/______test_files3'

if os.stat(foldername1).st_mtime < os.stat(foldername2).st_mtime:
    print('foldername1 較早')
else:
    print('foldername1 較晚')

string = 'this is a lion'
print(string)

string = string.replace('lion', 'mouse')
print(string)

print('------------------------------')  #30個


'''
import sys, os

print('目前位置 : ', os.getcwd())
os.chdir(os.path.expanduser('~/Documents'))
print('目前位置 : ', os.getcwd())
'''
print('------------------------------')  #30個



import abc
metaclass = abc.ABCMeta
print(metaclass)

import uuid
id = str(uuid.uuid4())
print(id)
    

import sys
if sys.version_info.major < 3 or sys.version_info.minor < 3:
    sys.exit("Error: clinic.py requires Python 3.3 or greater.")


print('------------------------------')  #30個






print('------------------------------')  #30個



print('格式化字串')

print(12345)

print('八位數 前面補0')
print('{:08d}\n{:08d}\n{:08d}'.format(123, 1234, 12345))




print('------------------------------')  #30個


import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

here = os.path.abspath(os.path.dirname(__file__))
par = os.path.pardir

print(here)
print(par)

ROOT = os.path.abspath(os.path.join(here, par, par))

print(ROOT)


import tempfile

cabname = tempfile.mktemp(suffix=".cab")
print(cabname)


print('------------------------------')  #30個



import os
import time

srcdir = os.path.abspath("../..")
PCBUILD="PCbuild"
major = 3
minor = 8

dll_file = "python%s%s.dll" % (major, minor)

dll_path = os.path.join(srcdir, PCBUILD, dll_file)
print(dll_path)

current_version = "%s.%s.%s" % (major, minor, int(time.time()/3600/24))

full_current_version = current_version

print(full_current_version)

print('------------------------------')  #30個



filename = "python-%s%s.msi" % (full_current_version, 'ccccc')
print(filename)


print('------------------------------')  #30個




import sys, os

execdir = os.path.dirname(sys.argv[0])
print(execdir)
executable = os.path.join(execdir, "Python")
print(executable)
resdir = os.path.join(os.path.dirname(execdir), "Resources")
print(resdir)
libdir = os.path.join(os.path.dirname(execdir), "Frameworks")
print(libdir)
mainprogram = os.path.join(resdir, "idlemain.py")
print(mainprogram)

    

print('------------------------------')  #30個




print('字串的 title 用法')
s = 'this is a lion mouse'

print(s.title())



print('------------------------------')  #30個







