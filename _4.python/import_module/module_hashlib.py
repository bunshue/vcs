"""

使用 Python 的 hashlib 模組計算資料的 MD5 與 SHA 雜湊值


md5(): 建立md5()方法的物件
update(): 更新數據文件內容
digest():    將數據文件轉成雜湊值
hexdigest(): 將數據文件轉成16進位的雜湊值

演算法 輸出雜湊值長度

MD5     128
SHA-0   160
SHA-1   160
SHA-2
    SHA-224 224
    SHA-256 256
    SHA-384 384
    SHA-512 512
    SHA-512/224 224
    SHA-512/256 256
SHA-3
    SHA3-224 224
    SHA3-256 256
    SHA3-384 384
    SHA3-512 512
    SHAKE128
    SHAKE256

"""


import sys
import hashlib


clear_text = "this is a lion-mouse"

print('------------------------------------------------------------')	#60個

print('可用的雜湊演算法')
print(hashlib.algorithms_available)

print('跨平台通用的雜湊演算法')
print(hashlib.algorithms_guaranteed)

clear_text = "this is a lion-mouse"
value = hashlib.md5(clear_text.encode('utf8'))
print(value)

#計算 MD5 雜湊值

# 建立 MD5 物件
m = hashlib.md5()

# 要計算 MD5 雜湊值的資料
clear_text = "this is a lion-mouse"

# 先將資料編碼，再更新 MD5 雜湊值
m.update(clear_text.encode("utf-8"))

# 取得 MD5 雜湊值
h = m.hexdigest()

print(h)

#計算檔案的 MD5 雜湊值

clear_filename = 'C:/_git/vcs/_1.data/______test_files1/calculate_hash.txt'

m = hashlib.md5()

with open(clear_filename, "rb") as f:
  # 分批讀取檔案內容，計算 MD5 雜湊值
  for chunk in iter(lambda: f.read(4096), b""):
    m.update(chunk)

h = m.hexdigest()
print(h)

print('------------------------------------------------------------')	#60個

def calculate_file_hash(clear_filename):
    """Return the SHA256 checksum for the file at `fpath`.

    Parameters
    ----------
    fpath : pathlib.Path
        The absolute path to the file that is to be checksummed.

    Returns
    -------
    str
        The SHA256 checksum of the file.
    """
    BLOCKSIZE = 65536
    hasher = hashlib.sha256()
    with open(clear_filename, "rb") as f:
        buf = f.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(BLOCKSIZE)

    return hasher.hexdigest()

clear_filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
calculated_filehash = calculate_file_hash(clear_filename)
print('SHA256')
print('預設答案 : ', '5d57e3deb441b789f6035d28dcbbaf6a436c54450972786fad4ce4527059d291')
print('計算結果 : ', calculated_filehash)

print('------------------------------------------------------------')	#60個

print('算一個字串的hashcode SHA1')
print('ccccccccccccccccccccccccccc')

s = hashlib.sha1()
clear_text = "this is a lion-mouse"
s.update(clear_text.encode('utf-8'))
result = s.hexdigest()
print(result)

print('計算 SHA 雜湊值')
s = hashlib.sha1()  # 建立 SHA1 物件
s.update(clear_text.encode("utf-8"))
result = s.hexdigest()
print(result)

result = hashlib.sha1(clear_text.encode('utf-8')).hexdigest()
print(result)


print('------------------------------------------------------------')	#60個

def compute_checksum(input, length=None):
    input = input or ''
    s = hashlib.sha1(input.encode('utf-8')).hexdigest()
    if length:
        s = s[:length]
    return s

input = 'cat-dog'
output = 'lion-mouse'
computed = compute_checksum(output, 20)
print(computed)

computed = "output={} input={}".format(compute_checksum(output, 16), compute_checksum(input, 16))

print(computed)

print('------------------------------------------------------------')	#60個

print('算一個檔案的hashcode SHA1')

clear_filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

s = hashlib.sha1()
s.update(clear_filename.encode('utf-8'))

with open(clear_filename, 'rb') as f:
    s.update(f.read())

h = s.hexdigest()
print(h)

print('------------------------------------------------------------')	#60個

#字符串轉 md5 工具

clear_text = "this is a lion-mouse"
print(clear_text)

string_data = clear_text.strip().replace("\n","").encode()

myMd5 = hashlib.md5()
myMd5.update(string_data)
myMd5_Digest = myMd5.hexdigest()
print(myMd5_Digest)

print('------------------------------------------------------------')	#60個

m = hashlib.md5()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
m.digest()
print(m.digest())

#    b'\\xbbd\\x9c\\x83\\xdd\\x1e\\xa5\\xc9\\xd9\\xde\\xc9\\xa1\\x8d\\xf0\\xff\\xe9'


print('------------------------------------------------------------')	#60個

clear_text = "this is a lion-mouse"
md5 = hashlib.md5(clear_text.encode()).hexdigest()
print('md5 : ', md5)

print('------------------------------------------------------------')	#60個

print('算一個檔案的hash值')

clear_filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
md5 = hashlib.md5(open(clear_filename, 'rb').read()).digest()
print(type(md5))
print(md5)

print('------------------------------------------------------------')	#60個

import os

print('用hash值找一個資料夾內的重複的檔案')
foldername = 'C:/_git/vcs/_1.data/______test_files1/compare'
filenames = os.listdir(foldername)    #單層
print(filenames)
allmd5s = dict()
for filename in filenames:
    long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
    img_md5 = hashlib.md5(open(long_filename,'rb').read()).digest()
    if img_md5 in allmd5s:
        print("---------------")
        print("以下為重覆的檔案：")
        print(os.path.abspath(filename))
        print(allmd5s[img_md5])
        os.system("open " + os.path.abspath(filename))
        os.system("open " + allmd5s[img_md5])
    else:
        allmd5s[img_md5] = os.path.abspath(filename)# img_md5是key, 全路徑是value

