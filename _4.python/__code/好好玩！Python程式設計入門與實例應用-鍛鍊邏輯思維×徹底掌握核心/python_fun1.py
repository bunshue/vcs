import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

string = "1,2,3"
#請輸入三個數值，以逗點隔開
num1, num2, num3 = eval(string)
total = num1 + num2 + num3
print('數值合計：', total)

print("------------------------------------------------------------")  # 60個

#利用 表2-2所列的內建函數將輸入數值做轉換

#int()函式將number轉為整數型別
number = 1234
print('型別：', type(number))
print('二進位：', bin(number))
print('八進位', oct(number))
print('十六進位', hex(number))
print('10進位：', number)

# 配合format函式去除前綴字元
print('二進位：', format(number, 'b'))
print('八進位：', format(number, 'o'))
print('十六進位：', format(number, 'x'))

print("------------------------------------------------------------")  # 60個

#認識正、負無限大

import math #匯入math模組
a = 1E309
print('a = 1E309, 輸出', a)

# 輸出True，表示它是NaN
print('為NaN?', math.isnan(float(a/a)))
b = -1E309
print('b = -1309, 輸出', b)

# 輸出True，表示它是Inf
print('為Inf? ', math.isinf(float(-1E309)))

print("------------------------------------------------------------")  # 60個

#將兩個複數進行加減乘除

num1 = 3 + 5j
num2 = 2-4j
print('相加：', num1 + num2)  #回傳  5 + 1j
print('相減：', num1 - num2)  #回傳  1 + 9j
print('相乘：', num1 * num2)  #回傳 26 - 2j
print('相除：', num1 / num2)  #回傳  -0.7 + 1.1j

print("------------------------------------------------------------")  # 60個

# 將兩個數值以decimal型別來處理

# 匯入decimal模組的Decimal()方法
from decimal import Decimal
num1 = Decimal('0.5534')
num2 = Decimal('0.427')
num3 = Decimal('0.37')
print('相加', num1 + num2 + num3)
print('相減', num1 - num2 - num3)
print('相乘', num1 * num2 * num3)
print('相除', num1 / num2)

print("------------------------------------------------------------")  # 60個

# 將代數轉為算術運算式
x = 23; y = 7; #指定變數x、y的值
"""
   1. 先算出(x-5)/(y+9)
   2. 再加上 12/x 之值
   3. 最後乘 數值9 再給變數z儲存
"""
z = 9 * (12 / x + (x - 5) / (y + 9))
print('z = ', z)

print("------------------------------------------------------------")  # 60個

import math	#匯入math模組

# 使用math類別的相關方法
num1 = 3
num2 = 8

# 求平方、立方根
print('平方根：', math.sqrt(num1), ', ', num2 ** 0.5)
print(num1, '^ 3 = ', math.pow(num1, 3))
print(num2, '立方根：', math.pow(num2, 1.0/3))

print('餘數：', math.fmod(num1, num2),
      ', GCD =', math.gcd(num1, num2))
print('兩數平方後相加再開根號', math.hypot(num1, num2))

#自然對數
print('指數函式：', math.e)
print('方法exp(4) =', math.exp(4))


print("------------------------------------------------------------")  # 60個

# for/in廻圈配合range()函式做數值累加

total = 0 # 儲存加總結果
count = 0 # 計數器
for count in range(1, 11): # 數值1~10
   total += count          # 將數值累加
   print('累加值', total)   # 觀看累加結果
else:
   print('數值累加完畢...')

print("------------------------------------------------------------")  # 60個

#雙層for建立九九乘法表

# 建立表頭
print('  |', end = '')
for k in range(1, 10):
   #不自動換行，只留空白字元
   print(format(k, '3d'), end = '') 
print() #換行
print('-' * 32)
 
# 第一層 for/in
for one in range(1, 10):
   print(one, '|', end = '')   # 輸出表頭
   # 第二層 for/in
   for two in range(1, 10):
      print(format(one * two, '3d'), end = '')   # 3d 表示欄寬為3
   print() #換行

