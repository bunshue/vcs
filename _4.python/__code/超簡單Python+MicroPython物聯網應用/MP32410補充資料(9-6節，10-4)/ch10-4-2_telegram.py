import xtools  
import urequests
from urlencode import urlencode

xtools.connect_wifi_led()

token = "<API權杖>"
chat_id = "<聊天室識別碼>"
message = "使用MicroPython送出Notification通知"

message = urlencode({"msg": message})[4:]
#url = "https://api.telegram.org/bot" + token 
#url += "/sendMessage?text=" + message
#url += "&chat_id=" + chat_id
url = "http://192.168.1.108:1880/telegram/" + chat_id
url += "/" + token + "/" + message
print(url)
           
urequests.get(url)
