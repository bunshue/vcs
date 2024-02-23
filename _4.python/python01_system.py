"""
系統操作與系統資料

"""

import sys
import platform

print('------------------------------------------------------------')	#60個

# Horizontal line length
LINE = 79

def get_machine_details():
    print('Getting machine details...')
    buildno, builddate = platform.python_build()
    python = platform.python_version()
    # XXX this is now always UCS4, maybe replace it with 'PEP393' in 3.3+?
    if sys.maxunicode == 65535:
        # UCS2 build (standard)
        unitype = 'UCS2'
    else:
        # UCS4 build (most recent Linux distros)
        unitype = 'UCS4'
    bits, linkage = platform.architecture()
    return {
        'platform': platform.platform(),
        'processor': platform.processor(),
        'executable': sys.executable,
        'implementation': getattr(platform, 'python_implementation',
                                  lambda:'n/a')(),
        'python': platform.python_version(),
        'compiler': platform.python_compiler(),
        'buildno': buildno,
        'builddate': builddate,
        'unicode': unitype,
        'bits': bits,
        }

def print_machine_details(d, indent=''):

    l = ['Machine Details:',
         '   Platform ID:    %s' % d.get('platform', 'n/a'),
         '   Processor:      %s' % d.get('processor', 'n/a'),
         '',
         'Python:',
         '   Implementation: %s' % d.get('implementation', 'n/a'),
         '   Executable:     %s' % d.get('executable', 'n/a'),
         '   Version:        %s' % d.get('python', 'n/a'),
         '   Compiler:       %s' % d.get('compiler', 'n/a'),
         '   Bits:           %s' % d.get('bits', 'n/a'),
         '   Build:          %s (#%s)' % (d.get('builddate', 'n/a'),
                                          d.get('buildno', 'n/a')),
         '   Unicode:        %s' % d.get('unicode', 'n/a'),
         ]
    joiner = '\n' + indent
    print(indent + joiner.join(l) + '\n')


def print_header(title='Benchmark'):
    name = 'david'
    print('-' * LINE)
    print('%s: %s' % (title, name))
    print('-' * LINE)
    print()
    print()
    if machine_details:
        print_machine_details(machine_details, indent='    ')
        print()

machine_details = None

machine_details = get_machine_details()

print_header()


print('------------------------------------------------------------')	#60個

import sys


'''
name = 'os.path'
module = sys.modules[name]
spec = module.__spec__
print(spec)

#module = sys.modules.get(name)

print(type(sys.modules))
#print(sys.modules)
for module_or_name in sys.modules:
    print(module_or_name, end = ' ')
print()

print(sys.modules.get(name))
print(sys.modules[name])
loader = sys.modules[name].__loader__
print(loader)
'''

'''
systeminfo
        module = sys.modules[fullname]
        if module is None:
            return None
        try:
            spec = module.__spec__
        except AttributeError:
            raise ValueError('{}.__spec__ is not set'.format(name))
        else:
            if spec is None:
                raise ValueError('{}.__spec__ is None'.format(name))
            return spec
'''




import _locale
print(_locale._getdefaultlocale())
print(_locale._getdefaultlocale()[1])


print('------------------------------------------------------------')	#60個
import os
import sys


print()

print('------------------------------------------------------------')	#60個

for path in sys.builtin_module_names:
    print(path)

print()



print('------------------------------------------------------------')	#60個



PYTHONDOCS = os.environ.get("PYTHONDOCS",
                            "http://docs.python.org/%d.%d/library"
                            % sys.version_info[:2])
print('PYTHONDOCS')
print(PYTHONDOCS)

encoding = sys.getfilesystemencoding()
print(encoding)


print('------------------------------------------------------------')	#60個


print('顯示模組的所有名稱')

import random
print(dir(random))

print('------------------------------------------------------------')	#60個





import platform
print(platform.win32_ver())
print(platform.platform())

print('------------------------------------------------------------')	#60個

import platform

print("目前Python版本是: ", sys.version)
print("目前Python版本是: ", sys.version_info)

print(sys.version_info)
print("---")
print(sys.platform)
print("---")
print(sys.argv)
print("---")
print(sys.path)

version_rows = [("platform", platform.platform()), ("Python", sys.version)]
print(version_rows)

if sys.version_info.major < 3 or sys.version_info.minor < 3:
    sys.exit("Error: clinic.py requires Python 3.3 or greater.")

print('------------------------------------------------------------')	#60個

print(f"全域變數 : {globals()}")

print('------------------------------------------------------------')	#60個



import builtins
print(dir(builtins))

print('------------------------------------------------------------')	#60個



maxsize = sys.maxsize  # smallest total size so far
print(maxsize)

