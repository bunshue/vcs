'''

python的日期當中分成
1. date(日期)
2. time(時間)
3. datetime(混合date跟time)
4. timedelta(計算歷時期間的型態)
5. timezone(處理時區資訊的型態)

'''

import datetime

#輸出當前的日期及時間

print(datetime.datetime.now())

print(datetime.datetime.today())

#而如果只想要輸出現在的日期的話則用
print(datetime.date.today())


#而如果要輸出此時準確的時間的話則

import time
print(time.localtime())

#而我們也可以一一拆解

tonow = datetime.datetime.now()
print(tonow.year)
print(tonow.month)
print(tonow.day)

#而我們也可以算今天是今年的第幾天

dts = '20201007'
dt = datetime.datetime.strptime(dts,"%Y%m%d")
another_dts = dts[:4]+"0101"
another_dt = datetime.datetime.strptime(another_dts,"%Y%m%d")
print(int((dt-another_dt).days)+1)


'''
由上可得知datetime.datetime.strptime()這個是將所輸入的dts轉換成日期的格式則格式為後面的年月日，再來取出輸入的西元年加上"0101"後一樣轉換成日期的格式最後將輸入日期減掉設定日期後+1輸出成今天為今年的第幾天
'''

loc_dt = datetime.datetime.today() 
time_del = datetime.timedelta(hours=3) 
new_dt = loc_dt + time_del 
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)


'''
由上可得知我們也可以調整時差，將我們現在的時間加上3小時的時差並將其輸出出來，一開始我們將抓出本地的時間並且將變數time_del宣告為時差差三個小時，最後將其相加就變成有時差三個小時最後將其指定格式後輸出，而以此類推我們也可以將時差晚三個小時
'''


loc_dt = datetime.datetime.today() 
time_del = datetime.timedelta(hours=3) 
new_dt = loc_dt - time_del 
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)











