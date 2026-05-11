from linenotify import LineNotify  
from machine import ADC
import xtools

xtools.connect_wifi_led()
adc = ADC(0)

token = "qpkAcFpPZZIU-----------------U9c6lolKW"
message = "取得光敏電阻值:"
light_value = adc.read()
print(message, light_value)

line = LineNotify(token)
line.notify(message + str(light_value))