print("------------------------------------------------------------")  # 60個

# while廻圈
number = 200; a, b = 2, 2 #宣告變數
result = a ** 2

# while廻圈 變數result小於number時，輸出運算結果
print('運算結果-->')
while result < number:
    result *= b
    print(result) #輸出後換行
    #print(result, end =', ') #輸出後不換行

print("------------------------------------------------------------")  # 60個

# 兩個數值的區間累加

total = 0

string = "3, 5"

#輸人兩個數值做區間累加

count, number = eval(string)
#print('數值', count, end = '')

while count <= number:
   total += count   # 儲存累加值
   print(count, total)
   count += 1       # 計數器
   
else:
   #print(' ~', number, '累計: ', total)
   #print('結束廻圈...')
   pass

print("------------------------------------------------------------")  # 60個

# while廻圈做分數加總

# total儲存總分，score儲存分數設，初值為0.0
total = score = 0.0
count = 0 # 計數器
#score = float(input('輸入分數，按-1結束-> '))

score = 60
total = total + score
count = count + 1

score = 70
total = total + score
count = count + 1

score = 90
total = total + score
count = count + 1

score = 70
total = total + score
count = count + 1

score = 60
total = total + score
count = count + 1

average = total / count # 計算平均值
print('共', count, '科，總分:', total,', 平均:', average)

print("------------------------------------------------------------")  # 60個

# break敘述中斷廻圈的執行
print('數值：', end ='')
result = 0
for x in range(1, 11):
    result = x**2
    #如果result的值大於就中斷廻圈的執行
    if result > 20:
        break
    print(result, end = ', ')

print("------------------------------------------------------------")  # 60個

word = 'Python'

# continue敘述
print('Continue: ', end = ' ')
for cha in word:
    if cha == 't':
        continue # 只中斷此次的執行
    print(cha, end = '')

# break敘述
print('\nBreak: ', end = ' ')
for cha in word:
    if cha == 't':
        break # 中斷廻圈的執行
    print(cha, end = '')

print("------------------------------------------------------------")  # 60個

# for/in廻圈讀取字串，enumerate()加入索引
name = 'Python'
print('%5s'% 'index', '%5s'% 'char')
print('-'*12)
for item in enumerate(name):
    print(' ', item)

print("------------------------------------------------------------")  # 60個

# format()函式, f-string

#{}格式碼，欄寬分別為3，6，8 靠右對齊
print('{:>3}{:>6}{:>8}'.format('x', 'x*x', 'x*x*x'))

print('-'*20)
for item in range(1, 11):
    print(f'{item:3d} {item**2:5d} {item**3:7,d}')

print("------------------------------------------------------------")  # 60個

# 建立Tuple，+運算子串接
tp1 = 22, 44; tp2 = (11, 33)
print('串接兩個Tuple', tp1 + tp2)

tp3 = 'Mary', 'look' + ' at', ' Tom'
print(tp3)

print('\n數值     索引')
print('-' * 14)

# 建立Tuple，使用index()方法
data = 38, 14, 45, 14, 117
print(f'第1個14{data.index(14):5}')

#index()方法從索引編號2開始
print(f'第2個14{data.index(14, 2):5}')

# 搜尋最後一個要加入邊界值
print(f'   117{data.index(117, 0, 5):5}')

print("------------------------------------------------------------")  # 60個

item = 0
name = 'Mary', 'Joson', 'Eric', 'Judy'   # Tuple

# while廻圈讀取元素
while item < len(name):
   print(item, name[item])
   item += 1

print("------------------------------------------------------------")  # 60個

# Tuple物件配合Packing, Unpacking
score = [78, 56, 33] # List
chin, math, eng = score # Unpacking

print(f'國文：{chin:2d} 數學：{math:2d} 英文：{eng:2d}')
print(f'總分：{sum(score)}')

n = 'Eric'; b = '1998/4/17'; t = 175
tp = (n, b, t)         # Packing
name, birth, tall = tp # Unpacking

