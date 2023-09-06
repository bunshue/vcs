'''

使用 Python 的 hashlib 模組計算資料的 MD5 與 SHA 雜湊值

'''
import hashlib

print('------------------------------------------------------------')	#60個

'''
print('可用的雜湊演算法')
print(hashlib.algorithms_available)

print('跨平台通用的雜湊演算法')
print(hashlib.algorithms_guaranteed)

string = 'this is a lion-mouse'
value = hashlib.md5(string.encode('utf8'))
print(value)

#計算 MD5 雜湊值

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

filename = 'C:/_git/vcs/_1.data/______test_files1/calculate_hash.txt'

m = hashlib.md5()

with open(filename, "rb") as f:
  # 分批讀取檔案內容，計算 MD5 雜湊值
  for chunk in iter(lambda: f.read(4096), b""):
    m.update(chunk)

h = m.hexdigest()
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

print('------------------------------------------------------------')	#60個

print('算一個字串的hashcode SHA1')
print('ccccccccccccccccccccccccccc')

s = hashlib.sha1()
string = "this is a lion-mouse"
s.update(string.encode('utf-8'))
result = s.hexdigest()
print(result)

print('計算 SHA 雜湊值')
s = hashlib.sha1()  # 建立 SHA1 物件
s.update(string.encode("utf-8"))
result = s.hexdigest()
print(result)

result = hashlib.sha1(string.encode('utf-8')).hexdigest()
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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

s = hashlib.sha1()
s.update(filename.encode('utf-8'))

with open(filename, 'rb') as f:
    s.update(f.read())

h = s.hexdigest()
print(h)

print('------------------------------------------------------------')	#60個

#字符串轉 md5 工具

string = 'lion-mouse'
print(string)

string_data = string.strip().replace("\n","").encode()

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

string = 'this is a lion-mouse'
md5 = hashlib.md5(string.encode()).hexdigest()
print('md5 : ', md5)

print('------------------------------------------------------------')	#60個

print('算一個檔案的hash值')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image_md5 = hashlib.md5(open(filename, 'rb').read()).digest()
print(image_md5)


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
        allmd5s[img_md5] = os.path.abspath(filename) 

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

'''
import hashlib

string = 'lion-mouse'
h = hashlib.md5(string).hexdigest()
    print(h)
'''

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


