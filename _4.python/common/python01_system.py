"""
系統操作與系統資料

"""
import os
import sys
import platform

print("------------------------------------------------------------")  # 60個

print("---- platform --------------------------------------------------------")  # 60個

print(platform)
print(platform.uname())

print("Python版本 : ", platform._sys_version(sys_version=None))
print("Python版本 : ", platform.python_implementation())
print("Python版本 : ", platform.python_version())
print("Python版本 : ", platform.python_version_tuple())
print("Python建立編號 : ", platform.python_build())
print("Python建立編號 : ", platform.python_build()[0])
print("Python分支版本 : ", platform.python_branch())
print("Python版本 : ", platform.python_revision())
print("Python編譯器 : ", platform.python_compiler())

print("作業系統 : ", platform.system())
print("作業系統版本 : ", platform.platform())
print("作業系統版本 : ", platform.platform(aliased=0, terse=0))
print("作業系統版本 : ", platform.release())
print("作業系統版本 : ", platform.version())

print("CPU : ", platform.processor())
print("機器 : ", platform.machine())
print("機器名稱 : ", platform.node())

print(platform.win32_ver())
print(platform.platform())

print("ccccc", platform.release().split(".")[0])

# Processor identification often has repeated spaces
cpu = " ".join(platform.processor().split())
print(
    "== %s %s on '%s' =="
    % (
        platform.machine(),
        platform.system(),
        cpu,
    )
)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


# Horizontal line length
LINE = 79


def get_machine_details():
    print("Getting machine details...")
    buildno, builddate = platform.python_build()
    python = platform.python_version()
    # XXX this is now always UCS4, maybe replace it with 'PEP393' in 3.3+?
    if sys.maxunicode == 65535:
        # UCS2 build (standard)
        unitype = "UCS2"
    else:
        # UCS4 build (most recent Linux distros)
        unitype = "UCS4"
    bits, linkage = platform.architecture()
    return {
        "platform": platform.platform(),
        "processor": platform.processor(),
        "executable": sys.executable,
        "implementation": getattr(platform, "python_implementation", lambda: "n/a")(),
        "python": platform.python_version(),
        "compiler": platform.python_compiler(),
        "buildno": buildno,
        "builddate": builddate,
        "unicode": unitype,
        "bits": bits,
    }


def print_machine_details(d, indent=""):
    l = [
        "Machine Details:",
        "   Platform ID:    %s" % d.get("platform", "n/a"),
        "   Processor:      %s" % d.get("processor", "n/a"),
        "",
        "Python:",
        "   Implementation: %s" % d.get("implementation", "n/a"),
        "   Executable:     %s" % d.get("executable", "n/a"),
        "   Version:        %s" % d.get("python", "n/a"),
        "   Compiler:       %s" % d.get("compiler", "n/a"),
        "   Bits:           %s" % d.get("bits", "n/a"),
        "   Build:          %s (#%s)"
        % (d.get("builddate", "n/a"), d.get("buildno", "n/a")),
        "   Unicode:        %s" % d.get("unicode", "n/a"),
    ]
    joiner = "\n" + indent
    print(indent + joiner.join(l) + "\n")


def print_header(title="Benchmark"):
    name = "david"
    print("-" * LINE)
    print("%s: %s" % (title, name))
    print("-" * LINE)
    if machine_details:
        print_machine_details(machine_details, indent="    ")


machine_details = None

machine_details = get_machine_details()

print_header()


print("------------------------------------------------------------")  # 60個

"""
name = 'os.path'
module = sys.modules[name]
spec = module.__spec__
print(spec)

#module = sys.modules.get(name)

print(type(sys.modules))
#print(sys.modules)
for module_or_name in sys.modules:
    print(module_or_name, end = ' ')

print(sys.modules.get(name))
print(sys.modules[name])
loader = sys.modules[name].__loader__
print(loader)
"""

"""
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
"""

import _locale

print(_locale._getdefaultlocale())
print(_locale._getdefaultlocale()[1])

print("------------------------------------------------------------")  # 60個

for path in sys.builtin_module_names:
    print(path)

print("------------------------------------------------------------")  # 60個

print("顯示模組的所有名稱")
import random

print(dir(random))

print("------------------------------------------------------------")  # 60個

