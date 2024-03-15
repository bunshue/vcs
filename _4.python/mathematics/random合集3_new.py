import sys

import random

#新進

print('------------------------------------------------------------')	#60個

# 猜數字：幾 A 幾 B

""" 
arr = []
for i in range(9):
    arr.append(i+1)

answer = []
for i in range(4):
    arrLength = int(len(arr)) - 1
    answer.append(arr.pop(random.randint(0, arrLength)))


 """
answer = random.sample(range(1,10), k=4)  # 使用 random.sample
print(answer)

n = 0

while True:
    user = str(input('請輸入四個數字：'))
    a = 0
    b = 0
    n += 1
    result = [0, 0, 0, 0]
    for i in range(4):
        result[i] = int(user[i])
    for i in range(4):
        if (result[i] in answer):
            if(answer[i] == result[i]):
                a += 1
            else:
                b += 1

    print('第 ' + str(n) + ' 次：' + user + \
          ' ( ' + str(a) + ' A ' + str(b) + ' B )')
    if a == 4:
        print('猜中囉')
        break

print("------------------------------------------------------------")  # 60個

""" 
arr = []
for i in range(1, 50):
    arr.append(i)

lto = []
for i in range(6):
    arrLength = int(len(arr)) - 1
    lto.append(arr.pop(random.randint(0, arrLength))) 
"""

# 使用 random.sample 一行搞定
lto = random.sample(range(1, 50), k=6)
lto.sort()
print(lto)

print("------------------------------------------------------------")  # 60個

# random.seed
# random.seed 隨機數的「種子」，數值一樣則產生的隨機數相同，若不設定則使用系統提供隨機源
# random.random() 並不是真正的隨機數

random.seed(5)
a = random.random()
random.seed(5)
b = random.random()
c = random.random()  # 重複 print 出來的結果是相同的
d = random.random()
print(f"{a}\n{b}\n{c}\n{d}")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\random\r02-randrange.py

# random.randrange 和 random.randint 都可產生隨機整數

a = random.randrange(2, 500, 2)  # randrange 可指定隨機數階層，一定偶數
print(a)
b = random.randrange(0, 1)  # randrange 不包含設定的最後一個數值，一定出現 0
print(b)
c = random.randint(0, 1)  # randint 包含設定的最後一個數值，0 和 1 隨機挑選
print(c)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\random\r03-choice.py

# random.choices

a = random.choice([1, 2, 3, 4, 5])  # choice 從 list 中選擇一個隨機元素
print(a)

# choices 從 list 中選擇指定數量的隨機元素 ( 可能會重複 )
b = random.choices([1, 2, 3, 4, 5, 6, 7, 8], k=5)
print(b)

# choices 可透過 weight 定義權重，有相對和累績兩種選一種的設定
# weights 為相對，cum_weights 為累積，下面的例子出現 8 的機率是 1 的八倍
c = random.choices([1, 2, 3, 4, 5, 6, 7, 8], weights=[1, 2, 3, 4, 5, 6, 7, 8], k=5)
print(c)

# shuffle 可以把清單打散為隨機位置
d = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(d)
print(d)

# sample 可以從清單中隨機取出不重複的值
e = random.sample([1, 2, 3, 4, 5, 6, 7, 8], k=4)
print(e)
f = random.sample(range(1, 50), k=6)  # 大樂透一行搞定？
print(f)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\random\r04-random.py

# random.random() 並不是真正的隨機數，如果 seed 相同則結果相同
a = random.random()
print(a)

# uniform 返回兩個值中間的隨機浮點數
b = random.uniform(3, 8)
print(b)

# triangular 返回兩個值中間的隨機浮點數
c = random.triangular(3, 8)
print(c)

# beta 分佈，兩個值需都大於 0，返回 0~1 之間隨機浮點數
d = random.betavariate(3, 8)
print(d)

# 指數分佈，不可為 0，若為負，則是小於零的福點數
e = random.expovariate(-5)
print(e)

# 其他還有
# random.gammavariate(alpha, beta)
# random.gauss(mu, sigma)
# random.lognormvariate(mu, sigma)
# random.normalvariate(mu, sigma)
# random.vonmisesvariate(mu, kappa)
# random.paretovariate(alpha)
# random.weibullvariate(alpha, beta)

# 參考：https://docs.python.org/zh-cn/3/library/random.html#random.random

print("------------------------------------------------------------")  # 60個


numberOfDice = 10

