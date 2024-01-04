import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch01\height.py

height=178
print("小郭的身高：%d" % height)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch01\hello.py

#我寫的程式
print("Hello World!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch01\setwidth.py

name1="多益題庫大全"
name2="國小單字入門手冊"
name3="英檢初級及中級合輯"
price1=500
price2=45
price3=125.85
print("%5s 商品價格為 %4d 元" % (name1, price1))
print("%5s 商品價格為 %4d 元" % (name2, price2))
print("%5s 商品價格為 %5.2f 元" % (name3, price3))

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch02\comment.py

'''
   範例程式:comment.py
   程式功能:本程式示範如何使用多行註解及單行註解
'''
number = 10 #將數值10設定給number
print(number) #輸出number變數值
a=b=c=55 #a, b, c三個變數的值都是55
a,b,c = 55,55,55 #也可以利用","隔開變數名稱,就能在同一列設定值
print(a) #輸出a變數值
print(b) #輸出b變數值
print(c) #輸出c變數值
a,f,name = 66,10.58, "Michael " #也可以混搭不同型態的變數一起宣告
print(a) #輸出a變數值,各位可以發現其值已被重新給定
print(f) #輸出f變數值
print(name) #輸出name變數值

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch02\escape.py

print("顯示反斜線: " + '\\')
print("顯示單引號: " + '\'');
print("顯示雙引號: " + '\"');
print("顯示16進位數: " + '\u0068')
print("顯示8進位數: " + '\123')
print("顯示倒退一個字元: " + '\b' + "xyz")
print("顯示空字元: " + "xy\0z")
print("雙引號的應用->\n\"跳脫字元的綜合運用\"")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch02\format.py

name1="多益題庫大全"
name2="國小單字入門手冊"
name3="英檢初級及中級合輯"
price1=500
price2=45
price3=125.85
print("%5s 商品價格為 %4d 元" % (name1, price1))
print("%5s 商品價格為 %4d 元" % (name2, price2))
print("%5s 商品價格為 %5.2f 元" % (name3, price3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch02\format_para.py

num1=9.86353
print("num1= {:.3f}".format(num1))  
num2=524.12345
print("num2= {:12.3f}".format(num2))
company="智能AI科技股份有限公司"
year=18
print("{} 已設立公司 {} 年" .format (company, year))
print("{0} 成立至今已 {1} 歲".format(company, year))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch02\strtoint.py

no1=input("請輸入甲班全班人數：")
no2=input("請輸入乙班全班人數：")
total1=no1+no2
print(type(total1))
print("兩班總人數為%s" %total1)    
total2=int(no1)+int(no2)
print(type(total2))
print("兩班總人數為%d" %total2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch02\type.py

a=8
b=3.14
c=True
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch03\AddMinus.py

num1=int(input("請輸入第一個整數: "))
num2=int(input("請輸入第二個整數: "))
print("第一個整數的值: %d" %num1)
print("第二個整數的值: %d" %num2)
print("兩個整數相加的值: %d" %(num1+num2))
print("兩個整數相減的值: %d" %(num1-num2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch03\bit_operator.py

#位元運算子綜合應用
x = 12; y = 8
print(x & y)  
print(x ^ y)   
print(x | y)  
print(~x)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch03\compound.py

"""
指派運算子練習
"""

a =3
b =1
c =2

x = a + b * c
print("{}".format(x)) #x=3+1*2=5
a += c 
print("a={0}".format(a,b))  #a=3+2=5
a -= b  
print("a={0}".format(a,b))  #a=5-1=4
a *= b
print("a={0}".format(a,b))  #a=4*1=4
a **= b
print("a={0}".format(a,b))  #a=4**1=4
a /= b
print("a={0}".format(a,b))  #a=4/1=4
a //= b
print("a={0}".format(a,b))  #a=4//1=4
a %= c
print("a={0}".format(a,b))  #a=4%2=0
s = "程式設計" + "很有趣"
print(s)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch03\exchange.py

num=int(input("請輸入將兌換金額:")) 
hundred=num//100
fifty=(num-hundred*100)//50
ten=(num-hundred*100-fifty*50)//10
print("百元鈔有 %d 張 五十元鈔有 %d 張 十元鈔有 %d 張" %(hundred,fifty,ten))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch03\logic.py

a,b,c=3,5,7;     #宣告a、b及c三個整數變數
print("a= %d b= %d c= %d" %(a,b,c))
print("====================================")
#包含關係與邏輯運算子的運算式求值
print("a<b and b<c or c<a = %d" %(a<b and b<c or c<a))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch03\precedence.py

a = 12
b = 2
c = 6*(24/a + (5+a)/b)

print("a=", a)
print("b=", b)
print("6*(24/a + (5+a)/b)=", c)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch03\relation.py

a = 54
b = 35
c = 21
ans1 = (a == b)  #判斷a是否等於b
ans2 = (b != c) #判斷b是否不等於c
ans3 = (a <= c) #判斷a是否大於等於c
print(ans1) 
print (ans2) 
print (ans3) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch03\score.py

s1=int(input("請輸入第一次月考成績: "))
s2=int(input("請輸入第二次月考成績: "))
s3=int(input("請輸入第三次月考成績: "))
print("三次月考的加總分數: %d" %(s1+s2+s3))
avg=(s1+s2+s3)/3
print("三次月考的平均分數: %3.1f" %avg)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch03\temperature.py

"""
輸入華氏(Fahrenheit)溫度轉換攝氏(Celsius)溫度
提示：C=5/9*(F-32)
"""
F= float( input("請輸入華氏溫度："))
C=5/9*(F-32)
print("華氏溫度 %3.1f 轉換為攝氏溫度為 %3.1f" %(F,C))

print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch04\discount.py

cost=float(input("請輸入消費總金額:"))    
if cost>=100000:
    cost=cost*0.85 #10萬元以上打85折       
elif cost>=50000:
    cost=cost*0.9  #5萬元到10萬元之間打9折     
else:
    cost=cost*0.95 #5萬元以下打95折
print("實際消費總額:%.1f元" %cost)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch04\if.py

Money=int(input("請輸入消費的金額:"))
if Money<1200:
    Money*=1.1; #消費未滿 1200，加收服務費1成
print("需繳付的實際金額是 %5.0f 元" %Money)   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch04\if_else.py

num = int(input('請輸入一個整數？'))
if num%5:
    print(num, '不是5的倍數')
else:
    print(num, '為5的倍數')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch04\if_else-1.py

value=int(input("請任意輸入一個整數：")) #輸入一個整數
#判斷是否為2或3的倍數   
if value%2==0 or value%3==0:
    if value%6!=0:
        print("符合所要的條件")
    else:
        print("不符合所要的條件") #為6的倍數  
else:
    print("不符合所要的條件")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch04\if_fee.py

print("停車超過一小時,每小時收費40元")
t=int(input("請輸入停車幾小時: ")) #輸入時數	     
if t>=1:
    total=t*40 #計算費用
    print("停車%d小時,總費用為:%d元" %(t,total))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch04\if_weight.py

weight = input('請輸入體重: ')
andy = int(weight) #將輸入體重的字串型態轉換為整數
if andy >= 80:    #體重大於或等於80
    print('體重過胖，要小心身材變形')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch04\leapYear.py

"""
程式名稱：閏年判斷程式
題目要求：
輸入西元年(4位數的整數year)判斷是否為閏年
條件1.逢4閏(除4可整除)而且逢100不閏(除100不可整除)
條件2.逢400閏(除400可整除)
滿足兩個條件之一即是閏年
"""
year = int(input("請輸入西元年份："))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("{0}是閏年".format(year))
else :
    print("{0}是平年".format(year))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch04\pos.py

print("目前提供的選擇如下") 
print(" 0.查詢其他相關的點心資料")
print(" 1.吉事漢堡" )
print(" 2.咖哩珍豬飽")
print(" 3.六塊麥克雞")
print("請點選您要的項目:" )
Select=int(input()) #輸入餐點的項目
if Select == 0: #選擇第0項?
    print("請稍等... 正在查詢其他相關的點心資料")
elif Select == 1: #是否選擇第1項?
    print("這個項目的單價:%d" %45)
elif Select == 2: #是否選擇第2項?
    print("這個項目的單價:%d" %55)
elif Select == 3: #是否選擇第3項?
    print("這個項目的單價:%d" %65)
else: #輸入錯誤的處理
    print("您可能輸入錯誤.... 請重新輸入")

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\99table.py

"""
程式名稱：九九乘法表
"""
for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\break.py

# break練習
total=0
for i in range(1,201,2):
    if i==101:
        break #跳出迴圈
    total+=i
print("1~99的奇數總和:%d" %total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\breaktable.py

# 九九乘法表的雙重迴圈
for i in range(1,10):
    for j in range (1,10):
        print('{0}*{1}={2:2d}  '.format(i,j,i*j), sep='\t',end='')
        if j>=7:
            break #設定跳出的條件
    print('\n-------------------------------------------------------\n')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\continue.py

#continue練習 
for a in range(10): #外層for迴圈控制y軸輸出
    for b in range(a+1): #內層for迴圈控制x軸輸出
        if b==6:
            continue
        print("%d " %b,end='')#印出b的值
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\divide.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\donate.py

total = 0
money = -1
count = 0 #計數器

# 進入while迴圈
while money != 0:
   money = int(input('輸入捐款金額：')) #以int()轉為整數
   total += money
   print('累計:', total)
   
print('最後總捐款金額總計:', total, '元')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\fac.py

#計算10! 的值
product=1
for i in range(1,11): #定義for迴圈
    product*=i
print("product=%d" %product) #印出乘積的結果

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\fac_total.py

product=0
n1=1
n=int(input("請輸入任一整數:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        n1*=j; # n!的值
    product+=n1;# 1!+2!+3!+..n!
    n1=1
print("1!+2!+3!+...+{0}!={1}".format(n,product))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\password.py

"""
讓使用者輸入密碼，並且進行密碼驗證,
輸入次數以三次為限，超過三次則不准登入，
假如目前密碼為3388。
"""
password=3388 #利用變數來儲存密碼以供驗證
i=1

while i<=3: #輸入次數以三次為限
    new_pw=int(input("請輸入密碼:"))
    if new_pw != password:  #如果輸入的密碼與預設密碼不同
        print("密碼發生錯誤!!")
        i=i+1
        continue #跳回while開始處
    else:
        print("密碼正確!!")
        break
if i>3:
        print("密碼錯誤三次，取消登入!!\n"); #密碼錯誤處理

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\pi.py

sigma=0
k=int(input("請輸入k值：")) #輸入k值
for n in range(0,k,1):
    if n & 1: #如果n是奇數
        sigma += float(-1/(2*n+1))
    else: #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\range.py

sum = 0 #儲存加總結果,初值為0
print('進行加總前的起始值', sum) #輸出加總前的起始值
for i in range(11, 21):   
    sum += i  #將數值累加   
    print('累加值=', sum) #輸出累加結果
else:   
    print('數值累加完畢...')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\reverse.py

n=int(input("請輸入任一整數:"))
print("反向輸出的結果:",end='') 
while n!=0:  #while迴圈
    print("%d" %(n%10),end='') #求出餘數值
    n//=10

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch05\while.py

x,sum=1,1000
while sum>0: #while迴圈
    sum-=x
    x=x+1
print(x-1)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


