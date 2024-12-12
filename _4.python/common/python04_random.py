# 不使用numpy

"""
random.seed()
random.random()
random.randint(num1, num2) # 僅 random.randint(num1, num2) 包含頭尾
random.choice
random.randrange
random.uniform(num1, num2)
random.sample
random.shuffle
random.其他

"""
print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

print(
    "---- random.seed() ST --------------------------------------------------------"
)  # 60個

"""
random.seed
random.seed 隨機數的「種子」，數值一樣則產生的隨機數相同，
若不設定則使用系統提供隨機源，這樣做出來的random資料並不是真正的隨機數
如果 seed 相同則結果相同
"""

print("不固定亂數種子")
for _ in range(10):
    print(random.random(), end=", ")
print()

print("固定亂數種子")
random.seed(5)

for _ in range(10):
    print(random.random(), end=", ")
print()

print("打亂亂數種子")
randseed = int(time.time())
random.seed(randseed)
for _ in range(10):
    print(random.random(), end=", ")
print()

# 修改隨機數生成的種子
random.seed()  # Seed based on system time or os.urandom()
random.seed(12345)  # Seed based on integer given
random.seed(b"bytedata")  # Seed based on byte data

print(
    "---- random.seed() SP --------------------------------------------------------"
)  # 60個

print(
    "---- random.random() ST --------------------------------------------------------"
)  # 60個

print("random.random(), 隨機產生 0.00 ~ 1.00 之間的一個浮點數")

print(random.random())  # 產生隨機浮點數n,0 <= n < 1.0

for _ in range(10):
    print(random.random())

print("------------------------------------------------------------")  # 60個

print("蒙地卡羅模擬")

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1  # x軸座標
    y = random.random() * 2 - 1  # y軸座標
    if x * x + y * y <= 1:  # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)

print(
    "---- random.random() SP --------------------------------------------------------"
)  # 60個

print(
    "---- random.randint(num1, num2) ST --------------------------------------------------------"
)  # 60個

print("------------------------------------------------------------")  # 60個

print("random.randint(M, N), 產生隨機整數, 包含頭尾")

print("產生隨機整數 1 ~ 10, 包含頭尾")
for i in range(20):
    cc = random.randint(1, 10)  # 隨機取得整數
    print(cc, end=" ")
print()

print("------------------------------------------------------------")  # 60個

num1, num2 = 0, 255
R = random.randint(num1, num2)  # 產生 num1 ~ num2 之間的亂數整數 含邊界
G = random.randint(num1, num2)  # 產生 num1 ~ num2 之間的亂數整數 含邊界
B = random.randint(num1, num2)  # 產生 num1 ~ num2 之間的亂數整數 含邊界
print("取得亂數 :", R, G, B)

num = random.randint(1, 6)  # 產生1~6之間的整數亂數 含頭尾
print("你擲的骰子點數為 :" + str(num))

print("------------------------------------------------------------")  # 60個

print("1~49號 取 6 個 為一集合")
my_set = set()  # 建立空集合
while len(my_set) < 6:  # 使用 while 迴圈，直到集合的長度等於 6 就停止
    num = random.randint(1, 49)  # 取出 1～49 得隨機整數
    # print('本次取得 :', num)
    my_set.add(num)  # 將隨機數加入集合
print(my_set)

print("------------------------------------------------------------")  # 60個

print("0~100間取N個整數 取平均")
N = 1000
my_list = [random.randint(0, 100) for i in range(N)]
# print("平均 :", my_list)
print("平均 :", sum(my_list) / float(len(my_list)))

print("------------------------------------------------------------")  # 60個


# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(random.randint(0, 15))  # Add a random digit
    return color


# Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord("0"))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord("A"))


class Ball:
    def __init__(self):
        self.x = 0  # Starting center position
        self.y = 0
        self.dx = 2  # Move right by default
        self.dy = 2  # Move down by default
        self.radius = 3  # The radius is fixed
        self.color = getRandomColor()  # Get random color


ballList = []  # Create a list for balls

length = len(ballList)
print("length = ", length)

for i in range(6):
    ballList.append(Ball())

length = len(ballList)
print("length = ", length)

for i in range(length):
    print("第", i, "個 : ", ballList[i].color)

