import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

# The card suit characters:
HEARTS = chr(9829)  # Character 9829 is '♥'
DIAMONDS = chr(9830)  # Character 9830 is '♦'
SPADES = chr(9824)  # Character 9824 is '♠'
CLUBS = chr(9827)  # Character 9827 is '♣'
# A list of chr() codes is at https://inventwithpython.com/chr


for _ in range(20):
    suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
    print(suit, end=" ")
print()


def getRandomCard():
    rank = random.choice(list("23456789JQKA") + ["10"])
    suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
    return (rank, suit)


cc = getRandomCard()
print(cc)


print("------------------------------------------------------------")  # 60個

# 宣告迷宮陣列
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

print("[迷宮的路徑(0的部分)]")
for i in range(10):
    for j in range(12):
        print(MAZE[i][j], end="")
    print()

print("------------------------------------------------------------")  # 60個


move = "   aaa     , bbb   , ccc   ,   ddd    "
n1, n2, n3, n4 = move.split(",")

print(n1.strip(), end="|\n")
print(n2.strip(), end="|\n")
print(n3.strip(), end="|\n")
print(n4.strip(), end="|\n")

print("------------------------------------------------------------")  # 60個

print("assert的語法")

# Set up the constants:
SUSPECTS = [
    "DUKE HAUTDOG",
    "MAXIMUM POWERS",
    "BILL MONOPOLIS",
    "SENATOR SCHMEAR",
    "MRS. FEATHERTOSS",
    "DR. JEAN SPLICER",
    "RAFFLES THE CLOWN",
    "ESPRESSA TOFFEEPOT",
    "CECIL EDGAR VANDERTON",
]
ITEMS = [
    "FLASHLIGHT",
    "CANDLESTICK",
    "RAINBOW FLAG",
    "HAMSTER WHEEL",
    "ANIME VHS TAPE",
    "JAR OF PICKLES",
    "ONE COWBOY BOOT",
    "CLEAN UNDERPANTS",
    "5 DOLLAR GIFT CARD",
]
PLACES = [
    "ZOO",
    "OLD BARN",
    "DUCK POND",
    "CITY HALL",
    "HIPSTER CAFE",
    "BOWLING ALLEY",
    "VIDEO GAME MUSEUM",
    "UNIVERSITY LIBRARY",
    "ALBINO ALLIGATOR PIT",
]
TIME_TO_SOLVE = 300  # 300 seconds (5 minutes) to solve the game.

# First letters and longest length of places are needed for menu display:
PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

# Basic sanity checks of the constants:
assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
# First letters must be unique:
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

print("------------------------------------------------------------")  # 60個


fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30", "Chicago"]
zipData = zip(fields, info)  # 執行zip
# print(type(zipData))                # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30"]
zipData = zip(fields, info)  # 執行zip
# print(type(zipData))                # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30", "Chicago"]
zipData = zip(fields, info)  # 執行zip
# print(type(zipData))                # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

f, i = zip(*player)  # 執行unzip
print("fields = ", f)
print("info   = ", i)

print("------------------------------------------------------------")  # 60個

fields = ["台北", "台中", "高雄"]
info = [80000, 50000, 60000]
zipData = zip(fields, info)  # 執行zip
sold_info = tuple(zipData)  # 將zip資料轉成元組
for city, sales in sold_info:
    print(f"{city} 銷售金額是 {sales}")

print("------------------------------------------------------------")  # 60個


def find_common_prefix(strs):
    prefix = []
    for c in zip(*strs):
        if len(set(c)) == 1:
            prefix.append(c[0])
        else:
            break
    return "".join(prefix)


print(find_common_prefix(["expensive", "export", "experience"]))

print("------------------------------------------------------------")  # 60個

X = [1, 2, 3, 4, 5]
Y = [1, 4, 9, 16, 25]
Z = list(zip(X, Y))  # zip : 兩串或更多串資料，同編號放一起的動作
print(Z)


X, Y = zip(*Z)  # Z裡面的點一個一個拿出來
print(X)
print(Y)

print("------------------------------------------------------------")  # 60個

a = [1, 2, 3]
b = ["a", "b", "c"]
c = zip(a, b)
print(list(c))  # 输出 [(1, 'a'), (2, 'b'), (3, 'c')]


loc = ([1, 2, 3, 4], [11, 12, 13, 14])
for i in zip(*loc):
    print(i)


x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
t = (x, y, z)
print(t)
for i in zip(*t):
    print(i)


# 4-3-3 在 list 生成式用 zip() 同時走訪多個容器

a = [1, -2, 3, -4, 5]
b = [9, 8, -7, -6, -5]

print([[x, y] for x, y in zip(a, b)])
print([x + y for x, y in zip(a, b)])

print("------------------------------------------------------------")  # 60個

a = [1, -2, 3, -4, 5]

b = [9, 8, -7, -6, -5]

print([x + y for x, y in zip(a, b) if x + y >= 0])


# 4-3-4 以巢狀 list 生成式產生複合 list

a = [1, 2, 3]

b = ["A", "B"]

print([[x, y] for x in a for y in b])


print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30", "Chicago"]
zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30"]
zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ["Name", "Age", "Hometown"]
info = ["Peter", "30", "Chicago"]
zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料類型
player = list(zipData)  # 將zip資料轉成串列
print(player)  # 列印串列

f, i = zip(*player)  # 執行unzip
print("fields = ", f)
print("info   = ", i)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
