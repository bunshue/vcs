import sys

import random
import numpy as np

print("------------------------------------------------------------")  # 60個


import random

target = random.randint(1, 100)
print("1~100亂數值: " + str(target))





CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

print('The category is:', CATEGORY)
secretWord = random.choice(WORDS)  # The word the player must guess.

print(secretWord)




print('從常態分佈抽樣')

N = 100
L = np.random.randn(N)

print(L.mean())
print(L.std())


print("------------------------------------------------------------")  # 60個

import random

for i in range(5):
    a = random.randint(1,10) #隨機取得整數
    print(a,end=' ')
print()
#給定items數列的初始值
items = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
random.shuffle(items)  #使用shuffle函數洗牌
print(items)#將洗牌後的序列輸出


print("------------------------------------------------------------")  # 60個

import random as r

print( r.random() ) #產生隨機浮點數n,0 <= n < 1.0
print( r.uniform(101, 200) ) #產生101-200之間的隨機浮點數
print( r.randint(-50, 0) ) #產生-50-0之間的隨機整數
print( r.randrange(0, 88, 11) ) #從序列中取一個隨機數
print( r.choice(["健康", "運勢", "事業", "感情", "流年"]) ) #

items = ['a','b','c','d']
r.shuffle(items) #將items序列打亂
print( items )
#從序列或集合擷取12個不重複的元素
print( r.sample('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', 12))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\range1.py

import random as r #以別名方式匯入random模組
for i in range(10): #執行10次
    print ( r.randrange(2, 500, 2) ) #從2-500間取10個偶數

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\range2.py

import random as r #以別名方式匯入random模組
for i in range(10): #執行10次
    print(r.randrange(100)) #從0-100取隨機整數

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\rint.py

import random as r #為random模組取別名
for j in range(6): #以迴圈執行6次
    print(r.randint(1,42), end=' ')#產生1-42的整數亂數
print() #換行1
for j in range(3): #以迴圈執行3次
    print(r.uniform(1,10), end=' ')#產生1-10間的亂數



print("------------------------------------------------------------")  # 60個



import random

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



import random

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


import random

for _ in range(10):
    cc = random.randrange(0, 100)
    print(cc)

print("------------------------------------------------------------")  # 60個

import random  # 導入模組random

lotterys = random.sample(range(1, 50), 7)  # 7組號碼
specialNum = lotterys.pop()  # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):  # 排序列印大樂透號碼
    print(lottery, end=" ")
print("\n特別號:%d" % specialNum)  # 列印特別號




print("------------------------------------------------------------")  # 60個


rawdata = """我
我的
眼睛
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止"""
words = rawdata.split("\n")


def poem():
    n = np.random.randint(2, 8)  # 2-8句, 決定有幾句

    for i in range(n):
        m = np.random.randint(1, 6)  # 決定每句的長度
        sentence = np.random.choice(words, m, replace=False)
        print(" ".join(sentence))


poem()




print("------------------------------------------------------------")  # 60個




import numpy as np

a = np.random.randint(0, 5, 10)
print(a)
print(np.unique(a))  # unique統計陣列中所有不同的值

print(np.bincount(a))  # bincount統計整數陣列中每個元素出現的次數

print("------------------------------------------------------------")  # 60個

print("設計一個函數產生指定長度的驗證碼，驗證碼由大小寫字母和數字構成。\n")

import random

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

print("np亂數建立一維陣列 1 ~ 7(不含尾), 300個")
a = np.random.randint(1, 7, 300)
print(a)

print("np亂數建立二維陣列 1 ~ 7(不含尾), 6X4")
a = np.random.randint(1, 7, (6, 4))
print(a)

for _ in range(10):
    a = np.random.uniform()
    print(a)


print("------------------------------------------------------------")  # 60個

x = np.random.normal(1,4,(3,5))
x = np.random.normal(1,4,(3,5))
y = np.argmax(x,axis=1)
print(x)
print(x.shape)
print(y)
print(y.shape)
                                                                                                                  
print('查詢函數用法')
help(np.max)

print("------------------------------------------------------------")  # 60個
N = 10
y = np.random.randn(N)

print(y)


print("------------------------------------------------------------")  # 60個

import random  # 導入模組random

fruits = ["蘋果", "香蕉", "西瓜", "水蜜桃", "百香果"]

count = []
for _ in range(10):
    cc = random.choice(fruits)
    print(cc)

print("------------------------------------------------------------")  # 60個


import random

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



import random

name = ["小明", "小黃", "小紅", "小綠", "小白"]

print("抽取一個元素：", random.choice(name))
print("抽取三個元素：", random.sample(name, 3))
print("抽取三個元素：", random.shuffle(name))

print("------------------------------------------------------------")  # 60個

import random

print("任一整數", random.randrange(100))
print("任一整數", random.randrange(52, 100))
print("奇數", random.randrange(1, 100, 2))
print("偶數", random.randrange(0, 100, 2))




print("------------------------------------------------------------")  # 60個


import random

for i in range(5):
    a = random.randint(1,10) #隨機取得整數
    print(a,end=' ')
print()
#給定items數列的初始值
word = ['apple','bird','tiger','happy','quick']
random.shuffle(word)  #使用shuffle函數打亂字的順序
print(word)#將打亂後字依序輸出



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