for ball in ballList:
    print(ball.color)

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

print("------------------------------------------------------------")  # 60個


def getrandbytes(size):
    return random.getrandbits(8 * size).to_bytes(size, "little")


ccc = b"111" + getrandbytes(100)

print(type(ccc))
print(ccc)

datacount = random.randint(16, 64) * 1024 + random.randint(1, 1024)

print("------------------------------------------------------------")  # 60個


def inputarr(data, size):
    for i in range(size):
        data[i] = random.randint(1, 100)


def showdata(data, size):
    for i in range(size):
        print("%3d" % data[i], end="")
    print()


def quick(d, size, lf, rg):
    # 第一筆鍵值為d[lf]
    if lf < rg:  # 排序資料的左邊與右邊
        lf_idx = lf + 1
        while d[lf_idx] < d[lf]:
            if lf_idx + 1 > size:
                break
            lf_idx += 1
        rg_idx = rg
        while d[rg_idx] > d[lf]:
            rg_idx -= 1
        while lf_idx < rg_idx:
            d[lf_idx], d[rg_idx] = d[rg_idx], d[lf_idx]
            lf_idx += 1
            while d[lf_idx] < d[lf]:
                lf_idx += 1
            rg_idx -= 1
            while d[rg_idx] > d[lf]:
                rg_idx -= 1
        d[lf], d[rg_idx] = d[rg_idx], d[lf]

        for i in range(size):
            print("%3d" % d[i], end="")
        print()

        quick(d, size, lf, rg_idx - 1)  # 以rg_idx為基準點分成左右兩半以遞迴方式
        quick(d, size, rg_idx + 1, rg)  # 分別為左右兩半進行排序直至完成排序


data = [0] * 100
size = 10
inputarr(data, size)
print("您輸入的原始資料是：")
showdata(data, size)
print("排序過程如下：")
quick(data, size, 0, size - 1)
print("最終排序結果：")
showdata(data, size)

print("------------------------------------------------------------")  # 60個

numberOfDice = 5
numberOfSides = 6

# Simulate the dice rolls:
rolls = []
for i in range(numberOfDice):
    rollResult = random.randint(1, numberOfSides)
    rolls.append(rollResult)

print(type(rolls))
print(rolls)

# Display the total:
print("Total:", sum(rolls))

# Display the individual rolls:
for i, roll in enumerate(rolls):
    rolls[i] = str(roll)
print(", ".join(rolls), end="")

print("------------------------------------------------------------")  # 60個

print("設計一個函數產生指定長度的驗證碼，驗證碼由大小寫字母和數字構成。\n")


def generate_code(code_len=4):
    # 生成指定長度的驗證碼
    #:param code_len: 驗證碼的長度(默認4個字符)
    #:return: 由大小寫英文字母和數字構成的隨機驗證碼
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_pos = len(all_chars) - 1
    code = ""
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


print(generate_code(10))

print("------------------------------------------------------------")  # 60個

dices = []
for loop in range(1, 4):
    for i in range(3):
        dice = random.randint(1, 6)
        dices.append(dice)
    print("%d : 隨機3組骰子值 : " % loop, sorted(dices))
    for i in range(3):
        dices.pop()

print("------------------------------------------------------------")  # 60個

print(
    "---- random.randint(num1, num2) SP --------------------------------------------------------"
)  # 60個

print(
    "---- random.choice ST --------------------------------------------------------"
)  # 60個

print("在名詞字串中隨機選取一個字串")
# animals = list("鼠牛虎兔龍蛇")
animals = ["鼠", "牛", "虎", "兔", "龍", "蛇"]
for _ in range(10):
    animal = random.choice(animals)
    print(animal)

print("------------------------------------------------------------")  # 60個

pretty_note = "♫♪♬"
pretty_text = ""

string_message = "abcdefg"
for i in string_message:
    pretty_text += i
    pretty_text += random.choice(pretty_note)

print(pretty_text)

print("------------------------------------------------------------")  # 60個

print("統計1~6隨機選擇的個數")
num = []
for i in range(600):
    num.append(random.choice([1, 2, 3, 4, 5, 6]))