print('------------------------------------------------------------')	#60個

import hashlib

def md5sum(t):
    return hashlib.md5(t).hexdigest()

print('------------------------------------------------------------')	#60個

import hashlib

hash_val = hashlib.sha512('aaaaaaa'.encode("utf-8"))
print(hash_val)

dicom_uid = str(int(hash_val.hexdigest(), 16))
print(dicom_uid)

print('------------------------------------------------------------')	#60個

"""
import hashlib
clear_text = "this is a lion-mouse"
h = hashlib.md5(clear_text).hexdigest()
print(h)
"""

print('------------------------------------------------------------')	#60個

import hashlib

clear_text = "this is a lion-mouse"

print('將字串轉成md5')

hashnum = hashlib.md5(bytes(clear_text, "utf-8")).digest()
print(hashnum)
print(hashnum[:16])

print('將字串轉成sha1')

hashnum = hashlib.sha1(bytes(clear_text, "utf-8")).digest()
print(hashnum)
print(hashnum[:16])

print("------------------------------------------------------------")  # 60個

import hashlib

data = hashlib.md5()  # 建立data物件
data.update(b"Ming-Chi Institute of Technology")  # 更新data物件內容

print("Hash Value         = ", data.digest())
print("Hash Value(16進位) = ", data.hexdigest())
print(type(data))  # 列出data資料型態
print(type(data.hexdigest()))  # 列出哈希值資料型態

print("------------------------------------------------------------")  # 60個

import hashlib

#使用中文字串 需要先encode
data = hashlib.md5()  # 建立data物件
clear_text = "歡迎來到美國"  # 中文字串
data.update(clear_text.encode("utf-8"))  # 更新data物件內容

print("Hash Value         = ", data.digest())
print("Hash Value(16進位) = ", data.hexdigest())
print(type(data))  # 列出data資料型態
print(type(data.hexdigest()))  # 列出哈希值資料型態

print("------------------------------------------------------------")  # 60個

print('用 hash 加密檔案資料')

import hashlib

data = hashlib.md5()                                # 建立data物件
clear_filename = "C:/_git/vcs/_1.data/______test_files1/calculate_hash.txt"

with open(clear_filename, "rb") as fn:                    # 以二進位方式讀取檔案
    btxt = fn.read()
    data.update(btxt)

print('Hash Value         = ', data.digest())
print('Hash Value(16進位) = ', data.hexdigest())
print(type(data))                                   # 列出data資料型態
print(type(data.hexdigest()))                       # 列出哈希值資料型態

print("------------------------------------------------------------")  # 60個

import hashlib

data = hashlib.sha1()  # 建立data物件
data.update(b"Ming-Chi Institute of Technology")  # 更新data物件內容

print("Hash Value         = ", data.digest())
print("Hash Value(16進位) = ", data.hexdigest())
print(type(data))  # 列出data資料型態
print(type(data.hexdigest()))  # 列出哈希值資料型態


print("------------------------------------------------------------")  # 60個

import hashlib

print(hashlib.algorithms_available)  # 列出此平台可使用的哈希演算法


print("------------------------------------------------------------")  # 60個

import hashlib

print(hashlib.algorithms_guaranteed)  # 列出跨平台可使用的哈希演算法

print("------------------------------------------------------------")  # 60個

import hashlib

data = hashlib.sha256()  # 建立data物件
data.update(b"Ming-Chi Institute of Technology")  # 更新data物件內容

print("Hash Value = ", data.hexdigest())
print(type(data))  # 列出data資料型態
print(type(data.hexdigest()))  # 列出雜湊碼資料型態


print("------------------------------------------------------------")  # 60個

import hashlib

data = hashlib.sha3_384()  # 建立data物件
data.update(b"Ming-Chi Institute of Technology")  # 更新data物件內容

print("Hash Value = ", data.hexdigest())
print(type(data))  # 列出data資料型態
print(type(data.hexdigest()))  # 列出雜湊碼資料型態


print("------------------------------------------------------------")  # 60個

import hashlib

data1 = hashlib.sha256()  # 建立data物件
data1.update(b"Ming-Chi Institute of Technology")  # 更新data物件內容
print("Hash Value = ", data1.hexdigest())

data2 = hashlib.sha256()  # 建立data物件
data2.update(b"ming-Chi Institute of Technology")  # 更新data物件內容
print("Hash Value = ", data2.hexdigest())


print("------------------------------------------------------------")  # 60個

"""
import hashlib

def create_password(pwd):
    data = hashlib.sha256()  # 建立data物件
    data.update(pwd.encode("utf-8"))  # 更新data物件內容
    return data.hexdigest()


acc = input("請建立帳號 : ")
pwd = input("請輸入密碼 : ")
account = {}
account[acc] = create_password(pwd)

print("歡迎進入系統")
userid = input("請輸入帳號 : ")
password = input("請輸入密碼 : ")
if userid in account:
    if account[userid] == create_password(password):
        print("歡迎進入系統")
    else:
        print("密碼錯誤")
else:
    print("帳號錯誤")
"""

print("------------------------------------------------------------")  # 60個

import hashlib

clear_text = "歡迎來到美國"
data = hashlib.md5()  # 建立data物件
data.update(clear_text.encode("utf-8"))  # 更新data物件內容
print("Hash Value(16進位) = ", data.hexdigest())

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
