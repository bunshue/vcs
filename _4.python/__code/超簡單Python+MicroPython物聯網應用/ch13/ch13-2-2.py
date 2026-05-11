import xtools, utime
from machine import ADC, Pin, RTC
import ntptime

xtools.connect_wifi_led()
adc = ADC(0)
rtc = RTC()
ntptime.settime()

# http://192.168.1.102:1880/make/hook.eu2.make.com/yzr1ofy1lb---bnauk19sanf7es0d6bz/time,2024-05-15_12:30:30,value,161
WEBHOOK_URL = "http://192.168.1.102:1880/make"
MAKE_DOMAIN="hook.eu2.make.com"
TOKEN ="yzr1ofy1lb---bnauk19sanf7es0d6bz"

while True:
    print("儲存距離資料!")
    utc = utime.mktime(utime.localtime())
    current=utime.localtime(utc+28800)
    distance = adc.read()
    dt = xtools.format_datetime(current).replace(' ', '_')
    print(dt , distance)
    data = "time,"+dt+",value,"+str(distance)
    url = WEBHOOK_URL + "/" + MAKE_DOMAIN + "/" + TOKEN + "/" + data
    print(url)
    xtools.webhook_get(url)
    utime.sleep(5)
    