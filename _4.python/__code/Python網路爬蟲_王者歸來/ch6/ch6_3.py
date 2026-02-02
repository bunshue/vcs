# ch6_3.py
import hashlib

data = hashlib.md5()                                # 建立data物件
filename = "data6_3.txt"

with open(filename, "rb") as fn:                    # 以二進位方式讀取檔案
    btxt = fn.read()
    data.update(btxt)

print('Hash Value         = ', data.digest())
print('Hash Value(16進位) = ', data.hexdigest())
print(type(data))                                   # 列出data資料型態
print(type(data.hexdigest()))                       # 列出哈希值資料型態








