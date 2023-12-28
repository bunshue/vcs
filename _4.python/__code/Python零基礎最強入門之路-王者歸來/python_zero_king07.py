import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_1.py

# ch7_1.py
sum = 1+2+3+4+5+6+7+8+9+10
print("總和 = ", sum)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_2.py

# ch7_2.py -- 不完整的程式
vipNames = ['James','Linda','Peter', ... , 'Kevin']
print("客戶1 = ", vipNames[0])
print("客戶2 = ", vipNames[1])
print("客戶3 = ", vipNames[2])
...
...
print("客戶999 = ", vipNames[999])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_3.py

# ch7_3.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:
    print(player)
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_4.py

# ch7_4.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_5.py

# ch7_5.py
players = ['curry', 'jordan', 'james', 'durant', 'obama']
for player in players:
    print(player.title( ) + ", it was a great game.")
    print("I can not wait to see your next game, " + player.title( ))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_6.py

# ch7_6.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
print("列印前3位球員")
for player in players[:3]:
    print(player)
print("列印後3位球員")
for player in players[-3:]:
    print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_7.py

# ch7_7.py
n = 5
number1 = list(range(n))
print("當n值是%d時的range( )串列 = " % n, number1)
n = 8
number2 = list(range(n))
print("當n值是%d時的range( )串列 = " % n, number2)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_8.py

# ch7_8.py
n = 5
print("當n值是%d時的range( )串列元素:" % n)
for number in range(n):
    print(number)
n = 8
print("當n值是%d時的range( )串列元素:" % n)
for number in range(n):
    print(number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_9.py

# ch7_9.py
start = 2
end = 6
number1 = list(range(start, end))
print("當start值是%2d, end值是%2d時的range( )串列 = " % (start, end), number1)
start = -2
end = 3
number2 = list(range(start, end))
print("當start值是%2d, end值是%2d時的range( )串列 = " % (start, end), number2)
start = -5
end = -1
number3 = list(range(start, end))
print("當start值是%2d, end值是%2d時的range( )串列 = " % (start, end), number3)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_10.py

# ch7_10.py
start = 2
end = 6
print("當start值是%d, end值是%d時的range( )串列元素:" % (start, end))
for number in range(start,end):
    print(number)
start = -2
end = 3
print("當start值是%d, end值是%d時的range( )串列元素:" % (start, end))
for number in range(start,end):
    print(number)
start = -5
end = -1
print("當start值是%d, end值是%d時的range( )串列元素:" % (start, end))
for number in range(start,end):
    print(number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_11.py

# ch7_11.py
start = 2
end = 9
step = 2
number1 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列 = " % (start, end, step), number1)
start = -2
end = 9
step = 3
number2 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列 = " % (start, end, step), number2)
start = 5
end = -5
step = -3
number3 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列 = " % (start, end, step), number3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_12.py

# ch7_12.py
start = 2
end = 9
step = 2
number1 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)
start = -2
end = 9
step = 3
number2 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)
start = 5
end = -5
step = -3
number3 = list(range(start, end, step))
print("當start值是%2d, end值是%2d, step值是%2d時的range( )串列元素:" % (start, end, step))
for number in range(start,end,step):
    print(number)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_13.py

# ch7_13.py
n = int(input("請輸入整數:"))
number = list(range(n + 1))
total = sum(number)
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_13_1.py

# ch7_13.py
n = int(input("請輸入整數:"))
number = list(range(n + 1))
total = sum(number)
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_14.py

# ch7_14.py
n = int(input("請輸入整數:"))
number = list(range(n + 1))       # 建立串列
total = 0                         # 總計
for i in number:
    total += i
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_15.py

# ch7_15.py
n = int(input("請輸入整數:"))
total = 0                         # 總計
for i in range(1, n+1):
    total += i