print(f"全域變數 : {globals()}")

print("------------------------------------------------------------")  # 60個

import builtins

print(dir(builtins))

print("------------------------------------------------------------")  # 60個

maxsize = sys.maxsize  # smallest total size so far
print(maxsize)

print("------------------------------------------------------------")  # 60個

print(os.name)
print(os.sep)
print(os.getpid())

print("------------------------------------------------------------")  # 60個

import random

packagedir = os.path.dirname(random.__file__)
print(packagedir)
print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

import bs4
print(bs4.__version__)

import numpy as np
print(np.__version__)

print("查詢已安裝的 Pandas 版本")

import pandas as pd
print(pd.__version__)

import matplotlib
print(matplotlib.__version__)

# import sklearn
import matplotlib

# import keras
print("Python version:", sys.version)
print("Numpy version:", numpy.version.version)
print("Pandas version:", pd.__version__)
# print("Scikit-learn version:", sklearn.__version__)
print("Matplotlib version:", matplotlib.__version__)
# print("Keras version:", keras.__version__)

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

length = len(sys.argv)
print("參數長度 : ", length)
for i in range(0, length):
    print(sys.argv[i])

if len(sys.argv) > 1:
    files = sys.argv[1:]
    print(files)

print("------------------------------------------------------------")  # 60個

if len(sys.argv) < 0:
    print("未有外部傳入參數")
else:
    for n in range(len(sys.argv)):
        print("param" + str(n) + "：", sys.argv[n])


print("列印參數")
print(sys.argv)

print("參數長度 = " + str(len(sys.argv)))
print("參數長度 = {}".format(len(sys.argv)))

# 印出所有參數
i = 0
for arg in sys.argv:
    print("第{}個參數是:{}".format(i, arg))
    print(sys.argv[i])
    i += 1

print(sys.argv[:])

print("------------------------------------------------------------")  # 60個

print("目前路徑 : ", sys.path)
print("打印系統路徑")
print(sys.path)

print("------------------------------------------------------------")  # 60個

print("系統命令")
os.system("cls")  # 在cmd視窗下清除螢幕 for Windows
os.system("clear")  # 在cmd視窗下清除螢幕 for non-Windows
os.system("ls")
# os.system('pause') 暫停
os.system("mkdir tmp_dir2")  # 建立 tmp_dir2 目錄
os.system("copy python00.py tmp_dir2\tmp_python00.py")  # 複製檔案

print("執行python程式")
# os.system('makecode.py test.c')

print("製作cmd指令")
"""
cmd = 'dir'
if os.system(cmd) != 0:
    raise RuntimeError(cmd)

os.system('cmd')
"""

# 用預設程式開啟檔案
# os.system('filename.png')  #開啟圖片
# os.system('filename.html')    # 開啟網頁

print("------------------------------------------------------------")  # 60個

print("系統命令, 開啟外部程式")

filename_r = "../data/article.txt"
os.system("notepad " + filename_r)
# os.system("svn checkout%s -q %s %s" % (creds, url, filename))

print("------------------------------------------------------------")  # 60個

print(os.environ.get("CI_COMMIT_TAG", "0.0.0"))
_version = os.environ.get("CI_COMMIT_TAG", "0.0.1.dev2")

"""here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
"""

print("------------------------------------------------------------")  # 60個

"""
print(sys.path)
sys.exit(1)	#立刻退出程式

#強制離開程式, 並說明原因
sys.exit('強制離開程式, 並說明原因')
"""

print("------------------------------------------------------------")  # 60個

print(os.name)

if os.name == "nt":
    print("Windows NT 系統")
    import nt

    print(sys.getwindowsversion())
    print(sys.getwindowsversion()[:2])
    if sys.getwindowsversion()[:2] >= (6, 0):
        print("Win10")
    else:
        print("非Win10")
else:
    print("非 Windows NT 系統")

print("------------------------------------------------------------")  # 60個

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
import time

print("Press Ctrl-C to stop.")

try:
    while True:  # Main program loop.
        print("wait", end=" ")
        time.sleep(1)  # Add a pause.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.
