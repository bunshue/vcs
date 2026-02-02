# ch6_2.py
import hashlib

data = hashlib.md5()                                # 建立data物件
school = '明志科技大學'                             # 中文字串
data.update(school.encode('utf-8'))                 # 更新data物件內容

print('Hash Value         = ', data.digest())
print('Hash Value(16進位) = ', data.hexdigest())
print(type(data))                                   # 列出data資料型態
print(type(data.hexdigest()))                       # 列出哈希值資料型態








