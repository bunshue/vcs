import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_6.py

fn = 'ch15_6.txt'               # 設定欲開啟的檔案

try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    wordList = data.split()     # 將文章轉成串列
    print(fn, " 文章的字數是 ", len(wordList))    # 列印文章字數


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_7.py

def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % fn)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(fn, " 文章的字數是 ", len(wordList))    # 列印文章字數



file = 'ch15_6.txt'                 # 設定欲開啟的檔案
wordsNum(file)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_8.py

def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % fn)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(fn, " 文章的字數是 ", len(wordList))    # 列印文章字數

files = ['data1.txt', 'data2.txt', 'data3.txt']       # 檔案串列
for file in files:
    wordsNum(file)




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_10.py

# ch15_10.py
def wordsNum(fn):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(fn) as file_Obj:  # 用預設"r"傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except Exception:
        print("Exception找不到 %s 檔案" % fn)
    else:
        wordList = data.split()     # 將文章轉成串列
        print(fn, " 文章的字數是 ", len(wordList))    # 列印文章字數

files = ['data1.txt', 'data2.txt', 'data3.txt']       # 檔案串列
for file in files:
    wordsNum(file)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_11.py

# ch15_11.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:   # 除數為0使用
        print("除數為0發生")
    except TypeError:           # 資料型別錯誤
        print("使用字元做除法運算異常")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_12.py

# ch15_12.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except (ZeroDivisionError, TypeError):   # 2個異常
        print("除數為0發生 或 使用字元做除法運算異常")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_13.py

# ch15_13.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except (ZeroDivisionError, TypeError) as e:   # 2個異常
        print(e)

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_14.py

# ch15_14.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except:                     # 捕捉所有異常
        print("異常發生")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_15.py

# ch15_15.py
def passWord(pwd):
    """檢查密碼長度必須是5到8個字元"""
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

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_16.py

# ch15_16.py
import traceback                            # 導入taceback

def passWord(pwd):
    """檢查密碼長度必須是5到8個字元"""
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
        errlog = open('errch15_16.txt', 'a')   # 開啟錯誤檔案
        errlog.write(traceback.format_exc())   # 寫入錯誤檔案
        errlog.close()                         # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案errch15_16.txt完成")
        print("密碼長度檢查異常發生: ", str(err))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_17.py

# ch15_17.py
import traceback

def division(x, y):
    try:                        # try - except指令
        return x / y
    except:                     # 捕捉所有異常
        errlog = open('errch15_17.txt', 'a')   # 開啟錯誤檔案
        errlog.write(traceback.format_exc())   # 寫入錯誤檔案
        errlog.close()                         # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案errch15_17.txt完成")
        print("異常發生")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch15\ch15_18.py

# ch15_18.py
def division(x, y):
    try:                             # try - except指令
        return x / y
    except:                          # 捕捉所有異常
        print("異常發生")
    finally:                         # 離開函數前先執行此程式碼
        print("階段任務完成")

print(division(10, 2),"\n")          # 列出10/2
print(division(5, 0),"\n")           # 列出5/0
print(division('a', 'b'),"\n")       # 列出'a' / 'b'
print(division(6, 3),"\n")           # 列出6/3






print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
