# ch6_4.py
import hashlib

data = hashlib.sha1()                               # 建立data物件
data.update(b'Ming-Chi Institute of Technology')    # 更新data物件內容

print('Hash Value         = ', data.digest())
print('Hash Value(16進位) = ', data.hexdigest())
print(type(data))                                   # 列出data資料型態
print(type(data.hexdigest()))                       # 列出哈希值資料型態








