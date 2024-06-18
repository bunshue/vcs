"""

使用 Python 的 hashlib 模組計算資料的 MD5 與 SHA 雜湊值

1. 通用
2. 字串 hash
3. 檔案 hash

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

import os
import sys
import hashlib

# 要計算 MD5 雜湊值的資料
clear_text = "this is a lion-mouse"

print("------------------------------------------------------------")  # 60個

print("列出此平台可使用的雜湊演算法")
print(hashlib.algorithms_available)

print("列出跨平台通用的雜湊演算法")
print(hashlib.algorithms_guaranteed)

print("------------------------------------------------------------")  # 60個

md5_value = hashlib.md5(clear_text.encode("utf8"))
print(md5_value)

# 計算 MD5 雜湊值

# 建立 MD5 物件
md5_value = hashlib.md5()

# 先將資料編碼，再更新 MD5 雜湊值
md5_value.update(clear_text.encode("utf-8"))

# 取得 MD5 雜湊值
md5_value = md5_value.hexdigest()
print(md5_value)

print("------------------------------------------------------------")  # 60個

print("算一個字串的hashcode SHA1")

sha1_value = hashlib.sha1()
sha1_value.update(clear_text.encode("utf-8"))
sha1_value = sha1_value.hexdigest()
print(sha1_value)

print("計算 SHA 雜湊值")
sha1_value = hashlib.sha1()  # 建立 SHA1 物件
sha1_value.update(clear_text.encode("utf-8"))
sha1_value = sha1_value.hexdigest()
print(sha1_value)

sha1_value = hashlib.sha1(clear_text.encode("utf-8")).hexdigest()
print(sha1_value)

print("------------------------------------------------------------")  # 60個


def compute_checksum(input, length=None):
    input = input or ""
    sha1_value = hashlib.sha1(input.encode("utf-8")).hexdigest()
    if length:
        sha1_value = sha1_value[:length]
    return sha1_value


input = "cat-dog"
output = "lion-mouse"
computed = compute_checksum(output, 20)
print(computed)

computed = "output={} input={}".format(
    compute_checksum(output, 16), compute_checksum(input, 16)
)

print(computed)

print("------------------------------------------------------------")  # 60個

print("算一個檔案的hashcode SHA1")

clear_filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

sha1_value = hashlib.sha1()
sha1_value.update(clear_filename.encode("utf-8"))

# 以二進位方式讀取檔案
with open(clear_filename, "rb") as f:
    sha1_value.update(f.read())

sha1_value = sha1_value.hexdigest()
print(sha1_value)

print("------------------------------------------------------------")  # 60個

print("算一個檔案的hashcode SHA256")


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
    sha256_value = hashlib.sha256()
    # 以二進位方式讀取檔案
    with open(clear_filename, "rb") as f:
        buf = f.read(BLOCKSIZE)
        while len(buf) > 0:
            sha256_value.update(buf)
            buf = f.read(BLOCKSIZE)

    return sha256_value.hexdigest()

clear_filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
calculated_filehash = calculate_file_hash(clear_filename)
print("SHA256")
print("預設答案 : ", "5d57e3deb441b789f6035d28dcbbaf6a436c54450972786fad4ce4527059d291")
print("計算結果 : ", calculated_filehash)

print("------------------------------------------------------------")  # 60個

# 字符串轉 md5 工具

string_data = clear_text.strip().replace("\n", "").encode()

md5_value = hashlib.md5()
md5_value.update(string_data)
md5_value = md5_value.hexdigest()
print(md5_value)

print("------------------------------------------------------------")  # 60個

md5_value = hashlib.md5()
md5_value.update(b"Nobody inspects")
md5_value.update(b" the spammish repetition")
md5_value = md5_value.digest()
print(md5_value)

print("------------------------------------------------------------")  # 60個

md5_value = hashlib.md5(clear_text.encode()).hexdigest()
print("md5 : ", md5_value)

print("------------------------------------------------------------")  # 60個

print("用hash值找一個資料夾內的重複的檔案")
foldername = "C:/_git/vcs/_1.data/______test_files1/compare"
filenames = os.listdir(foldername)  # 單層
print(filenames)
allmd5s = dict()
for filename in filenames:
    long_filename = os.path.join(foldername, filename)  # 取得檔案的絕對路徑
    # 以二進位方式讀取檔案
    md5_value = hashlib.md5(open(long_filename, "rb").read()).digest()
    if md5_value in allmd5s:
        print("---------------")
        print("以下為重覆的檔案：")
        print(os.path.abspath(filename))
        print(allmd5s[md5_value])
        os.system("open " + os.path.abspath(filename))
        os.system("open " + allmd5s[md5_value])
    else:
        allmd5s[md5_value] = os.path.abspath(filename)  # md5_value是key, 全路徑是value

print("------------------------------------------------------------")  # 60個

def md5sum(t):
    return hashlib.md5(t).hexdigest()

print("------------------------------------------------------------")  # 60個

sha512_value = hashlib.sha512("aaaaaaa".encode("utf-8"))
print(sha512_value)

dicom_uid = str(int(sha512_value.hexdigest(), 16))
print(dicom_uid)

print("------------------------------------------------------------")  # 60個

print("將字串轉成md5")

md5_value = hashlib.md5(bytes(clear_text, "utf-8")).digest()
print(md5_value)
print(md5_value[:16])

print("將字串轉成sha1")

sha1_value = hashlib.sha1(bytes(clear_text, "utf-8")).digest()
print(sha1_value)
print(sha1_value[:16])

print("------------------------------------------------------------")  # 60個

md5_value = hashlib.md5()  # 建立 md5_value 物件
md5_value.update(b"Ming-Chi Institute of Technology")  # 更新 md5_value 物件內容

print("Hash Value         = ", md5_value.digest())
print("Hash Value(16進位) = ", md5_value.hexdigest())
print(type(md5_value))  # 列出 md5_value 資料型態
print(type(md5_value.hexdigest()))  # 列出哈希值資料型態

print("------------------------------------------------------------")  # 60個

# 使用中文字串 需要先encode
md5_value = hashlib.md5()  # 建立md5_value物件
clear_text = "歡迎來到美國"  # 中文字串
md5_value.update(clear_text.encode("utf-8"))  # 更新md5_value物件內容

print("Hash Value         = ", md5_value.digest())
print("Hash Value(16進位) = ", md5_value.hexdigest())
print(type(md5_value))  # 列出md5_value資料型態
print(type(md5_value.hexdigest()))  # 列出哈希值資料型態

print("------------------------------------------------------------")  # 60個

sha1_value = hashlib.sha1()  # 建立 sha1_value 物件
sha1_value.update(b"Ming-Chi Institute of Technology")  # 更新 sha1_value 物件內容

print("Hash Value         = ", sha1_value.digest())
print("Hash Value(16進位) = ", sha1_value.hexdigest())
print(type(sha1_value))  # 列出sha1_value資料型態
print(type(sha1_value.hexdigest()))  # 列出哈希值資料型態

print("------------------------------------------------------------")  # 60個

sha256_value = hashlib.sha256()  # 建立 sha256_value 物件
sha256_value.update(b"Ming-Chi Institute of Technology")  # 更新 sha256_value 物件內容

print("Hash Value = ", sha256_value.hexdigest())
print(type(sha256_value))  # 列出 sha256_value 資料型態
print(type(sha256_value.hexdigest()))  # 列出雜湊碼資料型態

print("------------------------------------------------------------")  # 60個

sha3_384_value = hashlib.sha3_384()  # 建立 sha3_384_value 物件
sha3_384_value.update(b"Ming-Chi Institute of Technology")  # 更新 sha3_384_value 物件內容

print("Hash Value = ", sha3_384_value.hexdigest())
print(type(sha3_384_value))  # 列出 sha3_384_value 資料型態
print(type(sha3_384_value.hexdigest()))  # 列出雜湊碼資料型態

print("------------------------------------------------------------")  # 60個

sha256_value = hashlib.sha256()  # 建立 sha256_value 物件
sha256_value.update(b"Ming-Chi Institute of Technology")  # 更新 sha256_value 物件內容
print("Hash Value = ", sha256_value.hexdigest())

sha256_value = hashlib.sha256()  # 建立 sha256_value 物件
sha256_value.update(b"ming-Chi Institute of Technology")  # 更新 sha256_value 物件內容
print("Hash Value = ", sha256_value.hexdigest())

print("------------------------------------------------------------")  # 60個

"""

