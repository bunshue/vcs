from linenotify import LineNotify  
from machine import ADC, Pin
import xtools

xtools.connect_wifi_led()
adc = ADC(Pin(27))

token = "<存取權杖>"
message = "取得距離資料:"
distance = adc.read_u16()
print(message, distance)

line = LineNotify(token)
line.notify(message + str(distance))
