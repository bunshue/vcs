from machine import ADC, Pin
import utime, urequests, xtools
from machine import RTC
import ntptime

xtools.connect_wifi_led()
adc = ADC(0)
rtc = RTC()
ntptime.settime()

DB = "iot-distance-?????-default-rtdb"
URL = "https://"+DB+".firebaseio.com/Team-IOT/list.json"

while True:
    print("儲存距離資料!")
    utc = utime.mktime(utime.localtime())
    current=utime.localtime(utc+28800)
    distance = adc.read()
    data = {"datetime": xtools.format_datetime(current),
            "distance": distance}
    r = urequests.post(URL, json=data)
    print(r.text)    
    utime.sleep(5)
    