print('------------------------------------------------------------')	#60個


print(os.name)
print(os.sep)
print(os.getpid())


print('------------------------------------------------------------')	#60個


import random
packagedir = os.path.dirname(random.__file__)
print(packagedir)



print('------------------------------------------------------------')	#60個

import os
import sys
import platform

print('------------------------------------------------------------')	#60個

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



print("列印參數")
print(sys.argv)
print(sys.argv)

print("參數長度 = " + str(len(sys.argv)))
print("參數長度 = {}".format(len(sys.argv)))

#印出所有參數
i = 0
for arg in sys.argv:
    print("第{}個參數是:{}".format(i,arg))
    print(sys.argv[i])
    i += 1

print('------------------------------------------------------------')	#60個

print("目前路徑 : ", sys.path)
print("打印系統路徑")
print(sys.path)

print('------------------------------------------------------------')	#60個

print('系統命令');
os.system('cls')  #在cmd視窗下清除螢幕
os.system('clear')
os.system('ls')
#os.system('pause') 暫停
os.system('mkdir tmp_dir2')  # 建立 tmp_dir2 目錄
os.system('copy python00.py tmp_dir2\tmp_python00.py') # 複製檔案 

print('製作cmd指令')
"""
cmd = 'dir'
if os.system(cmd) != 0:
    raise RuntimeError(cmd)

os.system('cmd')
"""

print('------------------------------------------------------------')	#60個

print('系統命令, 開啟外部程式')

filename_r = '../data/article.txt'
os.system("notepad " + filename_r)
#os.system("svn checkout%s -q %s %s" % (creds, url, filename))

print('------------------------------------------------------------')	#60個

import sys
print(sys.version_info)
print(sys.version_info[0])
if sys.version_info[0] >= 3:
    print('python 新版')
else:
    print('python 舊版')
    
if sys.version < '3':
    print('python 舊版')
else:
    print('python 新版')

major, minor, micro, level, serial = sys.version_info

print('version_info')
print(sys.version_info)
print(major)
print(minor)
print(micro)
print(level)
print(serial)

print('------------------------------------------------------------')	#60個

import sys
python_version = "Python %d.%d" % (sys.version_info[0], sys.version_info[1])
print(python_version)


version = __version__ = "4.61.0.166 Unreleased"
print(version)

print('------------------------------------------------------------')	#60個

import os

print(os.environ.get("CI_COMMIT_TAG", "0.0.0"))
_version = os.environ.get("CI_COMMIT_TAG", "0.0.1.dev2")


"""here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
"""

print('------------------------------------------------------------')	#60個

print(sys.platform)

if sys.platform.startswith("win"):
    print('你用的作業系統是Windows')
else:
    print('你用的作業系統不是Windows')

import sys
if sys.platform == 'win32':
    print('Windows')
else:
    print('Non-Windows')

print("Python:", sys.version)
print(sys.version)
print(sys.version)

print('------------------------------------------------------------')	#60個

"""
import sys
print(sys.path)
sys.exit(1)	#立刻退出程式

#強制離開程式, 並說明原因
sys.exit('強制離開程式, 並說明原因')
"""

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



import sys

print('------------------------------------------------------------')	#60個

print("sys.argv:{}".format(sys.argv))
print("文件名稱{}".format(sys.argv[0]))
length = len(sys.argv)

""" 
if len(sys.argv) < 2:
    sys.exit(0)

for i in range(1,length):
     n1 = sys.argv[i]
     print( "第{}個引數是{}".format(i,n1))
"""

print('------------------------------------------------------------')	#60個

import os
print(os.name)

if os.name == 'nt':
    print('Windows NT 系統')
    import nt
    print(sys.getwindowsversion())
    print(sys.getwindowsversion()[:2])
    if sys.getwindowsversion()[:2] >= (6, 0):
        print('Win10')
    else:
        print('非Win10')
else:
    print('非 Windows NT 系統')

print('------------------------------------------------------------')	#60個


"""
print('Press Ctrl-C to quit.')

while True:
    try:
        time.sleep(1)
        print('A', end = ' ')
    except KeyboardInterrupt:
        print('你按了 ctrl + C, 離開')
        sys.exit()
"""

"""
import time, sys

print("Press Ctrl-C to stop.")

try:
    while True:  # Main program loop.
        print("wait", end=" ")
        time.sleep(1)  # Add a pause.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
"""



print('------------------------------------------------------------')	#60個

import os
import sys
m = sys.modules.get('__main__')

print(m)



print('------------------------------------------------------------')	#60個


import os

print(os.name)
print(os.sys.platform)




print('------------------------------------------------------------')	#60個


