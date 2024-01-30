import sys
import random

#不使用numpy
'''
"""
random.seed()
random.random()
random.randint(num1, num2)
random.choice
random.randrange
random.uniform(num1, num2)
random.sample
其他

"""

print('---- random.seed() --------------------------------------------------------')	#60個

random.seed(5)  #固定亂數種子

"""
for i in range(10):
    print(random.random(), end = ', ')

import time
randseed = int(time.time())
random.seed(randseed) #打亂亂數種子
for i in range(10):
    print(random.random(), end = ', ')


# 修改隨機數生成的種子
random.seed() # Seed based on system time or os.urandom()
random.seed(12345) # Seed based on integer given
random.seed(b'bytedata') # Seed based on byte data
"""

print('---- random.random() --------------------------------------------------------')	#60個

print('random.random(), 隨機分布, 產生 0.00 ~ 1.00 之間的一個浮點數')
for i in range(5):
    print(random.random())

print('------------------------------------------------------------')	#60個

print('蒙地卡羅模擬')

import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    if x * x + y * y <= 1:          # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)

print('---- random.randint(num1, num2) --------------------------------------------------------')	#60個

for i in range(10):
    print(random.randint(0, 2))

print('------------------------------------------------------------')	#60個

# 隨機整數
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))
print(random.randint(0,10))

print('------------------------------------------------------------')	#60個

lst = [random.randint(1, 100) for i in range(100)]
print(lst)
print("Average of the list is", sum(lst) / float(len(lst)))

print('------------------------------------------------------------')	#60個

num1, num2 = 0, 255
R = random.randint(num1, num2) #產生 num1 ~ num2 之間的亂數整數 包含邊界
G = random.randint(num1, num2) #產生 num1 ~ num2 之間的亂數整數 包含邊界
B = random.randint(num1, num2) #產生 num1 ~ num2 之間的亂數整數 包含邊界
print("取得亂數: ", R, G, B)
print("取得亂數1: {} 亂數2: {} 亂數3: {}".format(R, G, B))
print("取得亂數: (%d, %d, %d)" % (R, G, B))

print('取出 1 ~ 6 之間的整數')

num = random.randint(1, 6)
print("你擲的骰子點數為：" + str(num))

print('---- random.choice --------------------------------------------------------')	#60個

import random                   # 導入模組random

ANIMALS = '鼠牛虎兔龍蛇馬'
animalList = list(ANIMALS) #字串 轉 串列
print(type(animalList))
print(animalList)

for i in range(10):
    print(random.choice(animalList), end = ', ')
print()

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍']
print('在名詞字串中隨機選取一個字串')
animal = random.choice(animals)
print(animal)

print('------------------------------------------------------------')	#60個

NUMBER = 11
numberList = list(range(NUMBER))
print(type(numberList))
print(numberList)

for i in range(10):
    print(random.choice(numberList), end = ', ')
print()

print('------------------------------------------------------------')	#60個

for i in range(10):
    print(random.choice([1,2,3,4,5,6]), end = ', ')
print()

print('------------------------------------------------------------')	#60個

for i in range(10):
    t = random.choice(range(80, 180))
    print(t, end = ', ')
print()

print('------------------------------------------------------------')	#60個

pretty_note = '♫♪♬'
pretty_text = ''

string_message = 'abcdefg'
for i in string_message:
    pretty_text += i
    pretty_text += random.choice(pretty_note)
    
print(pretty_text)

print('------------------------------------------------------------')	#60個

print('統計1~6隨機選擇的個數')
num = []
for i in range(600):
    num.append(random.choice([1, 2, 3, 4, 5, 6]))
    
numCount = {i:num.count(i) for i in num}
for num in sorted(numCount.keys()):
    print(num, ':', numCount[num])

print('------------------------------------------------------------')	#60個

s = ''
for i in range(0, 10):
    s += random.choice('<>=^')
    s += random.choice('+- ')
    s += random.choice(('', 'E', 'e', 'G', 'g', 'F', 'f', '%'))

print(s)

print('------------------------------------------------------------')	#60個



print('---- random.randrange --------------------------------------------------------')	#60個

N = 5
minNo = 3
maxNo = 10

for _ in range(N):
    x = random.randrange(maxNo)
    print("取得亂數 : ", x)

for _ in range(N):
    result = random.randrange(minNo, maxNo) #整數不含尾
    print("取得亂數 : " + str(result))

for _ in range(N):
    result = random.randrange(minNo, maxNo, 2) #從minNo-maxNo間 隔2個隨機取亂數
    print("取得亂數 : " + str(result))


import random

print("任一整數", random.randrange(100))
print("任一整數", random.randrange(52, 100))
print("奇數", random.randrange(1, 100, 2))
print("偶數", random.randrange(0, 100, 2))

print( random.randrange(0, 88, 11) ) #從序列中取一個隨機數


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('---- random.uniform(num1, num2) --------------------------------------------------------')	#60個

import random                       # 導入模組random

print('random.uniform(num1, num2) 測試, num1 ~ num2 之間的浮點數')

num1, num2 = 2.34, 4.56
for i in range(30):
    print(random.uniform(num1, num2), end = '\n')
print()

print('------------------------------------------------------------')	#60個

print('建立一個隨機串列')
N = 5
data = [random.uniform(num1, num2) for _ in range(N)]
print(type(data))
print(len(data))
print(data)

print('------------------------------------------------------------')	#60個

import random
for i in range(10):
    print(random.uniform(1, 100), " ", end="")

print()

print('------------------------------------------------------------')	#60個

print('常態分布 1 ~ 10')
for i in range(5):
    print("uniform(1,10) : ", random.uniform(1, 10))

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


















print('------------------------------------------------------------')	#60個


print('--- random.sample ---------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍']

# 抽取樣本
print(random.sample(animals, 3))
print(random.sample(animals, 3))


list1 = random.sample(range(1,50), 7)
special = list1.pop()
list1.sort()
print("本期大樂透中獎號碼為：", end="")
for i in range(0,6):
    if i == 5:    print(str(list1[i]))
    else:    print(str(list1[i]), end=", ")
print("本期大樂透特別號為：" + str(special))

print('------------------------------------------------------------')	#60個

lotterys = random.sample(range(1,50), 7)    # 7組號碼
specialNum = lotterys.pop()                 # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):            # 排序列印大樂透號碼
    print(lottery, end=" ")
print("\n特別號:%d" % specialNum)           # 列印特別號




print('------------------------------------------------------------')	#60個


import random                               # 導入模組random

N = 7   #7組號碼
for i in range(10):
    numbers = random.sample(range(1, 50), N)   #結果為 1, 2, 3....49 不包含50之整數
    #print(type(numbers))
    print(numbers)

specialNum = numbers.pop()                 # 特別號, 最後一個數字是特別號, pop出後, numbers剩下6個號碼

print("第xxx期大樂透號碼 :", end = '')
for num in sorted(numbers):            # 排序列印大樂透號碼
    print(num, end = ' ')
print(f"\n特別號:{specialNum}")             # 列印特別號

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('--- random.shuffle(list) ---------------------------------------------------------')	#60個

ANIMALS = '鼠牛虎兔龍蛇馬'
animalList = list(ANIMALS) #字串 轉 串列
print(type(animalList))
print(animalList)

for i in range(5):
    random.shuffle(animalList)    # 將次序打亂重新排列
    print(animalList)


print('------------------------------------------------------------')	#60個

ANIMALS = '鼠牛虎兔龍蛇馬'
animalList = list(ANIMALS) #字串 轉 串列
print('原串列')
print(animalList)
print('次序打散')
random.shuffle(animalList)
print(animalList)
print('排序')
animalList.sort()
print(animalList)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍']
print('將次序打亂重新排列')
random.shuffle(animals)
print(animals)




print('------------------------------------------------------------')	#60個

#發牌遊戲

# Create a deck of cards
deck = [x for x in range(0, 52)]

# Create suits and ranks lists
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
      "10", "Jack", "Queen", "King"]
        
# Shuffle the cards
random.shuffle(deck)

# Display the first four cards
for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card number", deck[i], "is", rank, "of", suit)

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

tttt = hex(random.getrandbits(64))  # 64 bits randomness
print(tttt)

# 隨機二進制數的整數返回
print(random.getrandbits(200))


print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


from random import randint

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

class Ball:
    def __init__(self):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = 2 # Move right by default
        self.dy = 2 # Move down by default
        self.radius = 3 # The radius is fixed
        self.color = getRandomColor() # Get random color

ballList = [] # Create a list for balls

length = len(ballList)
print('length = ', length)

for i in range(6):
    ballList.append(Ball())

length = len(ballList)
print('length = ', length)

for i in range(length):
    print('第', i, '個 : ', ballList[i].color)

for ball in ballList:
    print(ball.color)

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

print('------------------------------------------------------------')	#60個




from random import randint, random, getrandbits

def getrandbytes(size):
    return getrandbits(8 * size).to_bytes(size, 'little')


ccc = b'111' + getrandbytes(100)

print(type(ccc))
print(ccc)

datacount = randint(16, 64) * 1024 + randint(1, 1024)

ddd = random() * randint(-1000, 1000)
print(ddd)



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('random 之 dir')
import random
print(dir(random))


print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個



target = random.randint(1, 100)
print("1~100亂數值: " + str(target))


CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

print('The category is:', CATEGORY)
secretWord = random.choice(WORDS)  # The word the player must guess.

print(secretWord)




print("------------------------------------------------------------")  # 60個

for i in range(5):
    a = random.randint(1,10) #隨機取得整數
    print(a,end=' ')
print()
#給定items數列的初始值
items = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
random.shuffle(items)  #使用shuffle函數洗牌
print(items)#將洗牌後的序列輸出


print("------------------------------------------------------------")  # 60個

print( random.random() ) #產生隨機浮點數n,0 <= n < 1.0
print( random.uniform(101, 200) ) #產生101-200之間的隨機浮點數
print( random.randint(-50, 0) ) #產生-50-0之間的隨機整數
print( random.choice(["健康", "運勢", "事業", "感情", "流年"]) ) #

items = ['a','b','c','d']
random.shuffle(items) #將items序列打亂
print( items )
#從序列或集合擷取12個不重複的元素
print( random.sample('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', 12))


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\rint.py

for j in range(6): #以迴圈執行6次
    print(random.randint(1,42), end=' ')#產生1-42的整數亂數
print() #換行1
for j in range(3): #以迴圈執行3次
    print(random.uniform(1,10), end=' ')#產生1-10間的亂數

print("------------------------------------------------------------")  # 60個

def inputarr(data,size):
    for i in range(size):
        data[i]=random.randint(1,100)
        
def showdata(data,size):
    for i in range(size):
        print('%3d' %data[i],end='')
    print()

def quick(d,size,lf,rg):
    #第一筆鍵值為d[lf]
    if lf<rg:  #排序資料的左邊與右邊
        lf_idx=lf+1
        while d[lf_idx]<d[lf]:
            if lf_idx+1 >size:
                break
            lf_idx +=1
        rg_idx=rg
        while d[rg_idx] >d[lf]:
            rg_idx -=1
        while lf_idx<rg_idx:
            d[lf_idx],d[rg_idx]=d[rg_idx],d[lf_idx]
            lf_idx +=1
            while d[lf_idx]<d[lf]:
                lf_idx +=1
            rg_idx -=1
            while d[rg_idx] >d[lf]:
                rg_idx -=1
        d[lf],d[rg_idx]=d[rg_idx],d[lf]

        for i in range(size):
            print('%3d' %d[i],end='')
        print()
       
        quick(d,size,lf,rg_idx-1)   #以rg_idx為基準點分成左右兩半以遞迴方式
        quick(d,size,rg_idx+1,rg)   #分別為左右兩半進行排序直至完成排序               
		
def main():
    data=[0]*100
    size=10
    inputarr (data,size)
    print('您輸入的原始資料是：')
    showdata (data,size)
    print('排序過程如下：')
    quick(data,size,0,size-1)
    print('最終排序結果：')
    showdata(data,size)

main()




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
print('Total:', sum(rolls))


# Display the individual rolls:
for i, roll in enumerate(rolls):
    rolls[i] = str(roll)
print(', '.join(rolls), end='')

print("------------------------------------------------------------")  # 60個

lotterys = random.sample(range(1, 50), 7)  # 7組號碼
specialNum = lotterys.pop()  # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):  # 排序列印大樂透號碼
    print(lottery, end=" ")
print("\n特別號:%d" % specialNum)  # 列印特別號




print("------------------------------------------------------------")  # 60個



print("設計一個函數產生指定長度的驗證碼，驗證碼由大小寫字母和數字構成。\n")

def generate_code(code_len=4):
    """
    生成指定長度的驗證碼

    :param code_len: 驗證碼的長度(默認4個字符)

    :return: 由大小寫英文字母和數字構成的隨機驗證碼
    """
    all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    last_pos = len(all_chars) - 1
    code = ""
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


print(generate_code(10))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果", "香蕉", "西瓜", "水蜜桃", "百香果"]

count = []
for _ in range(10):
    cc = random.choice(fruits)
    print(cc)

print("------------------------------------------------------------")  # 60個

val=0
data=[0]*80
for i in range(80):
    data[i]=random.randint(1,150)

print('資料內容：')
for i in range(10):
    for j in range(8):
        print('%2d[%3d]  ' %(i*8+j+1,data[i*8+j]),end='')
    print('')



print("------------------------------------------------------------")  # 60個

name = ["小明", "小黃", "小紅", "小綠", "小白"]

print("抽取一個元素：", random.choice(name))
print("抽取三個元素：", random.sample(name, 3))
print("抽取三個元素：", random.shuffle(name))

print("------------------------------------------------------------")  # 60個

for i in range(5):
    a = random.randint(1,10) #隨機取得整數
    print(a,end=' ')
print()
#給定items數列的初始值
word = ['apple','bird','tiger','happy','quick']
random.shuffle(word)  #使用shuffle函數打亂字的順序
print(word)#將打亂後字依序輸出


print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('新進的')



# ch13_16.py
import random                       # 導入模組random

for i in range(5):
    print("uniform(1,10) : ", random.uniform(1, 10))


# ch13_18.py
import random                       # 導入模組random

porker = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'J', 'Q', 'K', 'A']
for i in range(3):
    random.shuffle(porker)          # 將次序打亂重新排列
    print(porker)





# ch13_17_1.py
import random                       # 導入模組random

for i in range(10):
    print(random.choice([1,2,3,4,5,6]), end=",")





# ch13_17.py
import random                       # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
print(random.choice(fruits))



# ch13_15.py
import random

for i in range(5):
    print(random.random())

'''

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
#data = [F(1, 7), F(2, 7), F(3, 7), F(4, 7), F(5, 7), F(6, 7)]
#assert len(fruits)%2 == 0
print(fruits)
random.shuffle(fruits)
print(fruits)

