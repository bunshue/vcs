import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\append.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\copy.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\copy1.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\count.py

word = ["holiday", "happy", "birth",
             "yesterday", "holiday", "car",
             "yellow", "happy", "mobile",
             "cup", "happy", "holiday",
             "holiday", "desk", "birth",
             ]
print("holiday 出現的次數", word.count("holiday"))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\dict.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\english.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\index.py

word = ["holiday", "happy", "birth",
             "yesterday", "holiday", "car",
             "yellow", "happy", "mobile",
             "cup", "happy", "holiday",
             "holiday", "desk", "birth",
             ]
search_str="yellow"
print("單字 %s 第一次出現的索引值%d" %(search_str,word.index(search_str)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\listsort.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\reverse.py

no = [185, 278, 97, 48, 33, 61]
print('反轉前內容：', no)
no.reverse() 
print('反轉後內容：', no)

zoo = ['tiger', 'lion', 'horse', 'cattle']
print('反轉前內容：', zoo)
zoo.reverse() 
print('反轉後內容：', zoo)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\set.py

friendA= {"Andy", "Axel", "Michael","May"}
friendB = {"Peter", "Axel", "Andy","Julia"}
print(friendA & friendB)
print(friendA | friendB)
print(friendA - friendB)
print(friendA ^ friendB)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\swap.py

x = 859
y = 935
print("兩數經交換前的值: ")
print('x={},y={}'.format(x,y))
y,x = x,y
print("兩數經交換後的值: ")
print('x={},y={}'.format(x,y))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\tuple_create.py

tup = (28, 39, 58, 67,97, 54) 
print('目前元組內的所有元素：')
for item in range(len(tup)):
   print ('tup[%2d] %3d' %(item, tup[item]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\tuple_sorted.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\unpack.py

info = [['C程式設計','朱大峰','480'],
        ['Python程式設計','吳志明','500'],
        ['Java程式設計','許伯如','540']]

for(book, author,price) in info:
    print('%10s %3s'%(book,author),' 書籍訂價:',price)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch06\word.py

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



#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\align.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\arg.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\blessings.py

def blessings():
    print('一元復始，萬象更新')

blessings()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\blessings_para.py

def blessings(str1):
    print(str1)

blessings('一元復始，萬象更新')
blessings('恭賀新喜，財源滾滾')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\bonus.py

def payment():
    price = float(input("產品單價："))
    num = float(input("銷售數量："))
    rate = 0.35  #抽取獎金的百分比
    total = price*num * rate
    return price*num, total
 
e1 ,e2 = payment()
print("總銷售業績{},應付獎金：{}".format(e1, e2))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\common.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\count.py

str1="do your best what you can do"
s1=str1.count("do",0)
s2=str1.count("o",0,20)
print("{}\n「do」出現{}次,「o」出現{}次".format(str1,s1,s2))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\func.py

def func(a,b):
    x = a * b
    return x

print(func(4,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\func_default.py

def func(a,b,c=10):
    x = a - b + c
    return x

print(func(3,1,3)) # a=3 b=1 c=3
print(func(5,2))  # a=5 b=2 c=10

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\func_noreturn.py

def func(a,b):
    x = a * b
    print(x)

print(func(4,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\func1.py

def func(a,b):
    x = a * b
    print(x)

print(func(4,3))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\hello.py

def hello(word):
      print(word)

hello('Holiday')
hello('Birthday')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\keyword.py

def func(x,y,z):
    formula = x*x+y*y+z*z
    return formula

print(func(z=5,y=2,x=7))
print(func(7, 2, 5))
print(func(x=7, y=2 , z=5))
print(func(7, y=2 , z=5))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\lambda1.py

result = lambda x : 3*x-1  #lambda()函數
print(result(3)) #輸出數值8

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\lambda2.py

def formula(x, y): #自訂函數
    return 3*x+2*y

formula = lambda x, y : 3*x+2*y  #表示lambda有二個參數
print(formula (5,10)) ##傳入兩個數值讓lambda()函數做運算，輸出數值35

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\letterpy.py

phrase = 'never put off until tomorrow what you can do today.'
print('原字串：', phrase)
print('將首字大寫 ', phrase.capitalize())
print('每個單字的首字會大寫', phrase.title())
print('全部轉為小寫字元', phrase.lower()) 
print('判斷字串首字元是否為大寫', phrase.istitle())
print('是否皆為大寫字元', phrase.isupper())
print('是否皆為小寫字元', phrase.islower())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\numberfun.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\para.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\pow.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\replace.py

s= "My favorite sport is baseball."
print(s)
s1=s.replace("baseball", "basketball")
print(s1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\return01.py

def func(a,b):
    p1 = a * b
    p2 = a - b
    return p1, p2
 
num1 ,num2 = func(5, 4)
print(num1)  
print(num2)  

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\return02.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\sequence.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\split.py

str1 = "apple \nbanana \ngrape \norange"
print( str1.split() )
print( str1.split(' ', 2 ) )

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch07\startswith.py

wd = 'Python is funny and powerful.'
print('字串:', wd)
print('Python為開頭的字串嗎', wd.startswith('Python'))   #回傳True
print('funny為開頭的字串嗎', wd.startswith('funny', 0))#回傳False
print('funny從指定位置的開頭的字串嗎', wd.startswith('funny', 10))  #回傳True
print('powerful.為結尾字串嗎', wd.endswith('powerful.'))  #回傳True

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\attribute.py

import datetime
print(datetime.date.min)
print(datetime.date.max)
print(datetime.date(2019,5,10).year)
print(datetime.date(2019,8,24).month)
print(datetime.date(2019,8,24).day)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\date.py

import datetime
print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.date(2019,3,9).weekday())
print(datetime.date(2019,7,2).isoweekday())
print(datetime.date(2019,5,7).isocalendar())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\datetime.py

import datetime
print(datetime.date(2018,5,25))
print(datetime.time(12, 58, 41))
print(datetime.datetime(2018, 3, 5, 18, 45, 32))
print(datetime.timedelta(days=1))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\import.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\lastDay.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\math.py

import math as m #以別名取代
print("sqrt(16)= ",m.sqrt(16)) #平方根
print("fabs(-8)= ",m.fabs(-8)) #取絕對值
print("fmod(16,5)= ",m.fmod(16,5)) # 16%5
print("floor(3.14)= ",m.floor(3.14)) # 3

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\my_module.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\os.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\random.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\test_argv.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\time.py

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

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\time_fun.py

import datetime
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time(18,25,33).hour)
print(datetime.time(18,25,33).minute)
print(datetime.time(18,25,33).second)
print(datetime.time(18,25,33, 32154).microsecond)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch08\use_my_module.py

import my_module #匯入自己建立的模組
e1 ,e2 = my_module.payment()  #呼叫自訂模組內的函數
print("總銷售業績{},應付獎金：{}".format(e1, e2))

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch10\bubble.py

data=[99,95,90,88,78,67,33,26,12]#原始資料 
print('氣泡排序法：原始資料為：')
for i in range(len(data)):
    print('%3d' %data[i],end='')
print()

for i in range(len(data)-1,0,-1): #掃描次數
    for j in range(i):
        if data[j]>data[j+1]:#比較,交換的次數
            data[j],data[j+1]=data[j+1],data[j]#比較相鄰兩數,如果第一數較大則交換
    print('第 %d 次排序後的結果是：' %(len(data)-i),end='') #把各次掃描後的結果印出
    for j in range(len(data)):
        print('%3d' %data[j],end='')
    print()
	
print('排序後結果為：')
for j in range(len(data)):
    print('%3d' %data[j],end='')
print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch10\fib.py

def fib(n):	# 定義函數fib()
    if n==0 :
        return 0 # 如果n=0 則傳回 0
    elif n==1 or n==2:
        return 1
    else:   # 否則傳回 fib(n-1)+fib(n-2)
        return (fib(n-1)+fib(n-2))

n=int(input('請輸入所要計算第幾個費式數列:'))
for i in range(n+1):# 計算前n個費氏數列
    print('fib(%d)=%d' %(i,fib(i)))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch10\mouse.py

#老鼠走迷宮
class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.next=None

class Mouse:
    def __init__(self):
        self.first=None
        self.last=None
        
    def empty(self):
            return self.first==None

    def add(self,x,y):
        newNode=Node(x,y)
        if self.first==None:
            self.first=newNode
            self.last=newNode
        else:
            self.last.next=newNode
            self.last=newNode
        
    def remove(self):
        if self.first==None:
            print('[佇列已經空了]')
            return
        newNode=self.first
        while newNode.next!=self.last:
            newNode=newNode.next
        newNode.next=self.last.next
        self.last=newNode
        
ExitX= 8	#出口的X座標
ExitY= 10	#出口的Y座標
#宣告迷宮陣列
arr= [[1,1,1,1,1,1,1,1,1,1,1,1], \
       [1,0,0,0,1,1,1,1,1,1,1,1], \
       [1,1,1,0,1,1,0,0,0,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,0,0,0,0,1,1,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,0,1,1,0,1,1,0,1,1], \
       [1,1,1,1,1,1,0,1,1,0,1,1], \
       [1,1,0,0,0,0,0,0,1,0,0,1], \
       [1,1,1,1,1,1,1,1,1,1,1,1]]

def find(x,y,ex,ey):
    if x==ex and y==ey:     
        if(arr[x-1][y]==1 or arr[x+1][y]==1 or arr[x][y-1] ==1 or arr[x][y+1]==2):
            return 1
        if(arr[x-1][y]==1 or arr[x+1][y]==1 or arr[x][y-1] ==2 or arr[x][y+1]==1):
            return 1
        if(arr[x-1][y]==1 or arr[x+1][y]==2 or arr[x][y-1] ==1 or arr[x][y+1]==1):
            return 1
        if(arr[x-1][y]==2 or arr[x+1][y]==1 or arr[x][y-1] ==1 or arr[x][y+1]==1):
            return 1
    return 0

#主程式


path=Mouse()
x=1	
y=1

print('[迷宮的路徑(0的部分)]')
for i in range(10):
    for j in range(12):
        print(arr[i][j],end='')
    print()
while x<=ExitX and y<=ExitY:
    arr[x][y]=2
    if arr[x-1][y]==0:
        x -= 1
        path.add(x,y)
    elif arr[x+1][y]==0:
        x+=1
        path.add(x,y)
    elif arr[x][y-1]==0:
        y-=1
        path.add(x,y)
    elif arr[x][y+1]==0:
        y+=1
        path.add(x,y)
    elif find(x,y,ExitX,ExitY)==1:
        break
    else:
        arr[x][y]=2
        path.remove()
        x=path.last.x
        y=path.last.y
print('[老鼠走過的路徑(2的部分)]')
for i in range(10):
    for j in range(12):
        print(arr[i][j],end='')
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch10\quick.py

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
    size=int(input('請輸入陣列大小(100以下)：'))
    inputarr (data,size)
    print('您輸入的原始資料是：')
    showdata (data,size)
    print('排序過程如下：')
    quick(data,size,0,size-1)
    print('最終排序結果：')
    showdata(data,size)

main()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch10\search.py

import random

def bin_search(data,val):
    low=0
    high=49
    while low <= high and val !=-1:
        mid=int((low+high)/2)
        if val<data[mid]:
            print('%d 介於位置 %d[%3d]及中間值 %d[%3d]，找左半邊' \
                   %(val,low+1,data[low],mid+1,data[mid]))
            high=mid-1
        elif val>data[mid]:
            print('%d 介於中間值位置 %d[%3d] 及 %d[%3d]，找右半邊' \
                  %(val,mid+1,data[mid],high+1,data[high]))
            low=mid+1
        else:
            return mid
    return -1

val=1
data=[0]*50
for i in range(50):
    data[i]=val
    val=val+random.randint(1,5)

while True:
    num=0
    val=int(input('請輸入搜尋鍵值(1-150)，輸入-1結束：'))
    if val ==-1:
        break
    num=bin_search(data,val)
    if num==-1:
        print('##### 沒有找到[%3d] #####' %val)
    else:
        print('在第 %2d個位置找到 [%3d]' %(num+1,data[num]))

print('資料內容：')
for i in range(5):
    for j in range(10):
        print('%3d-%-3d' %(i*10+j+1,data[i*10+j]), end='')
    print()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch10\sentry.py

#加入崗哨的改良氣泡排序法
def showdata(data):    #利用迴圈列印資料
    for i in range(len(data)):
        print('%3d' %data[i],end='')
    print()
    
def bubble (data):
    for i in range(len(data)-1,0,-1):
        flag=0 #flag用來判斷是否有執行交換的動作
        for j in range(i):
            if data[j+1]<data[j]:
                data[j],data[j+1]=data[j+1],data[j]
                flag+=1  #如果有執行過交換，則flag不為0
        if flag==0:
            break
        #當執行完一次掃描就判斷是否做過交換動作，如果沒有交換過資料
	#，表示此時陣列已完成排序，故可直接跳出迴圈   
        print('第 %d 次排序：' %(len(data)-i),end='')
        for j in range(len(data)):
            print('%3d' %data[j],end='')
        print()
    print('排序後結果為：',end='')
    showdata (data)

def main():
    data=[1,2,3,4,5,6,8,9,7]  #原始資料
    print('原始資料：')
    showdata(data)
    print('改良氣泡排序法原始資料為：')
    bubble (data)
    
main()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch10\sequential.py

import random

val=0
data=[3,5,7,8,1,12,16,17,15,10,
      23,25,27,29,20,32,34,45,56,37]
      
while val!=-1:
    find=0
    val=int(input('請輸入搜尋鍵值(1-100)，輸入-1離開：'))
    for i in range(20):
        if data[i]==val:
            print('在第 %3d個位置找到鍵值 [%3d]' %(i+1,data[i]))
            find+=1
    if find==0 and val !=-1 :
        print('######沒有找到 [%3d]######' %val)
print('資料內容：')
for i in range(4):
    for j in range(5):
        print('%2d[%3d] ' %(i*5+j+1,data[i*5+j]),end='')
    print('')

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\book.py

class Book:
    #定義方法一：取得書籍名稱和價格
    def setInfo(self, title, price):
        self.title = title
        self.price = price
    #定義方法二：輸出書籍名稱和價格
    def showInfo(self):
        print('書籍名稱:{0:6s}, 價格:{1:4s}元'.format(
            self.title, self.price))
# 產生物件
book1=Book()#物件1
book1.setInfo('Python一週速成', '360')
book1.showInfo() #呼叫方法
book2=Book()#物件2
book2.setInfo('網路行銷與社群行銷', '520')
book2.showInfo()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\brother.py

class Tom():#父類別
    def __init__(self):
        self.height1=178

class Andy(Tom):#父類別是Tom
    def __init__(self):
        self.height2=180
        super().__init__()

class Michael(Tom):#父類別是Tom
    def __init__(self):
        self.height3=185
        super().__init__()
    def display(self):
        print('父親Tom的身高:', self.height1,'公分')
        print('兄弟Andy的身高:', Andy().height2,'公分')
        print('自己Michael的身高:', m1.height3,'公分')

m1=Michael()
m1.display()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\class.py

class Book:
    #定義方法一：取得書籍名稱和價格
    def setData(self, title, price):
        self.title = title
        self.price = price
    #定義方法二：輸出書籍名稱和價格
    def showData(self):
        print('書籍名稱:{0:6s}, 價格:{1:4s}'.format(
            self.title, self.price))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\company.py

#此程式單純類別定義,沒有任何輸出到螢幕的執行結果
class Company: #定義公司類別
    name='賺大錢有限公司'
    def slogan(self):
        print('優良品質 創新研發 強力行銷')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\datatype.py

class Date:
    def setDate(self,birthday): #第一種方法
        self.birthday =birthday
    def showDate(self): #第二種方法
        print("出生年月日:",self.birthday)
d1 = Date()#第一個物件
d1.setDate("民國67年7月3日")#呼叫方法時傳入字串
d1.showDate()
d2 = Date()#第二個物件
d2.setDate([67,7,3])#呼叫方法時傳入串列

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\init1.py

class Wage:
	def __init__(self, fee=200, hour=80):
		self.fee=fee
		self.hour=hour

	def getArea(self):
		return self.fee* self.hour

tom=Wage()
print("透過init()方法預設值的總薪資: ",tom.getArea(),"元")

jane= Wage(250,100)
print("透過init()方法傳入參數的總薪資: ",jane.getArea(),"元")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\isinstance.py

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
tiger = Animal()
daniel= Human()
goldfish=Fish()
alice = Mermaid()
print("tiger是屬於Animal類別:",isinstance(tiger,Animal))
print("daniel是屬於Animal類別:",isinstance(daniel,Animal))
print("goldfish是屬於Animal類別:",isinstance(goldfish,Animal))
print("alice是屬於Animal類別:",isinstance(alice,Animal))
print("===============================================")
print("tiger是屬於Human類別:",isinstance(tiger,Human))
print("daniel是屬於Human類別:",isinstance(daniel,Human))
print("goldfish是屬於Human類別:",isinstance(goldfish,Human))
print("alice是屬於Human類別:",isinstance(alice,Human))
print("===============================================")
print("tiger是屬於Fish類別:",isinstance(tiger,Fish))
print("daniel是屬於Fish類別:",isinstance(daniel,Fish))
print("goldfish是屬於Fish類別:",isinstance(goldfish,Fish))
print("alice是屬於Fish類別:",isinstance(alice,Fish))
print("===============================================")
print("tiger是屬於Mermaid類別:",isinstance(tiger,Mermaid))
print("daniel是屬於Mermaid類別:",isinstance(daniel,Mermaid))
print("goldfish是屬於Mermaid類別:",isinstance(goldfish,Mermaid))
print("alice是屬於Mermaid類別:",isinstance(alice,Mermaid))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\issubclass.py

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

print("Mermaid是屬於Fish子類別:",issubclass(Mermaid,Fish))
print("Mermaid是屬於Human子類別:",issubclass(Mermaid,Human))
print("Mermaid是屬於Animal子類別:",issubclass(Mermaid,Animal))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\multiple1.py

#多重繼承範例1

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature2(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature3(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
alice = Mermaid()
alice.feature1()
alice.feature2()
alice.feature3()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\multiple2.py

#多重繼承範例2

class Animal: #祖父類別
    def feature1(self):
        print('大多數動物能自發且獨立地移動')
        
class Human(Animal): #父類別一
    def feature2(self):
        print('人類是一種有思考能力與情感的高級動物')
        
class Fish(Animal): #父類別二
    def feature3(self):
        print('水生脊椎動物的總稱')

class Mermaid(Human, Fish): #子類別同時繼承兩種類別
    def feature4(self):
        print('又稱人魚,傳說中的生物同時具備人及魚的部份特性')

#產生子類別實體
alice = Mermaid()
alice.feature1()
alice.feature2()
alice.feature3()
alice.feature4()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\override.py

#子類別覆寫父類別的方法
class Normal(): #父類別
    def subsidy(self, income):
        self.money = income
        if self.money >= 500000:
            print('小康家庭補助金額：', end = ' ')
            return 5000
        
class Poor(Normal): #子類別
    def subsidy(self, income): #覆寫subsidy方法
        self.money = income
        if self.money < 300000:
            print('中低收入家庭補助金額：', end = ' ')
            return 10000

student1 = Normal()#建立父類別物件
print(student1.subsidy(780000),'元')

student2 = Poor()#建立子類別物件
print(student2.subsidy(250000),'元')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\polymorphism.py

#多型實作
class Colleague(): #父類別
    def __init__(self, name, income):
        self.name = name
        self.income = income

    def bonus(self):
        return self.income
    
    def title(self):
        return self.name
    
class Manager(Colleague):#子類別
    def bonus(self):        
        return self.income * 1.5
    
class Director(Colleague): #子類別
    def bonus(self):
        return self.income * 1.2
print('===============================')
obj1 = Colleague('一般性員工', 50000) #父類別物件
print('{:8s} 紅利 {:,}'.format(obj1.title(), obj1.bonus()))

print('===============================')
obj2 = Manager('經理級年終', 80000) #子類別物件
print('{:8s} 紅利 {:,}'.format(obj2.title(), obj2.bonus()))

print('===============================')
obj3 = Director('芏任級年終', 65000) #子類別物件
print('{:8s} 紅利 {:,}'.format(obj3.title(), obj3.bonus()))
print('===============================')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\private.py

class Wage:
	def __init__(self, h=80):
		self.__hour=h

	def getHour(self):
		return self.__hour

	def pay(self):
		return hour_fee*self.__hour
hour_fee=200
obj1=Wage(100)
print("每小時基本工資為:",hour_fee,"元")
print("總共工作的小時數:", obj1.getHour())
print("要付給這位工讀生的薪水總額:", obj1.pay(),"元")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\private_error.py

class Wage:
	def __init__(self, h=80):
		self.__hour=h

	def getHour(self):
		return self.__hour

	def pay(self):
		return hour_fee*self.__hour
hour_fee=200
obj1=Wage(100)
print("每小時基本工資為:",hour_fee,"元")
print("總共工作的小時數:", obj1.__hour)
print("要付給這位工讀生的薪水總額:", obj1.pay(),"元")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\single.py

class MobilePhone: #基礎類別
    def touch(self):
        print('我能提供螢幕觸控操作的功能')
        
class HTC(MobilePhone): #衍生類別
    pass

#產生子類別實體
u11 = HTC()
u11.touch()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\single1.py

class MobilePhone: #基礎類別
    def touch(self):
        print('我能提供螢幕觸控操作的功能')
        
class HTC(MobilePhone): #衍生類別
    def touch(self):
        MobilePhone.touch(self)
        print('我也能提供多點觸控的操作方式')

#產生子類別實體
u11 = HTC()
u11.touch()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\super1.py

#在子類別呼叫父類別方法—使用super()函式

class Weekday(): #父類別
    def display(self, pay):
        self.price=pay
        print('歡迎來購物')
        print('購買總金額{:,}'.format(self.price))
        
class Holiday(Weekday): #子類別
    def display(self, pay): #覆寫display方法        
        super().display(pay)
        if self.price >= 15000:            
            self.price *= 0.8
        else:
            self.price        
        print('8折 {:,}'.format(self.price))
        
monday = Weekday()#父類別物件
monday.display(25000)

Christmas = Holiday()#子類別物件
Christmas.display(18000)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\徹底研究-最新Python程式設計實例\ch11\super2.py

#__init__()方法呼叫super()

class Animal():#父類別
    def __init__(self):
        print('我屬於動物類別')
        
class Human(Animal): #子類別
    def __init__(self, name):
        super().__init__()
        print('我也屬於人類類別')

man = Human('黃種人')#子類別實體

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


