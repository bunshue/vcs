import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch01\first.py

print("我的第一支Python程式")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\add.py

no1=input("請輸入第1個浮數: ")
no2=input("請輸入第2個浮數: ")
print("兩數的和",float(no1)+float(no2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\bool.py

print( bool(0) )
print( bool("") )
print( bool(" ") )
print( bool(1) )
print( bool("XYZ") )

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\carry.py

num=123
print(num)
num1=bin(num) #2進位
print(num1)
num2=oct(num) #8進位
print(num2)
num3=hex(num) #16進位
print(num3)
print(int(num1,2)) #將2進位的字串轉換成10進位數值
print(int(num2,8)) #將8進位的字串轉換成10進位數值
print(int(num3,16))#將16進位的字串轉換成10進位數值

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\change.py

str = "{1} * {0} = {2}"
a = 3
b = "5"
print(str.format(a, b, a * int(b)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\date.py

print("請輸入日期(YYYY-MM-DD)：")
year=input()
month=input()
day=input()
print("日期：%s-%s-%s" %(year, month, day))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\digit.py

print("請輸入一個十進位數: ",end="")
Val=int(input())
print("Val的八進位數=%o" %Val)#以%o格式化字元輸出
print("Val的十六進位數=%x" %Val)#以%x格式化字元輸出 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\earth.py

print("請輸入您的體重(公斤):",end="")
weight=int(input())#輸入體重
print("您在月球上體重為：%.5f 公斤" %(weight * 0.17))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\format_1.py

company="藍海科技股份有限公司"
year=27
print("{}已成立公司 {} 年" .format (company, year))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\format_2.py

print("{0:10}收入：{1:_^12}".format("Axel", 52000))
print("{0:10}收入：{1:>12}".format("Michael", 87000))
print("{0:10}收入：{1:*<12}".format("May", 36000))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\print_%.py

num = 168
print ("數字 %s 的浮點數：%5.1f" % (num,num))
print ("數字 %s 的八進位：%o" % (num,num))
print ("數字 %s 的十六進位：%x" % (num,num))
print ("數字 %s 的二進位：%s" % (num,bin(num)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\salary.py

print("編號 姓名    底薪  業務獎金 加給補貼")
print("%3d %3s %6d %6d %6d" %(801,"朱正富",32000,10000,5000))
print("%3d %3s %6d %6d %6d" %(805,"曾自強",35000,8000,7000))
print("%3d %3s %6d %6d %6d" %(811,"陳威動",43000,15000,6000))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\str_error.py

print("13579")
print("1+2")
print("Hello, how are you?")
print("I'm all right, but it's raining.")
print('I\'m all right, but it\'s raining.')
print("I"m all right, but it"s raining.")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\type.py

print(type(23))  #輸出結果 <class 'int'>
print(type(3.14)) #輸出結果 <class 'float'>
print(type("happy birthday")) #輸出結果 <class 'str'>
print(type(True)) #輸出結果 <class 'bool'>

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch02\variable.py

num1=30
print(num1)
num1="happy"
print(num1)
a=b=12
print(a,b)
name,salary,weight="陳大富",60000,85.7
print(name,salary,weight)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\bit_op.py

x = 15; y = 10
print(x & y)  
print(x ^ y)   
print(x | y)  
print(~x)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\coin.py

print("請輸入將兌換金額: ",end="")
num=int(input())
hundred=num//100
fifty=(num-hundred*100)//50
ten=(num-hundred*100-fifty*50)//10
print("百元鈔有%d張 五十元鈔有%d張 十元鈔有%d張" %(hundred,fifty,ten))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\compare.py

a=19; b=13 
#比較運算子運算關係
print("a=%d b=%d " %(a,b))
print("--------------------------------")
print("a>b,比較結果為 %d 值" %(a>b))
print("a<b,比較結果為 %d 值" %(a<b))
print("a>=b,比較結果為 %d 值" %(a>=b))
print("a<=b,比較結果為 %d 值" %(a<=b))
print("a==b,比較結果為 %d 值" %(a==b))
print("a!=b,比較結果為 %d 值" %(a!=b))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\compound.py

num=8
num*=9
print(num)
num+=1
print(num)
num//=9
print(num)
num %= 5
print(num)
num -= 2
print(num)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\cost.py

x=(765/17+1)*2*210;
print("共需花費: %d 元" %x)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\logic.py

a,b,c=5,10,6
result = a>b and b>c;   #條件式a>b的傳回值與條件式b>c的傳回值做and運算
result = a<b or c!=a;   #條件式a<b的傳回值與條件式c!=a的傳回值做or運算
result = not result;	#將result的值做not運算

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\math.py

a=10;b=7;c=20
print(a/b)
print((a+b)*(c-10)/5)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\math1.py

A=5;B=8;C=10
B=B+1
A=B*(C-A)/(B-A)
print("A= ",A)
print("B= ",B)
print("C= ",C)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\mod.py

print("請輸入三位數以上整數: ", end="")
num=int(input())
num=(num/100)%10;
print("百位數的數字為%d" %num)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\relation.py

a,b,c=3,5,7 #宣告a、b及c三個整數變
print("a= %d b= %d c= %d" %(a,b,c))
print("====================================")
print("a<b and b<c or c<a = %d" %(a<b and b<c or c<a))
print("not(a==b)and (not a<b) = %d" %(not(a==b)and (not a<b)))
#包含關係與邏輯運算子的運算式求值

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch03\shift.py

b = 13
print(b << 2)
print(b >> 1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch04\35.py

value=int(input("請任意輸入一個整數："))
if value%5==0 or value%7==0: #判斷是否為5或7的倍數
    if value%35 !=0:
         print("符合所要的條件")
    else:
         print("不符合所要的條件") 
else:
    print("不符合所要的條件")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch04\caculator.py

a=float(input("請輸入a:"))
b=float(input("請輸入b:"))
op_key=input("請輸入+,-,*,/鍵：")#輸入字元並存入變數op_key
if op_key=='+': #如果op_key等於'+'
    print("{} {} {} = {}".format(a, op_key, b, a+b))
elif op_key=='-': #如果op_key等於'-'
    print("{} {} {} = {}".format(a, op_key, b, a-b))
elif op_key=='*': #如果op_key等於'*'
    print("{} {} {} = {}".format(a, op_key, b, a*b))
elif op_key=='/': #如果op_key等於'/'
    print("{} {} {} = {}".format(a, op_key, b, a/b))
else: #如果op_key不等於 + - * / 任何一個
    print("運算式有誤")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch04\exam.py

#定義整數變數 Score，儲存學生成績
Score=int(input("輸入學生的分數:"))
if Score>=60: #if 條件敘述
     print("得到 %d 分，還不錯唷..." %Score)
else:
     print("不太理想喔...，只考了 %d 分" %Score)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch04\function.py

print("功能選單") 
print(" 0.歡迎詞")
print(" 1.註冊會員資料" )
print(" 2.新增訂單")
print(" 3.查詢出貨明細")
print("請點選您要的項目:" )
Select=int(input()) 
if Select == 0: 
    print("歡迎光臨本系")
elif Select == 1: 
    print("呼叫註冊會員資料程式")
elif Select == 2: 
    print("呼叫新增訂單程式" )
elif Select == 3: 
    print("呼叫查詢出貨明細程式" )
else: #輸入錯誤的處理
    print("請重新選擇")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch04\leapYear.py

year = int(input("請輸入西元年份："))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("%d 是閏年" %year)
else :
    print("%d 是平年" %year)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch04\lotto.py

Result=77 #儲存答案
print("猜猜今晚樂透號碼(2位數): ",end="")
Select=int(input())
if Select!=Result:
     print("猜錯了....")
     print("答案是%d" %Result)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch04\nestif.py

Score=int(input("輸入學生的分數:")) #輸入學生成績
if Score > 100:     #判斷是否超過 
    print("輸入的分數超過 100.")
else:
    if Score<0: #判斷是否低於0
        print("怎麼會有負的分數??")
    else:
        if Score >= 60: #判斷是否及格
            print("得到 {}分，還不錯唷...".format(Score))
        else:
            print("不太理想喔...，只考了 {} 分".format(Score))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch04\shop.py

print("請輸入總消費金額：",end="")
charge=int(input())
#如果消費金額大於等於2000
if charge>=2000: print("請到10F領取周年慶禮品")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch04\six.py

value=int(input("請任意輸入一個整數："))
if value%2==0 or value%3==0: #判斷是否為2或3的倍數
    if value%6!=0:
         print("符合所要的條件")
    else:
         print("不符合所要的條件") #為6的倍數 
else:
    print("不符合所要的條件")

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\break.py

total=0
for i in range(1,201,2):
    if i==101:
        break
    total+=i
print("1~99的奇數總和:%d" %total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\common.py

a=1
n=int(input("請輸入一個數字："))
print("%d 的所有因數為:" %n,end="")
while a<=n: #定義while迴圈,且設定條件為a<=n
    if n%a==0: #當n能夠被a整除時~則a就是n的因數
        print("%d " %a,end="")
        if n!=a: print(",",end="")
    a+=1 #a值遞增1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\continue.py

for x in range(1, 10):
    if x == 5:
        continue
    print( x, end=" ")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\divide.py

print("求取兩正整數的最大公因數(g.c.d):")
print("輸入兩個正整數:")
#輸入兩數
Num1=int(input())
Num2=int(input())
if Num1 < Num2:
    TmpNum=Num1                           
    Num1=Num2
    Num2=TmpNum#找出兩數較大值
while Num2 != 0:
    TmpNum=Num1 % Num2            
    Num1=Num2                              
    Num2=TmpNum #輾轉相除法
print("最大公因數(g.c.d)的值為:%d" %Num1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\enum.py

phrase = ["三陽開泰", "事事如意", "五福臨門"]
for index, x in enumerate(phrase):
    print ("{0}--{1}".format(index, x))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\equation.py

total=0
n=int(input("請輸入任一整數:"))
if n>=1 or n<=100:
    for i in range(n+1):
        total+=i*i  #1*1+2*2+3*3+..n*n
    print("1*1+2*2+3*3+...+%d*%d=%d" %(n,n,total))
else:
    print("輸入數字超出範圍了!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\fac.py

total=0
n1=1
n=int(input("請輸入任一整數:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        n1*=j #n!的值
    total+=n1 #1!+2!+3!+..n!
    n1=1
print("1!+2!+3!+...+%d!=%d" %(n,total))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\factor.py

a=1
n=int(input("請輸入一個整數數字："))
print("%d的所有正因數為:" %n)
while a<=n:
    if n%a==0: #當n能夠被a整除時~則a就是n的因數
        print(a,end="")
        if n!=a: print(",",end="")
    a+=1 #a值遞增1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\innerbreak.py

for a in range(1,6): #外層for迴圈控制
    for b in range(1,a+1): #內層for迴圈控制
        if b==4:
            break
        print(b,end="") #印出b的值
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\max.py

MAX= 0
num=int(input("準備輸入數字的個數："))
for i in range(num): #利用for迴圈來輸入與尋找最大值
    print(">",end="")
    temp=int(input())
    if MAX<temp:
        MAX=temp
print("這些數字中的最大值為：%d" %MAX)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\min.py

MIN= 99999
num=int(input("準備輸入數字的個數："))
for i in range(num): #利用for迴圈來輸入與尋找最小值
    print(">",end="")
    temp=int(input())
    if MIN>temp:
        MIN=temp
print("這些數字中的最大小值為：%d" %MIN)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\odd.py

total=0
for count in range(1, 100, 2): 
    total += count #將數值累加
print("數值1~100之間的奇數累計=",total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\prime.py

n=int(input("請輸入n的值,n表示2~n之間的所有質數:"))
i=2;
while i<=n:
    no_prime=0
    for j in range(2,i,1):
        if i%j==0:
            no_prime=1
            break  #跳出迴圈
    if no_prime==0:
        print("%d " %i); #輸出質數
    i+=1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\rev.py

n=int(input("請輸入任一整數:"))
print("反向輸出的結果:",end="")
while n!=0:
    print("%d" %(n%10),end="") #求出餘數值
    n//=10
print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\sigma.py

k=int(input("請輸入k值："))
sigma=0
for n in range(int(k)+1):
    if(n % 2!=0): #如果n是奇數
        sigma += float(-1/(2*n+1))
    else:  #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\sum.py

total=0
for count in range(1, 101): #數值1~100
    total += count #將數值累加
print("數字1累加到100的總和=",total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\table.py

for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch05\while.py

x, y = 1, 10
while x < y:
    print(x, end = ' ')
    x += 1

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\align.py

str1 = 'Python is funny and powerful'
print('原字串', str1)
print('欄寬40，字串置中', str1.center(40))
print('字串置中，* 填補', str1.center(40, '*'))
print('欄寬10，字串靠左', str1.ljust(40, '='))
print('欄寬40，字串靠右', str1.rjust(40, '#'))

mobilephone = '931666888'
print('字串左側補0:', mobilephone.zfill(10))

str2 = 'Mayor,President'
print('以逗點分割字元', str2.partition(','))

str3 = '禮\n義\n廉\n恥'
print('依\\n分割字串', str3.splitlines(False))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\append.py

num=int(input('請輸入總人數: '))
student = [] 
print('請輸入{0}個數值：'.format(num))

# 依序讀取分數
for item in range(1,num+1):
    score = int(input()) #取得輸入數值
    student.append(score) #新增到串列

print('總共輸入的分數', end = '\n')
for item in student:   
    print('{:3d} '.format(item), end = '')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\column.py

print("|a1 b1|")
print("|a2 b2|")
arr=[[]*2 for i in range(2)]
arr=[[0,0],[0,0]]
arr[0][0]=int(input("請輸入a1:"))
arr[0][1]=int(input("請輸入b1:"))
arr[1][0]=int(input("請輸入a2:"))
arr[1][1]=int(input("請輸入b2:"))
ans= arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0] #求二階行列式的值
print("| %d %d |" %(arr[0][0],arr[0][1]))
print("| %d %d |" %(arr[1][0],arr[1][1]))
print("ans= %d" %ans)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\count.py

str1="Happy birthday to my best friend."
s1=str1.count("to",0) #從str1字串索引0的位置開始搜尋
s2=str1.count("e",0,34) #搜尋str1從索引值0到索引值34-1的位置
print("{}\n「to」出現{}次,「e」出現{}次".format(str1,s1,s2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExCarry.py

i = 10

for j in range(5):
    z = i + j
    print("小寫：%x\t大寫：%X" %(z, z))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\Exdict.py

dictStudent = {}

def isHasKeyAndNotNone():
    findKey = str(input("請輸入欲查詢的key："))
    
    if findKey in dictStudent and dictStudent.get(findKey, None) == None:
        EditData(findKey)
        
    elif findKey in dictStudent and dictStudent.get(findKey, None) != None:
        print("%s的值：%s" %(findKey, dictStudent[findKey]))
        CheckOtherKeyValue()
        
    else:
        dictStudent.setdefault(findKey, None)
        print("%s不存在已自動建立key" %(findKey))

def EditData(findKey):
    strInputValue = str(input("請輸入值："))
    dictStudent[findKey] = strInputValue
    CheckOtherKeyValue()

def CheckOtherKeyValue():
    for key, values in dictStudent.items():
        if values == None:
            print(dictStudent)
            strCheck = str(input("目前還有其他欄位值為None，是否繼續進行編輯(Y/N)："))

            while strCheck == "Y":
                isHasKeyAndNotNone()
            else:
                print(dictStudent)
                break

strFieldName = str(input("請輸入欄位名稱(以逗號分隔)："))
dictStudent = dictStudent.fromkeys(strFieldName.split(","))

isHasKeyAndNotNone()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExFloat.py

print("\n不足數位補0：%06.2f\n" %(1.2345))

print("不足數位預設空格：%6.2f\n" %(1.2345))

print("小數點保留2位：%.2f\n" %(1.2345))

print("不足數位補0(以*替代)：%0*.2f\n" %(6, 1.2345))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExInteger.py

print("\n不足數位補0：%05d\n" %(66))

print("不足數位預設空格：%5d\n" %(66))

print("小於位數則輸出全部：%2d\n" %(666))

print("不足數位補0(以*替代)：%0*d\n" %(5, 66))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExList.py

list1 = ["A", True, 10, 3.14, "G"]

for i in range(len(list1)):
   print("索引位置：%s\t對應值：%s\t型態：%s\n" %(i, list1[i], type(list1[i])))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExList2.py

person = ["John", "Merry", "Mi", "Jason"]

addPerson = str(input("請輸入新增人員名字："))

if person.count(addPerson) == 0:
   person.insert(len(person) - 2, addPerson)

print("搜尋剛新增人員索引位置：", person.index(addPerson))

person1 = person.copy()
person.clear()

print("複製原串列：", person1)
print("原串列：", person)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExSet.py

likeBasketball = set(("class A", "class B", "class C"))
likeDodgeball = set(("class A", "class F", "class k"))

setDifference = likeBasketball.difference(likeDodgeball)
print("\nlikeBasketball差集：", setDifference)
setDifference = likeDodgeball.difference(likeBasketball)
print("likeDodgeball差集：", setDifference)

setIntersection = likeBasketball.intersection(likeDodgeball)
print("\nlikeBasketball以及likeDodgeball的交集：", setIntersection)


setUnion = likeBasketball.union(likeDodgeball)
print("\nlikeBasketball以及likeDodgeball的聯集：", setUnion)

setSymmetric_difference = likeBasketball.symmetric_difference(likeDodgeball)
print("\nlikeBasketball以及likeDodgeball的對稱差：", setSymmetric_difference)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExSlice.py

Index = "Hello Python, This is Program"

print("Index字串：", Index)
print(Index[-3:-25:-2])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExString.py

strName = str(input("\n郵局："))
strCode = str(input("郵局代號："))
intAount = int(input ("戶頭："))
intMoney = int(input("金額："))
	
print("\n郵局：%s" %(strName))
print("郵局代號為%s，轉帳戶頭為%02d" %(strCode, intAount))
print("匯入金額：%c%.2f" %(36, intMoney))
	
if intMoney < 20000:
    print("%c\n" %("成"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExStrMethod.py

def EditData():
    if len(strEditTitle) > 0:
        print(strEditTitle)
    else:
        print(strTitle)

    print("作者：", strName)
    print("暱稱：", strId)
    print("Gmail：", strEmail)
    print("興趣：", strJoin)

strTitle = ""
strEditTitle = "撰寫Python小網站"

isEditTitle = str(input("是否要更改名稱(Y/N)："))
isSymbol = str(input("是否要更改前後星號(Y/N)："))

if isEditTitle == "Y" and isSymbol == "Y":
    strEditTitle = str(input("請輸入欲更改名稱："))
    strSymbol = str(input("請輸入欲更改前後符號："))

    strEditTitle = strEditTitle.center(36, strSymbol)
    
elif isEditTitle == "Y" and isSymbol == "N":
    strEditTitle = str(input("請輸入欲更改名稱："))
    strEditTitle = strEditTitle.center(36, "*")

elif isEditTitle == "N" and isSymbol == "Y":
    strSymbol = str(input("請輸入欲更改前後符號："))
    strTitle = strTitle.center(36, strSymbol)

strName = str(input("請輸入名字："))
strId = str(input("請輸入暱稱："))
strEmail = str(input("請輸入Gmail："))

while strEmail.endswith("@gmail.com") == False:
    strEmail = str(input("請重新輸入Gmail："))

strSavor = str(input("你的興趣(以逗號分隔)："))
strJoin = "|".join(strSavor.split(","))


print("="*30, "\n")
EditData()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\ExTuple.py

tupleData = ()
listData = []

print("\n\n")

strFieldName = str(input("請輸入不可修改欄位名稱(逗號為分隔索引位置；頓號則為放置在同一個索引位置)："))
strFieldData = str(input("請輸入欄位對應資料(逗號為分隔索引位置；頓號則為放置在同一個索引位置)："))

for i in range(len(strFieldName.split(","))):
    listData.append(strFieldName.split(",")[i])
    
for j in range(len(strFieldData.split(","))):
    x = 0

    if len(listData)%2 == 0:
        x = len(listData) - 1
    else:
        x = len(listData) + 1
        
    listData.insert(x, [strFieldData.split(",")[j] for x in range(1)])
    
listToTuple = tuple(listData)
print("\n")
print("list轉換tuple：", listToTuple)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\lotto.py

number={1,2,3,4,5,6,7,8,9,10,11,12}
print(number)
lotto1={3,5,7,10,12} #第一組幸運彩蛋
print("第一組樂透:",lotto1)
lotto2={2,5,6,11,12} #第二組幸運彩蛋
print("第二組樂透:",lotto2)
lucky=lotto1 | lotto2
print("有 %d 個數字出現在其中一次開獎" %len(lucky), lucky)
biglucky=lotto1 & lotto2
print("有 %d 個數字出現在每一次開獎" %len(biglucky), biglucky)
badnum=number -lucky
print("總共有 %d 個不幸運的數字" %len(badnum), badnum)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\phrase.py

phrase = 'Happy holiday.'
print('原字串：', phrase)
print('將首字大寫 ', phrase.capitalize())
print('每個單字的首字會大寫', phrase.title())
print('全部轉為小寫字元', phrase.lower()) 
print('判斷字串首字元是否為大寫', phrase.istitle())
print('是否皆為大寫字元', phrase.isupper())
print('是否皆為小寫字元', phrase.islower())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\replace.py

s= "我畢業於宜蘭高中."
print(s)
s1=s.replace("宜蘭高中", "高雄中學")
print(s1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\rev.py

fruit = ['apple', 'orange', 'watermelon']
print('反轉前內容：', fruit)
fruit.reverse() 
print('反轉後內容：', fruit)
score = [65,76,54,32,18]
print('反轉前內容：', score)
score.reverse() 
print('反轉後內容：', score)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\sort.py

score = [98, 46, 37, 66, 69]
print('排序前順序：',score)
score.sort() #省略reverse參數, 遞增排序
print('遞增排序：', score)
letter = ['one', 'time', 'happy', 'child']
print('排序前順序：')
print(letter)
letter.sort(reverse = True) #依字母做遞減排序
print('遞減排序：')
print(letter)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\split.py

str1 = "happy \nclever \nwisdom"
print( str1.split() ) #以空格與換行符號(\n)來分割
print( str1.split(' ', 2 ) ) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\startswith.py

wd = 'Alex is optimistic and clever.'
print('字串:', wd)
print('Alex為開頭的字串嗎', wd.startswith('Alex')) 
print('clever為開頭的字串嗎', wd.startswith('clever', 0))
print('optimistic從指定位置的開頭的字串嗎', wd.startswith('optimisti', 8)) 
print('clever.為結尾字串嗎', wd.endswith('clever.'))  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\tuple_sorted.py

pay = (8000, 7200, 8300, 4700, 5500)
print(pay)
print('由小而大：',sorted(pay))
print('由大而小：', sorted(pay, reverse = True))

print('資料仍維持原順序：')
print(pay)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\unpack01.py

word1 = "zoo"
word2 = "animal"
print("交換前: ")
print('單字1={},單字2={}'.format(word1,word2))
word2,word1 = word1,word2
print("交換後: ")
print('單字1={},單字2={}'.format(word1,word2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch06\unpack02.py

product = (('iPhone','手機','我預算的首選'),
        ('iPad','平板','視股票獲利'),
        ('iPod','播放','價格最親民'))

for(name, c_name,memo) in product:
    print('%-10s %-12s %-10s'%(name,c_name,memo))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\compare.py

def mymax(x,y):
    if x>y:
        return x
    else:
        return y

print('數字比大小')
a=int(input('請輸入a:'))
b=int(input('請輸入b:'))
print("較大者之值為:%d" %mymax(a,b))#函數呼叫

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\exchange.py

def exchange(num):
    num[0],num[1]=num[1],num[0] #交換兩數過程

print("請輸入兩個數值: ")
num=[]
num.append(int(input()))
num.append(int(input()))
print('num[0]=',num[0])
print('num[1]=',num[1])
exchange(num)
print('------------- exchange()函數交換 ----------------')
print('num[0]=',num[0])
print('num[1]=',num[1])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\fee.py

money=int(input('請輸入班遊剩餘的金額:'))
num=int(input('請輸入這次出遊的總人數:'))
ans=divmod(money,num)
print('每一位同學的平均退費為',ans[0],'元')
print('剩餘可以存入班費共同基金為 ',ans[1],'元')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\func.py

def func(a,b,c):
    x = a +b +c
    return x

print(func(1,2,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\func1.py

def func(a,b,c):
    x = a +b +c
    print(x)

print(func(1,2,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\keyword.py

def equation(x,y,z):
    ans = x*y+z*x+y*z
    return ans

print(equation(z=1,y=2,x=3))
print(equation(3, 2, 1))
print(equation(x=3, y=2 , z=1))
print(equation(3, y=2 , z=1))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\lambda.py

total=lambda a,b:a+b
num1=0
num2=0
num1=int(input('輸入數值 1：'))
num2=int(input('輸入數值 2：'))
print('數值 1+數值 2 =',total(num1,num2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\math.py

score=[97,76,89,76,90,100,87,65]
print('本學期總共考過的數學小考次數', len(score))
print('所有成績由小到大排序的結果為: {}'.format(sorted(score)))
print('本學期所有分數的總和', sum(score))
print('本學期所有分數的平均', round(sum(score)/len(score),1))
print('本學期考最差的分數為', min(score))
print('本學期考最好的分數為', max(score))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\para.py

def square_sum(*arg):
    ans=0
    for n in arg:
        ans += n*n
    return ans

ans1=square_sum(1)
print('1*1=',ans1)
ans2=square_sum(1,2)
print('1*1+2*2=',ans2)
ans3=square_sum(1,2,3)
print('1*1+2*2+3*3=',ans3)
ans4=square_sum(1,3,5,7)
print('1*1+3*3+5*5+7*7=',ans4)

def progname(**arg):
    return arg

print(progname(d1='python', d2='java', d3='visual basic'))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\para1.py

def dinner(mainmeal, *sideorder):
    #列出所點餐點的主餐及點心副餐
    print('所點的主餐為',mainmeal,'所點的副餐點心包括:')
    for snack in sideorder:
        print(snack)

dinner('鐵板豬','烤玉米')
dinner('泰式火鍋','德式香腸','香焦牛奶','幸運餅')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\pow.py

def Pow(x, y):
    p = 1;
    for i in range(y+1):
        p *= x
    return p
print('請輸入兩數x及y的值函數：')
x=int(input('x='))
y=int(input('y='))
print('次方運算結果：%d' %Pow(x, y))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\seq.py

import random

val=0
data=[0]*80
for i in range(80):
    data[i]=random.randint(1,150)
while val!=-1:
    find=0
    val=int(input('請輸入搜尋鍵值(1-150)，輸入-1離開：'))
    for i in range(80):
        if data[i]==val:
            print('在第 %3d個位置找到鍵值 [%3d]' %(i+1,data[i]))
            find+=1
    if find==0 and val !=-1 :
        print('######沒有找到 [%3d]######' %val)
print('資料內容：')
for i in range(10):
    for j in range(8):
        print('%2d[%3d]  ' %(i*8+j+1,data[i*8+j]),end='')
    print('')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\swap.py

def swap_test(x,y):
    print('函數內交換前：x=%d, y=%d' %(x,y))
    x,y=y,x #交換過程
    print('函數內交換前：x=%d, y=%d' %(x,y))     

a=10
b=20 #設定a,b的初值
print('函數外交換前：a=%d, b=%d' %(a,b))
swap_test(a,b) #函數呼叫
print('函數外交換後：a=%d, b=%d' %(a,b))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch07\value.py

print('int(9.6)=',int(9.6))
print('bin(20)=',bin(20))
print('hex(66)=',hex(66))
print('oct(135)=',oct(135))
print('float(70)=',float(70))
print('abs(-3.9)=',abs(-3.9))
print('chr(69)=',chr(69))
print('ord(\'%s\')=%d' %('D',ord('D')))
print('str(543)=',str(543))

print("------------------------------------------------------------")  # 60個

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\CalculateSalary.py

#設置底薪(BaseSalary)、結案獎金件數(Case)、職位獎金(OfficeBonus)
BaseSalary = 25000
CaseBonus = 1000
OfficeBonus = 5000


#請輸入職位名稱(Engineer)、結案獎金金額(CaseAmount)變數
Engineer = str(input("請輸入職位名稱："))
Case = int(input("請輸入結案案件數(整數)："))


#計算獎金function
def CalculateCase(case, caseBonus):
    return case * caseBonus

def CalculateSalary(baseSalary, officeBonus):
    return baseSalary + officeBonus

CaseAmount = CalculateCase(Case, CaseBonus)
SalaryAmount = CalculateSalary(BaseSalary, OfficeBonus)

print("該工程師薪資：", CaseAmount + SalaryAmount)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExCalendar.py

import calendar

y = int(input("請輸入年份:"))
m = int(input("請輸入月份:"))
ys = int(input("列印n年內為閏年的月曆:"))
notLeap = []

calendar.setfirstweekday(calendar.SUNDAY)

for i in range(ys):
    if calendar.isleap(y+i) == True:
        print("\n")
        calendar.prmonth(y+i, m)
    else:
        notLeap.append(y+i)

print("\n以下非閏年:", notLeap)
print("{}到{}期間有幾個閏年:{}".format(y, y+ys, calendar.leapdays(y, y+ys)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExMath.py

import math
x = 10
y = -2

z = math.fabs(x / y)
h = math.factorial(z)

if math.isnan(h) == False:
    print("計算後數值：", h)
    print("最大公約數：", math.gcd(h, x))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExRandomSort.py

import random
name = ["小明", "小黃", "小紅", "小綠", "小白"]

print("抽取一個元素：", random.choice(name))

print("抽取三個元素：", random.sample(name, 3))

print("抽取三個元素：", random.shuffle(name))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExRandrange.py

import random

print("任一整數", random.randrange(100))

print("任一整數", random.randrange(52, 100))

print("奇數", random.randrange(1, 100, 2))

print("偶數", random.randrange(0, 100, 2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\ExTime.py

import time

t = time.time()
tLocal = time.localtime(t)

print("轉換時間形式(年/月/日)：", time.strftime("%Y/%m/%d", tLocal))
print("轉換時間形式(年/月/日 時:分:秒)：", time.asctime (tLocal))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\GetParam.py

import sys
if len(sys.argv) < 0:
    print("未有外部傳入參數")
else:
    print("Python版本號：", sys.version)
    print("作業系統：", sys.platform)

    for n in range(len(sys.argv)):
        print("param" + str(n) + "：", sys.argv[n])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT雙效合一：快速學會最強AI，寫程式更有效率\ch08\import.py

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


