import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

filename = 'data14_8.txt'         # 設定欲開啟的檔案
with open(filename, 'r', encoding='cp950') as fObj:
    print(f"指針位置 {fObj.tell()}")    
    txt1 = fObj.read(3)
    print(f"{txt1}, 指針位置 {fObj.tell()}")
    txt2 = fObj.read(3)
    print(f"{txt2}, 指針位置 {fObj.tell()}")
    txt3 = fObj.read(3)
    print(f"{txt3}, 指針位置 {fObj.tell()}")     

print('------------------------------------------------------------')	#60個

filename = 'data14_9.txt'             # 設定欲開啟的檔案
chunk = 100
msg = ''
with open(filename, 'r', encoding='cp950') as fObj: 
    while True:
        txt = fObj.read(chunk)  # 一次讀取chunk數量
        if not txt:
            break
        msg += txt
print(msg)

print('------------------------------------------------------------')	#60個

print('複製binary檔案')

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'picture1_copied.jpg'

tmp = ''

with open(filename1, 'rb') as file_rd:
    tmp = file_rd.read()
    with open(filename2, 'wb') as file_wr:
        file_wr.write(tmp)

print('------------------------------------------------------------')	#60個

dst = 'random_data.bin'
bytedata = bytes(range(0,256))
with open(dst, 'wb') as file_dst:
    file_dst.write(bytedata)

print('------------------------------------------------------------')	#60個

src = 'random_data.bin'

with open(src, 'rb') as file_src:
    print("目前位移 : ", file_src.tell())
    file_src.seek(10)
    print("目前位移 : ", file_src.tell())
    data = file_src.read()
    print("目前內容 : ", data[0])
    file_src.seek(255)
    print("目前位移 : ", file_src.tell())
    data = file_src.read()
    print("目前內容 : ", data[0])

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





