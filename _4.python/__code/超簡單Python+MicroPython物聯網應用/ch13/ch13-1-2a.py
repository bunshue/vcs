import xtools, utime
from machine import RTC
import ntptime

xtools.connect_wifi_led()

rtc = RTC()
ntptime.settime()
utc = utime.localtime()
print(utc)   # 目前的 UTC 時間
# UTC 加 8小時 = 台灣時間
local_time = utime.localtime(utime.mktime(utc)+28800)
print(local_time)
