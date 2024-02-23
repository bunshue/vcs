# ch17_5.py
import hashlib

data = hashlib.sha256()                             # 建立data物件
data.update(b'Ming-Chi Institute of Technology')    # 更新data物件內容

print('Hash Value = ', data.hexdigest())
print(type(data))                                   # 列出data資料型態
print(type(data.hexdigest()))                       # 列出雜湊碼資料型態








