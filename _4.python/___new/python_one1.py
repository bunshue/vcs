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

print("------------------------------------------------------------")  # 60個


import time
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


while True:
    try:
        num = float(input("請輸入用電度數："))
        output = 0
        if num <= 200:
            output = num * 3.2
        elif num > 200 and num <= 300:
            output = 200 * 3.2 + (num - 200) * 3.4
        else:
            output = 200 * 3.2 + 100 * 3.4 + (num - 300) * 3.6
        print(f"用電 {num} 度共 {output} 元")
    except:
        break


print("------------------------------------------------------------")  # 60個

c = int(input("輸入 1 ( 公分 ) 或 2 ( 英吋 )："))
length = int(input("輸入長度數值："))

print("|cm   |m    |ich  |foot |yd   |")  # 印出說明
print("|-----|-----|-----|-----|-----|")  # 印出分隔線

if c == 1:
    print("|", end="")  # 印出表格左側的框線
    print(f"{str(length):<5.5s}", end="|")
    print(f"{str(length*0.01):<5.5s}", end="|")
    print(f"{str(length*0.394):<5.5s}", end="|")
    print(f"{str(length*0.03281):<5.5s}", end="|")
    print(f"{str(length*0.01094):<5.5s}", end="|")
else:
    print("|", end="")
    print(f"{str(length*2.54):<5.5s}", end="|")
    print(f"{str(length*0.0254):<5.5s}", end="|")
    print(f"{str(length):<5.5s}", end="|")
    print(f"{str(length/12):<5.5s}", end="|")
    print(f"{str(length/36):<5.5s}", end="|")


print("------------------------------------------------------------")  # 60個


year = int(input(">"))  # 使用變數 year 紀錄使用者輸入的年份
if year % 4 == 0:  # 如果除以 4 能整除
    if year % 100 == 0:  # 如果除以 100 能整除
        if year % 400 == 0:  # 如果除以 400 能整除，就是閏年
            print(f"{year} 是閏年")
        else:
            print(f"{year} 是平年")
    else:
        print(f"{year} 是閏年")
else:
    print(f"{year} 是平年")


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


text = input("請輸入一串英文或數字：")  # 新增 text 變數，記錄輸入的字串
repeat = []  # 新增 repeat 變數為空串列
not_repeat = []  # 新增 not_repeat 變數為空串列
for i in text:  # 使用 for 迴圈，依序取出每個字元
    a = text.count(i, 0, len(text))  # 判斷字元在字串中出現的次數
    if a > 1 and i not in repeat:  # 如果次數大於 1，且沒有存在 repeat 串列中
        repeat.append(i)  # 將字元加入 repeat 串列
    if a == 1 and i not in not_repeat:  # 如果次數等於 1，且沒有存在 not_repeat 串列中
        not_repeat.append(i)  # 將字元加入 not_repeat 串列

print(repeat)
print(not_repeat)


print("------------------------------------------------------------")  # 60個


import math  # import math 標準函式模組

text = input("輸入文字：")  # 讓使用者輸入文字
length = len(text)  # 取得輸入的文字長度
center = math.floor(length / 2)  # 取出中間值
if length % 2 == 0:  # 如果除以 2 餘數為 0，表示偶數
    print(f"{text[center-1:center+1]}")  # 取出中間兩個字元
else:
    print(f"{text[center]}")  # 如果是奇數，取出中間一個字元


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






print("------------------------------------------------------------")  # 60個

import time

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

num = input("輸入你的發票號碼：")
ns = "05701942"  # 特別獎
n1 = "97718570"  # 特獎
n2 = ["88400675", "73475574", "53038222"]  # 頭獎
if num == ns:
    print("對中 1000 萬元！")  # 對中特別獎
if num == n1:
    print("對中 200 萬元！")  # 對中特獎
# 頭獎判斷
for i in n2:
    if num == i:
        print("對中 20 萬元！")  # 對中頭獎
        break
    if num[-7:] == i[-7:]:
        print("對中 4 萬元！")  # 末七碼相同
        break
    if num[-6:] == i[-6:]:
        print("對中 1 萬元！")  # 末六碼相同
        break
    if num[-5:] == i[-5:]:
        print("對中 4000 元！")  # 末五碼相同
        break
    if num[-4:] == i[-4:]:
        print("對中 1000 元！")  # 末四碼相同
        break
    if num[-3:] == i[-3:]:
        print("對中 200 元！")  # 末三碼相同
        break


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


print("------------------------------------------------------------")  # 60個
print("Python 數學範例")
print("------------------------------------------------------------")  # 60個


a = input("請輸入兩個數字 ( 格式 a,b )：")  # 新增變數 a，內容是使用者輸入的兩個數字，數字以逗號分隔
b = a.split(",")  # 新增變數 b，內容使用 split 根據逗號將數字拆開為串列
b1 = int(b[0])  # 使用 int 將第一個值轉換為「數字」
b2 = int(b[1])  # 使用 int 將第二個值轉換為「數字」
print(f"{b1} + {b2} = {b1+b2}")  # 印出四則運算的結果
print(f"{b1} - {b2} = {b1-b2}")
print(f"{b1} x {b2} = {b1*b2}")
print(f"{b1} / {b2} = {b1/b2}")


print("------------------------------------------------------------")  # 60個


a = input("請輸入兩個數字 ( 格式 a,b )：")
b = a.split(",")
b1 = int(b[0])
b2 = int(b[1])
print(f"{b1} + {b2} = {b1+b2}")
print(f"{b1} - {b2} = {b1-b2}")
print(f"{b1} x {b2} = {b1*b2}")
print(f"{b1} / {b2} = {round(b1/b2,3)}")  # 使用 round 四捨五入到小數點三位
print(f"{b2} + {b1} = {b2+b1}")
print(f"{b2} - {b1} = {b2-b1}")
print(f"{b2} x {b1} = {b2*b1}")
print(f"{b2} / {b1} = {round(b2/b1,3)}")


print("------------------------------------------------------------")  # 60個


a = input("請輸入數字 ( 格式 a,b,c... )：")  # 新增變數 a，內容是使用者輸入的多個數字，數字以逗號分隔
b = a.split(",")  # 新增變數 b，內容使用 split 根據逗號將數字拆開為串列
output = 0  # 設定 output 從 0 開始
for i in b:  # 使用 for 迴圈，依序取出 b 串列的每個項目
    output += int(i)  # 將 output 的數值加上每個項目 ( 使用 int 將項目轉換成數字 )

print(f"數字總和為：{output}")


print("------------------------------------------------------------")  # 60個


while output != 0:  # 使用 while 迴圈，如果 output 等於 0 才會停止
    a = input("請輸入數字 ( 格式 a,b,c... )：")
    b = a.split(",")
    output = 0
    for i in b:
        output += int(i)
    print(f"數字總和為：{output}")


print("------------------------------------------------------------")  # 60個


nums = [int(i) for i in input().split(",")]  # 使用串列生成式，將輸入的數字轉換成串列
result = sum(nums)  # 將串列內的數字加總
print(result)  # 印出結果


print("------------------------------------------------------------")  # 60個

n = int(input())  # 輸入要產生的數字數量
arr = []  # 建立一個空串列，記錄數字
for i in range(n):  # 使用 for 迴圈，重複指定的數字
    if i == 0:  # 如果 i 等於 0，a 為 0
        a = 0
    elif i == 1:  # 如果 i 等於 1，a 為 1
        a = 1
        arr = [0, 1]  # 將串列設定為 [0, 1]
    else:  # 如果 i 大於 1
        a = arr[0] + arr[1]  # a 等於串列的兩個數字相加
        del arr[0]  # 刪除串列的第一個項目
        arr.append(a)  # 將 a 加入串列成為第二個項目
    print(a, end=",")  # 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181


print("------------------------------------------------------------")  # 60個


for a in range(1, 10):  # 讓 a 從 1 執行到 9
    for b in range(1, 10):  # 讓 b 從 1 執行到 9
        print(f"{a}x{b}={a*b}", end=" ")
    # 使用格式化字串，印出產生對應的字串，最後加上 end=' '表示不換行
    print("")
    # 內層迴圈執行結束後，執行 print('') 會換行顯示