print("從1到%d的總和是 = " % n, total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_16.py

# ch7_16.py
squares = []                     # 建立空串列
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    value = num * num            # 元素平方
    squares.append(value)        # 加入串列
print(squares)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_17.py

# ch7_17.py
squares = []                     # 建立空串列
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    squares.append(num ** 2)     # 加入串列
print(squares)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_18.py

# ch7_18.py
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
squares = [num ** 2 for num in range(1, n+1)]
print(squares)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_19.py

# ch7_19.py
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
    print()         # 換行輸出
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_20.py

# ch7_20.py
for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print("aa", end="")
    print()                # 換行輸出
    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_21.py

# ch7_21.py
print("測試1")
for digit in range(1, 11):
    if digit == 5:
        break
    print(digit, end=', ')
print( )
print("測試2")
for digit in range(0, 11, 2):
    if digit == 5:
        break
    print(digit, end=', ')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_22.py

# ch7_22.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama', 'Kevin', 'Lin']
n = int(input("請輸入人數 = "))
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引
for player in players:
    if index == n:
        break
    print(player, end=" ")
    index += 1                          # 索引加1


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_23.py

# ch7_23.py
scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if score < 30:                  # 小於30則不往下執行
        continue
    games += 1                      # 場次加1              
print("有%d場得分超過30分" % games)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_24.py

# ch7_24.py
players = [['James', 202],
           ['Curry', 193],
           ['Durant', 205],
           ['Jordan', 199],
           ['David', 211]]
for player in players:
    if player[1] < 200:
        continue
    print(player)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_25.py

# ch7_25.py
num = int(input("請輸入大於1的整數做質數測試 = "))
if num == 2:                                # 2是質數所以直接輸出
    print("%d是質數" % num)
else:
    for n in range(2, num):                 # 用2 .. num-1當除數測試
        if num % n == 0:                    # 如果整除則不是質數
            print("%d不是質數" % num)
            break                           # 離開迴圈

    else:                                   # 否則是質數
        print("%d是質數" % num)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_26.py

# ch7_26.py
msg1 = '人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
input_msg = ''                # 預設為空字串
while input_msg != 'q':
    input_msg = input(msg)
    print(input_msg)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_27.py

# ch7_27.py
msg1 = '人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
input_msg = ''                  # 預設為空字串
while input_msg != 'q':
    input_msg = input(msg)
    if input_msg != 'q':        # 如果輸入不是q才輸出訊息         
        print(input_msg)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_28.py

# ch7_28.py
msg1 = '人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
active = True
while active:                   # 迴圈進行直到active是False
    input_msg = input(msg)
    if input_msg != 'q':        # 如果輸入不是q才輸出訊息         
        print(input_msg)
    else:
        active = False          # 輸入是q所以將active設為False

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_29.py

# ch7_29.py
answer = 30                 # 正確數字
guess = 0                   # 設定所猜數字的初始值
while guess != answer:
    guess = int(input("請猜1-100間的數字 = "))
    if guess > answer:
        print("請猜小一點")
    elif guess < answer:
        print("請猜大一點")
    else:
        print("恭喜答對了")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_30.py

# ch7_30
index = 1
while index <= 5:
    print("第 %d 次while迴圈" % index)
    index += 1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_31.py

# ch7_31.py
i = 1                   # 設定i初始值
while i <= 9:           # 當i大於9跳出外層迴圈
    j = 1               # 設定j初始值
    while j <= 9:       # 當j大於9跳出內層迴圈
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
        j += 1          # 內層迴圈加1
    print()             # 換行輸出
    i += 1              # 外層迴圈加1
    
 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_32.py

# ch7_32.py
msg1 = '人機對話專欄,請告訴我妳喜歡吃的水果!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
while True:                     # 這是while無限迴圈
    input_msg = input(msg)
    if input_msg == 'q':        # 輸入q可用break跳出迴圈          
        break
    else:
        print("我也喜歡吃 %s " % input_msg.title( ))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_33.py

# ch7_33.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama', 'Kevin', 'Lin']
n = int(input("請輸入人數 = "))
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引index
while index < len(players):             # 是否index在串列長度範圍
    if index == n:                      # 是否達到想列出的人數
        break
    print(players[index], end=" ")
    index += 1                          # 索引index加1


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_34.py

# ch7_34.py
index = 0
while index <= 10:
    index += 1
    if ( index % 2 != 0 ):  # 測試是否奇數
        continue            # 不往下執行
    print(index)            # 輸出偶數
        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_35.py

# ch7_35.py
fruits = ['apple', 'orange', 'apple', 'banana', 'apple']
fruit = 'apple'
print("刪除前的fruits", fruits)
while fruit in fruits:      # 只要串列內有apple迴圈就繼續
    fruits.remove(fruit)
print("刪除後的fruits", fruits)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_36.py

# ch7_36.py
buyers = [['James', 1030],              # 建立買家購買紀錄
           ['Curry', 893],
           ['Durant', 2050],
           ['Jordan', 990],
           ['David', 2110]]
goldbuyers = []                         # Gold買家串列
vipbuyers =[]                           # VIP買家串列
while buyers:                           # 執行買家分類迴圈分類完成迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 1000:          # 用1000圓執行買家分類條件
        vipbuyers.append(index_buyer)   # 加入VIP買家串列
    else:
        goldbuyers.append(index_buyer)  # 加入Gold買家串列
print("VIP 買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)
    


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_37.py

# ch7_37.py
schools = ['明志科大', '台灣科大', '台北科大']
for school in schools:
    pass


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch7\ch7_38.py

# ch7_38.py
drinks = ["coffee", "tea", "wine"]
# 解析enumerate物件
for drink in enumerate(drinks):             # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")   
# 解析enumerate物件
for drink in enumerate(drinks, 10):         # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)








          



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
