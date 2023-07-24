'''

使用 Python 的 hashlib 模組計算資料的 MD5 與 SHA 雜湊值

'''

import hashlib

'''
print('可用的雜湊演算法')
print(hashlib.algorithms_available)

print('跨平台通用的雜湊演算法')
print(hashlib.algorithms_guaranteed)

string = 'this is a lion-mouse'
value = hashlib.md5(string.encode('utf8'))
print(value)

#計算 MD5 雜湊值
# 引入 hashlib 模組
import hashlib

# 建立 MD5 物件
m = hashlib.md5()

# 要計算 MD5 雜湊值的資料
data = "this is a lion-mouse"

# 先將資料編碼，再更新 MD5 雜湊值
m.update(data.encode("utf-8"))

# 取得 MD5 雜湊值
h = m.hexdigest()

print(h)

#計算檔案的 MD5 雜湊值
import hashlib

filename = 'C:/_git/vcs/_1.data/______test_files1/calculate_hash.txt'

m = hashlib.md5()

with open(filename, "rb") as f:
  # 分批讀取檔案內容，計算 MD5 雜湊值
  for chunk in iter(lambda: f.read(4096), b""):
    m.update(chunk)

h = m.hexdigest()
print(h)


print('計算 SHA 雜湊值')
import hashlib

# 建立 SHA1 物件
s = hashlib.sha1()

data = "G. T. Wang"
s.update(data.encode("utf-8"))
h = s.hexdigest()
print(h)

'''

def calculate_file_hash(filename):
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
    with open(filename, "rb") as f:
        buf = f.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(BLOCKSIZE)

    return hasher.hexdigest()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
calculated_filehash = calculate_file_hash(filename)
print('SHA256')
print('預設答案 : ', '5d57e3deb441b789f6035d28dcbbaf6a436c54450972786fad4ce4527059d291')
print('計算結果 : ', calculated_filehash)

print('------------------------------')  #30個

print('算一個字串的hashcode')
import hashlib

s = hashlib.sha1()
data = "this is a lion-mouse"
s.update(data.encode('utf-8'))
h = s.hexdigest()
print(h)


print('------------------------------')  #30個

print('算一個檔案的hashcode')

import hashlib

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

s = hashlib.sha1()
s.update(filename.encode('utf-8'))

with open(filename, 'rb') as f:
    s.update(f.read())

h = s.hexdigest()
print(h)
'''
string = 'this is a lion-mouse'
md5 = hashlib.md5(string).hexdigest()
print('md5 : ', md5)
'''

print('------------------------------')  #30個


#字符串轉 md5 工具
import hashlib

string = 'lion-mouse'
print(string)

string_data = string.strip().replace("\n","").encode()

myMd5 = hashlib.md5()
myMd5.update(string_data)
myMd5_Digest = myMd5.hexdigest()
print(myMd5_Digest)


print('------------------------------')  #30個

import hashlib

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







print('------------------------------')  #30個






print('------------------------------')  #30個






