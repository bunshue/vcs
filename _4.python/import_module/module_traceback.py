import sys
import traceback

print("------------------------------------------------------------")  # 60個

print("使用 traceback 將 Exception 寫入檔案")

import traceback

def passWord(pwd):
    #檢查密碼長度必須是5到8個字元
    pwdlen = len(pwd)                       # 密碼長度
    if pwdlen < 5:                          # 密碼長度不足            
        raise Exception("密碼長度不足")
    if pwdlen > 8:                          # 密碼長度太長
        raise Exception("密碼長度太長")
    print("密碼長度正確")

traceback_filename = "tmp_traceback1.txt"

for pwd in ("aaabbbccc", "aaa", "aaabbb"):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        errlog = open(traceback_filename, "a")   # 開啟錯誤檔案
        errlog.write(traceback.format_exc())   # 寫入錯誤檔案
        errlog.close()                         # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案 :", traceback_filename, "完成")
        print("密碼長度檢查異常發生: ", str(err))

print("------------------------------------------------------------")  # 60個

import traceback

traceback_filename = "tmp_traceback2.txt"

def division(x, y):
    try:  # try - except指令
        return x / y
    except:  # 捕捉所有異常
        errlog = open(traceback_filename, "a")  # 開啟錯誤檔案
        errlog.write(traceback.format_exc())  # 寫入錯誤檔案
        errlog.close()  # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案 :", traceback_filename, "完成")
        print("異常發生")


print(division(10, 2))  # 列出10/2
print(division(5, 0))  # 列出5/0
print(division("a", "b"))  # 列出'a' / 'b'
print(division(6, 3))  # 列出6/3

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個
