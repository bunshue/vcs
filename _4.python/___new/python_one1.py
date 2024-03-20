"""
一本精通 - Python 範例應用大全
"""

import os
import sys
import time
import random

# 有順序

print("------------------------------------------------------------")  # 60個
print("Python 常用標準函式庫")
print("------------------------------------------------------------")  # 60個

from concurrent.futures import ThreadPoolExecutor

a = True  # 定義 a 為 True


def run():
    global a  # 定義 a 是全域變數
    while a:  # 如果 a 為 True
        print(123)  # 不斷顯示 123
        time.sleep(1)  # 每隔一秒


def keyin():
    global a  # 定義 a 是全域變數
    if input() == "a":
        a = False  # 如果輸入的是 a，就讓 a 為 False，停止 run 函式中的迴圈


executor = ThreadPoolExecutor()
e1 = executor.submit(run)
e2 = executor.submit(keyin)
executor.shutdown()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Python 基礎範例")
print("------------------------------------------------------------")  # 60個

import re

# 要轉換的字串
text = """請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
"""

# 取得中文字和英文單字的正規表達式
# [a-zA-Z0-9]+ 表示開頭是英文字母後面連接一串字母或數字
regex = re.compile(r"[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+")

# 根據正規表達式，將每個中文字、標點符號和英文單字變成串列
arr = re.findall(regex, text)

# 使用空格合併串列
text = " ".join(arr)
print(text)

"""
請 求 您 幫 我 oxxo . studio 去 除 空 白 ok ？
但 是 要 保 留 換 行 可 以 嗎 ， ( 哈 哈 哈 ) ( 啊 哈 )
統 一 便 利 超 商 ( 711 ) 的 括 號 之 間 也 要 有 空 白 喔 ！
寫 作 規 範 就 是 這 麼 100 % 的 龜 毛 ～
"""


print("------------------------------------------------------------")  # 60個


import re

# 輸入字符串
text = """請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
"""

regex = re.compile(r"[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+")
arr = re.findall(regex, text)
text = " ".join(arr)

regex = re.compile(r"(?<=[^a-zA-Z0-9\u0021-\u002E])(\x20)(?=[^a-zA-Z0-9\u0021-\u002E])")
text = re.sub(regex, "", text)

regex = re.compile(r"(\x20)(?=[\(\%\uFF00-\uFFFF])")
text = re.sub(regex, "", text)

text = text.replace(" . ", ".")
print(text)

print("------------------------------------------------------------")  # 60個

n = 100
icon = "⋮⋰⋯⋱"  # 建立旋轉的符號清單
for i in range(n + 1):
    print(f"\r{icon[i%4]} {i*100/n}%", end="")
    time.sleep(0.1)

print("------------------------------------------------------------")  # 60個

a = 15  # 新增變數 a，設定金字塔有幾層
b = a * 2 + 1  # 新增變數 b，計算底部有幾個星星
for i in range(1, b, 2):  # 使用 for 迴圈，從 1～b，每隔 2 個一數
    move = round((b - i) / 2) - 1  # 計算星星的位移空白 ( 要將星星都置中 )
    print(f" " * move, end="")  # 印出星星前方的位移空白 ( 不換行 )
    print("*" * i)  # 加上「幾個星星」( 乘以 i )


print("------------------------------------------------------------")  # 60個

a = 15
b = a * 2 + 1
for i in range(1, b, 4):  # 改成 4 個一數，金字塔每一層就會增加 2，高度也會減半
    move = round((b - i) / 2) - 1
    print(f" " * move, end="")
    print("*" * i)


print("------------------------------------------------------------")  # 60個

a = 15  # 新增變數 a，設定金字塔有幾層
for i in range(1, a + 1):  # 使用 for 迴圈，重複指定的層數
    print(" " * (a - i) + "*" * (2 * i - 1))
    # ' ' * (a-i) 表示星星數越少，前面空白越多
    # '*' * (2*i-1) 串接後方星星的數量


