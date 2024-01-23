import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

num1, num2, num3 = eval(
    input('請輸入三個數值，以逗點隔開：'))
total = num1 + num2 + num3
print('數值合計：', total)

print("------------------------------------------------------------")  # 60個


#利用 表2-2所列的內建函數將輸入數值做轉換


#int()函式將number轉為整數型別
number = int(input('輸入一個數值-> '))
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

#CH0302.py 認識正、負無限大

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH03\CH0304.py


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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH03\CH0306.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH03\CH0307.py

import math	#匯入math模組

# 使用math類別的相關方法
num1, num2 = eval(
    input('輸入兩個數值做計算-> '))

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH04\CH0401.py

# for/in廻圈配合range()函式做數值累加

total = 0 # 儲存加總結果
count = 0 # 計數器
for count in range(1, 11): # 數值1~10
   total += count          # 將數值累加
   print('累加值', total)   # 觀看累加結果
else:
   print('數值累加完畢...')
   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH04\CH0407.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH04\CH0408.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH04\CH0409.py

# 兩個數值的區間累加

total = 0

count, number = eval(input('輸人兩個數值做區間累加 -> '))
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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH04\CH0410.py

# while廻圈做分數加總

# total儲存總分，score儲存分數設，初值為0.0
total = score = 0.0
count = 0 # 計數器
score = float(input('輸入分數，按-1結束-> '))

# 當score大於「零」時就持續進行
while score >= 0.0 :    
    total = total + score
    count = count + 1
    # 檢查變數 score 非 -1 才做加總
    score = float(input('輸入分數，按-1結束-> '))

average = total / count # 計算平均值
print('共', count, '科，總分:', total,', 平均:', average)

    



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH04\CH0411.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH04\CH0412.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0501.py

# if敘述做單向判斷

#將輸入分數以int()函式轉為integer型別
score = int(input('請輸入分數-> '))
if score >= 60:
    print('Passing...')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0502.py

import math   # 滙入數學模組

radius = int(input('請輸入圓形半徑-> '))

# if/else敘述
if radius < 0:   # 半徑小於零顯示錯誤訊息
    print('輸入錯誤!!')
else:            # 半徑大於零才算出圓面積
    area = radius * radius * math.pi
    print('圓形面積：', area)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0503.py

import random   # 滙入亂數模組

# 使用三元運算子 X if C else Y
number = random.randint(0, 9) # 產生 0~9 數字
guess = eval(input('輸入一個0~9數字來猜一猜-> '))
print(f'數字{guess}猜對了' # 利用逗號來形成兩行
      if number == guess else '猜錯了')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0504.py

# 1。使用巢狀if敘述 - 由小而大做條件判斷
score = 64
if score >= 60:
    if score >= 70:
        if score >= 80:            
            if score >= 90:
                print('A')
            else:
                print('B')
        else:
            print('C')
    else:
        print('D')
else:
    print('E')

"""    
# 2.使用巢狀if敘述 - 由小而大做條件判斷

grade = int(input('請輸入分數-> '))
#grade = 68
if grade >= 90:
    print('A')
else:
    if grade >= 80:
        print('B')
    else:
        if grade >= 70:
            print('C')
        else:
            if grade >= 60:
                print('D')
            else:
                print('E')
"""


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0505.py

# 使用if/elif敘述來逐一過濾條件
score = int(input('請輸入分數-> '))

if score <= 60:
   print('請多多努力！')
elif score <= 70:
   print('表現尚可！')
elif score <= 80:
   print('不錯噢')
elif score <= 90:
   print('好成績')
else:
   print('非常好！')
"""

score = int(input('請輸入分數-> '))
if score >= 90:
   print('非常好！')
elif score >= 80:
   print('好成績！')
elif score >= 70:
   print('不錯噢')
elif score >= 60:
   print('表現尚可')
else:
   print('請多多努力！')"""


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0506.py

# if/elif敘述，依據輸入月分顯示天數

month = int(input('請輸入1~12月分-> '))

# 第一層 if/else敘述判斷輸入數值是否在1~12之間，邏輯運算子and須前後條件皆符合才會回傳True
if month >=1 and month <= 12:
    
    #第二層if/elif 多重條件
    if month == 4 or month == 6 or month == 9 \
           or month == 11:
        print(month, '月有30天！')
    elif month == 2:
        print(month, '月有28或29天！')
    else:
        print(month, '月有31天！')

