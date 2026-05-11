import xtools, utime
from machine import RTC
import ntptime

xtools.connect_wifi_led()

rtc = RTC()
ntptime.settime()
# UTC 加 8小時 = 台灣時間
utc = utime.mktime(utime.localtime())
year,month,day,hour,minute,second,week,days=utime.localtime(utc+28800)
print("年:", year)
print("月:", month)
print("日:", day)
print("時:", hour)
print("分:", minute)
print("秒:", second)
print(xtools.format_datetime(utime.localtime(utc+28800)))