numCount = {i: num.count(i) for i in num}
for num in sorted(numCount.keys()):
    print(num, ":", numCount[num])

print("------------------------------------------------------------")  # 60個

s = ""
for i in range(0, 10):
    s += random.choice("<>=^")
    s += random.choice("+- ")
    s += random.choice(("", "E", "e", "G", "g", "F", "f", "%"))

print(s)

print("------------------------------------------------------------")  # 60個

CATEGORY = "Animals"
WORDS = "ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA".split()

print("The category is:", CATEGORY)
secretWord = random.choice(WORDS)  # The word the player must guess.

print(secretWord)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
for i in range(0, 7):
    print(random.choice("ABCDEFGHIJKLMN"), end=",")


print("------------------------------------------------------------")  # 60個


str1 = "abcde"
for i in range(0, 3):
    print(random.choice(str1), end=" ")

print("------------------------------------------------------------")  # 60個

list1 = ["a", "b", "c", "d", "e"]
for i in range(0, 3):
    print(random.choice(list1), end=" ")


print("------------------------------------------------------------")  # 60個

name = ["小明", "小黃", "小紅", "小綠", "小白"]
print("抽取一個元素：", random.choice(name))

print("------------------------------------------------------------")  # 60個


# 假設有一組伺服器
servers = ["Server1", "Server2", "Server3", "Server4"]

# 模擬1000次請求, 隨機分配到這些伺服器
requests = {server: 0 for server in servers}
for _ in range(1000):
    selected_server = random.choice(servers)
    requests[selected_server] += 1

print(requests)  # 顯示每個伺服器獲得的請求數

print("------------------------------------------------------------")  # 60個


animals = ["鼠", "牛", "虎", "兔", "龍"]
print(random.choice(animals))

print("------------------------------------------------------------")  # 60個


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


# 自訂密碼產生器


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


print("------------------------------------------------------------")  # 60個


print(
    "---- random.choice SP --------------------------------------------------------"
)  # 60個

print(
    "---- random.randrange ST --------------------------------------------------------"
)  # 60個

N = 5
minNo = 3
maxNo = 10

for _ in range(N):
    x = random.randrange(maxNo)
    print("取得亂數 : ", x)

for _ in range(N):
    result = random.randrange(minNo, maxNo)  # 整數不含尾
    print("取得亂數 : " + str(result))

for _ in range(N):
    result = random.randrange(minNo, maxNo, 2)  # 從minNo-maxNo間 隔2個隨機取亂數
    print("取得亂數 : " + str(result))

print("------------------------------------------------------------")  # 60個

# random.randrange 可產生隨機整數

a = random.randrange(2, 500, 2)  # randrange 可指定隨機數階層，一定偶數
print(a)
b = random.randrange(0, 1)  # randrange 不包含設定的最後一個數值，一定出現 0
print(b)

print("任一整數", random.randrange(100))
print("任一整數", random.randrange(52, 100))
print("奇數", random.randrange(1, 100, 2))
print("偶數", random.randrange(0, 100, 2))

print(random.randrange(0, 88, 11))  # 從序列中取一個隨機數

print("------------------------------------------------------------")  # 60個

print("任一整數", random.randrange(100))
print("任一整數", random.randrange(52, 100))
print("奇數", random.randrange(1, 100, 2))
print("偶數", random.randrange(0, 100, 2))

print("------------------------------------------------------------")  # 60個

for i in range(0, 5):
    print(random.randrange(0, 10, 2), end=" ")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print(
    "---- random.randrange SP --------------------------------------------------------"
)  # 60個

print(
    "---- random.uniform(num1, num2) ST --------------------------------------------------------"
)  # 60個

# uniform 返回兩個值中間的隨機浮點數
b = random.uniform(3, 8)
print(b)

print("random.uniform(num1, num2) 測試, num1 ~ num2 之間的浮點數")

num1, num2 = 2.34, 4.56
for i in range(30):
    print(random.uniform(num1, num2), end="\n")
print()

print("------------------------------------------------------------")  # 60個

print("建立一個隨機串列")
N = 5
data = [random.uniform(num1, num2) for _ in range(N)]
print(type(data))
print(len(data))
print(data)

print("------------------------------------------------------------")  # 60個

