# 日期時間操作 

import time  # 導入 time 模組

time.time()#通常是用來作為時間戳記，可以傳回從 1970/1/1 00:00:00 算起至今的秒數

import time # 引入 time 模組

seconds = time.time()
print(seconds)


time.localtime() #可以輸出 struct_time 的時間格式

import time  # 引入 time 模組

localtime = time.localtime() # 取得當前時間
print(localtime)


import time  # 引入 time 模組

localtime = time.localtime() # 取得當前時間
print("年:", localtime.tm_year)
print("月:", localtime.tm_mon)
print("日:", localtime.tm_mday)
print("時:", localtime.tm_hour)
print("分:", localtime.tm_min)
print("秒:", localtime.tm_sec)
print("星期(0為星期一):", localtime.tm_wday)
print("今天為今年第幾天:", localtime.tm_yday)
print("夏令時間(0為不是，1為是):", localtime.tm_isdst)


#strftime() 可以將時間格式化


import time

# 格式化為 2020-09-26 21:14:30
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化為Sat Sep 26 21:14:30 2020
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))


