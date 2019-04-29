#!/usr/bin/python
import time;  # This is required to include time module.

#取得tick數
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)


#獲取當前時間
localtime = time.localtime(time.time())
print("Local current time :", localtime)


#獲取格式化的時間
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

#獲取日曆月份
import calendar

cal = calendar.month(2019, 4)
print("Here is the calendar:")
print(cal)


#import datetime
from datetime import *; from dateutil.relativedelta import *

NOW = datetime.now()
TODAY = date.today()

print(NOW)
print(TODAY)

#how old is john
johnbirthday = datetime(1978, 4, 5, 12, 0)
#relativedelta(NOW, johnbirthday)

print(relativedelta(NOW, johnbirthday))


#使用dir()內置函數返回一個包含一個模塊中定義名稱的字符串的排序列表。
#該列表包含在一個模塊中定義的所有模塊，變量和函數的名稱。

import math
content = dir(math)
print(content)





Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   #global Money
   Money = Money + 1

print(Money)
AddMoney()
print(Money)