for i in range(10):
    print(random.uniform(1, 100), " ", end="")
print()

print("------------------------------------------------------------")  # 60個

print("常態分布 1 ~ 10")
for i in range(5):
    print("uniform(1,10) : ", random.uniform(1, 10))

print("------------------------------------------------------------")  # 60個

for i in range(5):
    print("uniform(1,10) : ", random.uniform(1, 10))


for j in range(3):  # 以迴圈執行3次
    print(random.uniform(1, 10), end=" ")  # 產生1-10間的亂數

print(random.uniform(101, 200))  # 產生101-200之間的隨機浮點數

print("------------------------------------------------------------")  # 60個


"""
data = [random.uniform(-100, 1000) for _ in range(1000)]
data = [random.uniform(-3, 8) for _ in range(1000)]
data = [random.uniform(1, 1000) for _ in range(100)]
"""

print("------------------------------------------------------------")  # 60個

for i in range(0, 3):
    print(random.uniform(0, 10), end=" ")

print("------------------------------------------------------------")  # 60個

for _ in range(5):
    print(random.uniform(0.2, 0.9))

print("------------------------------------------------------------")  # 60個

print(
    "---- random.uniform(num1, num2) SP --------------------------------------------------------"
)  # 60個


print("------------------------------------------------------------")  # 60個


print(
    "--- random.sample ST ---------------------------------------------------------"
)  # 60個

answer = random.sample(range(1, 10), k=4)  # 使用 random.sample

lto = random.sample(range(1, 50), k=6)
lto.sort()
print(lto)


# sample 可以從清單中隨機取出不重複的值
e = random.sample([1, 2, 3, 4, 5, 6, 7, 8], k=4)
print(e)
f = random.sample(range(1, 50), k=6)  # 大樂透一行搞定？
print(f)

print("------------------------------------------------------------")  # 60個

print("亂數不重複 範圍 個數")
num = random.sample(range(1, 20), 10)

print(type(num))
print(num)
print("排序")

num.sort()
print(num)

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍"]

# 抽取樣本
print(random.sample(animals, 3))
print(random.sample(animals, 3))

list1 = random.sample(range(1, 50), 7)
special = list1.pop()
list1.sort()
print("本期大樂透中獎號碼為：", end="")
for i in range(0, 6):
    if i == 5:
        print(str(list1[i]))
    else:
        print(str(list1[i]), end=", ")
print("本期大樂透特別號為：" + str(special))

print("------------------------------------------------------------")  # 60個

lotterys = random.sample(range(1, 50), 7)  # 7組號碼
specialNum = lotterys.pop()  # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):  # 排序列印大樂透號碼
    print(lottery, end=" ")
print("\n特別號:%d" % specialNum)  # 列印特別號

print("------------------------------------------------------------")  # 60個

N = 7  # 7組號碼
for i in range(10):
    numbers = random.sample(range(1, 50), N)  # 結果為 1, 2, 3....49 不包含50之整數
    # print(type(numbers))
    print(numbers)

specialNum = numbers.pop()  # 特別號, 最後一個數字是特別號, pop出後, numbers剩下6個號碼

print("第xxx期大樂透號碼 :", end="")
for num in sorted(numbers):  # 排序列印大樂透號碼
    print(num, end=" ")
print(f"\n特別號:{specialNum}")  # 列印特別號

print("------------------------------------------------------------")  # 60個

lotterys = random.sample(range(1, 50), 7)  # 7組號碼
specialNum = lotterys.pop()  # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):  # 排序列印大樂透號碼
    print(lottery, end=" ")
print("\n特別號:%d" % specialNum)  # 列印特別號

print("------------------------------------------------------------")  # 60個

# 從序列或集合擷取12個不重複的元素
print(random.sample("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", 12))

print("------------------------------------------------------------")  # 60個

# 產生六個不重複的1到49之間的隨機數字
lottery_numbers = random.sample(range(1, 50), 6)

# 將中獎號碼排序，以方便比對
lottery_numbers.sort()

# 印出中獎號碼
print("本期大樂透中獎號碼為：", lottery_numbers)

print("------------------------------------------------------------")  # 60個


str1 = "abcde"
print(random.sample(str1, 3))

