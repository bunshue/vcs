#各種檔案寫讀範例 txt 3

import sys

print('------------------------------------------------------------')	#60個


str1 = "黃河遠上白雲間\n"
str2 = "一片孤城萬仞山\n"
str3 = "羌笛何須怨楊柳\n"
str4 = "春風不度玉門關"
strs = [str1, str2, str3, str4]

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp950.txt'
print("用cp950編碼寫一檔, 檔名 :", filename)
with open(filename, 'w', encoding='cp950') as fObj:
    fObj.write(str1)
    fObj.write(str2)
    fObj.write(str3)
    fObj.write(str4)

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp936.txt'
print("用cp936編碼寫一檔, 檔名 :", filename)
with open(filename, 'w', encoding='cp936') as fObj:
    fObj.writelines(strs)

print("------------------------------------------------------------")  # 60個

filename = 'poem.utf-8.txt'
print("用utf-8編碼寫一檔, 檔名 :", filename)
with open(filename, 'w', encoding='utf-8') as fObj:
    fObj.writelines(strs)

print("------------------------------------------------------------")  # 60個

poem_text = "黃河遠上白雲間一片孤城萬仞山羌笛何須怨楊柳春風不度玉門關"

filename = 'poem.cp950b.txt'
print("用cp950編碼 分段寫檔, 檔名 :", filename)
size = len(poem_text)
offset = 0
chunk = 5                         # 每次寫入的單位
with open(filename, 'w', encoding='cp950') as fObj:
    while True:
        if offset > size:
            break
        print(fObj.write(poem_text[offset:offset+chunk]))
        offset += chunk

print("------------------------------------------------------------")  # 60個

print('用read()一次讀完全檔')
filename = 'poem.cp950.txt'
fObj = open(filename, 'r', encoding='cp950')    
data = fObj.read()      # 讀取檔案到變數data
fObj.close()            # 關閉檔案物件
print(data)             # 輸出變數data相當於輸出檔案

print("------------------------------------------------------------")  # 60個

print('一次讀一行')
filename = 'poem.cp950b.txt'
with open(filename, 'r', encoding='cp950') as fObj:    
    for line in fObj:       # 相當於逐列讀取
        print(line)         # 輸出line

print("------------------------------------------------------------")  # 60個

print('一次讀一行 加 rstrip()')
filename = 'poem.cp950b.txt'
with open(filename, 'r', encoding='cp950') as fObj:    
    for line in fObj:           # 相當於逐列讀取
        print(line.rstrip())    # 輸出line

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp950.txt'
with open(filename, 'r', encoding='cp950') as fObj:
    print("用readline()讀一行")
    str1 = fObj.readline()
    print(str1)

    print("用readline()讀一行")
    str2 = fObj.readline()
    print(str2)

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp950.txt'

print('用readlines()一次讀完全檔 至一個 list')

with open(filename, 'r', encoding='cp950') as fObj:    
    text_list = fObj.readlines()

#print(text_list)
for line in text_list:
    print(line)

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp950b.txt'
with open(filename, 'r', encoding='cp950') as fObj:
    print(f"目前指針位置 {fObj.tell()}")    
    str1 = fObj.read(7)
    print(f"讀出資料 : {str1}, 目前指針位置 {fObj.tell()}")
    str2 = fObj.read(7)
    print(f"讀出資料 : {str2}, 目前指針位置 {fObj.tell()}")
    str3 = fObj.read(7)
    print(f"讀出資料 : {str3}, 目前指針位置 {fObj.tell()}")  

print("------------------------------------------------------------")  # 60個

filename = 'poem.utf-8.txt'
chunk = 3
msg = ''
with open(filename, 'r', encoding='utf-8') as fObj: 
    while True:
        txt = fObj.read(chunk)  # 一次讀取chunk數量
        if not txt:
            break
        msg += txt
print(msg)





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('測試完成')

    



