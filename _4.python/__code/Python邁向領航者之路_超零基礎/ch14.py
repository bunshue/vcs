

print('------------------------------------------------------------')	#60個


# ch14_1.py
fobj = open("out14_1.txt", "w") 
print("明志科技大學", file=fobj)
fobj.close( )


print('------------------------------------------------------------')	#60個




#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_2.py

# ch14_2.py

fn = 'data14_2.txt'         # 設定欲開啟的檔案
file_Obj =  open(fn)        # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
data = file_Obj.read()      # 讀取檔案到變數data
file_Obj.close()            # 關閉檔案物件
print(data)                 # 輸出變數data相當於輸出檔案




    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_3.py

# ch14_3.py

fn = 'data14_2.txt'         # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    data = file_Obj.read()  # 讀取檔案到變數data
    print(data)             # 輸出變數data相當於輸出檔案




    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_4.py

# ch14_4.py

fn = 'data14_2.txt'         # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    data = file_Obj.read()  # 讀取檔案到變數data
    print(data.rstrip())    # 輸出變數data相當於輸出檔案,同時刪除末端字元




    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_5.py

# ch14_5.py

fn = 'data14_2.txt'         # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    for line in file_Obj:   # 逐行讀取檔案到變數line
        print(line)         # 輸出變數line相當於輸出一行






    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_6.py

# ch14_6.py

fn = 'data14_2.txt'          # 設定欲開啟的檔案
with open(fn) as file_Obj:   # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    for line in file_Obj:    # 逐行讀取檔案到變數line
        print(line.rstrip()) # 輸出變數line相當於輸出一行,同時刪除末端字元






    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_7.py

# ch14_7.py

fn = 'data14_7.txt'         # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

print(obj_list)             # 列印串列






    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_8.py

# ch14_8.py

fn = 'data14_7.txt'         # 設定欲開啟的檔案
with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

for line in obj_list:
    print(line.rstrip())    # 列印串列






    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_9.py

# ch14_9.py
fn = 'out14_9.txt'
string = 'I love Python.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(string)


print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_10.py

# ch14_10.py
fn = 'out14_10.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(str1)
    file_Obj.write(str2)




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_11.py

# ch14_11.py
fn = 'out14_11.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'w') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_12.py

# ch14_12.py
fn = 'out14_12.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'a') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_13.py

# ch14_13.py
import locale

print(locale.getpreferredencoding())






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_14.py

# ch14_14.py

fn = 'data14_14.txt'                    # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案




    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_15.py

# ch14_15.py

fn = 'utf14_15.txt'                     # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案




    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_16.py

# ch14_16.py

fn = 'utf14_15.txt'                     # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案




    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_17.py

# ch14_17.py
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

fn = "data14_17.txt"
with open(fn) as file_Obj:          # 開啟歌曲檔案
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

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch14\ch14_18.py

# ch14_18.py
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

fn = "zenofPython.txt"
with open(fn) as file_Obj:              # 開啟檔案
    msg = file_Obj.read()               # 讀取檔案
    
ciphertext = encrypt(msg, encry_dict)

print("原始字串")
print(msg)
print("加密字串")
print(ciphertext)


print('------------------------------------------------------------')	#60個