print("------------------------------------------------------------")  # 60個

name = ["小明", "小黃", "小紅", "小綠", "小白"]
print("抽取三個元素：", random.sample(name, 3))

print("------------------------------------------------------------")  # 60個


# 假設生產線上有一批產品序列號
product_serials = list(range(1000, 2000))

# 抽檢10個產品進行品質檢查
samples = random.sample(product_serials, 10)

for serial in samples:
    # 這裡會有一個品質檢查的函數
    print(f"檢查序列號 : {serial}")

print("------------------------------------------------------------")  # 60個


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

a = random.sample(range(1, 50), 6)
# 從包含 1～49 數字的串列中，取出六個不重複的數字變成串列
print(a)  # [9, 39, 10, 8, 25, 43]

print("------------------------------------------------------------")  # 60個

"""
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
"""
print("------------------------------------------------------------")  # 60個

"""
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
"""

print("------------------------------------------------------------")  # 60個


list1 = ["a", "b", "c", "d", "e"]
print(random.sample(list1, 3))


list1 = random.sample(range(1, 50), 7)
print(list1)
special = list1.pop()
print(special)
list1.sort()
print("本期大樂透中獎號碼為:", end="")
for i in range(0, 6):
    if i == 5:
        print(str(list1[i]))
    else:
        print(str(list1[i]), end=",")
print("本期大樂透特別號為:" + str(special))


print("------------------------------------------------------------")  # 60個


print(
    "--- random.sample SP ---------------------------------------------------------"
)  # 60個


print(
    "--- random.shuffle(list) ST ---------------------------------------------------------"
)  # 60個

# shuffle 可以把清單打散為隨機位置
d = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(d)
print(d)

print("------------------------------------------------------------")  # 60個

animals = "鼠牛虎兔龍蛇馬"
animalList = list(animals)  # 字串 轉 串列
print(type(animalList))
print(animalList)

for i in range(5):
    random.shuffle(animalList)  # 將次序打亂重新排列
    print(animalList)

print("------------------------------------------------------------")  # 60個

animals = "鼠牛虎兔龍蛇馬"
animalList = list(animals)  # 字串 轉 串列
print("原串列")
print(animalList)
print("次序打散")
random.shuffle(animalList)
print(animalList)
print("排序")
animalList.sort()
print(animalList)

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍"]
print("將次序打亂重新排列")
random.shuffle(animals)
print(animals)

print("------------------------------------------------------------")  # 60個

# 發牌遊戲

# Create a deck of cards
deck = [x for x in range(0, 52)]

# Create suits and ranks lists
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Shuffle the cards
random.shuffle(deck)

# Display the first four cards
for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card number", deck[i], "is", rank, "of", suit)

print("------------------------------------------------------------")  # 60個

# 給定items數列的初始值
items = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(items)  # 使用shuffle函數洗牌
print(items)  # 將洗牌後的序列輸出

print("------------------------------------------------------------")  # 60個

# shuffle 將list內的元素次序打亂重新排列

animals = ["鼠", "牛", "虎", "兔", "龍"]
print("原串列：", animals)

random.shuffle(animals)
print("新串列：", animals)

print("------------------------------------------------------------")  # 60個

# Every possible symbol that can be encrypted/decrypted:
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersList = list(LETTERS)  # 字串 轉 串列
print(type(lettersList))
print(lettersList)


def generateRandomKey():
    # Generate and return a random encryption key
    key = list(LETTERS)  # Get a list from the LETTERS string.
    random.shuffle(key)  # Randomly shuffle the list.
    return "".join(key)  # Get a string from the list.


print("------------------------------------------------------------")  # 60個

# data = list(range(10000))
# random.shuffle(data)

print("------------------------------------------------------------")  # 60個

# 給定items數列的初始值
word = ["apple", "bird", "tiger", "happy", "quick"]
random.shuffle(word)  # 使用shuffle函數打亂字的順序
print(word)  # 將打亂後字依序輸出

print("------------------------------------------------------------")  # 60個


import string


def encrypt(text, encryDict):  # 加密文件
    cipher = []
    for i in text:  # 執行每個字元加密
        v = encryDict[i]  # 加密
        cipher.append(v)  # 加密結果
    return "".join(cipher)  # 將串列轉成字串


