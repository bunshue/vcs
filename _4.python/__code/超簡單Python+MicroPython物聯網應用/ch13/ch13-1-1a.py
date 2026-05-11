from machine import RTC

rtc = RTC()
rtc.datetime((2022,9,24,13,18,0,0,0))
print(rtc.datetime())
