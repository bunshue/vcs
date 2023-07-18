import datetime


seconds = datetime.datetime(2004, 10, 26, 10, 33, 33, tzinfo=datetime.timezone(datetime.timedelta(0))).timestamp()

print(seconds)


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


os.chdir(foldername1)
curdir = os.getcwd()
print(curdir)

for fn in os.listdir(foldername1):
    print(fn)

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




'''
import sys, os

print('目前位置 : ', os.getcwd())
os.chdir(os.path.expanduser('~/Documents'))
print('目前位置 : ', os.getcwd())
'''



foldername3 = 'C:/_git/vcs/_1.data/______test_files3'

files = os.listdir(foldername3)
for sub in files:
    sub, ext = os.path.splitext(sub)
    fullname = 'aaaa' + "." + sub
    print(fullname)