"""
1x1=1 1x2=2 1x3=3 1x4=4 1x5=5 1x6=6 1x7=7 1x8=8 1x9=9
2x1=2 2x2=4 2x3=6 2x4=8 2x5=10 2x6=12 2x7=14 2x8=16 2x9=18
3x1=3 3x2=6 3x3=9 3x4=12 3x5=15 3x6=18 3x7=21 3x8=24 3x9=27
4x1=4 4x2=8 4x3=12 4x4=16 4x5=20 4x6=24 4x7=28 4x8=32 4x9=36
5x1=5 5x2=10 5x3=15 5x4=20 5x5=25 5x6=30 5x7=35 5x8=40 5x9=45
6x1=6 6x2=12 6x3=18 6x4=24 6x5=30 6x6=36 6x7=42 6x8=48 6x9=54
7x1=7 7x2=14 7x3=21 7x4=28 7x5=35 7x6=42 7x7=49 7x8=56 7x9=63
8x1=8 8x2=16 8x3=24 8x4=32 8x5=40 8x6=48 8x7=56 8x8=64 8x9=72
9x1=9 9x2=18 9x3=27 9x4=36 9x5=45 9x6=54 9x7=63 9x8=72 9x9=81
"""


print("------------------------------------------------------------")  # 60個


for a in range(1, 10):
    for b in range(1, 10):
        print("{}x{}={}".format(a, b, a * b), end=" ")
    print("")

for a in range(1, 10):
    for b in range(1, 10):
        print("%dx%d=%d" % (a, b, a * b), end=" ")
    print("")


print("------------------------------------------------------------")  # 60個


for a in range(1, 10):
    for b in range(1, 10):
        if (a * b) < 10:
            print(f"{a}x{b}={a*b}", end="  ")  # 如果 axb<10，讓結尾增加一個空白
        else:
            print(f"{a}x{b}={a*b}", end=" ")
    print("")

    """
    1x1=1  1x2=2  1x3=3  1x4=4  1x5=5  1x6=6  1x7=7  1x8=8  1x9=9
    2x1=2  2x2=4  2x3=6  2x4=8  2x5=10 2x6=12 2x7=14 2x8=16 2x9=18
    3x1=3  3x2=6  3x3=9  3x4=12 3x5=15 3x6=18 3x7=21 3x8=24 3x9=27
    4x1=4  4x2=8  4x3=12 4x4=16 4x5=20 4x6=24 4x7=28 4x8=32 4x9=36
    5x1=5  5x2=10 5x3=15 5x4=20 5x5=25 5x6=30 5x7=35 5x8=40 5x9=45
    6x1=6  6x2=12 6x3=18 6x4=24 6x5=30 6x6=36 6x7=42 6x8=48 6x9=54
    7x1=7  7x2=14 7x3=21 7x4=28 7x5=35 7x6=42 7x7=49 7x8=56 7x9=63
    8x1=8  8x2=16 8x3=24 8x4=32 8x5=40 8x6=48 8x7=56 8x8=64 8x9=72
    9x1=9  9x2=18 9x3=27 9x4=36 9x5=45 9x6=54 9x7=63 9x8=72 9x9=81
    """


print("------------------------------------------------------------")  # 60個


a = b = int(input("請輸入一個正整數："))  # 新增 a 和 b 變數，等於使用者輸入的數字
output = ""  # 新增 output 變數，作為輸出的文字
while True:  # 使用 while 迴圈
    for i in range(2, (a + 1)):  # 使用 for 迴圈
        if i == b:  # 如果 i 等於 b，表示是質數，跳出 for 迴圈
            break
        if a % i == 0:  # 如果可以被 i 整除，表示不是質數
            output += f"{i}"  # 設定 output 輸出的內容
            a = int(a / i)  # 重新將 a 設定為商
            break  # 跳出 for 迴圈
    if a == 1 or a == b:  # 如果商等於 1 或是質數，跳出 while 迴圈
        break
    else:
        output += "*"  # 否則在 output 後方加上 * 號，繼續 while 迴圈
if b == a and b != 1:
    print(f"{b} 是質數")  # while 迴圈結束後，如果 a 等於 b，印出質數的文字
elif b == 1:
    print(f"{b} 不是質數，也不能質因數分解")  # 如果輸入的是 1 或 2
else:
    print(f"{b}={output}")  # 否則印出質因數分解的結果


print("------------------------------------------------------------")  # 60個


a = range(2, 100)  # 產生 2～100 的串列
print(*a)
b = [i for i in a if i == a[0] or i % a[0] > 0]  # 找出第一個質數，並將串列裡該質數的倍數剔除
print(*b)
c = [i for i in b if i == b[1] or i % b[1] > 0]  # 找出第二個質數，並將串列裡該質數的倍數剔除
print(*c)
d = [i for i in c if i == c[2] or i % c[2] > 0]  # 找出第三個質數，並將串列裡該質數的倍數剔除
print(*d)


"""
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99
2 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99
2 3 5 7 11 13 17 19 23 25 29 31 35 37 41 43 47 49 53 55 59 61 65 67 71 73 77 79 83 85 89 91 95 97
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 49 53 59 61 67 71 73 77 79 83 89 91 97
"""


print("------------------------------------------------------------")  # 60個


a = range(2, 100)  # 產生 2～100 的串列
p = 0  # 設定 p 從 0 開始 ( 從 a[p] 也就是第一個項目開始 )


def g():  # 定義一個函式 g
    global p, a  # 設定 p 和 a 是全域變數
    if p < len(a):  # 如果 p 小於 a 的長度 ( 依序取值到 a 的最後一個項目 )
        a = [i for i in a if i == a[p] or i % a[p] > 0]  # 重新設定 a 為移除倍數後的串列
        p = p + 1  # p 增加 1
        g()  # 重新執行函式 g


g()  # 執行函式 g
print(*a)  # 印出 a ( 使用 * 將串列打散印出 )

"""
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
"""


print("------------------------------------------------------------")  # 60個


input_str = input("輸入數字 ( 逗號分隔 )：")  # 讓使用者輸入數字，數字間用逗號分隔
nums = input_str.split(",")  # 將輸入的文字，用逗號拆分成串列
for i in range(len(nums)):  # 將串列的每個項目轉換成文字
    nums[i - 1] = int(nums[i - 1])
nums.sort(reverse=True)  # 將串列從大到小排序
result = nums[0]  # 設定「暫定的最小公倍數」為最大的數字
while True:  # 執行 while 迴圈
    a = 0  # 新增 a 變數，當作餘數使用
    for i in nums:  # 依序取出串列中的每個數字
        a = result % i  # 用「暫定的最小公倍數」除以每個數字，求出餘數
        if a != 0:  # 如果餘數不為 0，跳出 for 迴圈再來一次
            break
    if a == 0:  # 如果全部餘數都為 0，跳出 while 迴圈
        break
    else:
        result = result + nums[0]  # 如果餘數不為 0，就將「暫定的最小公倍數」加上最大的數字，然後再來一次
print(result)  # while 迴圈結束後，印出最小公倍數


print("------------------------------------------------------------")  # 60個


input_str = input("輸入數字 ( 逗號分隔 )：")  # 讓使用者輸入數字，數字間用逗號分隔
nums_arr = input_str.split(",")  # 將輸入的文字，用逗號拆分成串列
for i in range(len(nums_arr)):  # 將串列的每個項目轉換成文字
    nums_arr[i - 1] = int(nums_arr[i - 1])
nums_arr.sort()  # 將串列從小到大排序
result = nums_arr[0]  # 建立變數 result，內容為輸入的第一個數字 ( 數字的最小值 )
arr = [result, 1]  # 建立一個變數 arr 為串列，內容預設為 [ 輸入的最小值, 1 ]
for i in range(2, result + 1):  # 使用 for 迴圈，找出 result 數字的每個因數
    if result % i == 0:  # 找因數的方法，將 result 依序除以 2、3、4...result
        result = int(result / i)  # 如果餘數為 0 ( 整除 )，表示這個數字為因數
        arr.append(i)  # 將因數加入 arr 串列中，並更新 result 為除以因數的數值
        arr.append(result)  # 也將 result 加入 arr 串列 ( 因為商也算是因數 )
