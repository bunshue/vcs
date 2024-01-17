# ch14_1.py
import os

print(os.getcwd())              # 列出目前工作目錄




#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_10.py

# ch14_10.py
fn = 'data14_10.txt'    # 設定欲開啟的檔案
fObj = open(fn, 'r', encoding='cp950')    
data = fObj.read()      # 讀取檔案到變數data
fObj.close()            # 關閉檔案物件
print(data)             # 輸出變數data相當於輸出檔案





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_11.py

# ch14_11.py
fn = 'data14_10.txt'        # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    data = fObj.read()      # 讀取檔案到變數data
print(data)                 # 輸出變數data





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_12.py

# ch14_12.py
fn = 'data14_10.txt'        # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    for line in fObj:       # 相當於逐列讀取
        print(line)         # 輸出line








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_13.py

# ch14_13.py
fn = 'data14_10.txt'            # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    for line in fObj:           # 相當於逐列讀取
        print(line.rstrip())    # 輸出line








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_14.py

# ch14_14.py
fn = 'data14_10.txt'        # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    txt1 = fObj.readline()
    print(txt1)             # 輸出txt1
    txt2 = fObj.readline()
    print(txt2)             # 輸出txt2








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_15.py

# ch14_15.py
fn = 'data14_15.txt'         # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    mylist = fObj.readlines()
print(mylist)   






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_16.py

# ch14_16.py
fn = 'data14_15.txt'        # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:    
    mylist = fObj.readlines()

for line in mylist:
    print(line)             # 列印串列






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_17.py

# ch14_17.py
fn = 'data14_17.txt'         # 設定欲開啟的檔案
with open(fn, 'r', encoding='cp950') as fObj:
    print(f"指針位置 {fObj.tell()}")    
    txt1 = fObj.read(3)
    print(f"{txt1}, 指針位置 {fObj.tell()}")
    txt2 = fObj.read(3)
    print(f"{txt2}, 指針位置 {fObj.tell()}")
    txt3 = fObj.read(3)
    print(f"{txt3}, 指針位置 {fObj.tell()}")  






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_18.py

# ch14_18.py
fn = 'data14_18.txt'            # 設定欲開啟的檔案
chunk = 100
msg = ''
with open(fn, 'r', encoding='utf-8') as fObj: 
    while True:
        txt = fObj.read(chunk)  # 一次讀取chunk數量
        if not txt:
            break
        msg += txt
print(msg)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_19.py

# ch14_19.py
fn = 'out14_19.txt'
string = 'I love Python.'

with open(fn, 'w', encoding='cp950') as fObj:
    print(fObj.write(string))








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_2.py

# ch14_2.py
import os

print(os.listdir("D:\\Python\\ch14"))
print(os.listdir("."))      # 這代表目前工作目錄





      





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_20.py

# ch14_20.py
fn = 'out14_20.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(x)       # 直接寫入數值x產生錯誤








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_20_1.py

# ch14_20_1.py
fn = 'out14_20_1.txt'
x = 100

with open(fn, 'w') as file_Obj:
    file_Obj.write(str(x))      # 使用str(x)輸出


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_21.py

# ch14_21.py
fn = 'out14_21.txt'
str1 = 'I love Python.'
str2 = '洪錦魁著'

with open(fn, 'w', encoding='cp950') as fObj:
    fObj.write(str1)
    fObj.write(str2)








print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_21_1.py

# ch14_21_1.py
fn = 'out14_21_1.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(fn, 'a') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_22.py

# ch14_22.py
zenofPython = '''Beautiful is better than ugly.
Explicit is better than implicits.
Simple is better than complex.
Flat is better than nested.
Sparse is better than desse.
Readability counts.
Special cases aren't special enough to break the rules.
...
...
By Tim Peters'''

fn = 'out14_22.txt'
size = len(zenofPython)
offset = 0
chunk = 100                         # 每次寫入的單位
with open(fn, 'w', encoding='cp950') as fObj:
    while True:
        if offset > size:
            break
        print(fObj.write(zenofPython[offset:offset+chunk]))
        offset += chunk





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_23.py

# ch14_23.py
fn = 'out14_23.txt'
mystr = ['相見時難別亦難\n', '東風無力百花殘\n', '春蠶到死絲方盡']

with open(fn, 'w', encoding='cp950') as fObj:
    fObj.writelines(mystr)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_24.py

# ch14_24.py
src = 'hung.jpg'
dst = 'hung1.jpg'
tmp = ''

with open(src, 'rb') as file_rd:
    tmp = file_rd.read()
    with open(dst, 'wb') as file_wr:
        file_wr.write(tmp)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_25.py

# ch14_25.py
dst = 'bdata'
bytedata = bytes(range(0,256))
with open(dst, 'wb') as file_dst:
    file_dst.write(bytedata)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_26.py

# ch14_26.py
src = 'bdata'

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
    









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_27.py

# ch14_27.py
import shutil

shutil.rmtree('dir27')  




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_28.py

