"""
random

"""

import sys
import random

print("------------------------------------------------------------")  # 60個

print(random.random())  # 產生隨機浮點數n,0 <= n < 1.0
print(random.uniform(101, 200))  # 產生101-200之間的隨機浮點數
print(random.randint(-50, 0))  # 產生-50-0之間的隨機整數
print(random.randrange(0, 88, 11))  # 從序列中取一個隨機數
print(random.choice(["健康", "運勢", "事業", "感情", "流年"]))  #

items = ["a", "b", "c", "d"]
random.shuffle(items)  # 將items序列打亂
print(items)
# 從序列或集合擷取12個不重複的元素
print(random.sample("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", 12))

print("------------------------------------------------------------")  # 60個

import random

for i in range(10):  # 執行10次
    print(random.randrange(2, 500, 2))  # 從2-500間取10個偶數

print("------------------------------------------------------------")  # 60個

import random

for i in range(10):  # 執行10次
    print(random.randrange(100))  # 從0-100取隨機整數

print("------------------------------------------------------------")  # 60個

import random

for j in range(6):  # 以迴圈執行6次
    print(random.randint(1, 42), end=" ")  # 產生1-42的整數亂數
print()  # 換行1
for j in range(3):  # 以迴圈執行3次
    print(random.uniform(1, 10), end=" ")  # 產生1-10間的亂數


print("------------------------------------------------------------")  # 60個

import random

for i in range(5):
    a = random.randint(1, 10)  # 隨機取得整數
    print(a, end=" ")
print()
# 給定items數列的初始值
items = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(items)  # 使用shuffle函數洗牌
print(items)  # 將洗牌後的序列輸出

print("------------------------------------------------------------")  # 60個

import random

NUM_DIGITS = 10


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


secretNum = getSecretNum()
print(secretNum)

print("------------------------------------------------------------")  # 60個

from random import randint
import os.path

# pfile = input("請輸入檔名：").strip()

pfile = "tmp_cccccc.txt"
if os.path.isfile(pfile):
    print("此檔案已經存在，程式終止")
else:
    poutfile = open(pfile, "w")

    for i in range(30):
        print(randint(0, 999), file=poutfile, end=" ")

    poutfile.close()

    pinfile = open(pfile, "r")
    ps = pinfile.read()

    pnumber = [eval(items) for items in ps.split()]
    pnumber.sort()

    for i in range(len(pnumber)):
        print(pnumber[i], end=" ")

    pinfile.close()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
