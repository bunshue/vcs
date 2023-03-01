import time
import datetime

# 獲取此時的時間
print(time.localtime())

# 獲取當天的日期
print(datetime.datetime.now())
print(datetime.date.today())

# 獲取昨天的日期
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    #print(type(today))  # 檢視獲取到時間的型別
    #print(type(yesterday))
    return yesterday
yesterday = getYesterday()
print("昨天的時間：", yesterday)

# 字串轉換為時間
def strTodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)
print(time.strftime("%Y-%m-%d", time.localtime()))
print(strTodatetime("2014-3-1","%Y-%m-%d"))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(strTodatetime("2019-4-15","%Y-%m-%d")-strTodatetime("2006-03-11","%Y-%m-%d"))


#兩日期相減 
d1 = datetime.datetime(2005, 2, 16) 
d2 = datetime.datetime(2004, 12, 31) 
print((d1 - d2).days)
#執行時間： 
starttime = datetime.datetime.now() 
endtime = datetime.datetime.now() 
print((endtime - starttime).seconds)
#計算當前時間向後10天的時間。 
# 如果是小時 days 換成 hours 
d1 = datetime.datetime.now() 
d3 = d1 - datetime.timedelta(days =10) 
print(str(d3) )
print(d3.ctime())
#print(time.ctime([sec]))#把秒數轉換成日期格式，如果不帶引數，則顯示當前的時間。
#time.ctime([ sec ])
print("time.ctime() : %s" % time.ctime())


ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)