def create_password(pwd):
    sha256_value = hashlib.sha256()  # 建立 sha256_value 物件
    sha256_value.update(pwd.encode("utf-8"))  # 更新 sha256_value 物件內容
    return sha256_value.hexdigest()


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

clear_text = "歡迎來到美國"
md5_value = hashlib.md5()  # 建立 md5_value 物件
md5_value.update(clear_text.encode("utf-8"))  # 更新 md5_value 物件內容
print("Hash Value(16進位) = ", md5_value.hexdigest())

print("------------------------------------------------------------")  # 60個

BUFSUZE = 8096

def calculate_md5sum(*files):
    sts = 0
    if len(files) == 1 and not isinstance(files[0], str):
        files = files[0]
    for f in files:
        if isinstance(f, str):
            sts = printsum(f) or sts
    return sts

def printsum(clear_filename):
    # 以二進位方式讀取檔案
    fp = open(clear_filename, 'rb')
    sts = printsumfp(fp, clear_filename)
    fp.close()
    return sts

def printsumfp(fp, clear_filename):
    md5_value = hashlib.md5()
    while 1:
        data = fp.read(BUFSUZE)
        if not data:
            break
        if isinstance(data, str):
            data = data.encode(fp.encoding)
        md5_value.update(data)
    return md5_value.hexdigest()