abc = string.printable[:-5]  # 取消不可列印字元
newAbc = abc[:]  # 產生新字串拷貝
abclist = list(newAbc)  # 轉成串列
random.shuffle(abclist)  # 打亂串列順序
subText = "".join(abclist)  # 轉成字串
encry_dict = dict(zip(subText, abc))  # 建立字典
print("列印編碼字典\n", encry_dict)  # 列印字典

msg = "If the implementation is easy to explain, it may be a good idea."
ciphertext = encrypt(msg, encry_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)

print("------------------------------------------------------------")  # 60個

import string


def encrypt(text, encryDict):  # 加密文件
    cipher = []
    for i in text:  # 執行每個字元加密
        v = encryDict[i]  # 加密
        cipher.append(v)  # 加密結果
    return "".join(cipher)  # 將串列轉成字串


def decrypt(cipher, decryDict):  # 解密文件
    text = []
    for i in cipher:  # 執行每個字元解密
        v = decryDict[i]  # 加密
        text.append(v)  # 解密結果
    return "".join(text)  # 將串列轉成字串


abc = string.printable[:-5]  # 取消不可列印字元
newAbc = abc[:]  # 產生新字串拷貝
abclist = list(newAbc)  # 轉成串列
random.shuffle(abclist)  # 打亂串列順序
subText = "".join(abclist)  # 轉成字串
encry_dict = dict(zip(subText, abc))  # 建立加密字典
decry_dict = dict(zip(abc, subText))  # 建立解密字典
print("列印解碼字典\n", decry_dict)  # 列印解碼字典

msg = "If the implementation is easy to explain, it may be a good idea."
ciphertext = encrypt(msg, encry_dict)
print("原始字串 ", msg)
print("加密字串 ", ciphertext)
decryMsg = decrypt(ciphertext, decry_dict)
print("解密字串 ", decryMsg)

print("------------------------------------------------------------")  # 60個


print(
    "--- random.shuffle(list) SP ---------------------------------------------------------"
)  # 60個


print(
    "--- random.其他 ST ---------------------------------------------------------"
)  # 60個

tttt = hex(random.getrandbits(64))  # 64 bits randomness
print(tttt)

# 隨機二進制數的整數返回
print(random.getrandbits(200))

print("------------------------------------------------------------")  # 60個

print("random 之 dir")
print(dir(random))
print("顯示模組的所有名稱dir()")
print(dir(random))

print("------------------------------------------------------------")  # 60個

print("triangular 返回兩個值中間的隨機浮點數")
c = random.triangular(3, 8)
print(c)

for _ in range(5):
    print(random.triangular(1, 5))
print()

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

# 假設一家公司想要測試兩種不同的廣告設計, 以看哪一種效果更好
ad_designs = ["Design A", "Design B"]

# 公司有一個1000人的郵件列表, 想要隨機選擇一半接收A廣告, 一半接收B廣告
recipients = {"Design A": [], "Design B": []}

# 隨機分配郵件
for i in range(1, 1001):
    chosen_design = random.choice(ad_designs)  # 隨機選擇一種設計
    recipients[chosen_design].append(f"user_{i}")

# 確保每種設計都有500個用戶
while len(recipients["Design A"]) != 500:
    if len(recipients["Design A"]) > 500:
        user_to_move = recipients["Design A"].pop()
        recipients["Design B"].append(user_to_move)
    else:
        user_to_move = recipients["Design B"].pop()
        recipients["Design A"].append(user_to_move)

# 假設這裡會發送郵件，然後根據用戶反饋進行分析

# 輸出每種設計的接收者數量，確保它們是平均分配的
print(f"A 廣告接收者數量 : {len(recipients['Design A'])}")
print(f"B 廣告接收者數量 : {len(recipients['Design B'])}")

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

for j in range(5):  # 使用 20 次的 for 迴圈
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
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


"""
双色球随机选号程序
"""


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=" ")
        print("%02d" % ball, end=" ")
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = random.randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(random.randint(1, 16))
    return selected_balls


n = 10
for _ in range(n):
    display(random_select())

print("------------------------------------------------------------")  # 60個

"""
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
"""