"""

print("------------------------------------------------------------")  # 60個

m = sys.modules.get("__main__")
print(m)

print("------------------------------------------------------------")  # 60個

print(os.name)
print(os.sys.platform)

print("------------------------------------------------------------")  # 60個

print("取得本程式名稱")
progname = os.path.basename(sys.argv[0])
print(progname)

print("------------------------------------------------------------")  # 60個

prog = sys.argv[0]
print(prog)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import email

packagedir = os.path.dirname(email.__file__)
print(packagedir)

print("------------------------------------------------------------")  # 60個

import numpy as np
import pandas as pd

import numpy

print(numpy.version.version)

# 使用 importlib.metadata 模块查找 NumPy 模块的版本
from importlib_metadata import version

print(version("numpy"))

import pkg_resources

print(pkg_resources.get_distribution("numpy").version)

print("------------------------------------------------------------")  # 60個

# import this	可以看到 Zen of Python

print("------------------------------------------------------------")  # 60個

import time
import getopt

opts, args = getopt.getopt(sys.argv[1:], "h:c:")
if len(opts) != 1:
    sys.stdout.write("Must specify exactly one output file\n")

for o, v in opts:
    if o == "-h":
        INC_DIR = v
    if o == "-c":
        SRC_DIR = v
if len(args) != 1:
    sys.stdout.write("Must specify single input file\n")

if len(opts) > 0:
    print(args[0])

print("------------------------------------------------------------")  # 60個

import getopt

inplace = False
backup = False
opts, args = getopt.getopt(sys.argv[1:], "ib:")
for o, a in opts:
    if o == "-i":
        inplace = True
    if o == "-b":
        backup = a


def errprint(*args):
    sep = ""
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = " "
    sys.stderr.write("\n")


# global verbose, filename_only
try:
    opts, args = getopt.getopt(sys.argv[1:], "qv")
except getopt.error as msg:
    errprint(msg)
for o, a in opts:
    if o == "-q":
        filename_only = filename_only + 1
    if o == "-v":
        verbose = verbose + 1
if not args:
    errprint("Usage:", sys.argv[0], "[-v] file_or_directory ...")
for arg in args:
    # check(arg)
    print(arg)

print("------------------------------------------------------------")  # 60個

import getopt

try:
    opts, args = getopt.getopt(
        args,
        "n:s:r:tcpvh",
        ["number=", "setup=", "repeat=", "time", "clock", "process", "verbose", "help"],
    )
except getopt.error as err:
    print(err)
    print("use -h/--help for command line help")


print("aaaaaaaaaaaaaaaaaaaaaa")

timer = time.time
stmt = "\n".join(args) or "pass"
number = 0  # auto-determine
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
        print(__doc__, end=" ")


print("ccccccc")

print("------------------------------------------------------------")  # 60個

import argparse

cmdline = argparse.ArgumentParser()
print(cmdline)

cmdline.add_argument("-f", "--force", action="store_true")
cmdline.add_argument("-o", "--output", type=str)
cmdline.add_argument("-v", "--verbose", action="store_true")
cmdline.add_argument("--converters", action="store_true")
cmdline.add_argument("--make", action="store_true")
cmdline.add_argument("filename", type=str, nargs="*")
print("---------------------")
print(cmdline)

cmdline.print_usage()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("目前Python版本是: ", sys.version)

print("------------------------------------------------------------")  # 60個

f = [x for x in range(1, 10)]

print(f)

print(sys.getsizeof(f))  # 查看對象佔用內存的字節數


""" input
print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline()
print(msg)

print("------------------------------------------------------------")  # 60個

print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline(8)         # 讀8個字
print(msg)
"""

print("------------------------------------------------------------")  # 60個

sys.stdout.write("I like Python")

print("------------------------------------------------------------")  # 60個

for dirpath in sys.path:
    print(dirpath)

print("------------------------------------------------------------")  # 60個

print("命令列參數 : ", sys.argv)

print("------------------------------------------------------------")  # 60個

from pprint import pprint

print("使用print")
print(sys.path)
print("使用pprint")
pprint(sys.path)

print("------------------------------------------------------------")  # 60個

print("目前Python版本是:     ", sys.version)
print("目前Python版本是:     ", sys.version_info)
print("目前Python平台是:     ", sys.platform)
print("目前Python視窗版本是: ", sys.getwindowsversion())
print("目前Python可執行檔路徑", sys.executable)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""

system
print(sys.builtin_module_names)


for fullname in sys.modules:
    module = sys.modules[fullname]
    print(fullname, module)

"""


