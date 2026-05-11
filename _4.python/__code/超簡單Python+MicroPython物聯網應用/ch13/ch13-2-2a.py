import xtools, utime
from machine import ADC, Pin, RTC
import ntptime

xtools.connect_wifi_led()
adc = ADC(Pin(27))
rtc = RTC()
ntptime.settime()

WEBHOOK_URL="https://hook.eu2.make.com/yzr1ofy1lbde...anf7es0d6bz"

while True:
    print("儲存距離資料!")
    utc = utime.mktime(utime.localtime())
    current=utime.localtime(utc+28800)
    distance = adc.read_u16()
    print(xtools.format_datetime(current), distance)
    xtools.webhook_get(WEBHOOK_URL + "?time=" +
                       xtools.format_datetime(current) +
                       "&value=" +str(distance))        
    utime.sleep(5)
