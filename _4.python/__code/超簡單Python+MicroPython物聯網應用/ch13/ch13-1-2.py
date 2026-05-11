import xtools, utime
from machine import RTC
import ntptime

xtools.connect_wifi_led()

rtc = RTC()
ntptime.settime()
print(rtc.datetime())
print(utime.localtime())
