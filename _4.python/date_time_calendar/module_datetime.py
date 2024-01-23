import datetime

print('------------------------------------------------------------')	#60個

import datetime

text = "2012-09-20"
y = datetime.datetime.strptime(text, "%Y-%m-%d")
z = datetime.datetime.now()
diff = z - y
print(diff)

print(z)
nice_z = datetime.datetime.strftime(z, "%A %B %d, %Y")
print(nice_z)


text = "2012-09-20"
year_s, mon_s, day_s = text.split("-")
ttt = datetime.datetime(int(year_s), int(mon_s), int(day_s))
print(ttt)


import datetime

print(datetime.date.min)
print(datetime.date.max)
print(datetime.date(2019,5,10).year)
print(datetime.date(2019,8,24).month)
print(datetime.date(2019,8,24).day)

import datetime

print(datetime.time.min)
print(datetime.time.max)
print(datetime.time(18,25,33).hour)
print(datetime.time(18,25,33).minute)
print(datetime.time(18,25,33).second)
print(datetime.time(18,25,33, 32154).microsecond)

import datetime

print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.date(2019,3,9).weekday())
print(datetime.date(2019,7,2).isoweekday())
print(datetime.date(2019,5,7).isocalendar())

import datetime

print(datetime.date(2018,5,25))
print(datetime.time(12, 58, 41))
print(datetime.datetime(2018, 3, 5, 18, 45, 32))
print(datetime.timedelta(days=1))



print("------------------------------------------------------------")  # 60個

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

year=2023
month=12
print("你要查詢的月份的最後一天是西元",check(year,month))



print('------------------------------------------------------------')	#60個

import datetime

timeNow = datetime.datetime.now()
print(type(timeNow))
print("列出現在時間 : ", timeNow)
print("年 : ", timeNow.year)
print("月 : ", timeNow.month)
print("日 : ", timeNow.day)
print("時 : ", timeNow.hour)
print("分 : ", timeNow.minute)
print("秒 : ", timeNow.second)

print("------------------------------------------------------------")  # 60個

import datetime

deltaTime = datetime.timedelta(days=3, hours=5, minutes=8, seconds=10)
print(deltaTime.days, deltaTime.seconds, deltaTime.microseconds)


print("------------------------------------------------------------")  # 60個

import datetime

deltaTime = datetime.timedelta(days=100)
timeNow = datetime.datetime.now()
print("現在時間是 : ", timeNow)
print("100天後是  : ", timeNow + deltaTime)

print("------------------------------------------------------------")  # 60個

import datetime

timeNow = datetime.datetime.now()
print(timeNow.strftime("%Y/%m/%d %H:%M:%S"))
print(timeNow.strftime("%y-%b-%d %H-%M-%S"))


print("------------------------------------------------------------")  # 60個

"""

import datetime

timeStop = datetime.datetime(2023, 11, 18, 17, 50, 0)
while datetime.datetime.now() < timeStop:
    print("program is sleeping.", end="")
print("Wake up")

print("------------------------------------------------------------")  # 60個


import datetime

timeStop = datetime.datetime(2024, 1, 1, 8, 0, 0)
while datetime.datetime.now() < timeStop:
    pass
print("女朋友生日")
"""






print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




