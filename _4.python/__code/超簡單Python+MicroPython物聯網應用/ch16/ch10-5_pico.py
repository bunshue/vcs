import xtools
from machine import Pin
import utime, urequests, ujson

xtools.connect_wifi_led()
button = Pin(14, Pin.IN, Pin.PULL_UP)

API_key = "<API金鑰>"
token = "<存取權杖>"
city = "Taipei"
country = "TW"
url  = "https://api.openweathermap.org/data/2.5/weather?"
url += "q=" + city + "," + country   # 城市與國別
url += "&units=metric&lang=zh_tw&"   # 單位
url += "appid=" + API_key

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

print("請按下按鍵開關來送出LINE Notify通知訊息…")      
while True:
    if button.value() == 0:   # 值 0 是按下
        print("送出LINE Notify!")
        message = get_weather_description()
        xtools.line_msg(token, message)
        utime.sleep(10)    
