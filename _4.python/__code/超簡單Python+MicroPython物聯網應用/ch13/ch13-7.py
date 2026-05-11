import xtools, utime
from machine import ADC, Timer

xtools.connect_wifi_led()
adc = ADC(0)

API_KEY = "<API金鑰>"
EVENT_NAME = "distance"
WEBHOOK_URL="https://maker.ifttt.com/trigger/" + EVENT_NAME
WEBHOOK_URL+="/with/key/" + API_KEY + "/?value1="

def add_row(t):
    global adc, WEBHOOK_URL
    print("儲存距離資料!")
    distance = adc.read()
    xtools.webhook_get(WEBHOOK_URL + str(distance))   
    
t = Timer(0)
t.init(period=5000, mode=Timer.PERIODIC, callback=add_row)