print(f'名字：{name:>4s}')
print(f'生日：{birth:9s}, 身高：{tall}')

print("------------------------------------------------------------")  # 60個

#Packing和Unpacking的用法(2)

name = 'Tom', 'Mary'    # Tuple
t, m = name             # Unpacking
print(f'置換前:{t}, {m}')
t, m = m, t             # Swap
print(f'置換後:{t}, {m}')

print("------------------------------------------------------------")  # 60個

# list.sort()做遞增、遞減排序
name = ['Tom', 'Judy', 'Anthea', 'Charles']

#省略參數，依字母做遞增
name.sort()
print(f'依字母遞增排序：\n{name}')

number = [49, 131, 85, 247]
number.sort(reverse = True) #遞減排序
print('遞減排序：', number)

print("------------------------------------------------------------")  # 60個

# BIF sorted()方法將Tuple元素排序
number = 447, 152, 814, 39, 211   #Tuple
print('原始資料：', number)

# 預設排序 -- 由小而大
print('遞增排序：', sorted(number))

# 遞減排序
print('遞減排序：', sorted(number, reverse = True))
print('原來Tuple：', number)

print("------------------------------------------------------------")  # 60個

#呼叫list.sort()方法將Tuple元素排序

name = 'Tom', 'Charles', 'Vicky', 'Judy'
print('Tuple排序前：')
print(name)

# 1.Tuple以list()函式轉為List物件，再做排序
covlt = list(name)
covlt.sort()

# 2.排序後再以tuple()函式轉為Tuple
covtp = tuple(covlt)
print('Tuple排序後：')
print(covtp)


print("------------------------------------------------------------")  # 60個

"""
# 將輸入的分數先儲存於List，再以sum()函式加總

score = [] # 建立List來存放成績

# for廻圈建立輸入成績的list
for item in range(5):
   data = int(input('分數%2d ' %(item + 1)))
   score += [data]
print('%5s %5s ' % ('index', 'score'))

ind = 0 #計數器，每讀取一個元素就位移一個

#while廻圈讀取成績並輸出
while ind < len(score):
   print(f'{ind:3d} {score[ind]:4d}')
   ind += 1

print('-' * 12)
# 內建函式sum()計算總分
print(f'總分 = {sum(score)}, 平均 = {sum(score) / 5}')
score.sort(reverse = True) # score()方法遞減排序
print('遞減排序：', score)
print('遞增排序：', sorted(score)) # 使用BIF
"""

print("------------------------------------------------------------")  # 60個

# List生成式 找出10~65之間被7整除的數字

num = [] #建立空的List

for item in range(10, 65):
    if(item % 13 == 0):
        num.append(item) #整除的數放入List中
print('10~65被13整除之數：', num)


print("------------------------------------------------------------")  # 60個

# List生成式(2)
num = [] #空的List
num = [item for item in range(10, 65)if(item % 13 == 0)]
print('10~65被13整除之數：', num)

print("------------------------------------------------------------")  # 60個

#應用一：計算分數平均
score = [(85, 75, 46, 91), (49, 76, 87),
        (76, 93, 67)]
avg = [sum(item)/len(item) for item in score]
print(f'平均: {avg[0]:.3f}, {avg[1]:.3f},\
      {avg[2]:.3f}')
print() #換行

#應用二：讀取字串長度
fruit = ['lemon', 'apple', 'orange', 'blueberry']
print('%9s'%'字串', '%2s'%'長度')
print('*----------------*')
print('\n'.join(['%10s:%2d'%(
    item, len(item)) for item in fruit]))

print("------------------------------------------------------------")  # 60個

# 自訂函式 情形一：無參數，無回傳值

# step 1. 定義函式
def message():
    zen = """
        Beautiful is better than ugly.
        Explicit is better than implicit.
    """
    print(zen)

# step 2. 呼叫函式
message()

print("------------------------------------------------------------")  # 60個

#定義函式
def funcTest(name, score):
    print('定義函式的。。。')
    name = 'Judy'      #情形一
    score.append(83)   #情形二
    print(name, 'id =', id(name))    
    print(score, 'id =', id(score))
    