print("------------------------------------------------------------")  # 60個

print("內建函式dir()檢視目前的名稱空間")
print(dir())

import qrcode

print(dir())

# 看單一模組的函式
import math

print(dir(math))

print("------------------------------------------------------------")  # 60個


# 以 dir() 與 help() 探索 Python 模組與物件

import datetime

print(dir(datetime))

print("")

print([_ for _ in dir(datetime) if "date" in _.lower()])

# help(datetime)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("Python版本號：", sys.version)
print("作業系統：", sys.platform)

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

print("------------------------------------------------------------")  # 60個


PYTHONDOCS = os.environ.get(
    "PYTHONDOCS", "http://docs.python.org/%d.%d/library" % sys.version_info[:2]
)
print("PYTHONDOCS")
print(PYTHONDOCS)

encoding = sys.getfilesystemencoding()
print(encoding)


print("------------------------------------------------------------")  # 60個

print(
    "* using %s %s"
    % (
        getattr(platform, "python_implementation", lambda: "Python")(),
        " ".join(sys.version.split()),
    )
)

print("------------------------------------------------------------")  # 60個

from distutils.util import get_platform

PLAT_SPEC = "%s-%s" % (get_platform(), sys.version[0:3])
src = os.path.join("build", "lib.%s" % PLAT_SPEC)
# sys.path.append(src)
print(src)

print("------------------------------------------------------------")  # 60個

print(sys.version_info)
print(sys.version_info[0])
if sys.version_info[0] >= 3:
    print("python 新版")
else:
    print("python 舊版")

if sys.version < "3":
    print("python 舊版")
else:
    print("python 新版")

major, minor, micro, level, serial = sys.version_info

print("version_info")
print(sys.version_info)
print(major)
print(minor)
print(micro)
print(level)
print(serial)

print("------------------------------------------------------------")  # 60個

python_version = "Python %d.%d" % (sys.version_info[0], sys.version_info[1])
print(python_version)

version = __version__ = "4.61.0.166 Unreleased"
print(version)

print("------------------------------------------------------------")  # 60個

print(sys.platform)

if sys.platform.startswith("win"):
    print("你用的作業系統是Windows")
else:
    print("你用的作業系統不是Windows")

if sys.platform == "win32":
    print("Windows")
else:
    print("Non-Windows")

print("Python:", sys.version)
print(sys.version)
print(sys.version)

print("Python版本號：", sys.version)
print("作業系統：", sys.platform)


print("------------------------------------------------------------")  # 60個

print("記事本 開啟")
import os
import win32process
import win32event

handle = win32process.CreateProcess(
    "c:\\windows\\notepad.exe",
    "",
    None,
    None,
    0,
    win32process.CREATE_NO_WINDOW,
    None,
    None,
    win32process.STARTUPINFO(),
)
win32event.WaitForSingleObject(handle[0], -1)
print("記事本 關閉")

print("------------------------------------------------------------")  # 60個

sys.path.append(os.path.dirname(os.getcwd()))

ROOT_DIR = os.getcwd()
sys.path.append(ROOT_DIR)

print("------------------------------------------------------------")  # 60個

PYTHONLIB = "libpython" + sys.version[:3] + ".a"
PC_PYTHONLIB = "Python" + sys.version[0] + sys.version[2] + ".dll"
NM = "nm -p -g %s"  # For Linux, use "nm -g %s"

print(PYTHONLIB)
print(PC_PYTHONLIB)
print(NM)

print("sys.getwindowsversion()")
print(sys.getwindowsversion())
print("sys.getwindowsversion()[:2]")
print(sys.getwindowsversion()[:2])
if sys.getwindowsversion()[:2] >= (6, 0):
    print("bbbbb")

if sys.getwindowsversion()[3] >= 2:
    print("ccccc")

print("sys.builtin_module_names")
print(sys.builtin_module_names)

if "ce" in sys.builtin_module_names:
    defpath = "\\Windows"


print(type(sys.path))
print(sys.path)

print("------------------------------------------------------------")  # 60個

import sys

