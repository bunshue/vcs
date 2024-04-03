import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

fn = 'data2/ch14_20.txt'              # 設定欲開啟的檔案
with open(fn) as file_Obj:      # 傳回檔案物件file_Obj
    data = file_Obj.read()      # 讀取檔案到變數data
    new_data = data.replace('工專', '科大') # 新變數儲存
    print(new_data.rstrip())    # 輸出檔案

print("------------------------------------------------------------")  # 60個

fn = 'data2/sse.txt'              # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

str_Obj = ''                # 先設為空字串
for line in obj_list:       # 將各行字串存入
    str_Obj += line.rstrip()

print("欲搜尋字串")
findstr = "aaaa"
if findstr in str_Obj:      # 搜尋檔案是否有欲尋找字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, fn))
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, fn))

print("------------------------------------------------------------")  # 60個

fn = 'data2/sse.txt'              # 設定欲開啟的檔案

with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

str_Obj = ''                # 先設為空字串
for line in obj_list:       # 將各行字串存入
    str_Obj += line.rstrip()

print("欲搜尋字串")
findstr = "aaaa"
index = str_Obj.find(findstr)     # 搜尋findstr字串是否存在
if  index >= 0:             # 搜尋檔案是否有欲尋找字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, fn))
    print("在索引 %s 位置出現" % index)
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, fn))

print("------------------------------------------------------------")  # 60個

fn = 'tmp_text01.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(str1)
    file_Obj.write(str2)

print("------------------------------------------------------------")  # 60個

fn = 'tmp_text02.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')

print("------------------------------------------------------------")  # 60個

fn = 'tmp_text03.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'a') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')

print("------------------------------------------------------------")  # 60個

""" no file
fn = 'data2/ansi14_44.txt'                    # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案
"""

print("------------------------------------------------------------")  # 60個

"""
fn = 'data2/utf14_45.txt'                     # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案
"""
print("------------------------------------------------------------")  # 60個

fn = 'data2/utf14_45.txt'                     # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案

print("------------------------------------------------------------")  # 60個

fn = 'data2/utf14_45.txt'                             # 設定欲開啟的檔案
with open(fn, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一行

print(obj_list)                                 # 列印串列

print("------------------------------------------------------------")  # 60個

filename = 'data2/data14_8.txt'         # 設定欲開啟的檔案

with open(filename, 'r', encoding='cp950') as fObj:
    print(f"指針位置 {fObj.tell()}")    
    txt1 = fObj.read(3)
    print(f"{txt1}, 指針位置 {fObj.tell()}")
    txt2 = fObj.read(3)
    print(f"{txt2}, 指針位置 {fObj.tell()}")
    txt3 = fObj.read(3)
    print(f"{txt3}, 指針位置 {fObj.tell()}")     

print('------------------------------------------------------------')	#60個

filename = 'data2/data14_9.txt'             # 設定欲開啟的檔案

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

print('寫入檔案')
fp = open("tmp_text06.txt", "w") 
print("用print的方法寫入檔案", file=fp)
fp.close( )

print('------------------------------------------------------------')	#60個

print('寫入檔案')
filename = 'tmp_text07.txt'
str1 = '寫入檔案字串1'
str2 = '寫入檔案字串2'

#with open(filename, 'w') as fp:    #覆寫模式
with open(filename, 'a') as fp:     #附加模式
    fp.write(str1 + '\n')
    fp.write(str2 + '\n')

print('------------------------------------------------------------')	#60個

print('讀取檔案, 一次讀一檔')
filename = 'data2/data14_2.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    data = fp.read()  # 讀取檔案到變數data
    print(data)             # 輸出變數data相當於輸出檔案

print('------------------------------------------------------------')	#60個

print('讀取檔案, 一次讀一行')
filename = 'data2/data14_2.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    for line in fp:   # 逐行讀取檔案到變數line
        print(line)         # 輸出變數line相當於輸出一行

print('------------------------------------------------------------')	#60個

print('讀取檔案, 一次讀一檔, 讀成串列')
filename = 'data2/data14_7.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    obj_list = fp.readlines()  # 每次讀一行

print(len(obj_list))
print(obj_list)             # 列印串列

for line in obj_list:
    print(line.rstrip())    # 列印串列



print("------------------------------------------------------------")  # 60個




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
        if wd in dict:
            dict[wd] += 1
        else:
            dict[wd] = 1

fn = "data2/ch14_51.txt"
with open(fn) as file_Obj:          # 開啟歌曲檔案
    data = file_Obj.read()          # 讀取歌曲檔案
    print("以下是所讀取的歌曲")
    print(data)                     # 列印歌曲檔案

dict = {}                           # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
print(dict)                         # 列印字典

print("------------------------------------------------------------")  # 60個

def passWord(pwd):
    #檢查密碼長度必須是5到8個字元
    pwdlen = len(pwd)                       # 密碼長度
    if pwdlen < 5:                          # 密碼長度不足            
        raise Exception('密碼長度不足')
    if pwdlen > 8:                          # 密碼長度太長
        raise Exception('密碼長度太長')
    print('密碼長度正確')

for pwd in ('aaabbbccc', 'aaa', 'aaabbb'):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        print("密碼長度檢查異常發生: ", str(err))

print("------------------------------------------------------------")  # 60個

#filename = 'C:/_git/vcs/_1.data/______test_files1/poetrya.txt'

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

filename = "data2/data14_17.txt"
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

def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    global mydict
    songList = songCount.split()    # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    mydict = {wd:songList.count(wd) for wd in set(songList)}

filename = "data2/AreYouSleeping.txt"
with open(filename) as file_Obj:          # 開啟歌曲檔案
    data = file_Obj.read()          # 讀取歌曲檔案
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


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個
