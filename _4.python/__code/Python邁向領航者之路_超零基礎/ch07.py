# ch7_1.py
sum = 1+2+3+4+5+6+7+8+9+10
print("總和 = ", sum)

print('------------------------------------------------------------')	#60個




#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_2.py

# ch7_2.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:
    print(player)
    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_3.py

# ch7_3.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama']
for player in players:print(player)
    


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_4.py

# ch7_4.py
players = ['curry', 'jordan', 'james', 'durant', 'obama']
for player in players:
    print(player.title( ) + ", it was a great game.")
    print("我迫不及待想看下一場比賽, " + player.title( ))


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_5.py

# ch7_5.py
files = ['da1.c','da2.py','da3.py','da4.java']
py = []
for file in files:
    if file.endswith('.py'):    # 以.py為副檔名
        py.append(file)         # 加入串列
print(py)









print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_6.py

# ch7_6.py
n = int(input("請輸入星號數量 : ")) # 定義星號的數量                           
for number in range(n):             # for迴圈    
    print("*",end="")               # 列印星號
    



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_7.py

# ch7_7.py
money = 50000
rate = 0.015
n = 5
for i in range(n):
    money *= (1 + rate)
    print("第 %d 年本金和 : %d" % ((i+1),int(money)))





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_8.py

# ch7_8.py
n = int(input("請輸入n值 : "))
sum = 0
for num in range(1,n+1):
    sum += num
print("總和 = ", sum)



    



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_9.py

# ch7_9.py
start = 2
end = 9
step = 2
number1 = list(range(start, end, step))
print("start=%2d, end=%2d, step=%2d的串列 = " % (start, end, step), number1)
start = -2
end = 9
step = 3
number2 = list(range(start, end, step))
print("start=%2d, end=%2d, step=%2d的串列 = " % (start, end, step), number2)
start = 5
end = -5
step = -3
number3 = list(range(start, end, step))
print("start=%2d, end=%2d, step=%2d的串列 = " % (start, end, step), number3)

print('------------------------------------------------------------')	#60個




#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_10.py

# ch7_10.py
squares = []                     # 建立空串列
n = int(input("請輸入整數:"))
if n > 10 : n = 10               # 最大值是10
for num in range(1, n+1):        
    value = num * num            # 元素平方
    squares.append(value)        # 加入串列
print(squares)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_11.py

# ch7_11.py
h = eval(input('請輸入星形高度 : '))
for i in range(h):
    print(' '*(h-i-1)+'*'*(2*i+1))





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_12.py

# ch7_12.py
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
    print()         # 換行輸出
    


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_13.py

# ch7_13.py
scores = [94, 82, 60, 91, 88, 79, 61, 93, 99, 77]
scores.sort(reverse = True)         # 從大到小排列
count = 0
for sc in scores:
    count += 1
    print(sc, end=" ")
    if count == 5:                  # 取前5名成績
        break                       # 離開for迴圈




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_14.py

# ch7_14.py
scores = [33, 22, 41, 25, 39, 43, 27, 38, 40]
games = 0
for score in scores:
    if score < 30:                  # 小於30則不往下執行
        continue
    games += 1                      # 場次加1              
print("有%d場得分超過30分" % games)



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_15.py

# ch7_15.py
msg1 = '人機對話專欄,告訴我心事吧,我會重複你告訴我的心事!'
msg2 = '輸入 q 可以結束對話'
msg = msg1 + '\n' + msg2 + '\n' + '= '
input_msg = ''                  # 預設為空字串
while input_msg != 'q':
    input_msg = input(msg)
    if input_msg != 'q':        # 如果輸入不是q才輸出訊息         
        print(input_msg)



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_16.py

# ch7_16.py
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



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_17.py

# ch7_17.py
i = 1                   # 設定i初始值
while i <= 9:           # 當i大於9跳出外層迴圈
    j = 1               # 設定j初始值
    while j <= 9:       # 當j大於9跳出內層迴圈
        result = i * j
        print("%d*%d=%-3d" % (i, j, result), end=" ")
        j += 1          # 內層迴圈加1
    print()             # 換行輸出
    i += 1              # 外層迴圈加1
    


 

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_18.py

# ch7_18.py
store = 'DeepMind購物中心'
products = ['電視','冰箱','洗衣機','電扇','冷氣機']
cart = []                       # 購物車
print(store)
print(products,"\n")
while True:                     # 這是while無限迴圈
    msg = input("請輸入購買商品(q=quit) : ")
    if msg == 'q' or msg=='Q':
        break
    else:
        if msg in products:
            cart.append(msg)

print("今天購買商品", cart)





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_19.py

# ch7_19.py
sc = [[1, '洪錦魁', 80, 95, 88, 0, 0, 0],
      [2, '洪冰儒', 98, 97, 96, 0, 0, 0],
      [3, '洪雨星', 91, 93, 95, 0, 0, 0],
      [4, '洪冰雨', 92, 94, 90, 0, 0, 0],
      [5, '洪星宇', 92, 97, 90, 0, 0, 0],
     ]
# 計算總分與平均
print("填入總分與平均")
for i in range(len(sc)):
    sc[i][5] = sum(sc[i][2:5])              # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)     # 填入平均
    print(sc[i])
sc.sort(key=lambda x:x[5],reverse=True)     # 依據總分高往低排序
# 以下填入名次
print("填入名次")
for i in range(len(sc)):                    # 填入名次
    sc[i][7] = i + 1
    print(sc[i])
# 以下依座號排序
sc.sort(key=lambda x:x[0])                  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])


















print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_20.py

# ch7_20.py
x = 1000000
pi = 0
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        print("當 i = %7d 時 PI = %20.19f" % (i, pi))


  













          



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_21.py

# ch7_21.py
prime = []
num = int(input("請輸入大於1的整數做質數測試 = "))
if num == 2:                                # 2是質數所以直接輸出
    prime.append(num)
else:
    for n in range(2, num):             # 用2 .. num-1當除數測試
        if num % n == 0:                # 如果整除則不是質數
            break                       # 離開迴圈
    else:                               # 否則是質數
        prime.append(num)
if prime:                   
    print("{} 是質數".format(num))
else:                                   
    print("{} 不是質數".format(num))



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_22.py

# ch7_22.py
e = 1
val = 1
for i in range(1,101):
    val = val / i
    e += val
    if i % 10 == 0:
        print("當i是 %3d 時 e = %40.39f" % (i, e))


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_23.py

# ch7_23.py
chicken = 0
while True:
    rabbit = 35 - chicken                       # 頭的總數
    if 2 * chicken + 4 * rabbit == 100:         # 腳的總數
        print('雞有 {} 隻, 兔有 {} 隻'.format(chicken, rabbit))
        break
    chicken += 1





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch07\ch7_24.py

# ch7_24.py
sum = 0
for i in range(64):
    if i == 0:
        wheat = 1
    else:
        wheat = 2 ** i
    sum += wheat       
print('麥粒總共 = {}'.format(sum))



print('------------------------------------------------------------')	#60個