else:
    print('月分在1~12之間...')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0507.py

# 使用脫逸字元
word1 = 'I\'m Student' #使用單引號
print(word1)
word2 = 'Today \"is nice day!\"' #使用雙引號
print(word2)
word3 = 'The\tLiving Beauty' #使用TAB鍵
print(word3)
word4 = 'Ah!\n the sea!' #使用換行符號
print(word4)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0508.py

# for/in廻圈讀取字串，enumerate()加入索引
name = 'Python'
print('%5s'% 'index', '%5s'% 'char')
print('-'*12)
for item in enumerate(name):
    print(' ', item)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0509.py

# 使用 %運算子格式化字串
blackTea = 45
name = input('請輸入你的名字：')
qty = int(input('輸入購買杯數：'))

print('Hi! %10s' % name)
if qty >= 10:
    total = qty * blackTea * 0.9
    print('飲料 NT$ %4.2f' % total)
else:
    total = qty * blackTea
    print("飲料 NT$ %4d" % total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0510.py

#內建函式format()
salary = int(input('請輸入薪資-> '))
# 依據薪資扣除稅額
if salary >= 28000:
    tax = salary * 0.06
elif salary >= 32000:
    tax = salary * 0.08
else: # < 28000不扣稅
    tax = 0
income = salary - tax #實領薪資
print('薪資：' , format(salary, ' >12d'))
print('扣除額 = ', format(tax, '>12,.2f'))
print('實領薪資：NT$', format(income, '>6,.2f'))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0511.py

# 使用str.format()方法或 f_string
import math	#匯入math模組

radius = int(input('輸入半徑值-> '))
#print('PI = {0.pi}'.format(math)) # 輸出PI值
print(f'PI = {math.pi}')
#計算圓面積
area = (math.pi) * radius ** 2 
#print('圓面積 = {0:,.3f}'.format(area))
print(f'圓面積 = {area:,.3f}')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH05\CH0512.py

# format()函式, f-string

#{}格式碼，欄寬分別為3，6，8 靠右對齊
print('{:>3}{:>6}{:>8}'.format('x', 'x*x', 'x*x*x'))

print('-'*20)
for item in range(1, 11):
    print(f'{item:3d} {item**2:5d} {item**3:7,d}')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0601.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0602.py

item = 0
name = 'Mary', 'Joson', 'Eric', 'Judy'   # Tuple

# while廻圈讀取元素
while item < len(name):
   print(item, name[item])
   item += 1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0603.py


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0604.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0605.py

#Packing和Unpacking的用法(2)

name = 'Tom', 'Mary'    # Tuple
t, m = name             # Unpacking
print(f'置換前:{t}, {m}')
t, m = m, t             # Swap
print(f'置換後:{t}, {m}')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0606.py

# List呼叫append()方法新增元素

ambit = 5    # 設定range()函式範圍
friends = [] # 建立空的串列

# 以for廻圈讀取資料
print('請輸入5個名字：')
for item in range(ambit):
   name = input() # 取得輸入名稱   
   # 將輸入名字以append()方法新增到List
   if name != '':
       friends.append(name)
else:
   print('輸入完畢...')

# 輸出資料
print('名字', end = '->')
for item in friends:   
   print(f'{item:7}', end = '')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0607.py

# list.sort()做遞增、遞減排序
name = ['Tom', 'Judy', 'Anthea', 'Charles']

#省略參數，依字母做遞增
name.sort()
print(f'依字母遞增排序：\n{name}')

number = [49, 131, 85, 247]
number.sort(reverse = True) #遞減排序
print('遞減排序：', number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0608.py

# BIF sorted()方法將Tuple元素排序
number = 447, 152, 814, 39, 211   #Tuple
print('原始資料：', number)

# 預設排序 -- 由小而大
print('遞增排序：', sorted(number))

# 遞減排序
print('遞減排序：', sorted(number, reverse = True))
print('原來Tuple：', number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0609.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0610.py

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

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0611.py
#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0612.py

# List生成式 找出10~65之間被7整除的數字

num = [] #建立空的List

for item in range(10, 65):
    if(item % 13 == 0):
        num.append(item) #整除的數放入List中
print('10~65被13整除之數：', num)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0613.py

# List生成式(2)
num = [] #空的List
num = [item for item in range(10, 65)if(item % 13 == 0)]
print('10~65被13整除之數：', num)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH06\CH0614.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0701.py

# 自訂函式
# step 1.定義函式 - 傳入兩個數值，比較它們的大小
def funcMax(n1, n2):
    if n1 > n2:
        result = n1
    else:
        result = n2
    return result

# step 2.呼叫函式
num1, num2 = eval(input('輸入兩個數值：'))
print('較大值', funcMax(num1, num2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0702.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0703.py

# step1 定義函式：有3個參數，運算值以return敘述回傳
def total(start, finish, step):
    outcome = 0 # 儲存計算結果
    for item in range(num1, num2+1, num3):
        outcome += item # 儲存相加結果
    return outcome

print('計算數值總和')
num1, num2, num3 = eval(input(
    '輸入起始值, 終止值, 間距值-> '))

#2.呼叫自訂函式total 
result = total(num1, num2, num3)
# 單一變數，呼叫 BIF format()做格式化輸出
print(f'總和 = {result:,}')

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0704.py

# 自訂函式，return有多個回傳值
# step1 自訂函式
def funcMulti(a, b):
    return a+b, a*b, a/b
    
#呼叫函式
one, two = eval(input('輸入兩個數值做運算:'))
result = funcMulti(one, two)
print('運算結果:')
# 針對每一個Tuple元素做格式化
print('加 = {0[0]:6d} \n乘 = {0[1]:,d}\
      \n除 = {0[2]:11.4f}'.format(result))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0705.py

# 自訂函式，呼叫main()，它會呼叫cubeV

# 定義函式一main()
def main():
    number = int(input('輸入數值：'))
    result = funCube(number)
    
# 自訂函式二 funCube
def funCube(num):
    print('立方值：')
    for item in range(1, num + 1):
        result = item ** 3
        print(format(result, ','), end = ' ')  

# 呼叫主程式
main()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0706.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0707.py

# 定義函式一
def getFruit(item, name = None):
    
    # 用is運算子判別name是否為None
    if name is None:
        name = [] # 空的List
    #append()方法新增 list 元素
    name.append(item)
    print('水果：', name)

# 定義函式二
def main():
    key = input('y 繼續..，n 結束廻圈..:')
    while key == 'y':
        wd = input('輸入水果名稱：')
        getFruit(wd) #呼叫getFruit()函式
        key = input('y繼續..，n結束廻圈..:')
        
# 呼叫main()函式
main()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0708.py

#定義函式一
def main():
    # 呼叫函式factorial()
    outcome = factorial(
        port = [5, 11, 17, 23], begin = 1)
    print(f'數值 5, 11, 17, 23 相乘結果: {outcome:,}')
    
# 定義函式二
def factorial(port, begin):
    result = begin #階乘的開始值
    for item in port:
        result *= item #讀進數值並相乘
    return result

#呼叫函式main()
main()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0709.py

# *運算式 Unpacking
pern = ('Vicky', 'Female', 65, 75, 93)   # Tuple
# Tuple做Unpacking
name, sex, *score = pern
#輸出相關的name & score
print(f'{name}: {score}')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0710.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0711.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0712.py

# 定義函式
def funcData(n1, n2, n3, n4, n5):
    print('基本資料:\n',n1, n2, n3, n4, n5)
    
#呼叫函式，使用*運算子拆解「可迭代物件
data = [1988, 3, 18]
funcData('Mary', 'Birth', *data)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0713.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0714.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH07\CH0715.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0801.py

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0802.py

from random import randint

#產生10~100的整數亂數
num1, num2 = eval(input(
    '請輸入小於100的兩個數值來產生隨意值：'))
number = randint(num1, num2)

if __name__ == '__main__':
    print('我是主程式')
print('隨意數值：', number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0803.py

from random import randint

#產生10~100的整數亂數

number = randint(10, 100)

if __name__ == '__main__':
    print('我是主程式')
else:
    print('我被當作模組')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0804.py

from CH0803 import number #匯入模組

count = 1 #統計次數
guess = 0 #儲存輸入數值

while guess != number :
   guess = int(input('輸入1~100之間的數字->'))
   # if/elif 敘述來反應猜測狀況
   if guess == number:
      print(f'第{count}次猜對，數字：{number}')
   elif guess >= number:
      print('數字太大了')
   else:
      print('數字太小了')
   count += 1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0805.py


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




