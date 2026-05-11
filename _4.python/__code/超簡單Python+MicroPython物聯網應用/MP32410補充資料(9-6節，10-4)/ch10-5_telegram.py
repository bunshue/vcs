import xtools
from machine import Pin
import utime, urequests, ujson
from urlencode import urlencode

xtools.connect_wifi_led()
button = Pin(4, Pin.IN, Pin.PULL_UP)
API_key = "<API金鑰>"
city = "Taipei"
country = "TW"
#url  = "https://api.openweathermap.org/data/2.5/weather?"
#url += "q=" + city + "," + country   # 城市與國別
#url += "&units=metric&lang=zh_tw&"   # 單位
#url += "appid=" + API_key
url = "http://192.168.1.108:1880/weather/" + city
url += "/" + country + "/" + API_key

def get_weather_description():
    try:
        response = urequests.get(url)
        data = ujson.loads(response.text); 
    except:
        data = None
    if not data:
        return "沒有查詢到天氣資料"
    else:    
        weather = data["weather"][0]
        return weather["description"]

token = "<API權杖>"
chat_id = "<聊天室識別碼>"
print("請按下按鍵開關來送出Telegram Notification通知訊息…")      
while True:
    if button.value() == 0:   # 值 0 是按下
        print("送出Telegram Notification!")
        message = get_weather_description()
        message = urlencode({"msg": message})[4:]
        url2 = "http://192.168.1.108:1880/telegram/" + chat_id
        url2 += "/" + token + "/" + message
        urequests.get(url2)
        utime.sleep(10)    
