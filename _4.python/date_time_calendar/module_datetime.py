import os
import sys
import time
import datetime

print('------------------------------------------------------------')	#60個
'''
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

print('------------------------------------------------------------')	#60個

print(datetime.date.min)
print(datetime.date.max)
print(datetime.date(2019,5,10).year)
print(datetime.date(2019,8,24).month)
print(datetime.date(2019,8,24).day)

print('------------------------------------------------------------')	#60個

print(datetime.time.min)
print(datetime.time.max)
print(datetime.time(18,25,33).hour)
print(datetime.time(18,25,33).minute)
print(datetime.time(18,25,33).second)
print(datetime.time(18,25,33, 32154).microsecond)

print('------------------------------------------------------------')	#60個

print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.date(2019,3,9).weekday())
print(datetime.date(2019,7,2).isoweekday())
print(datetime.date(2019,5,7).isocalendar())

print('------------------------------------------------------------')	#60個

print(datetime.date(2018,5,25))
print(datetime.time(12, 58, 41))
print(datetime.datetime(2018, 3, 5, 18, 45, 32))

print("------------------------------------------------------------")  # 60個

def check(y,m):    
    temp_d=datetime.date(y,m,1)
    temp_year = temp_d.year
    temp_month= temp_d.month
    
    if temp_month == 12 :
        temp_month = 1
        temp_year += 1
    else:
        temp_month += 1   
        
    return datetime.date(temp_year,temp_month,1)+ datetime.timedelta(days=-1)

year=2023
month=12
print("你要查詢的月份的最後一天是西元",check(year,month))

print('------------------------------------------------------------')	#60個

now = datetime.datetime.now()
print(now.ctime())

now = datetime.datetime.now()
print(type(now))
print("列出現在時間 : ", now)
print("年 : ", now.year)
print("月 : ", now.month)
print("日 : ", now.day)
print("時 : ", now.hour)
print("分 : ", now.minute)
print("秒 : ", now.second)

now = datetime.datetime.now()
print(now.strftime("%Y/%m/%d %H:%M:%S"))
print(now.strftime("%y-%b-%d %H-%M-%S"))

print("------------------------------------------------------------")  # 60個

"""
timeStop = datetime.datetime(2023, 11, 18, 17, 50, 0)
while datetime.datetime.now() < timeStop:
    print("program is sleeping.", end="")
print("Wake up")

print("------------------------------------------------------------")  # 60個

timeStop = datetime.datetime(2024, 1, 1, 8, 0, 0)
while datetime.datetime.now() < timeStop:
    pass
print("女朋友生日")
"""

print('------------------------------------------------------------')	#60個

dateObj = datetime.datetime.strptime('2025/1/1', '%Y/%m/%d')
print(dateObj)

print('------------------------------------------------------------')	#60個

work = datetime.date(2021, 10, 9)
print(work)
print(f'一週的第{work.weekday()}天')
num = work.isoweekday()
print('星期天' if num == 7 else '星期 '+ str(num))

print('------------------------------------------------------------')	#60個

# 字串轉換為時間
def strTodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)
print(strTodatetime("2014-3-1", "%Y-%m-%d"))
print(strTodatetime("2019-4-15","%Y-%m-%d") - strTodatetime("2006-03-11","%Y-%m-%d"))

print("------------------------------------------------------------")  # 60個

# 某個日期區間，以1日為間隔值
begin = datetime.date(2021, 10, 1)
end = datetime.date(2021, 10, 15)
step = datetime.timedelta(days = 1)

result = []  #空的List，用來存放日期

# while迴圈 加入date物件
while begin < end:
    result.append(begin.strftime('%Y-%m-%d'))
    begin += step
    
width = 11 #欄寬   
# for/in 讀取並做格式化輸出
for item in result:
    print('{0:{width}}'.format(
        item, width = width), end = '')

print("------------------------------------------------------------")  # 60個

tody = datetime.date.today() # 今天日期
#yr, mt, dt = eval(input('請輸入出生的年、月、日->'))
#2006,3,11

yr, mt, dt = 2006, 3, 11

# 某人生日
birth = datetime.date(yr, mt, dt)
ageDays = tody - birth


print(f'天數：{ageDays.days:,}天')
age = ageDays/datetime.timedelta(days = 365)   # 年齡
print(f'年齡 {age:.2f}')

print("------------------------------------------------------------")  # 60個

# 設兩個時間
d1 = datetime.timedelta(days = 4, hours = 5)
d2 = datetime.timedelta(hours = 2.8)

#將兩個時間相加
dtAdd = d1 + d2    
print(f'共{dtAdd.days}天')
print(f'   7.8時 = {dtAdd.seconds:7,}')
print(f'4天7.8時 = {dtAdd.total_seconds():9,} 秒')

print("------------------------------------------------------------")  # 60個

"""
d1 = datetime.datetime(2018, 9, 2)
print('日期：', d1 + (datetime.timedelta(days = 7)))

d2 = datetime.datetime(2020, 1, 22)
d3 = datetime.timedelta(days = 106)
dt = d2 - d3 # 將兩個日期相減
print('日期二：', datetime.strftime('%Y-%m-%d'))
"""
print("------------------------------------------------------------")  # 60個

#建立儲存星期的list物件
weeklst = ['Monday', 'Tuesday', 'Wednesday',
         'Thursday', 'Friday', 'Saturday', 'Sunday']

# 定義函式
def getWeeks(wkName, beginDay = None):
    #如果未傳入beginDay之日期，就以今天為主
    if beginDay is None:
        beginDay = datetime.datetime.today()
        
    #weekday()方法回傳取得星期的索引值，Monday索引值為0
    indexNum = beginDay.weekday()
    target = weeklst.index(wkName)
    lastWeek = ( 7 + indexNum - target) % 7
    if lastWeek == 0:
        lastWeek = 7
        
    #timedelta()建構式取得天數
    lastWeek_Day = beginDay - datetime.timedelta(
        days = lastWeek)
    return lastWeek_Day.strftime('%Y-%m-%d')

#呼叫函式，只傳入一個參數
print('今天的上週三：', getWeeks('Wednesday'))

#呼叫函式，傳入二個參數
dt = datetime.datetime(2017, 4, 11)
print('2017/4/11 的上週二：', getWeeks('Tuesday', dt))

print('------------------------------------------------------------')	#60個

# a = input('請輸入你的出生年月日 ( yyyy/mm/dd )：')
a = "2006/03/11"
now = datetime.datetime.now()

ad = datetime.datetime.strptime(a, "%Y/%m/%d")
y = now.year - ad.year
m = now.month - ad.month
d = now.day - ad.day

print(f"你的生日是：{y} 歲 {m} 個月又 {d} 天")  # 使用 python3 語法

print("------------------------------------------------------------")  # 60個

today = datetime.date.today()
print("今天的日期 :", today)

print('------------------------------------------------------------')	#60個


x = datetime.datetime(2020, 10, 22)
print(x)

x = datetime.datetime(year=2020, month=10, day=22)
print(x)

y = datetime.datetime(2020, 10, 22, 10, 30, 45)  # 設定日期與時間
print(y)

print("------------------------------------------------------------")  # 60個

# timedelta 物件

x = datetime.timedelta(hours=1, minutes=30)  # 1 小時又 30 分

print(x)
y = datetime.timedelta(days=1, seconds=30)  # 1 天又 30 秒
print(y)

# 用 timedelta 來增減 datetime 或 timedelta 的時間

x = datetime.datetime(2020, 10, 22, 10, 30, 45)  # 原始時間

y = datetime.timedelta(days=1, hours=2, minutes=5)

print(x)

print(x + y)  # 用 timedelta 來增減 datetime 的時間

print(x - y)

print(x + y * 2)



print(datetime.timedelta(days=1))

deltaTime = datetime.timedelta(days=3, hours=5, minutes=8, seconds=10)
print(deltaTime.days, deltaTime.seconds, deltaTime.microseconds)

print("------------------------------------------------------------")  # 60個

now = datetime.datetime.now()
print("現在時間是 : ", now)

deltaTime = datetime.timedelta(days=100)
print("100天後是  : ", now + deltaTime)

print("------------------------------------------------------------")  # 60個








print("------------------------------------------------------------")  # 60個


""" fail
# 將 datetime 時間以格式化方式輸出

x = datetime.datetime(2020, 10, 22, 10, 30, 45)

s1 = x.strftime("%Y/%m/%d %H-%M-%S")
print(s1)

s2 = x.strftime("%Y 年 %m 月 %d 日 %H : %M : %S")
print(s2)
"""

print("------------------------------------------------------------")  # 60個

# 用字串來建立 datetime 物件

s = "2020/10/22 10-30-45"  # 含有特定格式之日期時間字串
x = datetime.datetime.strptime(s, "%Y/%m/%d %H-%M-%S")

print(x)
print(type(x))

print('------------------------------------------------------------')	#60個

def is_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

now = datetime.datetime.now()
date = now.date
month = now.month
year = now.year

m, y = (month, year) if month >= 3 else (month + 12, year - 1)
c, y = y // 100, y % 100
w = (y + y // 4 + c // 4 - 2 * c + 26 * (m + 1) // 10) % 7
month_words = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
print(f"{month_words[month - 1]} {year}".center(20))
print("Su Mo Tu We Th Fr Sa")
print(" " * 3 * w, end="")
days = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
][is_leap(year)][month - 1]
for day in range(1, days + 1):
    print(str(day).rjust(2), end=" ")
    w += 1
    if w == 7:
        print()
        w = 0
print()



print("------------------------------------------------------------")  # 60個

print('---- strftime() 可以將時間格式化 --------------------------------------------------------')	#60個

now = datetime.datetime.now()
print('現在的日期時間 :', now)

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

current_time = now.strftime("%H:%M:%S")
print("時分秒 :", current_time)

date_time = now.strftime("%Y-%m-%d %H:%M:%S")
print("年月日時分秒 :", date_time)

filename = now.strftime("news-%y-%m-%d %H-%M-%S.json")
print(filename)

string = ("%d" % now.year)
print(string)

datetime_format = '%Y/%m/%d %H:%M:%S'

current_time = 'DateTime_{:{}}'.format(now, datetime_format)
print(current_time)



print("------------------------------------------------------------")  # 60個

print('現在的日期時間 :', datetime.datetime.today())
print('現在的日期 :', datetime.date.today())

TODAY = datetime.date.today()
print(TODAY)

#而如果只想要輸出現在的日期的話則用
print(datetime.date.today())

today = str(datetime.datetime.today().date())
current = str(datetime.datetime.today())

print('------------------------------------------------------------')	#60個

now = datetime.datetime.now()
print("今天是{}".format(datetime.datetime.strftime(now, "%Y-%m-%d")))

#date = input("請輸入一個日期（yyyy-mm-dd):")
print('請輸入一個日期')
date = '2006-03-11'
print(date)
target = datetime.datetime.strptime(date, "%Y-%m-%d")
diff = now - target
print("到今天共經過了{}天。".format(diff.days))

print('------------------------------------------------------------')	#60個

year, month, day, hours, minutes, seconds = 2023, 9, 22, 12, 34, 56
cc = datetime.datetime(year, month, day, hours, minutes, seconds)
print(cc)

print('------------------------------------------------------------')	#60個

#取得查詢當年年份及上個月月份
now = datetime.datetime.now() # 取得查詢當下的時間
now_year = now.year # 取得查詢當下當年年份

# 取得查詢當下上個月月份
if(now.month != 1):
    last_month = now.month - 1
else:
    last_month = 12

print("now_year = " + str(now_year))
print("last_month = " + str(last_month))

#how old is john
johnbirthday = datetime.datetime(1978, 4, 5, 12, 0)
#relativedelta(NOW, johnbirthday)

#print(relativedelta(NOW, johnbirthday))

print('---- timediff --------------------------------------------------------')	#60個

#執行時間： 
datetime_st = datetime.datetime.now()

time.sleep(0.3456)  #過了一段時間

datetime_sp = datetime.datetime.now()

print("量測時間 :", (datetime_sp - datetime_st).seconds)

print('------------------------------------------------------------')	#60個

d1 = datetime.datetime(2005, 2, 16)
d2 = datetime.datetime(2004, 12, 31)
print("兩日期相減 :", (d1 - d2).days)

print('------------------------------------------------------------')	#60個

a = datetime.datetime(2012, 3, 1)
b = datetime.datetime(2012, 2, 28)

print(a - b)
print("兩者時間差" , a - b)

a = datetime.datetime(2012, 3, 1, 10, 5, 30)
b = datetime.datetime(2012, 2, 28, 12, 34, 56)

print(a - b)
print("兩者時間差" , a - b)

a = datetime.datetime(2006, 3, 11, 9, 15, 30)
b = datetime.datetime.now()

print("過去時間" , a)
print("現在時間" , b)
print("兩者時間差" , b - a)

print('------------------------------------------------------------')	#60個

datetime_st = datetime.datetime(2016, 1, 1)
datetime_sp = datetime.datetime(2017, 1, 1)

datetime_st = datetime.datetime(2016, 7, 17)
print(datetime_st)

datetime_sp = datetime.datetime(2016, 7, 24)
print(datetime_sp)

expected = [datetime.datetime(2016, 7, i) for i in range(17, 24)]
print(expected)

today = datetime.datetime.today()
birthday = datetime.datetime(2006, 3, 11, 9, 15, 0)
print('相距天時分秒 :', today - birthday)

print('------------------------------------------------------------')	#60個

today = datetime.date.today()
#month = int(input("請問你是在哪一個月份出生："))
month = 3
#day = int(input("請問你是出生日是幾號："))
day = 11
birthday = datetime.date(today.year, month, day)

if birthday < today:
  birthday = datetime.date(today.year+1, month, day)

diff = birthday - today
if diff.days == 0:
  print("不會吧！今天是你的生日，祝你生日快樂！")
else:
  print("哇！再過 " + str(diff.days) + " 天就是你的生日了！")

print('------------------------------------------------------------')	#60個

print('---- datetime.now() --------------------------------------------------------')	#60個

tt = datetime.datetime.strptime("2018-01-31", "%Y-%m-%d")
print(tt)

dateString = "7-May-2018"
dateFormatter = "%u-%b-%Y"
tt = datetime.datetime.strptime(dateString, dateFormatter)
print(tt)

dateString = "31/12/2013"
dateFormatter = "%d/%m/%Y"
tt = datetime.datetime.strptime(dateString, dateFormatter)
print(tt)

dateString = "31/12/2013"
dateFormatter = "%d/%m/%Y"
tt = datetime.datetime.strptime(dateString, dateFormatter)
print(tt)

dateString = "Monday, July 16, 2018 20:01:56"
dateFormatter = "%A, %B %d, %Y %H:%M:%S"
tt = datetime.datetime.strptime(dateString, dateFormatter)
print(tt)

now1 = datetime.datetime.now()
now2 = datetime.datetime.now().date()

print(now1)
print(now2)
print(now2.year)
print(now2.month)
print(now2.day)

print('字串轉日期格式')
date1 = '2023-03-11'
print(date1)
date2 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
print(date2)
print(date2.year)
print(date2.month)
print(date2.day)

date3 = datetime.datetime.now()
mesg = "{} {}:{}:{}".format(date3, date3.hour, date3.minute, date3.second)
print(mesg)

print('字串轉日期格式')
date4 = '2023-04-07 15:41:26'
date5 = datetime.datetime.strptime(date4, "%Y-%m-%d %H:%M:%S")
print(date5)

def transform_date(date): #轉換日期
    y, m, d, h = date[:4],date[5:7],date[8:10],date[11:13]
    return y + '/' + m  + '/' + d  + '/' + h  

old_date = datetime.datetime.now() # 取得現在時間

old_date = str(old_date)    #先轉成字串

#old_date = '2023/05/24 13:00:00' ex

print(old_date)

new_date = transform_date(old_date)
print(new_date)

new_date = now2 + datetime.timedelta(-1)    #昨天
print(new_date)

print('今日日期')
today = datetime.date.today()
print(today)

print('現在時間')
now = datetime.datetime.now()
print(now)

print('1天前的時間')
time_1day = datetime.timedelta(days=1)
print(time_1day)

print('60天前的時間')
time_60day = datetime.timedelta(days=60)
print(time_60day)

print('現在時間 - 60天前的時間')
diff60days = now - time_60day
print(diff60days)

print('現在的年份')
print("%d" % datetime.datetime.now().year)
print('300天後的年份')
print("%d" % (datetime.datetime.now() + datetime.timedelta(days=300)).year)
print('600天後的年份')
print("%d" % (datetime.datetime.now() + datetime.timedelta(days=600)).year)
print('900天後的年份')
print("%d" % (datetime.datetime.now() + datetime.timedelta(days=900)).year)

print('相隔一段時間')
time_diff = datetime.timedelta(weeks=1, days=30, hours=2, minutes=40)
print(time_diff)

print('相隔一段時間')
dt1 = datetime.datetime(2024, 4, 29, 12, 34, 56)
dt2 = datetime.datetime(2006, 3, 11, 9, 15, 30)
print(dt1-dt2)

print('------------------------------------------------------------')	#60個

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)

#而我們也可以算今天是今年的第幾天

dts = '20201007'
dt = datetime.datetime.strptime(dts,"%Y%m%d")
another_dts = dts[:4]+"0101"
another_dt = datetime.datetime.strptime(another_dts,"%Y%m%d")
print(int((dt-another_dt).days)+1)

#由上可得知datetime.datetime.strptime()這個是將所輸入的dts轉換成日期的格式則格式為後面的年月日，再來取出輸入的西元年加上"0101"後一樣轉換成日期的格式最後將輸入日期減掉設定日期後+1輸出成今天為今年的第幾天

loc_dt = datetime.datetime.today()
time_del = datetime.timedelta(hours = 3)
new_dt = loc_dt + time_del
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)

#由上可得知我們也可以調整時差，將我們現在的時間加上3小時的時差並將其輸出出來，一開始我們將抓出本地的時間並且將變數time_del宣告為時差差三個小時，最後將其相加就變成有時差三個小時最後將其指定格式後輸出，而以此類推我們也可以將時差晚三個小時

loc_dt = datetime.datetime.today() 
time_del = datetime.timedelta(hours = 3) 
new_dt = loc_dt - time_del 
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)

print('------------------------------------------------------------')	#60個

d0 = datetime.date(1993, 12, 15)
d1 = datetime.date(2020, 12, 15)

delta = datetime.timedelta(days = 1)
print('日期 :', d0 + delta)

delta = datetime.timedelta(days = 10000)
print('日期 :', d0 + delta)

print('相距日期 :', d1 - d0, '天')

d0 = datetime.date(2021, 5, 24)
d1 = datetime.date(2023, 8, 21)
print('相距日期 :', d1 - d0, '天')

print("------------------------------------------------------------")  # 60個



print('---- timedelta() --------------------------------------------------------')	#60個

print("獲取昨天的日期");
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    yesterday = today - oneday
    #print(type(today))  # 檢視獲取到時間的型別
    #print(type(yesterday))
    return yesterday
yesterday = getYesterday()
print("昨天的時間：", yesterday)

print('------------------------------------------------------------')	#60個

#計算當前時間向後10天的時間。
# 如果是小時 days 換成 hours
d1 = datetime.datetime.now()
d3 = d1 - datetime.timedelta(days = 10)
print(str(d3))
print(d3.ctime())
#print(time.ctime([sec]))#把秒數轉換成日期格式，如果不帶引數，則顯示當前的時間。
#time.ctime([ sec ])
print("time.ctime() : %s" % time.ctime())

print('------------------------------------------------------------')	#60個

path = 'C:/_git/vcs/_4.python'
t1 = datetime.datetime.fromtimestamp(os.stat(path).st_mtime, datetime.timezone.utc)
print(t1)

t2 = t1.astimezone().isoformat()
print(t2)

print('------------------------------------------------------------')	#60個

seconds = datetime.datetime(2004, 10, 26, 10, 33, 33, tzinfo = datetime.timezone(datetime.timedelta(0))).timestamp()
print(seconds)

print('------------------------------------------------------------')	#60個

print('列印一段日期')
start = '2023-09-01'
end   = '2023-09-05'

date_start = datetime.datetime.strptime(start,'%Y-%m-%d')
date_end  = datetime.datetime.strptime(end,'%Y-%m-%d')

print(date_start)
print(date_end)
print('----------------------------')
while date_start<date_end:
    print(date_start)
    date_start+=datetime.timedelta(days=1)    # 日期变量自增

print("------------------------------------------------------------")  # 60個

"""
dt = datetime.datetime.strptime('ttttt', '%Y-%m-%dT%H:%M')  #讀取日期時間
dt = dt.strftime('{d}%Y-%m-%d, {t}%H:%M').format(d='日期為：', t='時間為：')  #轉為字串
"""

print('------------------------------------------------------------')	#60個

def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")

print('------------------------------------------------------------')	#60個


import datetime

# Set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

def getCalendarFor(year, month):
    calText = ''  # calText will contain the string of our calendar.

    # Put the month and year at the top of the calendar:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:
    # (!) Try changing this to abbreviations: SUN, MON, TUE, etc.
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

    # The horizontal line string that separate weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blankRow = ('|          ' * 7) + '|\n'

    # Get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)

    # Roll back currentDate until it is Sunday. (weekday() returns 6
    # for Sunday, not 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # Loop over each week in the month.
        calText += weekSeparator

        # dayNumberRow is the row with the day number labels:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Go to next day.
        dayNumberRow += '|\n'  # Add the vertical line after Saturday.

        # Add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(3):  # (!) Try changing the 4 to a 5 or 10.
            calText += blankRow

        # Check if we're done with the month:
        if currentDate.month != month:
            break

    # Add the horizontal line at the very bottom of the calendar.
    calText += weekSeparator
    return calText

print('建立月行事曆')

year = 2024
month = 4

calText = getCalendarFor(year, month)
print(calText)  # Display the calendar.

# Save the calendar to a text file:
calendarFilename = 'tmp_calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

#print('檔案 :', calendarFilename)


print('------------------------------------------------------------')	#60個

import datetime

now = datetime.datetime.now().strftime("%H:%M:%S")
print(now)  # 14:30:23


print("------------------------------------------------------------")  # 60個

import datetime
import time

while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\r{now}", end="")  # 前方加上 \r
    time.sleep(1)


print("------------------------------------------------------------")  # 60個


import datetime
import time


def timezone(h):
    GMT = datetime.timezone(datetime.timedelta(hours=h))  # 取得時區
    return datetime.datetime.now(tz=GMT).strftime("%H:%M:%S")  # 回傳該時區的時間


# 六個時區的名稱與時差
local = {"倫敦": 1, "台灣": 8, "日本": 9, "紐約": -4, "洛杉磯": -7, "紐西蘭": 12}

while True:
    print("\r", end="")  # 開始時將游標移到開頭
    # 讀取 local 的 key
    for i in local:
        now = timezone(local[i])  # 根據 key 的 value 取得時間
        print(f"{i}>{timezone(local[i])}  ", end="")
    time.sleep(1)
    # 倫敦>08:43:09  台灣>15:43:09  日本>16:43:09  紐約>03:43:09  洛杉磯>00:43:09  紐西蘭>19:43:09


print("------------------------------------------------------------")  # 60個

import datetime  # import datetime 標準函式

today = datetime.date.today()  # 使用 datetime.date 取得今天的日期
age = input("輸入生日 ( YYYY/MM/DD )：")  # 讓使用者輸入生日，格式為 YYYY/MM/DD
age_list = age.split("/")  # 將使用者輸入的日期，使用「/」拆成串列
year = today.year - int(age_list[0])  # 用今天的年份，減去使用者的生日年份 ( 年份差 )
month = today.month - int(age_list[1])  # 用今天的月份，減去使用者生日的月份 ( 月份差 )
if month < 0:  # 如果月份差的數字小於零，表示生日還沒到
    year = year - 1  # 將年份差減少 1 ( 表示跨了一年 )
    month = 12 + month  # 將月份差改成 12 + 月份差
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 建立一個每個月有多少天的串列
day = today.day - int(age_list[2])  # 用今天的日期，點去使用者生日的日期 ( 月份差 )
if day < 0:  # 如果月份差的數字小於 0，表示生日還沒到
    month = month - 1  # 將月份差減少 1
    if month < 0:  # 如果月份差減少後小於 0
        year = year - 1  # 再將年份差減少 1 ( 表示跨了一年 )
        month = 12 + month  # 將月份差改成 12 + 月份差
    day = day_list[month] + day  # 將日期差改成該月的天數 + 日期差

print(f"{year} 歲 {month} 個月 {day} 天")  # 印出現在幾歲幾個月又幾天


print("------------------------------------------------------------")  # 60個

import datetime

date = '20210311'
date = datetime.datetime.strptime(date, '%Y%m%d')
print(date.weekday())

print('------------------------------------------------------------')	#60個

import datetime

start_date_str = "20210125"
end_date_str = "20210201"

start_date = datetime.datetime.strptime(start_date_str, '%Y%m%d')
end_date = datetime.datetime.strptime(end_date_str, '%Y%m%d')

totaldays = (end_date - start_date).days + 1
dates = []
for daynumber in range(totaldays):
    date = (start_date + datetime.timedelta(days=daynumber))
    if date.weekday() < 6:
        dates.append(date.strftime('%Y%m%d'))
print(dates)
'''
print('------------------------------------------------------------')	#60個

print("cnlunardate：農曆日期")

# pip install cnlunardate
from cnlunardate import cnlunardate
from datetime import date

year = 2023  # @param {type:'slider', min:1950, max:2020}
month = 2  # @param {type:'slider', min:1, max:12}
try:
    cnlunardate(year, month, 1, True)
    print("農曆 {} 年 {} 月「是」閏月。".format(year, month))
except:
    print("農曆 {} 年 {} 月「不是」閏月。".format(year, month))

print(cnlunardate.fromsolardate(date(1974, 9, 24)))
print(cnlunardate.fromsolardate(date(2006, 3, 11)))
print(cnlunardate.fromsolardate(date(2023, 9, 20)))

print(cnlunardate(2017, 9, 1).tosolardate())
print(cnlunardate(2017, 6, 10, True).tosolardate())
print(cnlunardate(2017, 6, 10, False).tosolardate())

print(cnlunardate(2017, 6, 1, False).toordinal())

n1 = cnlunardate(2017, 6, 1, False).toordinal()
n2 = cnlunardate(2015, 10, 12, False).toordinal()
print(n1 - n2)

print("------------------------------------------------------------")  # 60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