data = [0, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9]
random.shuffle(data)





import random

try:
    import pyperclip  # pyperclip copies text to the clipboard.
except ImportError:
    pass  # If pyperclip is not installed, do nothing. It's no big deal.

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lettersList = list(LETTERS) #字串 轉 串列
print(type(lettersList))
print(lettersList)

def generateRandomKey():
    """Generate and return a random encryption key."""
    key = list(LETTERS)  # Get a list from the LETTERS string.
    random.shuffle(key)  # Randomly shuffle the list.
    return ''.join(key)  # Get a string from the list.

print("------------------------------------------------------------")  # 60個


# syntax
print("顯示模組的所有名稱dir()")
print(dir(random))


import random

print(dir(random))


import random

my_list = ["鼠", "牛", "虎", "兔", "龍"]

for _ in range(10):
    random_element = random.choice(my_list)
    print(random_element)

print("------------------------------------------------------------")  # 60個

import random

lst1 = list(range(11))
lst1 = list("鼠牛虎兔龍蛇馬羊猴雞狗豬")
print(lst1)
r3 = random.choice(lst1)
print(r3)

print("------------------------------------------------------------")  # 60個

import random

# 產生六個不重複的1到49之間的隨機數字
lottery_numbers = random.sample(range(1, 50), 6)

# 將中獎號碼排序，以方便比對
lottery_numbers.sort()

# 印出中獎號碼
print("本期大樂透中獎號碼為：", lottery_numbers)

print("------------------------------------------------------------")  # 60個




"""

        data = [random.uniform(-100, 1000) for _ in range(1000)]
        data = [random.uniform(-3, 8) for _ in range(1000)]
        data = [random.uniform(1, 1000) for _ in range(100)]



random() 	隨機產生一個介於0與1之間小數

random.randint(1, 10)	產生1~10之間的整數亂數 包含頭尾
random.randint(0, 10)  #random之randint含尾, 只有這個特別不一樣


        data = list(range(10000))
        random.shuffle(data)






"""
