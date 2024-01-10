"""
範例來的混合資料 1


"""


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch01\height.py

height=178
print("小郭的身高：%d" % height)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch01\hello.py

#我寫的程式
print("Hello World!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch01\setwidth.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch02\comment.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch02\escape.py

print("顯示反斜線: " + '\\')
print("顯示單引號: " + '\'');
print("顯示雙引號: " + '\"');
print("顯示16進位數: " + '\u0068')
print("顯示8進位數: " + '\123')
print("顯示倒退一個字元: " + '\b' + "xyz")
print("顯示空字元: " + "xy\0z")
print("雙引號的應用->\n\"跳脫字元的綜合運用\"")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch02\format.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch02\format_para.py

num1=9.86353
print("num1= {:.3f}".format(num1))  
num2=524.12345
print("num2= {:12.3f}".format(num2))
company="智能AI科技股份有限公司"
year=18
print("{} 已設立公司 {} 年" .format (company, year))
print("{0} 成立至今已 {1} 歲".format(company, year))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch02\strtoint.py

no1=input("請輸入甲班全班人數：")
no2=input("請輸入乙班全班人數：")
total1=no1+no2
print(type(total1))
print("兩班總人數為%s" %total1)    
total2=int(no1)+int(no2)
print(type(total2))
print("兩班總人數為%d" %total2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch02\type.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch03\AddMinus.py

num1=int(input("請輸入第一個整數: "))
num2=int(input("請輸入第二個整數: "))
print("第一個整數的值: %d" %num1)
print("第二個整數的值: %d" %num2)
print("兩個整數相加的值: %d" %(num1+num2))
print("兩個整數相減的值: %d" %(num1-num2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch03\compound.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch03\exchange.py

num=int(input("請輸入將兌換金額:")) 
hundred=num//100
fifty=(num-hundred*100)//50
ten=(num-hundred*100-fifty*50)//10
print("百元鈔有 %d 張 五十元鈔有 %d 張 十元鈔有 %d 張" %(hundred,fifty,ten))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch03\logic.py

a,b,c=3,5,7;     #宣告a、b及c三個整數變數
print("a= %d b= %d c= %d" %(a,b,c))
print("====================================")
#包含關係與邏輯運算子的運算式求值
print("a<b and b<c or c<a = %d" %(a<b and b<c or c<a))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch03\precedence.py

a = 12
b = 2
c = 6*(24/a + (5+a)/b)

print("a=", a)
print("b=", b)
print("6*(24/a + (5+a)/b)=", c)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch03\relation.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch03\score.py

s1=int(input("請輸入第一次月考成績: "))
s2=int(input("請輸入第二次月考成績: "))
s3=int(input("請輸入第三次月考成績: "))
print("三次月考的加總分數: %d" %(s1+s2+s3))
avg=(s1+s2+s3)/3
print("三次月考的平均分數: %3.1f" %avg)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch03\temperature.py

"""
輸入華氏(Fahrenheit)溫度轉換攝氏(Celsius)溫度
提示：C=5/9*(F-32)
"""
F= float( input("請輸入華氏溫度："))
C=5/9*(F-32)
print("華氏溫度 %3.1f 轉換為攝氏溫度為 %3.1f" %(F,C))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch04\discount.py

cost=float(input("請輸入消費總金額:"))    
if cost>=100000:
    cost=cost*0.85 #10萬元以上打85折       
elif cost>=50000:
    cost=cost*0.9  #5萬元到10萬元之間打9折     
else:
    cost=cost*0.95 #5萬元以下打95折
print("實際消費總額:%.1f元" %cost)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch04\if.py

Money=int(input("請輸入消費的金額:"))
if Money<1200:
    Money*=1.1; #消費未滿 1200，加收服務費1成
print("需繳付的實際金額是 %5.0f 元" %Money)   

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch04\if_else.py

num = int(input('請輸入一個整數？'))
if num%5:
    print(num, '不是5的倍數')
else:
    print(num, '為5的倍數')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch04\if_else-1.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch04\if_fee.py

print("停車超過一小時,每小時收費40元")
t=int(input("請輸入停車幾小時: ")) #輸入時數	     
if t>=1:
    total=t*40 #計算費用
    print("停車%d小時,總費用為:%d元" %(t,total))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch04\if_weight.py

weight = input('請輸入體重: ')
andy = int(weight) #將輸入體重的字串型態轉換為整數
if andy >= 80:    #體重大於或等於80
    print('體重過胖，要小心身材變形')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch04\leapYear.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch04\pos.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\99table.py

"""
程式名稱：九九乘法表
"""
for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\break.py

# break練習
total=0
for i in range(1,201,2):
    if i==101:
        break #跳出迴圈
    total+=i
print("1~99的奇數總和:%d" %total)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\breaktable.py

# 九九乘法表的雙重迴圈
for i in range(1,10):
    for j in range (1,10):
        print('{0}*{1}={2:2d}  '.format(i,j,i*j), sep='\t',end='')
        if j>=7:
            break #設定跳出的條件
    print('\n-------------------------------------------------------\n')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\continue.py

#continue練習 
for a in range(10): #外層for迴圈控制y軸輸出
    for b in range(a+1): #內層for迴圈控制x軸輸出
        if b==6:
            continue
        print("%d " %b,end='')#印出b的值
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\divide.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\donate.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\fac.py

#計算10! 的值
product=1
for i in range(1,11): #定義for迴圈
    product*=i
print("product=%d" %product) #印出乘積的結果

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\fac_total.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\password.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\pi.py

sigma=0
k=int(input("請輸入k值：")) #輸入k值
for n in range(0,k,1):
    if n & 1: #如果n是奇數
        sigma += float(-1/(2*n+1))
    else: #如果n是偶數
        sigma += float(1/(2*n+1))
print("PI = %f" %(sigma*4))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\range.py

sum = 0 #儲存加總結果,初值為0
print('進行加總前的起始值', sum) #輸出加總前的起始值
for i in range(11, 21):   
    sum += i  #將數值累加   
    print('累加值=', sum) #輸出累加結果
else:   
    print('數值累加完畢...')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\reverse.py

n=int(input("請輸入任一整數:"))
print("反向輸出的結果:",end='') 
while n!=0:  #while迴圈
    print("%d" %(n%10),end='') #求出餘數值
    n//=10

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch05\while.py

x,sum=1,1000
while sum>0: #while迴圈
    sum-=x
    x=x+1
print(x-1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\append.py

num=int(input('請輸入總人數: '))
student = [] #建立空的list串列
print('請輸入{0}個數值：'.format(num))

# 以for/in廻圈依序讀取要輸入的分數
for item in range(1,num+1):
    score = int(input()) #取得輸入數值
    student.append(score) #將輸入數值新增到串列

print('已輸入完畢')
#輸出資料
print('總共輸入的分數', end = '\n')
for item in student:   
    print('{:3d} '.format(item), end = '')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\copy.py

parents= ["勤儉", "老實", "客氣"]
child=parents[:]
daughter=parents[:]
print("parents特點",parents)
print("child特點",child)
print("daughter特點",daughter)
child.append("毅力")
daughter.append("時尚")
print("分別新增小孩的特點後:")
print("child特點",child)
print("daughter特點",daughter)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\copy1.py

parents= ["勤儉", "老實", "客氣"]
child=parents
daughter=parents
print("parents特點",parents)
print("child特點",child)
print("daughter特點",daughter)
child.append("毅力")
daughter.append("時尚")
print("分別新增小孩的特點後:")
print("child特點",child)
print("daughter特點",daughter)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\count.py

word = ["holiday", "happy", "birth",
             "yesterday", "holiday", "car",
             "yellow", "happy", "mobile",
             "cup", "happy", "holiday",
             "holiday", "desk", "birth",
             ]
print("holiday 出現的次數", word.count("holiday"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\dict.py

labor = {'高中仁':'RD', '許富強':'SA'} #設定字典的資料
labor['陳月風'] = 'CEO' #新增一個項目
labor.setdefault('陳月風')
print('目前字典:')
print(labor)
labor['陳月風'] ='PRESIDENT' 
#以update()方法更新字典
labor.update({'周慧宏':'RD', '鄭大富':'SA'})
print('依名字遞增排序:')
for key in sorted(labor):
    print('%8s %9s' % (key, labor[key]))

person = {'陳志強':'SA','蔡工元':'RD'}
labor.update(person) # 更新字典
labor.update(胡慧蘭 = 'RD', 周大全 = 'SA')#以指派方式更新
print('更新字典內容：\n', labor)
labor.pop('陳志強')#刪除指定資料
print('刪除後依名字排序:')
for value in sorted(labor, reverse = False):
    print('%8s %9s' % (value, labor[value]))
print('將字典內容清空:')
print(labor.clear())
print(labor)#輸出字典

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\english.py

#小班制的同學清單
classmate={'陳大慶','許大為','朱時中','莊秀文','吳彩鳳',
           '黃小惠','曾明宗','馬友友','韓正文','胡天明'}
test1={'陳大慶','許大為','朱時中','馬友友','胡天明'} #中高級名單
test2={'許大為','朱時中','吳彩鳳','黃小惠','馬友友','韓正文'} #中級名單
goodguy=test1 | test2
print("全班有 %d 人通過兩種檢定其中一種" %len(goodguy), goodguy)
bestguy=test1 & test2
print("全班有 %d 人兩種檢定全部通過" %len(bestguy), bestguy)
poorguy=classmate -goodguy
print("全班有 %d 人沒有通過任何檢定" %len(poorguy), poorguy)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\index.py

word = ["holiday", "happy", "birth",
             "yesterday", "holiday", "car",
             "yellow", "happy", "mobile",
             "cup", "happy", "holiday",
             "holiday", "desk", "birth",
             ]
search_str="yellow"
print("單字 %s 第一次出現的索引值%d" %(search_str,word.index(search_str)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\listsort.py

no = [105, 25, 8, 179, 60, 57]
print('排序前的資料順序：',no)
no.sort() #省略reverse參數, 遞增排序
print('遞增排序：', no)
zoo = ['tiger', 'elephant', 'lion', 'rabbit']
print('排序前的資料順序：')
print(zoo)
zoo.sort(reverse = True) #依字母做遞減排序
print('依單字字母遞減排序：')
print(zoo)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\reverse.py

no = [185, 278, 97, 48, 33, 61]
print('反轉前內容：', no)
no.reverse() 
print('反轉後內容：', no)

zoo = ['tiger', 'lion', 'horse', 'cattle']
print('反轉前內容：', zoo)
zoo.reverse() 
print('反轉後內容：', zoo)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\set.py

friendA= {"Andy", "Axel", "Michael","May"}
friendB = {"Peter", "Axel", "Andy","Julia"}
print(friendA & friendB)
print(friendA | friendB)
print(friendA - friendB)
print(friendA ^ friendB)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\swap.py

x = 859
y = 935
print("兩數經交換前的值: ")
print('x={},y={}'.format(x,y))
y,x = x,y
print("兩數經交換後的值: ")
print('x={},y={}'.format(x,y))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\tuple_create.py

tup = (28, 39, 58, 67,97, 54) 
print('目前元組內的所有元素：')
for item in range(len(tup)):
   print ('tup[%2d] %3d' %(item, tup[item]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\tuple_sorted.py

salary = (86000, 72000, 83000, 47000, 55000)
print('原有資料：')
print(salary)
print('--------------------------------')

# 由小而大
print('薪資由小而大排序：',sorted(salary))
print('--------------------------------')

# 遞減排序
print('薪資由大而小排序：', sorted(salary, reverse = True))
print('--------------------------------')

print('資料經排序後仍保留原資料位置：')
print(salary)
print('--------------------------------')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\unpack.py

info = [['C程式設計','朱大峰','480'],
        ['Python程式設計','吳志明','500'],
        ['Java程式設計','許伯如','540']]

for(book, author,price) in info:
    print('%10s %3s'%(book,author),' 書籍訂價:',price)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch06\word.py

original= ["abase", "abate", "abdicate","abhor", "abate", "acrid","appoint", "abate", "kindle"]
print("單字收集的原始內容: ")
print(original)
set1=set(original)
not_duplicatd=list(set1)
print("刪除重複單字的最佳內容: ")
print(not_duplicatd)
print("按照字母的排列順序: ")
not_duplicatd.sort()
print(not_duplicatd)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\align.py

str1 = '淡泊以明志，寧靜以致遠'
print('原字串', str1)
print('欄寬20，字串置中', str1.center(20))
print('字串置中，# 填補', str1.center(20, '#'))
print('欄寬20，字串靠左', str1.ljust(20, '@'))
print('欄寬20，字串靠右', str1.rjust(20, '!'))

mobilephone = '931828736'
print('字串左側補0:', mobilephone.zfill(10))

str2 = 'Time create hero.,I love my family.'
print('以逗點分割字元', str2.partition(','))

str3 = '忠孝\n仁愛\n信義\n和平'
print('依\\n分割字串', str3.splitlines(False))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\arg.py

def fun1(obj, price):
    obj = 'Microwave'
    print('函數內部修改字串及串列資料')
    print('物品名稱:', obj)
    #新增價格
    price.append(12000)
    print('物品售價:', price)

obj1 = 'TV'  #未呼叫函數前的字串
price1 = [24000, 18000, 35600] #未呼叫函數前的串列
print('函數呼叫前預設的字串及串列')
print('物品名稱:', obj1)
print('物品售價:', price1)
fun1(obj1, price1)

print('函數內部被修改過字串及串列:')
print('名字:', obj1) #字串內容沒變
print('分數:', price1) #串列內容已改變

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\blessings.py

def blessings():
    print('一元復始，萬象更新')

blessings()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\blessings_para.py

def blessings(str1):
    print(str1)

blessings('一元復始，萬象更新')
blessings('恭賀新喜，財源滾滾')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\bonus.py

def payment():
    price = float(input("產品單價："))
    num = float(input("銷售數量："))
    rate = 0.35  #抽取獎金的百分比
    total = price*num * rate
    return price*num, total
 
e1 ,e2 = payment()
print("總銷售業績{},應付獎金：{}".format(e1, e2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\common.py

def Common_Divisor():
    print("請輸入兩個數值")
    Num1=int(input("數值 1："))
    Num2=int(input("數值 2："))
    print(Num1,'及',Num2)
    while Num2 != 0: #利用輾轉相除法計算最大公因數
        Temp=Num1 % Num2
        Num1 = Num2
        Num2 = Temp
    return Num1

Min=Common_Divisor(); #函數呼叫
print("的最大公因數為：",Min)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\count.py

str1="do your best what you can do"
s1=str1.count("do",0)
s2=str1.count("o",0,20)
print("{}\n「do」出現{}次,「o」出現{}次".format(str1,s1,s2))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\func.py

def func(a,b):
    x = a * b
    return x

print(func(4,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\func_default.py

def func(a,b,c=10):
x = a - b + c
return x

print(func(3,1,3)) # a=3 b=1 c=3
print(func(5,2))  # a=5 b=2 c=10

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\func_noreturn.py

def func(a,b):
    x = a * b
    print(x)

print(func(4,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\func1.py

def func(a,b):
    x = a * b
    print(x)

print(func(4,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\hello.py

def hello(word):
      print(word)

hello('Holiday')
hello('Birthday')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\keyword.py

def func(x,y,z):
    formula = x*x+y*y+z*z
    return formula

print(func(z=5,y=2,x=7))
print(func(7, 2, 5))
print(func(x=7, y=2 , z=5))
print(func(7, y=2 , z=5))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\lambda1.py

result = lambda x : 3*x-1  #lambda()函數
print(result(3)) #輸出數值8

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\lambda2.py

def formula(x, y): #自訂函數
    return 3*x+2*y

formula = lambda x, y : 3*x+2*y  #表示lambda有二個參數
print(formula (5,10)) ##傳入兩個數值讓lambda()函數做運算，輸出數值35

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\letterpy.py

phrase = 'never put off until tomorrow what you can do today.'
print('原字串：', phrase)
print('將首字大寫 ', phrase.capitalize())
print('每個單字的首字會大寫', phrase.title())
print('全部轉為小寫字元', phrase.lower()) 
print('判斷字串首字元是否為大寫', phrase.istitle())
print('是否皆為大寫字元', phrase.isupper())
print('是否皆為小寫字元', phrase.islower())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\numberfun.py

print('int(8.4)=',int(8.4))
print('bin(14)=',bin(14))
print('hex(84)=',hex(84))
print('oct(124)=',oct(124))
print('float(6)=',float(6))
print('abs(-6.4)=',abs(-6.4))
print('divmod(58,5)=',divmod(58,5))
print('pow(3,4)=',pow(3,4))
print('round(3.5)=',round(3.5))
print('chr(68)=',chr(68))
print('ord(\'%s\')=%d' %('A',ord('A')))
print('str(1234)=',str(1234))
print('sorted([5,7,1,8,9])=',sorted([5,7,1,8,9]))
print('max(4,6,7,12,3)=',max(4,6,7,12,3))
print('min(4,6,7,12,3)=',min(4,6,7,12,3))
print('len([5,7,1,8,9])=',len([5,7,1,8,9]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\para.py

def factorial(*arg):
    product=1
    for n in arg:
        product *= n
    return product

ans1=factorial(5)
print(ans1)
ans2=factorial(5,4)
print('5*4=',ans2)
ans3=factorial(5,4,3)
print('5*4*3=',ans3)
ans4=factorial(5,4,3,2)
print('5*4*3*2=',ans4)


def myfruit(**arg):
    return arg

print(myfruit(d1='apple', d2='mango', d3='grape'))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\pow.py

#引數：x 為底數       
#y 為指數       
#傳回值：次方運算結果 
def Pow(x,y):
    p=1
    for i in range(y):
        p *= x
    return p
print("請輸入次方運算（ex.2 3）：")
x,y=input().split()
print('x=',x)
print('y=',y)
print("次方運算結果: %d" %Pow(int(x), int(y)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\replace.py

s= "My favorite sport is baseball."
print(s)
s1=s.replace("baseball", "basketball")
print(s1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\return01.py

def func(a,b):
    p1 = a * b
    p2 = a - b
    return p1, p2
 
num1 ,num2 = func(5, 4)
print(num1)  
print(num2)  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\return02.py

def func(length,width,height):
    p1 = length*width*height
    p2 = length+width+height
    p3 = (length*width+height*length+width*height)*2
    return p1, p2, p3
 
num1 ,num2, num3 = func(5, 4, 3)
print(num1)  
print(num2)
print(num3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\sequence.py

str1="I love python."
print("原字串內容: ",str1)
print("轉換成串列: ",list(str1))
print("轉換成值組: ",tuple(str1))
print("字串長度: ",len(str1))

list1=[8,23,54,33,12,98]
print("原串列內容: ",list1)
print("串列中最大值: ",max(list1))
print("串列中最小值: ",min(list1))

relist=reversed(list1)#反轉串列
for i in relist: #將反轉後的串列內容依序印出
    print(i,end=' ')
print()#換行
print("串列所有元素總和: ",sum(list1))#印出總和
print("串列元素由小到大排序: ",sorted(list1))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\split.py

str1 = "apple \nbanana \ngrape \norange"
print( str1.split() )
print( str1.split(' ', 2 ) )

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch07\startswith.py

wd = 'Python is funny and powerful.'
print('字串:', wd)
print('Python為開頭的字串嗎', wd.startswith('Python'))   #回傳True
print('funny為開頭的字串嗎', wd.startswith('funny', 0))#回傳False
print('funny從指定位置的開頭的字串嗎', wd.startswith('funny', 10))  #回傳True
print('powerful.為結尾字串嗎', wd.endswith('powerful.'))  #回傳True

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\attribute.py

import datetime
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date(2019,5,10).year)
print(datetime.date(2019,8,24).month)
print(datetime.date(2019,8,24).day)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\date.py

import datetime
print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.date(2019,3,9).weekday())
print(datetime.date(2019,7,2).isoweekday())
print(datetime.date(2019,5,7).isocalendar())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\datetime.py

import datetime
print(datetime.date(2018,5,25))
print(datetime.time(12, 58, 41))
print(datetime.datetime(2018, 3, 5, 18, 45, 32))
print(datetime.timedelta(days=1))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\import.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\lastDay.py

import datetime as d

def check(y,m):    
    temp_d=d.date(y,m,1)
    temp_year = temp_d.year
    temp_month= temp_d.month
    
    if temp_month == 12 :
        temp_month = 1
        temp_year += 1
    else:
        temp_month += 1   
        
    return d.date(temp_year,temp_month,1)+ d.timedelta(days=-1)

year=int(input("請輸入要查詢的西元年："))
month=int(input("請輸入要查詢的月份1-12："))
print("你要查詢的月份的最後一天是西元",check(year,month))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\math.py

import math as m #以別名取代
print("sqrt(16)= ",m.sqrt(16)) #平方根
print("fabs(-8)= ",m.fabs(-8)) #取絕對值
print("fmod(16,5)= ",m.fmod(16,5)) # 16%5
print("floor(3.14)= ",m.floor(3.14)) # 3

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\my_module.py

'''
    函數功能：計算獎金的百分比
    price:產品單價
    num:銷售數量
    price*num:銷售業績總額
    total:實得獎金
'''
def payment():
    price = float(input("產品單價："))
    num = float(input("銷售數量："))
    rate = 0.35  #抽取獎金的百分比
    total = price * num * rate
    return price*num, total

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\os.py

import os
directory=os.getcwd()

os.mkdir(directory+"/example")  #建立資料夾
os.mkdir(directory+"/doc")  #建立資料夾
directory_listdir=os.listdir( directory )
print("資料夾裡的文件與資料夾:{}".format(directory_listdir))

os.rename(directory+"/example",directory+"/sample") #更名
directory_listdir=os.listdir( directory )
print("資料夾裡的文件與資料夾:{}".format(directory_listdir))

os.rmdir(directory+"/doc")
directory_listdir=os.listdir( directory )
print("資料夾裡的文件與資料夾:{}".format(directory_listdir))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\random.py

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

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\range1.py

import random as r #以別名方式匯入random模組
for i in range(10): #執行10次
    print ( r.randrange(2, 500, 2) ) #從2-500間取10個偶數

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\range2.py

import random as r #以別名方式匯入random模組
for i in range(10): #執行10次
    print(r.randrange(100)) #從0-100取隨機整數

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\rint.py

import random as r #為random模組取別名
for j in range(6): #以迴圈執行6次
    print(r.randint(1,42), end=' ')#產生1-42的整數亂數
print() #換行1
for j in range(3): #以迴圈執行3次
    print(r.uniform(1,10), end=' ')#產生1-10間的亂數

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\test_argv.py

import sys

print("sys.argv:{}".format(sys.argv))
print("文件名稱{}".format(sys.argv[0]))
length = len(sys.argv)
 
if len(sys.argv) < 2:
    sys.exit(0)

for i in range(1,length):
     n1 = sys.argv[i]
     print( "第{}個引數是{}".format(i,n1))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\time.py

import time as t

print(t.time())
print(t.localtime())

field=t.localtime(t.time())#以元組資料的名稱去取得資料
print('tm_year= ',field.tm_year)
print('tm_mon= ',field.tm_mon)
print('tm_mday= ',field.tm_mday)
print('tm_hour= ',field.tm_hour)
print('tm_min= ',field.tm_min)
print('tm_mec= ',field.tm_sec)
print('tm_wday= ',field.tm_wday)
print('tm_yday= ',field.tm_yday)
print('tm_isdst= ',field.tm_isdst)

for j in range(9):#以元組的索引值取得的資料內容
    print('以元組的索引值取得資料= ',field[j])
            
print("我有一句話想對你說:")
t.sleep(1) #程式停1秒
print("學習Python的過程唯然漫長,但最終的果實是甜美的")
print("程式執行到目前的時間是"+str(t.process_time()))
t.sleep(2) #程式停2秒
print("程式執行到目前的時間是"+str(t.perf_counter()))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\time_fun.py

import datetime
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time(18,25,33).hour)
print(datetime.time(18,25,33).minute)
print(datetime.time(18,25,33).second)
print(datetime.time(18,25,33, 32154).microsecond)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\輕鬆學會運算思維與Python程式設計\ch08\use_my_module.py

import my_module #匯入自己建立的模組
e1 ,e2 = my_module.payment()  #呼叫自訂模組內的函數
print("總銷售業績{},應付獎金：{}".format(e1, e2))

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
