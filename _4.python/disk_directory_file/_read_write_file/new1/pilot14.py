'''
檔案讀寫

'''
import sys

print('------------------------------------------------------------')	#60個

print('寫入檔案')
fp = open("test_write1.txt", "w") 
print("用print的方法寫入檔案", file=fp)
fp.close( )

print('------------------------------------------------------------')	#60個

print('寫入檔案')
filename = 'test_write2.txt'
str1 = '寫入檔案字串1'
str2 = '寫入檔案字串2'

#with open(filename, 'w') as fp:    #覆寫模式
with open(filename, 'a') as fp:     #附加模式
    fp.write(str1 + '\n')
    fp.write(str2 + '\n')

print('------------------------------------------------------------')	#60個

print('讀取檔案, 一次讀一檔')
filename = 'data14_2.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    data = fp.read()  # 讀取檔案到變數data
    print(data)             # 輸出變數data相當於輸出檔案

print('------------------------------------------------------------')	#60個

print('讀取檔案, 一次讀一行')
filename = 'data14_2.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    for line in fp:   # 逐行讀取檔案到變數line
        print(line)         # 輸出變數line相當於輸出一行

print('------------------------------------------------------------')	#60個

print('讀取檔案, 一次讀一檔, 讀成串列')
filename = 'data14_7.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    obj_list = fp.readlines()  # 每次讀一行

print(len(obj_list))
print(obj_list)             # 列印串列

for line in obj_list:
    print(line.rstrip())    # 列印串列

print('------------------------------------------------------------')	#60個

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