arr.sort(reverse=True)  # 完成後將 arr 從大到小排序

for j in arr:  # 依序取出 arr 串列中的每個數字
    a = 0  # 建立 a 變數，記錄餘數
    output = 1  # 建立 output 變數，記錄最大公因數 ( 預設 1 )
    for i in nums_arr:  # 依序將輸入的數字除以 arr 串列中的數字
        a = a + i % j  # 將餘數加入 a 變數 ( 如果沒有餘數，a 就一直會是 0 )
        output = j  # 將 output 等於目前的因數
    if a == 0:  # 如果 a 為 0 表示都整除，將 result 等於 output
        result = output
        break
print(result)  # 印出最大公因數


print("------------------------------------------------------------")  # 60個

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
    os.rename(i, f"./demo/img-{n:03d}.jpg")  # 改名時，使用字串格式化的方式進行三位數補零
    n = n + 1  # 每次重複時將 n 增加 1


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import tkinter as tk

root = tk.Tk()  # 產生 tkinter 視窗
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width, height)
root.destroy()  # 關閉視窗


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch12\code057.py

from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
screen = QtWidgets.QApplication.desktop()
width = screen.width()
height = screen.height()
print(width, height)


print("------------------------------------------------------------")  # 60個

socket.socket(family, type, proto)
# family：IPv4 本機、IPv4 網路、IPv6 網路。
# type：使用 TCP 或 UDP 方式。
# protocol: 串接協定 ( 通常預設 0 )。


print("------------------------------------------------------------")  # 60個

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
print(ip)
s.close()


print("------------------------------------------------------------")  # 60個

import requests

ip = requests.get("https://api.ipify.org").text

print(ip)


print("------------------------------------------------------------")  # 60個

import socket

hostname = "google.com"
print(socket.gethostbyname(hostname))


print("------------------------------------------------------------")  # 60個

import os

hostname = "google.com"
response = os.system("ping -c 3 -i 1 " + hostname)
print(response)

response = os.popen(f"ping -c 3 -i 1 {hostname}").read()
print(response)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Python 影像處理")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import glob
from PIL import Image

jpg = glob.glob("./demo/*.[jJ][pP][gG]")  # 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
print(jpg)
for i in jpg:
    print(i)
    im = Image.open(i)  # 開啟圖片檔案
    name = i.lower().split("/")[::-1][0]  # 將檔名換成小寫 ( 避免 JPG 與 jpg 干擾 )
    png = name.replace("jpg", "png")  # 取出圖片檔名，將 jpg 換成 png
    im.save(f"./demo/png/{png}", "png")  # 轉換成 png 並存檔


print("------------------------------------------------------------")  # 60個

import glob
from PIL import Image

jpg = glob.glob("./demo/*.[jJ][pP][gG]")  # 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
print(jpg)
for i in jpg:
    print(i)
    im = Image.open(i)  # 開啟圖片檔案
    name = i.split("/")[::-1][0]  # 取出檔名
    im.save(f"./demo/jpg/{name}", quality=65, subsampling=0)  # 設定參數並存檔


print("------------------------------------------------------------")  # 60個

import glob
from PIL import Image

imgs = glob.glob("./oxxo/*.jpg")  # 取得 demo 資料夾內所有的圖片
for i in imgs:
    im = Image.open(i)  # 依序開啟每一張圖片
    size = im.size  # 取得圖片尺寸
    print(size)


print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("oxxostudio.jpg")  # 開啟圖片
img2 = img.resize((200, 200))  # 調整圖片尺寸為 200x200
img2.save("test.jpg")  # 調整後存檔到 resize 資料夾


print("------------------------------------------------------------")  # 60個

import glob
from PIL import Image

imgs = glob.glob("./oxxo/*.jpg")
for i in imgs:
    im = Image.open(i)
    size = im.size
    name = i.split("/")[::-1][0]  # 取得圖片的名稱
    im2 = im.resize((200, 200))  # 調整圖片尺寸為 200x200
    im2.save(f"./oxxo/resize/{name}")  # 調整後存檔到 resize 資料夾


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.png")  # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(factor)  # 調整亮度，factor 為一個浮點數值
# 調整後的數值 = 原始數值 x factor


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.jpg")  # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(1.5)  # 提高亮度
output.save("oxxostudio_b15.jpg")  # 存檔

output = brightness.enhance(0.5)  # 降低亮度
output.save("oxxostudio_b05.jpg")  # 存檔


print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("./oxxostudio.jpg")  # 開啟圖片
img_crop = img.crop((0, 0, 200, 100))  # 裁切圖片
img_crop.save("./test.jpg")  # 存檔
# img_crop.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("./oxxostudio.jpg")
img_r1 = img.rotate(30)  # 旋轉 30 度
img_r2 = img.rotate(30, expand=1)  # 旋轉 30 度，expand 設定 1
img_r1.save("./test1.jpg")
img_r2.save("./test2.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image

bg = Image.new("RGB", (400, 300), "#ff0000")  # 產生 RGB 色域，400x300 背景紅色的圖片
bg.save("oxxostudio.jpg")
# bg.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個


from PIL import Image

bg = Image.new("RGB", (400, 300), "#ff000055")  # 產生 RGBA 色域，400x300 背景半透明紅色的圖片
bg.save("oxxostudio.png")


print("------------------------------------------------------------")  # 60個

from PIL import Image

bg = Image.new("RGB", (1200, 800), "#000000")  # 產生一張 1200x800 的全黑圖片
for i in range(1, 9):
    img = Image.open(f"d{i}.jpg")  # 開啟圖片
    img = img.resize((300, 400))  # 縮小尺寸為 300x400
    x = (i - 1) % 4  # 根據開啟的順序，決定 x 座標
    y = (i - 1) // 4  # 根據開啟的順序，決定 y 座標 ( // 為快速取整數 )
    bg.paste(img, (x * 300, y * 400))  # 貼上圖片

bg.save("oxxostudio.jpg")


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageOps

bg = Image.new("RGB", (1240, 840), "#000000")  # 因為擴張，所以將尺寸改成 1240x840
for i in range(1, 9):
    img = Image.open(f"d{i}.jpg")
    img = img.resize((300, 400))
    img = ImageOps.expand(img, 20, "#ffffff")  # 擴張邊緣，產生邊框
    x = (i - 1) % 4
    y = (i - 1) // 4
    bg.paste(img, (x * 300, y * 400))

bg.save("oxxostudio.jpg")


print("------------------------------------------------------------")  # 60個


from PIL import Image

img = Image.open("./watermark-photo.jpg")  # 開啟風景圖
icon = Image.open("./oxxostudio-icon.png")  # 開啟浮水印 icon
img.paste(icon, (0, 0), icon)  # 將風景圖貼上 icon
img.save("./ok.jpg")  # 存檔為 ok.jpg
# img.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個


from PIL import Image

img = Image.open("./watermark-photo.jpg")
icon = Image.open("./oxxostudio-icon.png")

img_w, img_h = img.size  # 取得風景圖尺寸
icon_w, icon_h = icon.size  # 取得 icon 尺寸
x = int((img_w - icon_w) / 2)  # 計算置中時 icon 左上角的 x 座標
y = int((img_h - icon_h) / 2)  # 計算置中時 icon 左上角的 y 座標

img.paste(icon, (x, y), icon)  # 設定 icon 左上角座標
img.save("./ok.jpg")


print("------------------------------------------------------------")  # 60個


import glob
from PIL import Image

imgs = glob.glob("./demo/*.jpg")  # 讀取 demo 資料夾裡所有的圖片
icon = Image.open("./oxxostudio-icon.png")
for i in imgs:
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    img = Image.open(i)  # 開啟圖片
    img.paste(icon, (0, 0), icon)  # 加入浮水印
    img.save(f"./demo/watermark/{name}")  # 以原本的名稱存檔


print("------------------------------------------------------------")  # 60個


from PIL import Image

img = Image.open("./watermark-photo.jpg")  # 準備合成浮水印的圖
img2 = Image.open("./watermark-photo.jpg")  # 底圖
icon = Image.open("./oxxostudio-icon.png")

img_w, img_h = img.size
icon_w, icon_h = icon.size
x = int((img_w - icon_w) / 2)
y = int((img_h - icon_h) / 2)
img.paste(icon, (x, y), icon)  # 合成浮水印
img.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
img2.paste(img, (0, 0), img)  # 合成底圖
img2.save("./ok.jpg")


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFont, ImageDraw

img = Image.open("./photo.jpg")  # 開啟圖片
font = ImageFont.truetype("Teko-Regular.ttf", 100)  # 設定字型
draw = ImageDraw.Draw(img)  # 準備在圖片上繪圖
draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)  # 將文字畫入圖片
img.save("./ok.jpg")  # 儲存圖片
# img.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFont, ImageDraw

