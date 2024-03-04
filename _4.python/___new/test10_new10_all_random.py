"""

相關抽出

random

"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


import random

a = []  # 建立空串列
while len(a) < 6:  # 使用 while 迴圈，直到串列的長度等於 6 就停止
    b = random.randint(1, 49)  # 取出 1～49 得隨機整數
    if b not in a:  # 判斷如果 a 裡面沒有 b
        a.append(b)  # 將 b 放入 a
print(a)  # [34, 18, 31, 11, 47, 46]


print("------------------------------------------------------------")  # 60個


import random

a = set()  # 建立空集合
while len(a) < 6:  # 使用 while 迴圈，直到集合的長度等於 6 就停止
    b = random.randint(1, 49)  # 取出 1～49 得隨機整數
    a.add(b)  # 將隨機數加入集合
print(a)  # {34, 41, 48, 49, 19, 30}


print("------------------------------------------------------------")  # 60個


import random

a = random.sample(range(1, 50), 6)
# 從包含 1～49 數字的串列中，取出六個不重複的數字變成串列
print(a)  # [9, 39, 10, 8, 25, 43]


import random

a = random.randint(1, 99)  # 產生 1～99 的隨機整數
b = int(input("輸入 1～99 的數字："))  # 讓使用者輸入數字，使用 int 轉換成數字
while a != b:  # 使用 while 迴圈，如果 a 不等於 b，就不斷繼續
    if b < a:
        b = int(input("數字太小囉！再試一次吧："))  # 如果 b<a，提示數字太小
    elif b > a:
        b = int(input("數字太大囉！再試一次吧："))  # 如果 b>a，提示數字太大
print("答對囉！")  # 如果 b=a 會停止 while 迴圈，顯示正確答案


print("------------------------------------------------------------")  # 60個

import random

answer = random.sample(range(1, 10), 4)
print(answer)
a = b = n = 0  # 設定 a、b、n 三個變數，預設值 0
while a != 4:  # 使用 while 迴圈，直到 a 等於 4 才停止
    a = b = n = 0  # 每次重複時將 a、b、n 三個變數再次設定為 0
    user = list(input("輸入四個數字："))  # 讓使用者輸入數字，並透過 list 轉換成串列
    for i in user:  # 使用 for 迴圈，將使用者輸入的數字一一取出
        if int(user[n]) == answer[n]:  # 因為使用者輸入的是「字串」，透過 int 轉換成數字，和答案串列互相比較
            a += 1  # 如果位置和內容都相同，就將 a 增加 1
        else:
            if int(i) in answer:  # 如果位置不同，但答案裡有包含使用者輸入的數字
                b += 1  # 就將 b 增加 1
        n += 1  # 因為輸入的每個數字都要判斷，將 n 增加 1
    output = ",".join(user).replace(",", "")  # 四個數字都判斷後，使用 join 將串列合併成字串
    print(f"{output}: {a}A{b}B")
print("答對了！")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch10\code026.py_

import random
import time  # import time 模組

answer = random.sample(range(1, 10), 4)
print(answer)
a = b = n = 0
num = 0  # 新增 num 變數為 0，作為計算次數使用
t = time.time()  # 新增 t 變數為現在的時間
while a != 4:
    num += 1  # 每次重複時將 num 增加 1
    a = b = n = 0
    user = list(input("輸入四個數字："))
    for i in user:
        if int(user[n]) == answer[n]:
            a += 1
        else:
            if int(i) in answer:
                b += 1
        n += 1
    output = ",".join(user).replace(",", "")
    print(f"{output}: {a}A{b}B")
t = round((time.time() - t), 3)  # 當 a 等於 4 時，計算結束和開始的時間差
print(f"答對了！總共猜了 {num} 次，用了 {t} 秒")  # 印出對應的文字

print("------------------------------------------------------------")  # 60個

import random

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
for j in range(20):  # 使用 20 次的 for 迴圈
    local = random.choice(list(local_table.keys()))

    check_arr = list(str(local_table[local]))
    check_arr[0] = int(check_arr[0])
    check_arr[1] = int(check_arr[1]) * 9

    sex = random.choice([1, 2])
    check_arr.append(sex * 8)

    nums_str = ""
    for i in range(7):
        nums = random.randint(0, 9)
        nums_str = nums_str + str(nums)
        check_arr.append(nums * (7 - i))

    check_num = 10 - sum(check_arr) % 10
    if check_num == 10:
        check_num = 0

    id_number = str(local) + str(sex) + nums_str + str(check_num)
    print(id_number)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