print('取得本程式名稱')
progname = os.path.basename(sys.argv[0])
print(progname)



print('------------------------------------------------------------')	#60個

try:
    import a_python_module
except ImportError:
    print("匯入模組 a_python_module 失敗")
    print("請安裝模組")
    # sys.exit()

print("------------------------------------------------------------")  # 60個

import sys

if len(sys.argv) < 0:
    print("未有外部傳入參數")
else:
    print("Python版本號：", sys.version)
    print("作業系統：", sys.platform)

    for n in range(len(sys.argv)):
        print("param" + str(n) + "：", sys.argv[n])
 

print('------------------------------------------------------------')	#60個

import email
packagedir = os.path.dirname(email.__file__)
print(packagedir)

print('------------------------------------------------------------')	#60個


import numpy as np
import pandas as pd

print(np.__version__)

import numpy

print(numpy.version.version)

# 使用 importlib.metadata 模块查找 NumPy 模块的版本
from importlib_metadata import version

print(version("numpy"))

import pkg_resources

print(pkg_resources.get_distribution("numpy").version)


print("查詢已安裝的 Pandas 版本")
print(pd.__version__)

import pandas as pd

print(pd.__version__)

print("------------------------------------------------------------")  # 60個

# import this	可以看到 Zen of Python



print('------------------------------------------------------------')	#60個


import os
import sys
import time
import getopt

print('------------------------------------------------------------')	#60個

length = len(sys.argv)
print('參數長度 : ', length);
for i in range (0, length):
    print(sys.argv[i])

if len(sys.argv) > 1:
    files = sys.argv[1:]
    print(files)

print('------------------------------------------------------------')	#60個

prog = sys.argv[0]
print(prog)

print('------------------------------------------------------------')	#60個

opts, args = getopt.getopt(sys.argv[1:], "h:c:")
if len(opts) != 1:
    sys.stdout.write("Must specify exactly one output file\n")

for o, v in opts:
    if o == '-h':
        INC_DIR = v
    if o == '-c':
        SRC_DIR = v
if len(args) != 1:
    sys.stdout.write("Must specify single input file\n")

if len(opts) > 0:
    print(args[0])

print('------------------------------------------------------------')	#60個

import sys, os

import getopt
inplace = False
backup = False
opts, args = getopt.getopt(sys.argv[1:], "ib:")
for o, a in opts:
    if o == '-i':
        inplace = True
    if o == '-b':
        backup = a


def errprint(*args):
    sep = ""
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = " "
    sys.stderr.write("\n")

#global verbose, filename_only
try:
    opts, args = getopt.getopt(sys.argv[1:], "qv")
except getopt.error as msg:
    errprint(msg)
for o, a in opts:
    if o == '-q':
        filename_only = filename_only + 1
    if o == '-v':
        verbose = verbose + 1
if not args:
    errprint("Usage:", sys.argv[0], "[-v] file_or_directory ...")
for arg in args:
    #check(arg)
    print(arg)

print('------------------------------------------------------------')	#60個

import getopt

try:
    opts, args = getopt.getopt(args, "n:s:r:tcpvh",
                               ["number=", "setup=", "repeat=",
                                "time", "clock", "process",
                                "verbose", "help"])
except getopt.error as err:
    print(err)
    print("use -h/--help for command line help")


print('aaaaaaaaaaaaaaaaaaaaaa')

timer = time.time
stmt = "\n".join(args) or "pass"
number = 0 # auto-determine
setup = []
repeat = 5
verbose = 0
precision = 3
for o, a in opts:
    if o in ("-n", "--number"):
        number = int(a)
    if o in ("-s", "--setup"):
        setup.append(a)
    if o in ("-r", "--repeat"):
        repeat = int(a)
        if repeat <= 0:
            repeat = 1
    if o in ("-t", "--time"):
        timer = time.time
    if o in ("-c", "--clock"):
        timer = time.clock
    if o in ("-p", "--process"):
        timer = time.process_time
    if o in ("-v", "--verbose"):
        if verbose:
            precision += 1
        verbose += 1
    if o in ("-h", "--help"):
        print(__doc__, end=' ')


print('ccccccc')

print('------------------------------------------------------------')	#60個

import argparse
cmdline = argparse.ArgumentParser()
print(cmdline)

cmdline.add_argument("-f", "--force", action='store_true')
cmdline.add_argument("-o", "--output", type=str)
cmdline.add_argument("-v", "--verbose", action='store_true')
cmdline.add_argument("--converters", action='store_true')
cmdline.add_argument("--make", action='store_true')
cmdline.add_argument("filename", type=str, nargs="*")
print('---------------------')
print(cmdline)

cmdline.print_usage()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