# ch14_28.py
import send2trash

send2trash.send2trash('data14_28.txt')  




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_29.py

# ch14_29.py
import zipfile
import glob, os

fileZip = zipfile.ZipFile('out29.zip', 'w')
for name in glob.glob('zipdir29/*'):        # 遍歷zipdir29目錄
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
fileZip.close()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_3.py

# ch14_3.py
import os

for dirName, sub_dirNames, fileNames in os.walk('oswalk'):
    print("目前工作目錄名稱:   ", dirName)
    print("目前子目錄名稱串列: ", sub_dirNames)
    print("目前檔案名稱串列:   ", fileNames, "\n")
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_30.py

# ch14_30.py
import zipfile

listZipInfo = zipfile.ZipFile('out29.zip', 'r')
print(listZipInfo.namelist())       # 以列表列出所有壓縮檔案
print("\n")
for info in listZipInfo.infolist():
    print(info.filename, info.file_size, info.compress_size)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_31.py

# ch14_31.py
import zipfile

fileUnZip = zipfile.ZipFile('out29.zip')
fileUnZip.extractall('out31')
fileUnZip.close()




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_32.py

# ch14_32.py

fn = 'data14_32.txt'                    # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='cp950')  # 預設encoding='cp950'開檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_33.py

# ch14_33.py

fn = 'data14_33.txt'                    # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='cp950')  # 預設encoding='cp950'開檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_34.py

# ch14_34.py

fn = 'data14_33.txt'                    # 設定欲開啟的檔案
file_Obj =  open(fn, encoding='utf-8')  # 預設encoding='utf-8'開檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_35.py

# ch14_35.py

fn = 'data14_35.txt'                            # 設定欲開啟的檔案
with open(fn, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一列

print(obj_list)                                 # 列印串列






    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_36.py

# ch14_36.py

fn = 'data14_35.txt'                             # 欲開啟的檔案
with open(fn, encoding='utf-8-sig') as file_Obj: # utf-8-sig
    obj_list = file_Obj.readlines()              # 每次讀一列

print(obj_list)                                  # 列印串列






    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_37.py

# ch14_37.py

fn = 'data14_37.txt'                            # 設定欲開啟的檔案
with open(fn, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一列

print(obj_list)                                 # 列印串列






    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_39.py

# ch14_39.py
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

fn = "data14_39.txt"
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









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_4.py

# ch14_4.py
import os

print(os.path.abspath('.'))             # 列出目前目錄的絕對路徑
print(os.path.abspath('..'))            # 列出上一層目錄的絕對路徑
print(os.path.abspath('ch14_4.py'))     # 列出檔案的絕對路徑







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_40.py

# ch14_40.py
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









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_41.py

# ch14_41.py
with open('backup.csv', 'w') as file:
    for data in database_data:
        file.write(','.join(data) + '\n')




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_42.py

# ch14_42.py
with open('app.log', 'a') as log_file:
    log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - 工作項目 1\n')



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_43.py

# ch14_43.py
import shutil
import glob
import time

log_files = glob.glob('/path/to/logs/*.log')
backup_path = '/path/to/backup/'

for log_file in log_files:
    shutil.copy(log_file, backup_path + time.strftime("%Y%m%d_%H%M%S_") + log_file.split('/')[-1])



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_5.py

# ch14_5.py
import os

print(os.path.relpath('D:\\'))              # 目前目錄至D:\的相對路徑
print(os.path.relpath('D:\\Python\\ch13'))  # 目前目錄至特定path的相對路徑
print(os.path.relpath('D:\\', 'ch14_5.py')) # 目前檔案至D:\的相對路徑







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_6.py

# ch14_6.py
import os

mydir = 'test'
# 如果mydir不存在就建立此資料夾
if os.path.exists(mydir):
    print(f"{mydir} 已經存在")
else:
    os.mkdir(mydir)
    print(f"建立 {mydir} 資料夾成功")









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_7.py

# ch14_7.py
import os

mydir = 'test'
# 如果mydir存在就刪除此資料夾
if os.path.exists(mydir):
    os.rmdir(mydir)
    print(f"刪除 {mydir} 資料夾成功")
else:
    print(f"{mydir} 資料夾不存在")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_8.py

# ch14_8.py
import os

print(os.path.join('D:\\','Python','ch14','ch14_8.py')) # 4個參數
print(os.path.join('D:\\Python','ch14','ch14_8.py'))    # 3個參數
print(os.path.join('D:\\Python\\ch14','ch14_8.py'))     # 2個參數





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all03\ch14_9.py

# ch14_9.py
import os
import glob

print("方法1:列出\\Python\\ch14工作目錄的所有檔案與大小")
for file in glob.glob('D:\\Python\\ch14\\*.*'):
    print(f"{file} : {os.path.getsize(file)} bytes")
    
print("方法2:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_1*.py'):
    print(file)
    
print("方法3:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_2*.*'):
    print(file)




      





print("------------------------------------------------------------")  # 60個

