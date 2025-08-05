import os
import tempfile

print("------------------------------------------------------------")  # 60個

filename = tempfile.NamedTemporaryFile().name
print("製作暫存檔案")
print(filename)


# fp = tempfile.NamedTemporaryFile()


print("------------------------------------------------------------")  # 60個

(os_id, abs_path) = tempfile.mkstemp(suffix=".pgm")

print(os_id)
print(abs_path)

print("---- 臨時資料夾 --------------------------------------------------------")  # 60個

tempdir = tempfile.gettempdir()
print("臨時資料夾 : ", tempdir)

tempdir1 = os.path.join(tempdir, "dir")
tempdir_same = os.path.join(tempdir, "dir-same")
tempdir_diff = os.path.join(tempdir, "dir-diff")

print("臨時資料夾1 : ", tempdir1)
print("臨時資料夾2 : ", tempdir_same)
print("臨時資料夾3 : ", tempdir_diff)

tmp_filename = os.path.join(tempdir, "pywin32_postinstall.log")
print(tmp_filename)

tmp_filename = os.path.join(tempdir, "pywin32_postinstall.log", "ccccc")
print(tmp_filename)

print("------------------------------------------------------------")  # 60個

cabname = tempfile.mktemp(suffix=".cab")
print(cabname)

print("------------------------------------------------------------")  # 60個

tmp_filename = tempfile.mktemp()
print("建立臨時檔案 :", tmp_filename)
fp = open(tmp_filename, "wb")  # wb : 二進位寫, w : 純文字寫
fp.write(b"cccc" + b"\n")
# fp.write("quit\n")
fp.close()

print("讀取此臨時檔案")
fp = open(tmp_filename, "rb")
data = fp.read()
fp.close()
print(data)

# os.unlink(tmp_filename)   #等於是刪除tmp_filename

print("------------------------------------------------------------")  # 60個


import os

import tempfile

(fd, filename) = tempfile.mkstemp()
os.close(fd)
print(filename)

# os.unlink(filename)


import tempfile

filename = tempfile.mktemp()
with open(filename, "w") as file:
    text = "AAAAAAAAAAAAAAAA"
    file.write(text)

# os.unlink(filename)


print("------------------------------------------------------------")  # 60個

import glob
import socket
import tempfile

tempdir = os.path.join(tempfile.gettempdir(), ".grail-unix")
filename = tempdir

# 撈出單層檔案
maybes = glob.glob(filename)
if maybes:
    print(
        "%s started at %s\n\tLocal addr: %s\n\tRemote addr:%s"
        % (self.__class__.__name__, time.ctime(time.time()), localaddr, remoteaddr),
        file=DEBUGSTREAM,
    )


print("------------------------------------------------------------")  # 60個

import os
import tempfile

with tempfile.TemporaryDirectory() as tmpdir:
    fn = os.path.join(tmpdir, "foo")
    print(fn)
    with open(fn, "w") as stream:
        stream.write("ccccccccc")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



# Topic: 临时文件和目录

from tempfile import TemporaryFile
from tempfile import TemporaryDirectory
from tempfile import NamedTemporaryFile
import tempfile


with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    print(data)

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)

with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)

print(tempfile.mkstemp())
print(tempfile.mkdtemp())
print(tempfile.gettempdir())


import tempfile
with tempfile.NamedTemporaryFile(delete=True) as fp:
    print("暫時檔案 :", fp.name)

temp_dir = tempfile.TemporaryDirectory()
psg_dir = os.path.join(temp_dir.name, 'PySimpleGUI')

import tempfile
tmpfilename = os.path.join(tempfile.gettempdir(), "bsd.txt")


import tempfile

tmpdir = tempfile.gettempdir()
print(tmpdir)

import tempfile

tmpdir = tempfile.gettempdir()
print(tmpdir)


csv_filename = os.path.join(tmpdir, "users.csv")

print(csv_filename)


import tempfile

tmpdir = tempfile.gettempdir()
print(tmpdir)
db_filename = os.path.join(tmpdir, "users.db")
print(db_filename)








