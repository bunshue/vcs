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



print("------------------------------------------------------------")  # 60個