# 查看搜尋模組套件的路徑優先順序
for path in sys.path:
    print(path)

print("------------------------------------------------------------")  # 60個

import sys

print("目前python程式所在位置 sys.executable :")
print(sys.executable)

print("sys.version :")
print(sys.version)
print("sys.version_info :")
print(sys.version_info)
print("sys.platform :")
print(sys.platform)
print("sys.hexversion")
print(sys.hexversion)

py3 = sys.version_info >= (3, 0)
print(py3)

if sys.hexversion >= 0x02020000:
    print("aaaaa")

version_suffix = "%r%r" % sys.version_info[:2]
print(version_suffix)
print("Python%s.dll" % version_suffix)

from _msi import *
import os, string, re, sys

AMD64 = "AMD64" in sys.version
Itanium = "Itanium" in sys.version
Win64 = AMD64 or Itanium

print(AMD64)
print(Itanium)
print(Win64)

print("取得系統的預設編碼")
cc = sys.getdefaultencoding()
print(cc)

print("------------------------------------------------------------")  # 60個


"""


所有版本


1. 作業系統

2. Python

3. 各套件

# many
# pd.show_versions()

"""


import random

print(dir(random))


import math

help(math.sqrt)
help(math.pow)

print("help 的用法")
import random

print(dir(random))
help(random.randint)
help(random.choice)

print("------------------------------------------------------------")  # 60個

# 用預設程式開啟檔案
# os.system('cccc.mp3')

# 用預設程式wav檔案
# os.startfile('harumi99.wav')

# 用系統預設程式開啟檔案
# os.system('tmp_pic.png')

print("------------------------------------------------------------")  # 60個

import os

print("HOME環境變數:", os.environ["HOME"])


df = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"], "data1": range(7)})
print(df)

print(__name__)


if __name__ == "__main__":
    print("It's main")
else:
    print("It's not main")


import pandas

cc = dir(pandas)
print(cc)

print("------------------------------------------------------------")  # 60個

import platform, os, sys, getopt, textwrap, shutil, stat, time

FW_PREFIX = ["Library", "Frameworks", "Python.framework"]
FW_VERSION_PREFIX = "--undefined--"

# The directory we'll use to create the build (will be erased and recreated)
WORKDIR = "C:/_git/vcs/_1.data/______test_files3aaaa"

# The directory we'll use to store third-party sources. Set this to something
# else if you don't want to re-fetch required libraries every time.
DEPSRC = os.path.join(WORKDIR, "third-party")
DEPSRC = os.path.expanduser("~/Universal/other-sources")

SDKPATH = "/Developer/SDKs/MacOSX10.4u.sdk"

universal_opts_map = {
    "32-bit": (
        "i386",
        "ppc",
    ),
    "64-bit": (
        "x86_64",
        "ppc64",
    ),
    "intel": ("i386", "x86_64"),
    "3-way": ("ppc", "i386", "x86_64"),
    "all": (
        "i386",
        "ppc",
        "x86_64",
        "ppc64",
    ),
}

UNIVERSALOPTS = tuple(universal_opts_map.keys())

UNIVERSALARCHS = "32-bit"

ARCHLIST = universal_opts_map[UNIVERSALARCHS]

# Source directory
SRCDIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEPTARGET = "10.3"


def getTargetCompilers():
    target_cc_map = {
        "10.3": ("gcc-4.0", "g++-4.0"),
        "10.4": ("gcc-4.0", "g++-4.0"),
        "10.5": ("gcc-4.2", "g++-4.2"),
        "10.6": ("gcc-4.2", "g++-4.2"),
    }
    return target_cc_map.get(DEPTARGET, ("clang", "clang++"))


SRCDIR = os.path.abspath(SRCDIR)
WORKDIR = os.path.abspath(WORKDIR)
SDKPATH = os.path.abspath(SDKPATH)
DEPSRC = os.path.abspath(DEPSRC)

CC, CXX = getTargetCompilers()

FW_VERSION_PREFIX = FW_PREFIX[:] + ["Versions", "aaaaa"]

print("Source directory:    %s" % SRCDIR)
print("Build directory:     %s" % WORKDIR)
print("SDK location:        %s" % SDKPATH)
print("Third-party source:  %s" % DEPSRC)
print("Deployment target:   %s" % DEPTARGET)
print("Universal archs:     %s" % str(ARCHLIST))
print("C compiler:          %s" % CC)
print("C++ compiler:        %s" % CXX)

