# ch17_7.py
import hashlib

data1 = hashlib.sha256()                             # 建立data物件
data1.update(b'Ming-Chi Institute of Technology')    # 更新data物件內容
print('Hash Value = ', data1.hexdigest())

data2 = hashlib.sha256()                             # 建立data物件
data2.update(b'ming-Chi Institute of Technology')    # 更新data物件內容
print('Hash Value = ', data2.hexdigest())