img = Image.open("./photo.jpg")
w, h = img.size  # 取得圖片尺寸
font = ImageFont.truetype("Teko-Regular.ttf", 100)
draw = ImageDraw.Draw(img)
draw.text(
    (0, h - 100), "OXXO.STUDIO", fill=(255, 255, 255), font=font
)  # 使用 h-100 定位到下方
img.save("./ok.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

img = Image.open("./photo.jpg")
font = ImageFont.truetype("Teko-Regular.ttf", 150)
# 設定一張空白圖片，背景 (0,0,0,0) 表示透明背景
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)  # 畫入文字
text = text.rotate(30, expand=1)  # 旋轉這張圖片，expand 設定 1 表示展開旋轉，不要裁切
img.paste(text, (50, 0), text)  # 將文字的圖片貼上原本的圖
img.save("./ok.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

# import os
img = Image.open("./photo.jpg")
w, h = img.size

font = ImageFont.truetype("Teko-Regular.ttf", 150)
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)
text = text.rotate(30, expand=1)

img2 = Image.open("./photo.jpg")  # 再次開啟原本的圖為 img2
img2.paste(text, (50, 0), text)  # 將文字貼上 img2
img2.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img2.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
img.paste(img2, (0, 0), img2)  # 將 img2 貼上 img
img.save("./ok.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

imgs = glob.glob("./demo/*.jpg")  # 讀取 demo 資料夾裡所有的圖片

for i in imgs:
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    img = Image.open(i)  # 開啟圖片
    w, h = img.size
    font = ImageFont.truetype("Teko-Regular.ttf", 100)
    text = Image.new(mode="RGBA", size=(400, 100), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(text)
    draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)
    text = text.rotate(30, expand=1)
    img2 = Image.open(i)
    img2.paste(text, (50, 0), text)
    img2.convert("RGBA")
    img2.putalpha(150)
    img.paste(img2, (0, 0), img2)
    img.save(f"./test/{name}")


print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("oxxostudio.jpg")  # 開啟圖片
w, h = img.size  # 讀取圖片長寬
level = 50  # 設定縮小程度
img2 = img.resize((int(w / level), int(h / level)))  # 縮小圖片
img2 = img2.resize((w, h), resample=Image.NEAREST)  # 放大圖片為原始大小
img2.save("test.jpg")  # 存檔

print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("oxxostudio.jpg")
w, h = img.size
level = 20
img2 = img.resize((int(w / level), int(h / level)))
img2 = img2.resize((w, h), resample=Image.NEAREST)

x1, y1 = 60, 60  # 定義選取區域的左上角座標
x2, y2 = 250, 250  # 定義選取區域的右上角座標
area = img2.crop((x1, y1, x2, y2))  # 裁切區域
img.paste(area, (x1, y1))  # 在原本的圖片裡貼上馬賽克區域
img.save("test.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")  # 開啟圖片
output = img.filter(ImageFilter.BLUR)  # 套用基本模糊化
output.save("output.jpg")
# output.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(ImageFilter.BoxBlur(5))  # 套用 BoxBlur，設定模糊半徑為 5
output.save("output.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(ImageFilter.GaussianBlur(5))  # 套用 GaussianBlur，設定模糊半徑為 5
output.save("output.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(
    ImageFilter.UnsharpMask(radius=5, percent=-100, threshold=3)
)  # 套用 UnsharpMask
output.show()


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")  # 開啟圖片
output = img.filter(ImageFilter.SHARPEN)  # 套用圖片銳利化
output.save("output.jpg")  # 存檔
# output.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
for i in range(3):
    img = img.filter(ImageFilter.SHARPEN)
img.save("output.jpg")


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(
    ImageFilter.UnsharpMask(radius=5, percent=100, threshold=10)
)  # 套用 UnsharpMask
output.show()


print("------------------------------------------------------------")  # 60個


from PIL import Image
import piexif

img = Image.open("./oxxostudio.jpg")  # 使用 PIL Image 開啟圖片
exif = piexif.load(img.info["exif"])  # 使用 piexif 讀取圖片 Exif 資訊
print(exif)


print("------------------------------------------------------------")  # 60個


from PIL import Image
import piexif

img = Image.open("./oxxostudio.jpg")
exif = piexif.load(img.info["exif"])
# 建立字典對照表
info = {
    "0th": [271, 272, 282, 283, 305, 306, 316],
    "Exif": [
        33434,
        33437,
        34855,
        36867,
        36868,
        36880,
        36881,
        36882,
        40962,
        40963,
        42035,
        42036,
    ],
    "1st": [282, 283],
    "GPS": [2, 4, 5, 17, 24, 31],
}
# 根據對照表，印出照片 exif 裡的資訊 ( 有就印出，沒有就略過 )
for i in info:
    for j in info[i]:
        if j in exif[i]:
            print(j, ":", exif[i][j])


print("------------------------------------------------------------")  # 60個


from PIL import Image
import piexif

img = Image.open("./oxxostudio.jpg")
exif = piexif.load(img.info["exif"])

exif["0th"][305] = b"OXXO.STUDIO"  # 修改編輯軟體
exif["0th"][306] = b"2020:01:01 00:00:00"  # 修改編輯時間
exif["Exif"][36867] = b"2020:01:01 00:00:00"  # 加入檔案建立時間
exif["Exif"][36868] = b"2020:01:01 00:00:00"  # 加入檔案建立時間
exif_new = piexif.dump(exif)  # 更新 Exif
img.save("./iphone-edit.jpg", exif=exif_new)  # 另存新檔並加入 Exif


print("------------------------------------------------------------")  # 60個


from PIL import Image
import pytesseract

img = Image.open("english.jpg")
text = pytesseract.image_to_string(img, lang="eng")
print(text)


print("------------------------------------------------------------")  # 60個


from PIL import Image
import pytesseract

img = Image.open("chinese.jpg")
text = pytesseract.image_to_string(img, lang="chi_tra")
print(text)


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("Python 聲音處理")
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
print(song)  # <pydub.audio_segment.AudioSegment object at 0x7faaa545a7f0>


print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song.export("oxxostudio.wav", format="wav")  # 輸出為 wav
print("ok")  # 輸出後印出 ok


print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song.export("output.wav", bitrate="96k")  # 輸出壓縮比率為 96k 的 mp3 檔案
print("ok")  # 輸出後印出 ok


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
duration = song.duration_seconds  # 讀取長度
channels = song.channels  # 讀取聲道數量
print(channels, duration)  # 印出資訊


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song[1500:5500].export("output.mp3")  # 取出 1500 毫秒～5500 毫秒長度的聲音，輸出為 output.mp3
print("ok")  # 輸出後印出 ok


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment

song1 = AudioSegment.from_mp3("oxxo1.mp3")  # 讀取第一個 mp3 檔案
song2 = AudioSegment.from_mp3("oxxo2.mp3")  # 讀取第二個 mp3 檔案
output = song1 + song2  # 串接兩段聲音
output.export("output.mp3")  # 輸出為 output.mp3
print("ok")  # 輸出後印出 ok


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
output = song * 3  # 乘以 3，重複三次變成三倍長
output.export("output.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3
output1 = song[:] + 10  # 將所有陣列中的資料增加 10 ( 變大聲 )
output2 = song[:] - 10  # 將所有陣列中的資料減少 10 ( 變小聲 )
output1.export("output1.mp3")  # 輸出聲音
output2.export("output2.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")
output1 = song.apply_gain(10)  # 將音量增加 10 ( 變大聲 )
output2 = song.apply_gain(-10)  # 將音量減少 10 ( 變小聲 )
output1.export("output1.mp3")
output2.export("output2.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")
output1 = song.fade_in(3000)  # 開頭三秒 ( 3000ms ) 淡入
output2 = song.fade_out(3000)  # 結尾三秒 ( 3000ms ) 淡出
output1.export("output1.mp3")
output2.export("output2.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")

output1 = song.fade(to_gain=15, start=1000, duration=2000)
# 從 1 秒的位置開始，慢慢變大聲到增加 15，過程持續 2 秒

output2 = song.fade(to_gain=-30, end=3000, duration=2000)
# 從 1 秒的位置開始 ( 3000-2000 )，慢慢變小聲到減少 30，過程持續 2 秒

output1.export("output1.mp3")
output2.export("output2.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取背景音樂 mp3 檔案
voice = AudioSegment.from_mp3("voice.mp3")  # 讀取說話聲音 mp3 檔案
output = voice.overlay(song, loop=True)  # 混合說話聲音和背景音樂
output.export("output.mp3")


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

voice = AudioSegment.from_mp3("voice.mp3")  # 讀取說話聲音 mp3 檔案
output = voice.reverse()  # 反轉說話聲音
output.export("output.mp3")


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment

song = AudioSegment.from_mp3("test.mp3")  # 讀取聲音檔案


# 定義加速與減速的函式
def speed_change(sound, speed=1.0):
    rate = sound._spawn(
        sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)}
    )
    return rate.set_frame_rate(sound.frame_rate)


song_slow = speed_change(song, 0.75)  # 聲音減速
song_fast = speed_change(song, 2.0)  # 聲音加速

song_slow.export("song_slow.mp3")
song_fast.export("song_fast.mp3")


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組
from pydub.playback import play  # 載入 pydub.playback 的 play 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 開啟聲音檔案
output = song * 2  # 讓聲音檔案變成兩倍長
play(output)  # 播放聲音


print("------------------------------------------------------------")  # 60個


from IPython.display import Audio  # 載入 IPython.display 的 Audio模組

Audio("output.mp3")  # 播放聲音


print("------------------------------------------------------------")  # 60個


import pyaudio
import wave

chunk = 1024  # 記錄聲音的樣本區塊大小
sample_format = (
    pyaudio.paInt16
)  # 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
channels = 2  # 聲道數量
fs = 44100  # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
seconds = 5  # 錄音秒數
filename = "oxxostudio.wav"  # 錄音檔名

p = pyaudio.PyAudio()  # 建立 pyaudio 物件

print("開始錄音...")

# 開啟錄音串流
stream = p.open(
    format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True,
)

frames = []  # 建立聲音串列

for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)  # 將聲音記錄到串列中

stream.stop_stream()  # 停止錄音
stream.close()  # 關閉串流
p.terminate()

print("錄音結束...")

wf = wave.open(filename, "wb")  # 開啟聲音記錄檔
wf.setnchannels(channels)  # 設定聲道
wf.setsampwidth(p.get_sample_size(sample_format))  # 設定格式
wf.setframerate(fs)  # 設定取樣頻率
wf.writeframes(b"".join(frames))  # 存檔
wf.close()


print("------------------------------------------------------------")  # 60個

import pyaudio
import wave
from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組
from pydub.playback import play  # 載入 pydub.playback 的 play 模組

chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
fs = 44100
seconds = 5
filename = "oxxostudio.wav"

p = pyaudio.PyAudio()

print("開始錄音...")

stream = p.open(
    format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True,
)

frames = []

for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print("錄音結束...")

wf = wave.open(filename, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b"".join(frames))
wf.close()

song = AudioSegment.from_mp3("song.mp3")  # 讀取背景音樂 mp3 檔案
voice = AudioSegment.from_wav("oxxostudio.wav")  # 讀取錄音 wav 檔案
output = voice.overlay(song, loop=True)  # 混合錄音和背景音樂
play(output)  # 播放聲音
output.export("output.mp3")  # 輸出為 mp3
print("ok")

print("------------------------------------------------------------")  # 60個

import numpy as np

samplerate = 44100  # 取樣頻率


def get_wave(freq, duration=0.5):
    amplitude = 4096  # 震幅 ( 音量大小 )
    t = np.linspace(
        0, duration, int(samplerate * duration)
    )  # 使用等差級數，在指定時間長度裡，根據取樣頻率建立區間
    wave = amplitude * np.sin(2 * np.pi * freq * t)  # 在每個區間裡放入指定頻率的波形
    return wave


def get_piano_notes():
    octave = ["C", "c", "D", "d", "E", "F", "f", "G", "g", "A", "a", "B"]  # 建立音符英文字對照表
    base_freq = 261.63  # 預設為 C4 的頻率
    note_freqs = {
        octave[i]: base_freq * pow(2, (i / 12)) for i in range(len(octave))
    }  # 產生頻率和英文字的對照
    note_freqs[""] = 0.0  # 如果是空值則為 0 ( 無聲音 )
    return note_freqs


def get_song_data(music_notes):
    note_freqs = get_piano_notes()  # 取的英文與音符對照表
    song = [
        get_wave(note_freqs[note]) for note in music_notes.split("-")
    ]  # 根據音樂的音符，對應到對照表產生指定串列
    song = np.concatenate(song)  # 連接為新陣列
    return song


# 音樂的音符表
music_notes = "C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C"
data = get_song_data(music_notes)  # 轉換成頻率對照表
data = data * (16300 / np.max(data))  # 調整震幅 ( 音量大小 )

from scipy.io.wavfile import write

write("twinkle-twinkle.wav", samplerate, data.astype(np.int16))  # 寫入檔案


print("------------------------------------------------------------")  # 60個

{
    A0: {frequency: "27.50", wavelength: "1254.55"},
    A1: {frequency: "55.00", wavelength: "627.27"},
    A2: {frequency: "110.00", wavelength: "313.64"},
    A3: {frequency: "220.00", wavelength: "156.82"},
    A4: {frequency: "440.00", wavelength: "78.41"},
    A5: {frequency: "880.00", wavelength: "39.20"},
    A6: {frequency: "1760.00", wavelength: "19.60"},
    A7: {frequency: "3520.00", wavelength: "9.80"},
    A8: {frequency: "7040.00", wavelength: "4.90"},
    B0: {frequency: "30.87", wavelength: "1117.67"},
    B1: {frequency: "61.74", wavelength: "558.84"},
    B2: {frequency: "123.47", wavelength: "279.42"},
    B3: {frequency: "246.94", wavelength: "139.71"},
    B4: {frequency: "493.88", wavelength: "69.85"},
    B5: {frequency: "987.77", wavelength: "34.93"},
    B6: {frequency: "1975.53", wavelength: "17.46"},
    B7: {frequency: "3951.07", wavelength: "8.73"},
    B8: {frequency: "7902.13", wavelength: "4.37"},
    C0: {frequency: "16.35", wavelength: "2109.89"},
    C1: {frequency: "32.70", wavelength: "1054.94"},
    C2: {frequency: "65.41", wavelength: "527.47"},
    C3: {frequency: "130.81", wavelength: "263.74"},
    C4: {frequency: "261.63", wavelength: "131.87"},
    C5: {frequency: "523.25", wavelength: "65.93"},
    C6: {frequency: "1046.50", wavelength: "32.97"},
    C7: {frequency: "2093.00", wavelength: "16.48"},
    C8: {frequency: "4186.01", wavelength: "8.24"},
    D0: {frequency: "18.35", wavelength: "1879.69"},
    D1: {frequency: "36.71", wavelength: "939.85"},
    D2: {frequency: "73.42", wavelength: "469.92"},
    D3: {frequency: "146.83", wavelength: "234.96"},
    D4: {frequency: "293.66", wavelength: "117.48"},
    D5: {frequency: "587.33", wavelength: "58.74"},
    D6: {frequency: "1174.66", wavelength: "29.37"},
    D7: {frequency: "2349.32", wavelength: "14.69"},
    D8: {frequency: "4698.63", wavelength: "7.34"},
    E0: {frequency: "20.60", wavelength: "1674.62"},
    E1: {frequency: "41.20", wavelength: "837.31"},
    E2: {frequency: "82.41", wavelength: "418.65"},
    E3: {frequency: "164.81", wavelength: "209.33"},
    E4: {frequency: "329.63", wavelength: "104.66"},
    E5: {frequency: "659.25", wavelength: "52.33"},
    E6: {frequency: "1318.51", wavelength: "26.17"},
    E7: {frequency: "2637.02", wavelength: "13.08"},
    E8: {frequency: "5274.04", wavelength: "6.54"},
    F0: {frequency: "21.83", wavelength: "1580.63"},
    F1: {frequency: "43.65", wavelength: "790.31"},
    F2: {frequency: "87.31", wavelength: "395.16"},
    F3: {frequency: "174.61", wavelength: "197.58"},
    F4: {frequency: "349.23", wavelength: "98.79"},
    F5: {frequency: "698.46", wavelength: "49.39"},
    F6: {frequency: "1396.91", wavelength: "24.70"},
    F7: {frequency: "2793.83", wavelength: "12.35"},
    F8: {frequency: "5587.65", wavelength: "6.17"},
    G0: {frequency: "24.50", wavelength: "1408.18"},
    G1: {frequency: "49.00", wavelength: "704.09"},
    G2: {frequency: "98.00", wavelength: "352.04"},
    G3: {frequency: "196.00", wavelength: "176.02"},
    G4: {frequency: "392.00", wavelength: "88.01"},
    G5: {frequency: "783.99", wavelength: "44.01"},
    G6: {frequency: "1567.98", wavelength: "22.00"},
    G7: {frequency: "3135.96", wavelength: "11.00"},
    G8: {frequency: "6271.93", wavelength: "5.50"},
    "A#0": {frequency: "29.14", wavelength: "1184.13"},
    "Bb0": {frequency: "29.14", wavelength: "1184.13"},
    "A#1": {frequency: "58.27", wavelength: "592.07"},
    "Bb1": {frequency: "58.27", wavelength: "592.07"},
    "A#2": {frequency: "116.54", wavelength: "296.03"},
    "Bb2": {frequency: "116.54", wavelength: "296.03"},
    "A#3": {frequency: "233.08", wavelength: "148.02"},
    "Bb3": {frequency: "233.08", wavelength: "148.02"},
    "A#4": {frequency: "466.16", wavelength: "74.01"},
    "Bb4": {frequency: "466.16", wavelength: "74.01"},
    "A#5": {frequency: "932.33", wavelength: "37.00"},
    "Bb5": {frequency: "932.33", wavelength: "37.00"},
    "A#6": {frequency: "1864.66", wavelength: "18.50"},
    "Bb6": {frequency: "1864.66", wavelength: "18.50"},
    "A#7": {frequency: "3729.31", wavelength: "9.25"},
    "Bb7": {frequency: "3729.31", wavelength: "9.25"},
    "A#8": {frequency: "7458.62", wavelength: "4.63"},
    "Bb8": {frequency: "7458.62", wavelength: "4.63"},
    "C#0": {frequency: "17.32", wavelength: "1991.47"},
    "Db0": {frequency: "17.32", wavelength: "1991.47"},
    "C#1": {frequency: "34.65", wavelength: "995.73"},
    "Db1": {frequency: "34.65", wavelength: "995.73"},
    "C#2": {frequency: "69.30", wavelength: "497.87"},
    "Db2": {frequency: "69.30", wavelength: "497.87"},
    "C#3": {frequency: "138.59", wavelength: "248.93"},
    "Db3": {frequency: "138.59", wavelength: "248.93"},
    "C#4": {frequency: "277.18", wavelength: "124.47"},
    "Db4": {frequency: "277.18", wavelength: "124.47"},
    "C#5": {frequency: "554.37", wavelength: "62.23"},
    "Db5": {frequency: "554.37", wavelength: "62.23"},
    "C#6": {frequency: "1108.73", wavelength: "31.12"},
    "Db6": {frequency: "1108.73", wavelength: "31.12"},
    "C#7": {frequency: "2217.46", wavelength: "15.56"},
    "Db7": {frequency: "2217.46", wavelength: "15.56"},
    "C#8": {frequency: "4434.92", wavelength: "7.78"},
    "Db8": {frequency: "4434.92", wavelength: "7.78"},
    "D#0": {frequency: "19.45", wavelength: "1774.20"},
    "Eb0": {frequency: "19.45", wavelength: "1774.20"},
    "D#1": {frequency: "38.89", wavelength: "887.10"},
    "Eb1": {frequency: "38.89", wavelength: "887.10"},
    "D#2": {frequency: "77.78", wavelength: "443.55"},
    "Eb2": {frequency: "77.78", wavelength: "443.55"},
    "D#3": {frequency: "155.56", wavelength: "221.77"},
    "Eb3": {frequency: "155.56", wavelength: "221.77"},
    "D#4": {frequency: "311.13", wavelength: "110.89"},
    "Eb4": {frequency: "311.13", wavelength: "110.89"},
    "D#5": {frequency: "622.25", wavelength: "55.44"},
    "Eb5": {frequency: "622.25", wavelength: "55.44"},
    "D#6": {frequency: "1244.51", wavelength: "27.72"},
    "Eb6": {frequency: "1244.51", wavelength: "27.72"},
    "D#7": {frequency: "2489.02", wavelength: "13.86"},
    "Eb7": {frequency: "2489.02", wavelength: "13.86"},
    "D#8": {frequency: "4978.03", wavelength: "6.93"},
    "Eb8": {frequency: "4978.03", wavelength: "6.93"},
    "F#0": {frequency: "23.12", wavelength: "1491.91"},
    "Gb0": {frequency: "23.12", wavelength: "1491.91"},
    "F#1": {frequency: "46.25", wavelength: "745.96"},
    "Gb1": {frequency: "46.25", wavelength: "745.96"},
    "F#2": {frequency: "92.50", wavelength: "372.98"},
    "Gb2": {frequency: "92.50", wavelength: "372.98"},
    "F#3": {frequency: "185.00", wavelength: "186.49"},
    "Gb3": {frequency: "185.00", wavelength: "186.49"},
    "F#4": {frequency: "369.99", wavelength: "93.24"},
    "Gb4": {frequency: "369.99", wavelength: "93.24"},
    "F#5": {frequency: "739.99", wavelength: "46.62"},
    "Gb5": {frequency: "739.99", wavelength: "46.62"},
    "F#6": {frequency: "1479.98", wavelength: "23.31"},
    "Gb6": {frequency: "1479.98", wavelength: "23.31"},
    "F#7": {frequency: "2959.96", wavelength: "11.66"},
    "Gb7": {frequency: "2959.96", wavelength: "11.66"},
    "F#8": {frequency: "5919.91", wavelength: "5.83"},
    "Gb8": {frequency: "5919.91", wavelength: "5.83"},
    "G#0": {frequency: "25.96", wavelength: "1329.14"},
    "Ab0": {frequency: "25.96", wavelength: "1329.14"},
    "G#1": {frequency: "51.91", wavelength: "664.57"},
    "Ab1": {frequency: "51.91", wavelength: "664.57"},
    "G#2": {frequency: "103.83", wavelength: "332.29"},
    "Ab2": {frequency: "103.83", wavelength: "332.29"},
    "G#3": {frequency: "207.65", wavelength: "166.14"},
    "Ab3": {frequency: "207.65", wavelength: "166.14"},
    "G#4": {frequency: "415.30", wavelength: "83.07"},
    "Ab4": {frequency: "415.30", wavelength: "83.07"},
    "G#5": {frequency: "830.61", wavelength: "41.54"},
    "Ab5": {frequency: "830.61", wavelength: "41.54"},
    "G#6": {frequency: "1661.22", wavelength: "20.77"},
    "Ab6": {frequency: "1661.22", wavelength: "20.77"},
    "G#7": {frequency: "3322.44", wavelength: "10.38"},
    "Ab7": {frequency: "3322.44", wavelength: "10.38"},
    "G#8": {frequency: "6644.88", wavelength: "5.19"},
    "Ab8": {frequency: "6644.88", wavelength: "5.19"},
}


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Python 影片處理")
print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片

format_list = ["avi", "mov", "wmv", "flv", "asf", "mkv"]  # 要轉換的格式清單

# 使用 for 迴圈轉換成所有格式
for i in format_list:
    output = video.copy()
    output.write_videofile(
        f"output.{i}",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
    )

print("ok")

print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

format_list = ["avi", "mov", "wmv", "flv", "asf", "mkv"]

for n in range(3):
    video = VideoFileClip(f"oxxo_{n}.mp4")  # 使用 for 迴圈讀取影片
    for i in format_list:
        output = video.copy()
        output.write_videofile(
            f"output_{n}.{i}",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
            codec="libx264",
            audio_codec="aac",
        )

print("ok")


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

video = AudioSegment.from_file("oxxostudio.mp4")  # 讀取 mp4 檔案
output.export("video.mp3")  # 講讀取的聲音輸出為 mp3
print("ok")


print("------------------------------------------------------------")  # 60個


from pydub import AudioSegment

video = AudioSegment.from_file("oxxostudio.mp4")
output = video[2000:10000]  # 剪輯聲音
output = output[:] + 10  # 放大聲音
output.export("output.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
audio = video.audio  # 取出聲音
audio.write_audiofile("song.mp3")  # 輸出聲音為 mp3
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
audio = AudioFileClip("song.mp3")  # 讀取音樂

output = video2.set_audio(audio)  # 合併影片與聲音
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 注意要設定相關參數，不然轉出來的影片會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output = video.subclip(12, 15)  # 剪輯影片 ( 單位秒 )
output.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

o1 = VideoFileClip("oxxo1.mp4")  # 開啟第一段影片
o2 = VideoFileClip("oxxo2.mp4")  # 開啟第二段影片
o3 = VideoFileClip("oxxo3.mp4")  # 開啟第三段影片
output = concatenate_videoclips([o1, o2, o3])  # 合併影片
output.write_videofile(
    "output123.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")

print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

o1 = VideoFileClip("oxxo1.mp4")
o1 = o1.resize((1280, 720))  # 改變尺寸
o2 = VideoFileClip("oxxo2.mp4")
o3 = VideoFileClip("oxxo3.mp4")
output = concatenate_videoclips([o1, o2, o3])
output.write_videofile(
    "output456.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

o1 = VideoFileClip("oxxo1.mp4")
o2 = VideoFileClip("oxxo2.mp4")
o3 = VideoFileClip("oxxo3.mp4")
output = concatenate_videoclips([o1, o2, o3], method="compose")  # 設定 method 為 compose
output.write_videofile(
    "output456.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

v1 = VideoFileClip("oxxo1.mp4")  # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")  # 讀取影片
v3 = VideoFileClip("oxxo3.mp4")  # 讀取影片
v4 = VideoFileClip("oxxo4.mp4")  # 讀取影片
v1 = v1.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
v2 = v2.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
v3 = v3.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
v4 = v4.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
output = clips_array([[v1, v2], [v3, v4]])  # 排列影片，v1 和 v2 一組，v3 和 v4 一組
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

v1 = VideoFileClip("oxxo1.mp4")  # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")  # 讀取影片
output = CompositeVideoClip([v2, v1])  # 混合影片
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

v1 = VideoFileClip("oxxo1.mp4")  # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")  # 讀取影片
v1 = mask_color(v1, color=0, thr=10, s=0)  # 設定 v1 遮罩為半透明
# color=0 表示黑色，thr 和 s 是參數，這種設定為半透明
output = CompositeVideoClip([v2, v1])  # 混合影片
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
clip_1 = video.subclip(2, 5)  # 裁切出三秒影片
clip_2 = video.subclip(17, 21).set_start(2).crossfadein(1)  # 裁切出四秒影片，設定兩秒後再開始，淡入一秒
clip_3 = video.subclip(50, 53).set_start(5).crossfadein(1)  # 裁切出三秒影片，設定五秒後再開始，淡入一秒

output = CompositeVideoClip([clip_1, clip_2, clip_3])

output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output = video.resize((480, 360))  # 改變尺寸
output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")
output = video.resize(width=480)  # 改變尺寸，設定寬度改變為 480
output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")
output_1 = crop(video, x1=10, y1=10, width=50, height=50)  # 方法 1，指定左上 (x1, y1) 座標和寬高
output_2 = crop(
    video, x1=10, y1=10, x2=50, y2=50
)  # 方法 2，指定左上 (x1, y1) 座標和右下 ( x2, y2 )座標
output_3 = crop(video, x1=10, width=100)  # 方法 3，指定左上 x1 座標和寬度，就會自動採用 y1=0 和影片高度

output_1.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")
output = video.rotate(90)  # 影片旋轉 90 度
output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")
output_x = mirror_x(video)  # 左右翻轉
output_y = mirror_y(video)  # 垂直翻轉

output_x.write_videofile(
    "output_x.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_y.write_videofile(
    "output_y.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output_1 = speedx(video, factor=2)  # 2 倍速
output_2 = speedx(video, factor=0.5)  # 0.5 倍速
output_3 = speedx(video, final_duration=2)  # 將影片變成 2 秒長

output_1.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_3.write_videofile(
    "output_3.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output_1 = time_mirror(video)  # 反轉影片
output_2 = time_symmetrize(video)  # 播到底後反轉影片回頭

output_1.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")
output_1 = lum_contrast(video, lum=-50, contrast=0)  # 亮度減少 50
output_2 = lum_contrast(video, lum=150, contrast=0)  # 亮度增加 150
output_3 = lum_contrast(video, lum=0, contrast=-0.5)  # 對比減少 0.5
output_4 = lum_contrast(video, lum=0, contrast=2)  # 對比增加 2

output_1.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_3.write_videofile(
    "output_3.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_4.write_videofile(
    "output_4.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")
output_1 = colorx(video, 1.5)  # 調整顏色
output_2 = gamma_corr(video, 1)  # 調整 gamma 值
output_3 = blackwhite(video)  # 黑白影片
output_4 = invert_colors(video)  # 負片效果

output_1.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_3.write_videofile(
    "output_3.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_4.write_videofile(
    "output_4.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output = video.resize((360, 180))  # 壓縮影片
output = output.subclip(13, 15)  # 取出 13～15 秒的片段
output.write_gif("output.gif")  # 將這個片段轉換成 gif
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")
output = video.resize((360, 180))
output = output.subclip(13, 15)
output.write_gif("output_fps24.gif", fps=24)  # 256 色一秒 24 格
output.write_gif("output_fps8.gif", fps=8)  # 256 色一秒 8 格
output.write_gif("output_fps8_c2.gif", fps=8, colors=2)  # 2 色一秒 8 格
output.write_gif("output_fps8_c16.gif", fps=8, colors=16)  # 16 色一秒 8 格
print("ok")


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (360, 180))  # 建立色彩模式為 RGBA，尺寸 360x180 的空白圖片
font = ImageFont.truetype("NotoSansTC-Regular.otf", 40)  # 設定字型與尺寸
draw = ImageDraw.Draw(img)  # 準備在圖片上繪圖
# 將文字畫入圖片
draw.text(
    (10, 120),
    "OXXO.STUDIO",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="red",
)
draw.text(
    xy=(50, 0),
    text="大家好\n哈哈",
    align="center",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="blue",
)
img.save("ok.png")  # 儲存為 png


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (360, 180))
font = ImageFont.truetype("NotoSansTC-Regular.otf", 40)
draw = ImageDraw.Draw(img)
draw.text(
    (10, 120),
    "OXXO.STUDIO",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="red",
)
draw.text(
    xy=(50, 0),
    text="大家好\n哈哈",
    align="center",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="blue",
)
img.save("ok.png")

video = VideoFileClip("baby_shark.mp4")  # 讀取影片
clip = video.resize((360, 180)).subclip(10, 12)  # 縮小影片尺寸，剪輯出 10～12 秒的片段
text_clip = ImageClip("ok.png", transparent=True).set_duration(2)  # 讀取圖片，將圖片變成長度兩秒的影片

output = CompositeVideoClip([clip, text_clip])  # 混合影片
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw

img_empty = Image.new("RGBA", (360, 180))  # 產生 RGBA 空圖片
font = ImageFont.truetype("NotoSansTC-Regular.otf", 24)  # 設定文字字體和大小
video = VideoFileClip("oxxostudio.mp4").resize((360, 180))  # 讀取影片，改變尺寸
output_list = []  # 記錄最後要組合的影片片段


# 建立文字字卡函式
def text_clip(xy, text, name):
    img = img_empty.copy()  # 複製空圖片
    draw = ImageDraw.Draw(img)  # 建立繪圖物件，並寫入文字
    draw.text(
        xy, text, fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill="black"
    )
    img.save(name)  # 儲存


# 建立影片和文字合併的函式
def text_in_video(t, text_img):
    clip = video.subclip(t[0], t[1])  # 剪輯影片到指定長度
    text = ImageClip(text_img, transparent=True).set_duration(
        t[1] - t[0]
    )  # 讀取字卡，調整為影片長度
    combine_clip = CompositeVideoClip([clip, text])  # 合併影片和文字
    output_list.append(combine_clip)  # 添加到影片片段裡


# 文字串列，包含座標和內容
text_list = [
    [(100, 140), "你到底要怎樣？"],
    [(90, 140), "給我 CDPRO2 呀！"],
    [(60, 140), "但是 CDPRO2 過時啦！"],
]

# 影片串列，包含要切取的時間片段
video_list = [[13, 16], [21, 24], [38, 41]]

# 使用 for 迴圈，產生文字字卡
for i in range(len(text_list)):
    text_clip(text_list[i][0], text_list[i][1], f"text_{i}.png")

# 使用 for 迴圈，合併字卡和影片
for i in range(len(video_list)):
    text_in_video(video_list[i], f"text_{i}.png")

output = concatenate_videoclips(output_list)  # 合併所有影片片段
output.write_gif("output.gif", fps=6, colors=32)  # 轉換成 gif 動畫
print("ok")


print("------------------------------------------------------------")  # 60個


# 定義轉換為總秒數的函式
def time2sec(t):
    arr = t.split(" --> ")  # 根據「' --> '」拆分文字
    s1 = arr[0].split(",")  # 前方的文字為開始時間
    s2 = arr[1].split(",")  # 後方的文字為結束時間
    # 計算開始時間的總秒數
    start = (
        int(s1[0].split(":")[0]) * 3600
        + int(s1[0].split(":")[1]) * 60
        + int(s1[0].split(":")[2])
        + float(s1[1]) * 0.001
    )
    # 計算結束時間的總秒數
    end = (
        int(s2[0].split(":")[0]) * 3600
        + int(s2[0].split(":")[1]) * 60
        + int(s2[0].split(":")[2])
        + float(s2[1]) * 0.001
    )
    return [start, end]  # 回傳開始時間與結束時間的串列


f = open("oxxostudio.srt", "r")  # 使用 open 方法的 r 開啟字幕檔案
srt = f.read()  # 讀取字幕檔案內容
f.close()  # 關閉檔案
srt_list = srt.split("\n")  # 將內容根據換行符號 \n 拆分成串列
sec = 1  # 串列中秒數從第二項開始 ( 串列的第二項的索引值為 1 )
text = 2  # 串列中文字內容從第三項開始 ( 串列的第三項的索引值為 2 )
sec_list = [[0, 0]]  # 定義時間串列的開頭為 [0,0]
text_list = [""]  # 定義字幕內容串列的開頭為空字串 ''
# 使用迴圈，讀取字幕檔案串列的每個項目
for i in range(len(srt_list)):
    if i == sec:
        sec = sec + 4  # 如果遇到時間內容，就將 sec + 4 ( 因為時間每隔 4 個項目會出現 )
        # 如果兩個串列項目內容前後對不上 ( 前一個結束時間不等於後一個的開始時間 )
        if sec_list[-1][1] != time2sec(srt_list[i])[0]:
            # 在時間串列中間添加一個開始時間與結束時間內容 ( 表示該區間沒有字幕 )
            sec_list.append([sec_list[-1][1], time2sec(srt_list[i])[0]])
            # 在文字串列中間添加一個空字串 ( 表示該區間沒有字幕 )
            text_list.append("")
        sec_list.append(time2sec(srt_list[i]))  # 添加時間到時間串列
    if i == text:
        text = text + 4  # 如果遇到文字內容，就將 text + 4 ( 因為文字每隔 4 個項目會出現 )
        text_list.append(srt_list[i])  # 添加文字到文字串列

print(sec_list)
print(text_list)


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw


def time2sec(t):
    arr = t.split(" --> ")
    s1 = arr[0].split(",")
    s2 = arr[1].split(",")
    start = (
        int(s1[0].split(":")[0]) * 3600
        + int(s1[0].split(":")[1]) * 60
        + int(s1[0].split(":")[2])
        + float(s1[1]) * 0.001
    )
    end = (
        int(s2[0].split(":")[0]) * 3600
        + int(s2[0].split(":")[1]) * 60
        + int(s2[0].split(":")[2])
        + float(s2[1]) * 0.001
    )
    return [start, end]


f = open("oxxostudio.srt", "r")
srt = f.read()
f.close()
srt_list = srt.split("\n")
# print(text_list)
sec = 1
text = 2
srt_list = [[0, 0]]
text_list = [""]
for i in range(len(srt_list)):
    if i == sec:
        sec = sec + 4
        if sec_list[-1][1] != time2sec(srt_list[i])[0]:
            sec_list.append([sec_list[-1][1], time2sec(srt_list[i])[0]])
            text_list.append("")
        sec_list.append(time2sec(srt_list[i]))
    if i == text:
        text = text + 4
        text_list.append(srt_list[i])

print(sec_list)
print(text_list)

img_empty = Image.new("RGBA", (480, 240))  # 產生 RGBA 空圖片
font = ImageFont.truetype("NotoSansTC-Regular.otf", 20)  # 設定文字字體和大小
video = VideoFileClip("baby_shark.mp4").resize((480, 240))  # 讀取影片，改變尺寸
video_duration = float(video.duration)  # 讀取影片總長度
output_list = []  # 記錄最後要組合的影片片段

# 如果字幕最後的時間小於總長度
if sec_list[-1][1] != video_duration:
    sec_list.append([sec_list[-1][1], video_duration])  # 添加時間到時間串列
    text_list.append("")  # 添加空字串到文字串列


# 建立文字字卡函式
def text_clip(text, name):
    img = img_empty.copy()  # 複製空圖片
    draw = ImageDraw.Draw(img)  # 建立繪圖物件，並寫入文字
    text_width = 21 * len(text)  # 在 480x240 文字大小 20 狀態下，一個中文字長度約 21px
    draw.text(
        ((480 - text_width) / 2, 10),
        text,
        fill=(255, 255, 255),
        font=font,
        stroke_width=2,
        stroke_fill="black",
    )
    img.save(name)  # 儲存


# 建立影片和文字合併的函式
def text_in_video(t, text_img):
    clip = video.subclip(t[0], t[1])  # 剪輯影片到指定長度
    text = ImageClip(text_img, transparent=True).set_duration(
        t[1] - t[0]
    )  # 讀取字卡，調整為影片長度
    combine_clip = CompositeVideoClip([clip, text])  # 合併影片和文字
    output_list.append(combine_clip)  # 添加到影片片段裡


# 使用 for 迴圈，產生文字字卡
for i in range(len(text_list)):
    text_clip(text_list[i], "srt.png")
    text_in_video(sec_list[i], "srt.png")

output = concatenate_videoclips(output_list)  # 合併所有影片片段
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")
frame = video.save_frame("frame1.jpg", t=22)
frame = video.save_frame("frame2.jpg", t=22.1)
frame = video.save_frame("frame3.jpg", t=22.2)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

img_clip = ImageClip("oxxostudio.jpg", transparent=True).set_duration(2)
img_clip.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

img1 = ImageClip("oxxo1.jpg", transparent=True).set_duration(3)
img2 = (
    ImageClip("oxxo2.jpg", transparent=True).set_duration(4).set_start(2).crossfadein(1)
)
img3 = (
    ImageClip("oxxo3.jpg", transparent=True).set_duration(3).set_start(5).crossfadein(1)
)

output = CompositeVideoClip([img1, img2, img3])

output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")

print("------------------------------------------------------------")  # 60個


from moviepy.editor import *

video = VideoFileClip("oxxostudio.gif")
video.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



