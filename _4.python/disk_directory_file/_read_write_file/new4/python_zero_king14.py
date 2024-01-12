import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

print("檔案或資料夾存在 = ", os.path.exists('ch14'))
print("檔案或資料夾存在 = ", os.path.exists('D:\\Python\\ch14'))
print("檔案或資料夾存在 = ", os.path.exists('ch14_4.py'))
print(" --- ")

print("是絕對路徑 = ", os.path.isabs('ch14_4.py'))
print("是絕對路徑 = ", os.path.isabs('D:\\Python\\ch14\\ch14_4.py'))
print(" --- ")

print("是資料夾 = ", os.path.isdir('D:\\Python\\ch14\\ch14_4.py'))
print("是資料夾 = ", os.path.isdir('D:\\Python\\ch14'))
print(" --- ")

print("是檔案 = ", os.path.isfile('D:\\Python\\ch14\\ch14_4.py'))
print("是檔案 = ", os.path.isfile('D:\\Python\\ch14'))

print("------------------------------------------------------------")  # 60個

newdir = 'D:\\Python'

currentdir = os.getcwd()
print("列出目前工作資料夾 ", currentdir)

# 如果newdir不存在就建立此資料夾
if os.path.exists(newdir):
    print("已經存在 %s " % newdir)
else:
    os.mkdir(newdir)
    print("建立 %s 資料夾成功" % newdir)

# 將目前工作資料夾改至newdir
os.chdir(newdir)
print("列出最新工作資料夾 ", os.getcwd())

# 將目前工作資料夾返回
os.chdir(currentdir)
print("列出返回工作資料夾 ", currentdir)

print("------------------------------------------------------------")  # 60個

files = ['ch14_1.py', 'ch14_2.py', 'ch14_3.py']
for file in files:
    print(os.path.join('D:\\Python\\ch14', file))   

print("------------------------------------------------------------")  # 60個

# 如果檔案在目前工作目錄下可以省略路徑
print(os.path.getsize("ch14_1.py"))
print(os.path.getsize("D:\\Python\\ch14\\ch14_1.py"))

print("------------------------------------------------------------")  # 60個

print(os.listdir("D:\\Python\\ch14"))
print(os.listdir("."))                  # 這代表目前工作目錄

print("------------------------------------------------------------")  # 60個

totalsizes = 0
print("列出D:\\Python\\ch14工作目錄的所有檔案")
for file in os.listdir('D:\\Python\\ch14'):
    print(file)
    totalsizes += os.path.getsize(os.path.join('D:\\Python\\ch14', file))

print("全部檔案大小是 = ", totalsizes)
   
print("------------------------------------------------------------")  # 60個

import glob

print("方法1:列出\\Python\\ch14工作目錄的所有檔案")
for file in glob.glob('D:\\Python\\ch14\*.*'):
    print(file)
    
print("方法2:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_1*.py'):
    print(file)
    
print("方法3:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_2*.*'):
    print(file)

print("------------------------------------------------------------")  # 60個

for dirName, sub_dirNames, fileNames in os.walk('oswalk'):
    print("目前工作目錄名稱:   ", dirName)
    print("目前子目錄名稱串列: ", sub_dirNames)
    print("目前檔案名稱串列:   ", fileNames, "\n")
    
print("------------------------------------------------------------")  # 60個

#copy  拷貝放在一起以比較之

fn = 'ch14_20.txt'              # 設定欲開啟的檔案
with open(fn) as file_Obj:      # 傳回檔案物件file_Obj
    data = file_Obj.read()      # 讀取檔案到變數data
    new_data = data.replace('工專', '科大') # 新變數儲存
    print(new_data.rstrip())    # 輸出檔案

print("------------------------------------------------------------")  # 60個

fn = 'sse.txt'              # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

str_Obj = ''                # 先設為空字串
for line in obj_list:       # 將各行字串存入
    str_Obj += line.rstrip()

findstr = input("請輸入欲搜尋字串 = ")
if findstr in str_Obj:      # 搜尋檔案是否有欲尋找字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, fn))
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, fn))

print("------------------------------------------------------------")  # 60個

fn = 'sse.txt'              # 設定欲開啟的檔案

with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

str_Obj = ''                # 先設為空字串
for line in obj_list:       # 將各行字串存入
    str_Obj += line.rstrip()

findstr = input("請輸入欲搜尋字串 = ")
index = str_Obj.find(findstr)     # 搜尋findstr字串是否存在
if  index >= 0:             # 搜尋檔案是否有欲尋找字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, fn))
    print("在索引 %s 位置出現" % index)
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, fn))

print("------------------------------------------------------------")  # 60個

msg = '''CIA Mark told CIA Linda that the secret USB
had given to CIA Peter'''
print("CIA最後出現位置: ", msg.rfind("CIA",0,len(msg)))

print("------------------------------------------------------------")  # 60個

msg = '''CIA Mark told CIA Linda that the secret USB
had given to CIA Peter'''
print("CIA最後出現位置: ", msg.rfind("CIA"))

print("------------------------------------------------------------")  # 60個

fn = 'out14_26.txt'
string = 'I love Python.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(string)

print("------------------------------------------------------------")  # 60個

fn = 'out14_27.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(x)               # 直接輸出數值x產生錯誤

print("------------------------------------------------------------")  # 60個

fn = 'out14_28.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(str(x))      # 使用str(x)輸出

print("------------------------------------------------------------")  # 60個

fn = 'out14_29.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(str1)
    file_Obj.write(str2)

print("------------------------------------------------------------")  # 60個

fn = 'out14_30.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')

print("------------------------------------------------------------")  # 60個

fn = 'out14_31.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'a') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')

print("------------------------------------------------------------")  # 60個

fn = 'ansi14_44.txt'                    # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案
  
print("------------------------------------------------------------")  # 60個

fn = 'utf14_45.txt'                     # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案

print("------------------------------------------------------------")  # 60個

fn = 'utf14_45.txt'                     # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案

print("------------------------------------------------------------")  # 60個

fn = 'utf14_45.txt'                             # 設定欲開啟的檔案
with open(fn, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一行

print(obj_list)                                 # 列印串列

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

fn = "ch14_51.txt"
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
