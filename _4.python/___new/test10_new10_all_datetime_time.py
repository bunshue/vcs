"""
相關抽出

datetime
time
calendar


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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


"""
localtime()返回元組的日期與時間資料結構 用索引方式獲得個別內容
索引	名稱	說明
0	tm_year	年 	2020
1	tm_mon	月 	1-12
2	tm_mday 日	1-31
3	tm_hour	時	0-23
4	tm_min	分	0-59
5	tm_sec	秒	0-59
6	tm_wday	星期	0:一, 1:二...
7	tm_yday	年第幾天
8	tm_isdst 夏令時間 0:不是, 1:是
"""

xtime = time.localtime()            #使用localtime()方法列出目前時間的結構
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("年 ", xtime.tm_year)         # 物件設定方式顯示
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print('range(5)', range(5))
print('list(range(5))', list(range(5)))

# range
tStart = time.time()
for i in range(10000000):
    pass
tEnd = time.time()
print('range time:', tEnd - tStart)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