print("sys.version_info = ", sys.version_info)
print("platform.system() = ", platform.system())
print("platform.release() = ", platform.release())
"""
print('os.environ = ', os.environ)
for ev in list(os.environ):
    print(ev)
"""

print("------------------------------------------------------------")  # 60個

print("globals()用法")
# print(globals())

ccc = (
    textwrap.dedent(
        """\
    WORKDIR : %(WORKDIR)r
    DEPSRC : %(DEPSRC)r
    SDKPATH : %(SDKPATH)r
    SRCDIR : %(SRCDIR)r
    DEPTARGET : %(DEPTARGET)r
    UNIVERSALOPTS : %(UNIVERSALOPTS)r,
    UNIVERSALARCHS : %(UNIVERSALARCHS)r
"""
    )
    % globals()
)


print(ccc)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

os.system(filename)  # 用系統內建的程式開啟檔案

print("------------------------------------------------------------")  # 60個

print("列出所有區域變數的名稱與內容")
cc = locals()
print(cc)

print("列出所有全域變數的名稱與內容")
cc = globals()
print(cc)

import sys

# 目前 python程式 路徑
print(sys.executable)

# shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
os.system("ls -l")
# os.chdir('/Users/Hao')
os.system("ls -l")
# os.mkdir('test')

import os

cur_path = os.getcwd()  # 取得目前路徑
os.system("cls")  # 清除螢幕
os.system("mkdir dir2")  # 建立 dir2 目錄
os.system("copy ossystem.py dir2\copyfile.py")  # 複製檔案
file = cur_path + "\dir2\copyfile.py"
os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔


os.system("leaks %d" % os.getpid())


print("------------------------------------------------------------")  # 60個

"""
os.system 整理

import os

開啟外部程式
#rc = os.system("nasm -f win64 -DNEAR -Ox -g ms\\uptable.asm")

rc = os.system('calc')

os.system('cls') #在cmd視窗下清除螢幕

os.system('cls' if os.name == 'nt' else 'clear')

file=cur_path + "\dir2\copyfile.py" 
os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔

os.system("cls")  # 清除螢幕
os.system("mkdir dir2")  # 建立 dir2 目錄
os.system("copy ossystem.py dir2\copyfile.py") # 複製檔案 
file=cur_path + "\dir2\copyfile.py" 
os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔

#os.system("notepad " + filename_r)

"""

print("------------------------------------------------------------")  # 60個


def msg(str):
    sys.stderr.write(str + "\n")


longlist = "-l"
filename = "test01_io.py"

sts = os.system("ls " + longlist + " " + filename)
if sts:
    msg('"ls -l" exit status: ' + repr(sts))

sts = os.system("ls " + filename)
if sts:
    msg('"ls -l" exit status: ' + repr(sts))

sts = os.system("dir")
if sts:
    msg('"ls -l" exit status: ' + repr(sts))
else:
    print(sts)


print("------------------------------------------------------------")  # 60個

"""
如何将Python调用的os.system命令的错误信息反馈回来（Window）
本文探讨了Python中os.system与os.popen两种执行外部命令的方法。os.system仅反馈执行成功与否，无法直接获取错误信息；os.popen返回命令输出，但非同步且无法直接反馈错误。通过重定向输出至文件，可以解决获取错误信息的问题。

os.system只能反馈执行是否成功的标志位，想要获取错误信息，只能使用重定向其输出结果到文件中。 

"""

"""
os.popen方式：
返回值：cmd的输出信息。本身是异步调用，返回为一个Io文件指针，读取IO才会导致同步阻塞
"""

import os

cmd = "dir"
f = os.popen(cmd)
print(f.read())

"""
如果正确输出可以看到信息。但是有两个问题：
1.正确的输出信息不是同步反馈的
2.如果调用该命令出错，返回信息为空，并不返回错误信息。
"""
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


"""
hostname = "google.com"
response = os.system("ping -c 3 -i 1 " + hostname)
print(response)

response = os.popen(f"ping -c 3 -i 1 {hostname}").read()
print(response)



"""