#clear_filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
clear_filename = "Python-3.7.17.tar.xz"
#clear_filename = "\\192.168.1.231\RD_Soft\_主機程式\542-0002\BOOT.bin"

print('計算一個檔案的 MD5 值 1')
print('檔案 :', clear_filename)
cc = calculate_md5sum(clear_filename)
print('結果 :', cc)

print('----------')
print('dd94cab4541b57b88cf3dab32d6336e3')

print("------------------------------------------------------------")  # 60個

print('計算一個檔案的 MD5 值 2')

clear_filename = "C:/_git/vcs/_1.data/______test_files1/calculate_hash.txt"
clear_filename = "Python-3.7.17.tar.xz"

md5_value = hashlib.md5()

# 以二進位方式讀取檔案
with open(clear_filename, "rb") as f:
    # 分批讀取檔案內容，計算 MD5 雜湊值
    for chunk in iter(lambda: f.read(4096), b""):
        md5_value.update(chunk)

md5_value = md5_value.hexdigest()
print(md5_value)

print("------------------------------------------------------------")  # 60個

print('計算一個檔案的 MD5 值 3')

clear_filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
clear_filename = "Python-3.7.17.tar.xz"

# 以二進位方式讀取檔案
md5_value = hashlib.md5(open(clear_filename, "rb").read()).digest()
print(type(md5_value))
print(md5_value)

print("------------------------------------------------------------")  # 60個

print('計算一個檔案的 MD5 值 4')

md5_value = hashlib.md5()  # 建立 md5_value 物件
clear_filename = "C:/_git/vcs/_1.data/______test_files1/calculate_hash.txt"
clear_filename = "Python-3.7.17.tar.xz"

# 以二進位方式讀取檔案
with open(clear_filename, "rb") as fn:
    btxt = fn.read()
    md5_value.update(btxt)

print("Hash Value         = ", md5_value.digest())
print("Hash Value(16進位) = ", md5_value.hexdigest())
print(type(md5_value))  # 列出md5_value資料型態
print(type(md5_value.hexdigest()))  # 列出哈希值資料型態

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
