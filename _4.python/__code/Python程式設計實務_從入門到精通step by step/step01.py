import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

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

str1="Happy birthday to my best friend."
s1=str1.count("to",0) #從str1字串索引0的位置開始搜尋
s2=str1.count("e",0,34) #搜尋str1從索引值0到索引值34-1的位置
print("{}\n「to」出現{}次,「e」出現{}次".format(str1,s1,s2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\ExCarry.py

i = 10

for j in range(5):
    z = i + j
    print("小寫：%x\t大寫：%X" %(z, z))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%06.2f\n" %(1.2345))

print("不足數位預設空格：%6.2f\n" %(1.2345))

print("小數點保留2位：%.2f\n" %(1.2345))

print("不足數位補0(以*替代)：%0*.2f\n" %(6, 1.2345))

print("------------------------------------------------------------")  # 60個

print("\n不足數位補0：%05d\n" %(66))

print("不足數位預設空格：%5d\n" %(66))

print("小於位數則輸出全部：%2d\n" %(666))

print("不足數位補0(以*替代)：%0*d\n" %(5, 66))

print("------------------------------------------------------------")  # 60個

list1 = ["A", True, 10, 3.14, "G"]

for i in range(len(list1)):
   print("索引位置：%s\t對應值：%s\t型態：%s\n" %(i, list1[i], type(list1[i])))

print("------------------------------------------------------------")  # 60個

person = ["John", "Merry", "Mi", "Jason"]

addPerson = "David"

if person.count(addPerson) == 0:
   person.insert(len(person) - 2, addPerson)

print("搜尋剛新增人員索引位置：", person.index(addPerson))

person1 = person.copy()
person.clear()

print("複製原串列：", person1)
print("原串列：", person)

print("------------------------------------------------------------")  # 60個

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

Index = "Hello Python, This is Program"

print("Index字串：", Index)
print(Index[-3:-25:-2])

print("------------------------------------------------------------")  # 60個

strName = "台北永和三支"
strCode = "3388128"
intAount = 123456
intMoney = 456789
	
print("\n郵局：%s" %(strName))
print("郵局代號為%s，轉帳戶頭為%02d" %(strCode, intAount))
print("匯入金額：%c%.2f" %(36, intMoney))
	
if intMoney < 20000:
    print("%c\n" %("成"))

print("------------------------------------------------------------")  # 60個


print("="*30, "\n")

print("------------------------------------------------------------")  # 60個

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

phrase = 'Happy holiday.'
print('原字串：', phrase)
print('將首字大寫 ', phrase.capitalize())
print('每個單字的首字會大寫', phrase.title())
print('全部轉為小寫字元', phrase.lower()) 
print('判斷字串首字元是否為大寫', phrase.istitle())
print('是否皆為大寫字元', phrase.isupper())
print('是否皆為小寫字元', phrase.islower())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\replace.py

s= "我畢業於宜蘭高中."
print(s)
s1=s.replace("宜蘭高中", "高雄中學")
print(s1)

print("------------------------------------------------------------")  # 60個

fruit = ['apple', 'orange', 'watermelon']
print('反轉前內容：', fruit)
fruit.reverse() 
print('反轉後內容：', fruit)
score = [65,76,54,32,18]
print('反轉前內容：', score)
score.reverse() 
print('反轉後內容：', score)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\sort.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\split.py

str1 = "happy \nclever \nwisdom"
print( str1.split() ) #以空格與換行符號(\n)來分割
print( str1.split(' ', 2 ) ) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\startswith.py

wd = 'Alex is optimistic and clever.'
print('字串:', wd)
print('Alex為開頭的字串嗎', wd.startswith('Alex')) 
print('clever為開頭的字串嗎', wd.startswith('clever', 0))
print('optimistic從指定位置的開頭的字串嗎', wd.startswith('optimisti', 8)) 
print('clever.為結尾字串嗎', wd.endswith('clever.'))  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\tuple_sorted.py

pay = (8000, 7200, 8300, 4700, 5500)
print(pay)
print('由小而大：',sorted(pay))
print('由大而小：', sorted(pay, reverse = True))

print('資料仍維持原順序：')
print(pay)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\unpack01.py

word1 = "zoo"
word2 = "animal"
print("交換前: ")
print('單字1={},單字2={}'.format(word1,word2))
word2,word1 = word1,word2
print("交換後: ")
print('單字1={},單字2={}'.format(word1,word2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch06\unpack02.py

product = (('iPhone','手機','我預算的首選'),
        ('iPad','平板','視股票獲利'),
        ('iPod','播放','價格最親民'))

for(name, c_name,memo) in product:
    print('%-10s %-12s %-10s'%(name,c_name,memo))

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

def func(a,b,c):
    x = a +b +c
    return x

print(func(1,2,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\func1.py

def func(a,b,c):
    x = a +b +c
    print(x)

print(func(1,2,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\keyword.py

def equation(x,y,z):
    ans = x*y+z*x+y*z
    return ans

print(equation(z=1,y=2,x=3))
print(equation(3, 2, 1))
print(equation(x=3, y=2 , z=1))
print(equation(3, y=2 , z=1))

print("------------------------------------------------------------")  # 60個

total=lambda a,b:a+b
num1=0
num2=0
num1=123
num2=456
print('數值 1+數值 2 =',total(num1,num2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\math.py

score=[97,76,89,76,90,100,87,65]
print('本學期總共考過的數學小考次數', len(score))
print('所有成績由小到大排序的結果為: {}'.format(sorted(score)))
print('本學期所有分數的總和', sum(score))
print('本學期所有分數的平均', round(sum(score)/len(score),1))
print('本學期考最差的分數為', min(score))
print('本學期考最好的分數為', max(score))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\para.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\para1.py

def dinner(mainmeal, *sideorder):
    #列出所點餐點的主餐及點心副餐
    print('所點的主餐為',mainmeal,'所點的副餐點心包括:')
    for snack in sideorder:
        print(snack)

dinner('鐵板豬','烤玉米')
dinner('泰式火鍋','德式香腸','香焦牛奶','幸運餅')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\pow.py

def Pow(x, y):
    p = 1;
    for i in range(y+1):
        p *= x
    return p
print('請輸入兩數x及y的值函數：')
x=3
y=8
print('次方運算結果：%d' %Pow(x, y))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\seq.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\swap.py

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

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch07\value.py

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

import calendar

y = 2023
m = 12
ys = 5 # int(input("列印n年內為閏年的月曆:"))
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

"""
import math
x = 10
y = -2

z = math.fabs(x / y)
h = math.factorial(z)

if math.isnan(h) == False:
    print("計算後數值：", h)
    print("最大公約數：", math.gcd(h, x))
"""

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch08\ExRandomSort.py

import random
name = ["小明", "小黃", "小紅", "小綠", "小白"]

print("抽取一個元素：", random.choice(name))

print("抽取三個元素：", random.sample(name, 3))

print("抽取三個元素：", random.shuffle(name))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch08\ExRandrange.py

import random

print("任一整數", random.randrange(100))

print("任一整數", random.randrange(52, 100))

print("奇數", random.randrange(1, 100, 2))

print("偶數", random.randrange(0, 100, 2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch08\ExTime.py

import time

t = time.time()
tLocal = time.localtime(t)

print("轉換時間形式(年/月/日)：", time.strftime("%Y/%m/%d", tLocal))
print("轉換時間形式(年/月/日 時:分:秒)：", time.asctime (tLocal))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch08\GetParam.py

import sys
if len(sys.argv) < 0:
    print("未有外部傳入參數")
else:
    print("Python版本號：", sys.version)
    print("作業系統：", sys.platform)

    for n in range(len(sys.argv)):
        print("param" + str(n) + "：", sys.argv[n])

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python程式設計實務_從入門到精通step by step\ch08\import.py

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



print("作業完成")