print("------------------------------------------------------------")  # 60個

a = 10  # 要產生的金字塔層數
for i in range(1, a + 1):  # 使用 for 迴圈，重複 1～10 ( a+1 ) 的數字
    print(" " * 3 * (a - i), end="")  # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    for j in range(1, i + 1):  # 第二層 for 迴圈，重複不同層內的數字
        if j == 1:  # 如果是第一個數字
            print(j, end="")  # 單純印出數字即可 ( 後方不換行 )
        else:  # 如果是第二個以後的數字
            print(f"{j:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    for j in range(i - 1, 0, -1):  # 剛剛的 for 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f"{j:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
    print("")  # 最後執行換行的 print


print("------------------------------------------------------------")  # 60個

a = 10
for i in range(1, a + 1):
    print(" " * 3 * (a - i), end="")
    for j in range(0, i):  # ragne 改成從 0 開始，因為 2 的 0 次方等於 1
        k = 2**j  # 計算 2 的幾次方
        if k == 1:
            print(k, end="")
        else:
            print(f"{k:>3d}", end="")
    for j in range(i - 2, -1, -1):  # 修改 range，使其最後一位數為 0
        k = 2**j  # 計算 2 的幾次方
        print(f"{k:>3d}", end="")
    print("")


print("------------------------------------------------------------")  # 60個


a = 10  # 要產生的金字塔層數
b = 1  # 提供 while 迴圈停止的依據
while b <= a:  # 如果 b <= a 就讓 while 迴圈繼續
    n = 1  # 設定從 1 開始
    print(" " * 3 * (a - b), end="")  # 根據不同的層數，讓第一個數字前方增加指定的空白字元 ( 後方不換行 )
    while n <= b:  # 第二層 while 迴圈，如果 n <= b 就讓 while 迴圈繼續
        if n == 1:  # 如果是第一個數字
            print(n, end="")  # 單純印出數字即可 ( 後方不換行 )
        else:  # 如果是第二個以後的數字
            print(f"{n:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n + 1  # 將 n 增加 1
    while n > 2:  # 剛剛的 while 迴圈是由小到大，加入另外一個由大到小的迴圈
        print(f"{n-2:>3d}", end="")  # 格式化數字，使其寬度為 3，並靠右對齊 ( 後方不換行 )
        n = n - 1  # 將 n 減少 1
    print("")  # 最後執行換行的 print
    b = b + 1  # 將 b 增加 1

print("------------------------------------------------------------")  # 60個

local_table = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 34,
    "J": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "O": 35,
    "P": 23,
    "Q": 24,
    "R": 25,
    "S": 26,
    "T": 27,
    "U": 28,
    "V": 29,
    "W": 32,
    "X": 30,
    "Y": 31,
    "Z": 33,
}
id_number = input("輸入身分證字號：")
check = False  # 新增 check=False 變數，與 while 迴圈搭配
while True:  # 使用 while 迴圈
    id_arr = list(id_number)  # 新增 id_arr 變數，將身分證字號轉換成串列存入
    if len(id_arr) != 10:
        break  # 判斷如果 id_arr 長度不等於 10，就跳出 while 迴圈
    local = str(local_table[id_arr[0]])  # 將對應的二位數字轉換成字串
    check_arr = list(local)  # 將字串轉換成陣列，例如 '10' 會轉換成 ['1','0']
    check_arr[0] = int(check_arr[0])  # 將串列中的第一個項目轉換成數字
    check_arr[1] = int(check_arr[1]) * 9  # 將串列中的第二個項目轉換成數字
    sex = id_arr[1]  # 取得第二碼數字
    if sex != "1" and sex != "2":
        break  # 判斷如果不是 '1' 也不是 '2' 就跳出 while 迴圈
    check_arr.append(int(sex) * 8)  # 將 sex 內容轉換成數字並乘以 8，存入 check_arr 裡
    for i in range(7):  # 使用 for 迴圈，重複七次
        check_arr.append(int(id_arr[i + 2]) * (7 - i))  # 每次重複，按照檢查碼程式，將數字乘以對應的數值
    check_num = 10 - sum(check_arr) % 10  # 計算使用者輸入的檢查碼
    if check_num != int(id_arr[9]):
        break  # 如果檢查碼不相同，跳出 while 迴圈
    check = True  # 如果迴圈都沒有跳出，讓 check 等於 True。
    break  # 結束後跳出迴圈

if check == False:  # while 迴圈結束後，如果 check 等於 Fasle，表示身分證字號錯誤
    print("身分證字號格式錯誤")
else:
    print("身分證字號正確")


print("------------------------------------------------------------")  # 60個


local_table = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 34,
    "J": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "O": 35,
    "P": 23,
    "Q": 24,
    "R": 25,
    "S": 26,
    "T": 27,
    "U": 28,
    "V": 29,
    "W": 32,
    "X": 30,
    "Y": 31,
    "Z": 33,
}
while True:  # 新增 while 迴圈，就可以重複輸入
    id_number = input("輸入身分證字號：")
    check = False
    while True:
        try:  # 使用 try
            id_arr = list(id_number)
            if len(id_arr) != 10:
                break
            local = str(local_table[id_arr[0]])
            check_arr = list(local)
            check_arr[0] = int(check_arr[0])
            check_arr[1] = int(check_arr[1]) * 9
            sex = id_arr[1]
            if sex != "1" and sex != "2":
                break
            check_arr.append(int(sex) * 8)
            for i in range(7):
                check_arr.append(int(id_arr[i + 2]) * (7 - i))
            check_num = 10 - sum(check_arr) % 10
            if check_num != int(id_arr[9]):
                break
            check = True
            break
        except:  # 使用 except，如果發生例外狀況，跳出迴圈
            break

    if check == False:
        print("身分證字號格式錯誤")
    else:
        print("身分證字號正確")


print("------------------------------------------------------------")  # 60個

table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}  # 轉換對照表
roman = [i for i in input()]  # 將輸入的羅馬數字變成串列
r = roman[::-1]  # 反轉串列
output = table[r[0]]  # 讓 output 先等於第一個數字
for i in range(1, len(r)):  # 從第二個數字開始依序取到最後一個數字
    if table[r[i]] < table[r[i - 1]]:  # 如果後面數字比較小
        output = output - table[r[i]]  # 讓 output 減去後面的數字
    else:
        output = output + table[r[i]]  # 如果後面數字比較大，讓 output 加上後面的數字
print(output)

# 輸入 IVMVIIMVVMVM 就會得到 3994

print("------------------------------------------------------------")  # 60個


num_table = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"],
]  # 建立對照表
num = int(input())  # 將輸入的文字轉換成數字
output = ""  # 設定輸出的 output 字串
for i in num_table:  # 依序判斷對照表中每個數字
    a = divmod(num, i[0])  # 取得商 ( a[0] ) 和餘數 ( a[1] )
    if a[0] != 0:  # 如果 a[0] 不為 0
        num = a[1]  # 取得餘數繼續往下除
        output = output + i[1] * a[0]  # 組合字串
print(output)

print("------------------------------------------------------------")  # 60個
print("Python 實際應用")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import glob
import os

images = glob.glob("./demo/*")
print(images)

n = 1  # 設定名稱從 1 開始
for i in images:
    #偽執行
    #os.rename(i, f"./demo/img-{n:03d}.jpg")  # 改名時，使用字串格式化的方式進行三位數補零
    n = n + 1  # 每次重複時將 n 增加 1


print("------------------------------------------------------------")  # 60個

from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
screen = QtWidgets.QApplication.desktop()
width = screen.width()
height = screen.height()
print(width, height)


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


