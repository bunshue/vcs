from machine import ADC
import xtools  
import urequests
from urlencode import urlencode

xtools.connect_wifi_led()
adc = ADC(0)

token = "<API權杖>"
chat_id = "<聊天室識別碼>"
message = "取得距離資料:"
distance = adc.read()
print(message, distance)

message = urlencode({"msg": message})[4:]
url = "http://192.168.1.108:1880/telegram/" + chat_id
url += "/" + token + "/" + message + str(distance)
print(url)

urequests.get(url)
