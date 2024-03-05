#各種檔案寫讀範例 新進暫存

import sys

print('------------------------------------------------------------')	#60個


'''

"""
std_data = dict()
with open(filename, encoding='utf-8') as fp:
    alldata = fp.readlines()
    for item in alldata:
        no, name = item.rstrip('\n').split(',')
        std_data[no] = name
print(std_data)
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

data = b'wxy\x7a'
print(data)               # b'wxyz'，以ASCII字元輸出

print(type(data), type(data[0]))
# <class 'bytes'>, <class 'int'>

print(data[0], hex(data[0]))
# 'w' ASCII碼119，十六進位'0x77'

print(b'\x7a' in data)    # 可以用 in 來判斷
print(data[2:])           # 可以切片

print("------------------------------------------------------------")  # 60個

data = b'wxy\x7a'
print(data)               # b'wxyz'，以ASCII字元輸出

ba = bytearray(data)
print(type(ba), type(ba[0]))
# <class 'bytearray'>, <class 'int'>

ba[3] = 0x70              # 修改資料
print(ba)                 # 變成 bytearray(b'wxyp')


print("------------------------------------------------------------")  # 60個

str1 = '葉'

print(str1.encode('big5'))     
# 轉big-5編碼，b'\xb8\xad'

print(str1.encode('gbk'))      
# 轉bgk編碼，b'\xc8~'

print(str1.encode('utf-8'))    
# 轉utf-8編碼，b'\xe8\x91\x89'


data = b'\xB8\xAD'

print(data.decode('big5'))
# 將bytes轉為big5文字，'葉'

print(data.decode('gbk'))
# 將bytes轉為gbk文字，'腑'

"""
print(data.decode('utf-8'))
# 將bytes轉為ytf-8文字，解碼規則無法解碼
"""
'''
print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個