print("一次丟 ", numberOfDice, "個骰子, 丟100萬次")

# Set up a dictionary to store the results of each dice roll:
results = {}
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    results[i] = 0

# Simulate dice rolls:
print("Simulating 1,000,000 rolls of {} dice...".format(numberOfDice))
lastPrintTime = time.time()
for i in range(1000000):
    if time.time() > lastPrintTime + 1:
        print("{}% done...".format(round(i / 10000, 1)))
        lastPrintTime = time.time()

    total = 0
    for j in range(numberOfDice):
        total = total + random.randint(1, 6)
    results[total] = results[total] + 1

# Display results:
print("TOTAL - ROLLS - PERCENTAGE")
for i in range(numberOfDice, (numberOfDice * 6) + 1):
    roll = results[i]
    percentage = round(results[i] / 10000, 1)
    print("  {} - {} rolls - {}%".format(i, roll, percentage))

print("------------------------------------------------------------")  # 60個

print("亂數不重複 範圍 個數")
num = random.sample(range(1, 20), 10)

print(type(num))
print(num)
print("排序")

num.sort()
print(num)

print("------------------------------------------------------------")  # 60個


from random import randint, randrange


# 產生某個區間的整數亂數
def numRand(x, y):
    cout = 1  # 計數器
    while cout <= 10:
        number = randint(x, y)
        print(number, end=" ")
        cout += 1
    print()


# 將產生以append()方法加至List
def numRand2(x, y):
    cout = 1
    result = []  # 存放亂數
    while cout <= 10:
        number = randint(x, y)
        result.append(number)
        cout += 1
    return result


print("------------------------------------------------------------")  # 60個


# 能計算時間長度的產生器

import time
import random


def elapsed_time_gen():
    last_time = time.perf_counter()
    while True:
        now = time.perf_counter()
        yield now - last_time
        last_time = now


elapsed_time = elapsed_time_gen()

for _ in range(5):
    time.sleep(random.randint(1, 10) / 10)
    print(next(elapsed_time))

print("------------------------------------------------------------")  # 60個




rand = []
for i in range(10):
    rand.append(random.randint(0, 100))
print(rand)

print("------------------------------------------------------------")  # 60­э

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


import random  # 引用random亂數套件

#  將 1~49 的整數放入num串列中
num = []
for i in range(49):
    num.append(i + 1)
# 使用 random套件的sample函式由num中隨機取得不重複的7個元素
lot = random.sample(num, 7)

print("大樂透  號碼：", end="")
# 印出 lot[0]~lot[5]
for i in range(6):
    print(lot[i], end=", ")

print()
print("大樂透特別號：%2d" % (lot[6]))  # 印出 lot[6]


print("------------------------------------------------------------")  # 60個


# 自訂密碼產生器

import random


def set_password_source(source):
    def password_gen(length):
        output = []
        for i in range(length):
            output.append(random.choice(source))
        return "".join(output)

    return password_gen


my_password_gen = set_password_source("0123456789abcdefghij")
print(my_password_gen(10))

print("------------------------------------------------------------")  # 60個

# dictGame.py

import random

bossHp = 100
listPcCard = [["青眼白龍", 20], ["紅髮女妖", 11], ["白骷髏王", 9], ["碧眼狐怪", 12]]
random.shuffle(listPcCard)
dictMyCard = dict(listPcCard)

while True:
    n = int(input("功能選項：1.抽卡攻擊 2.補齊卡牌 3.目前卡牌 4.離開遊戲："))
    if n == 1:
        if not dictMyCard:
            print("目前沒有卡牌，請補卡牌")
            continue
        card = dictMyCard.popitem()
        listCard = list(card)
        cardName = listCard[0]
        cardAttack = listCard[1]
        bossHp -= cardAttack
        if bossHp <= 0:
            bossHp = 0
            print("%s最後一擊 %d 點\t魔王血量歸 %d，成功過關" % (cardName, cardAttack, bossHp))
            break
        print("使用%s攻擊 %d 點\t魔王目前血量：%d" % (cardName, cardAttack, bossHp))
    elif n == 2:
        random.shuffle(listPcCard)
        dictMyCard = dict(listPcCard)
        print("完成補齊卡牌!")
    elif n == 3:
        print("目前卡牌：", dictMyCard)
    elif n == 4:
        break
    else:
        print("無此選項功能!")

print("------------------------------------------------------------")  # 60個


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



print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



