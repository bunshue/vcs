'''
檔案讀寫

'''
import sys

print('------------------------------------------------------------')	#60個

print('寫入檔案')
fp = open("out14_1.txt", "w") 
print("用print的方法寫入檔案", file=fp)
fp.close( )

print('------------------------------------------------------------')	#60個

print('寫入檔案')
filename = 'out14_10.txt'
str1 = '寫入檔案字串1'
str2 = '寫入檔案字串2'

with open(filename, 'w') as fp:
    fp.write(str1)
    fp.write(str2)

print('------------------------------------------------------------')	#60個

print('寫入檔案')
filename = 'out14_11.txt'
str1 = '寫入檔案字串1'
str2 = '寫入檔案字串2'

with open(filename, 'w') as fp:
    fp.write(str1 + '\n')
    fp.write(str2 + '\n')

print('------------------------------------------------------------')	#60個

print('寫入檔案')
filename = 'out14_12.txt'
str1 = '寫入檔案字串1'
str2 = '寫入檔案字串2'

with open(filename, 'a') as fp:
    fp.write(str1 + '\n')
    fp.write(str2 + '\n')

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

print('讀取檔案')
filename = 'data14_2.txt'         # 設定欲開啟的檔案
fp =  open(filename)        # 用預設mode=r開啟檔案,傳回檔案物件fp
data = fp.read()      # 讀取檔案到變數data
fp.close()            # 關閉檔案物件
print(data)                 # 輸出變數data相當於輸出檔案

print('------------------------------------------------------------')	#60個

print('讀取檔案')
filename = 'data14_2.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    data = fp.read()  # 讀取檔案到變數data
    print(data)             # 輸出變數data相當於輸出檔案

print('------------------------------------------------------------')	#60個

print('讀取檔案')
filename = 'data14_2.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    data = fp.read()  # 讀取檔案到變數data
    print(data.rstrip())    # 輸出變數data相當於輸出檔案,同時刪除末端字元

print('------------------------------------------------------------')	#60個

print('讀取檔案')
filename = 'data14_2.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    for line in fp:   # 逐行讀取檔案到變數line
        print(line)         # 輸出變數line相當於輸出一行

print('------------------------------------------------------------')	#60個

print('讀取檔案')
filename = 'data14_2.txt'          # 設定欲開啟的檔案
with open(filename) as fp:   # 用預設mode=r開啟檔案,傳回檔案物件fp
    for line in fp:    # 逐行讀取檔案到變數line
        print(line.rstrip()) # 輸出變數line相當於輸出一行,同時刪除末端字元

print('------------------------------------------------------------')	#60個

print('讀取檔案')
filename = 'data14_7.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    obj_list = fp.readlines()  # 每次讀一行

print(obj_list)             # 列印串列

print('------------------------------------------------------------')	#60個

print('讀取檔案')
filename = 'data14_7.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    obj_list = fp.readlines()  # 每次讀一行

for line in obj_list:
    print(line.rstrip())    # 列印串列

print('------------------------------------------------------------')	#60個

def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    songList = songCount.split()    # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    for wd in songList:
        if wd in mydict:
            mydict[wd] += 1
        else:
            mydict[wd] = 1

filename = "data14_17.txt"
with open(filename) as fp:          # 開啟歌曲檔案
    data = fp.read()          # 讀取歌曲檔案
    print("以下是所讀取的歌曲")
    print(data)                     # 列印歌曲檔案

mydict = {}                         # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)                       # 列印字典

print('------------------------------------------------------------')	#60個

import string

def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串
    
abc = string.printable[:-3]             # 取消不可列印字元
subText = abc[-3:] + abc[:-3]           # 加密字串字串
encry_dict = dict(zip(subText, abc))    # 建立字典

filename = "zenofPython.txt"
with open(filename) as fp:              # 開啟檔案
    msg = fp.read()               # 讀取檔案
    
ciphertext = encrypt(msg, encry_dict)

print("原始字串")
print(msg)
print("加密字串")
print(ciphertext)

print('------------------------------------------------------------')	#60個
