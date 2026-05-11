from linenotify import LineNotify  
from machine import ADC
import xtools

xtools.connect_wifi_led()
adc = ADC(0)

token = "<存取權杖>"
message = "取得距離資料:"
distance = adc.read()
print(message, distance)

line = LineNotify(token)
line.notify(message + str(distance))
