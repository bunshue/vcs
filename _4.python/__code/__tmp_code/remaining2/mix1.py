import sys

print('------------------------------------------------------------')	#60個

import datetime

print(datetime.date.min)
print(datetime.date.max)
print(datetime.date(2019,5,10).year)
print(datetime.date(2019,8,24).month)
print(datetime.date(2019,8,24).day)

print('------------------------------------------------------------')	#60個
"""
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
"""
print('------------------------------------------------------------')	#60個

import random

print(random.random()) #產生隨機浮點數n,0 <= n < 1.0
print(random.uniform(101, 200)) #產生101-200之間的隨機浮點數
print(random.randint(-50, 0)) #產生-50-0之間的隨機整數
print(random.randrange(0, 88, 11)) #從序列中取一個隨機數
print(random.choice(["健康", "運勢", "事業", "感情", "流年"]) ) #

items = ['a','b','c','d']
random.shuffle(items) #將items序列打亂
print(items)
#從序列或集合擷取12個不重複的元素
print(random.sample('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', 12))

print('------------------------------------------------------------')	#60個

import random
for i in range(10): #執行10次
    print (random.randrange(2, 500, 2) ) #從2-500間取10個偶數

print('------------------------------------------------------------')	#60個

import random
for i in range(10): #執行10次
    print(random.randrange(100)) #從0-100取隨機整數

print('------------------------------------------------------------')	#60個

import random
for j in range(6): #以迴圈執行6次
    print(random.randint(1,42), end=' ')#產生1-42的整數亂數
print() #換行1
for j in range(3): #以迴圈執行3次
    print(random.uniform(1,10), end=' ')#產生1-10間的亂數

print('------------------------------------------------------------')	#60個

import time

print(time.time())
print(time.localtime())

field=time.localtime(time.time())#以元組資料的名稱去取得資料
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

print('------------------------------------------------------------')	#60個

import datetime
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time(18,25,33).hour)
print(datetime.time(18,25,33).minute)
print(datetime.time(18,25,33).second)
print(datetime.time(18,25,33, 32154).microsecond)

print('------------------------------------------------------------')	#60個

import datetime
print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.date(2019,3,9).weekday())
print(datetime.date(2019,7,2).isoweekday())
print(datetime.date(2019,5,7).isocalendar())

print('------------------------------------------------------------')	#60個

import datetime
print(datetime.date(2018,5,25))
print(datetime.time(12, 58, 41))
print(datetime.datetime(2018, 3, 5, 18, 45, 32))

print('------------------------------------------------------------')	#60個

import random

for i in range(5):
    a = random.randint(1,10) #隨機取得整數
    print(a,end=' ')
print()
#給定items數列的初始值
items = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
random.shuffle(items)  #使用shuffle函數洗牌
print(items)#將洗牌後的序列輸出

print('------------------------------------------------------------')	#60個

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

#year=int(input("請輸入要查詢的西元年："))
#month=int(input("請輸入要查詢的月份1-12："))
year= 2024
month = 4
print("你要查詢的月份的最後一天是西元",check(year,month))

print('------------------------------------------------------------')	#60個

import math as m #以別名取代
print("sqrt(16)= ",m.sqrt(16)) #平方根
print("fabs(-8)= ",m.fabs(-8)) #取絕對值
print("fmod(16,5)= ",m.fmod(16,5)) # 16%5
print("floor(3.14)= ",m.floor(3.14)) # 3

print('------------------------------------------------------------')	#60個



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

"""
import my_module #匯入自己建立的模組
e1 ,e2 = my_module.payment()  #呼叫自訂模組內的函數
print("總銷售業績{},應付獎金：{}".format(e1, e2))
"""
print('------------------------------------------------------------')	#60個

import random

NUM_DIGITS = 10

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')  # Create a list of digits 0 to 9.
    random.shuffle(numbers)  # Shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


secretNum = getSecretNum()
print(secretNum)

print("------------------------------------------------------------")  # 60個

from random import randint
import os.path

#pfile = input("請輸入檔名：").strip()

pfile = 'tmp_cccccc.txt'
if os.path.isfile(pfile):
    print("此檔案已經存在，程式終止")
else:
    poutfile = open(pfile, "w")
        
    for i in range(30):
        print(randint(0, 999), file = poutfile, end = " ")
       
    poutfile.close()
        
    pinfile = open(pfile, "r")
    ps = pinfile.read()
    
    pnumber = [eval(items) for items in ps.split()]
    pnumber.sort()
        
    for i in range(len(pnumber)):
        print(pnumber[i], end = " ")
            
    pinfile.close()

print("------------------------------------------------------------")  # 60個

import datetime
now = datetime.datetime.now() # current date and time

date_time = now.strftime('%Y年%m月%d日, %H:%M:%S')
print("現在時間 :", date_time)

import datetime

dt = datetime.datetime(2006, 3, 11, 9, 15),
print(dt)

cc = time.strftime("%Y-%m-%d %H:%M")
print(cc)

cc = time.strftime('%Y-%m-%d %H:%M+%Z')
print(cc)

print("------------------------------------------------------------")  # 60個

import time
currentTime = time.asctime()

print("時間 :", currentTime)

entrySecond = time.time()
print("時間 :", entrySecond)

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