#呼叫函式
one = 'Mary'; two = [75, 68]
funcTest(one, two)

print('\n呼叫函式時...')
print(one, '分數：', two)

#name不可變物件, score為可變物件
print('one', 'id =', id(one))
print('two', 'id =', id(two))

print("------------------------------------------------------------")  # 60個

# *運算式 Unpacking
pern = ('Vicky', 'Female', 65, 75, 93)   # Tuple
# Tuple做Unpacking
name, sex, *score = pern
#輸出相關的name & score
print(f'{name}: {score}')

print("------------------------------------------------------------")  # 60個

#定義函式
def funTest(*number):
    outcome = 1
    for item in number:
        outcome *= item
    return outcome

#呼叫函式
print('1個引數:', funTest(7))
print('2個引數:', funTest(12, 3))
print('4個引數:', funTest(3, 5, 9, 14))

print("------------------------------------------------------------")  # 60個

#自訂函式
def student(name, *score, subject = 4):
    if subject >= 1:        
        print(f'{name:6}{subject} 科', end = '')
        #print(f'{name}{subject}{*score}')
        print('分數 ', *score)
    total = sum(score) # 合計分數
    print(f'總分: {total}',
          f'平均: {total / subject:.4f}')

#呼叫函式
student('Peter', 65, 93, 82, 47)
print()
student('Judy', 85, 69, 79, subject = 3)

print("------------------------------------------------------------")  # 60個

# 定義函式
def funcData(n1, n2, n3, n4, n5):
    print('基本資料:\n',n1, n2, n3, n4, n5)
    
#呼叫函式，使用*運算子拆解「可迭代物件
data = [1988, 3, 18]
funcData('Mary', 'Birth', *data)

print("------------------------------------------------------------")  # 60個

# 定義函式
def person(name, salary, s2, s3):
    print(name)
    # format()函式分設欄寬為10, 6 並加千位符號
    print(f'扣除額：{(s2 + s3):11,}')
    salary =  salary - s2 - s3    
    print(f'實領金額 NT$ {salary:6,}')
        
income = [28800, 605, 405]
#呼叫函式 -- number串列物件，可迭代
person('Tomas', *income)

print("------------------------------------------------------------")  # 60個

# List 含有 Tuple
student = [('Eugene', 1989, 'Taipei'),
            ('Davie', 1993, 'Kaohsiung'),
            ('Michelle', 1999, 'Yilan'),
            ('Peter', 1988, 'Hsinchu'),
            ('Connie', 1997, 'Pingtung')]

#定義sort()方法參數key
na = lambda item: item[0] 
student.sort(key = na)
print('依名字排序：')
for name in student:
    print('{:6s},{}, {:10s}'.format(*name))

#直接在sort()方法帶入lamdba()函式
student.sort(key = lambda item: item[2],
             reverse = True)
print('依出生地遞減排序：')
for name in student:
    print('{:6s},{}, {:10s}'.format(*name))

print("------------------------------------------------------------")  # 60個

fruit = 'Apple'
# 定義函式
def Favorite():
    global fruit
    print('Favorite fruit is', fruit)
    fruit = 'Blueberry'
    print('I like', fruit, 'ice cream.')
    
# 呼叫函式
Favorite()

print("------------------------------------------------------------")  # 60個

from random import randint, randrange

#產生某個區間的整數亂數
def numRand(x, y):
    cout = 1 # 計數器
    while cout <= 10: 
        number = randint(x, y)
        print(number, end = ' ')
        cout += 1
    print()

# 將產生以append()方法加至List
def numRand2(x, y):
    cout = 1
    result = [] # 存放亂數
    while cout <= 10:
        number = randint(x, y)
        result.append(number)
        cout += 1
    return result

print("------------------------------------------------------------")  # 60個

from random import randint

#產生10~100的整數亂數

number = randint(10, 100)

if __name__ == '__main__':
    print('我是主程式')
else:
    print('我被當作模組')

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個




