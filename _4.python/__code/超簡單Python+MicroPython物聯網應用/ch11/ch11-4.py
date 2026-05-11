import urequests, ujson
import xtools, utime

xtools.connect_wifi_led()

ADAFRUIT_AIO_USERNAME = "<USERNAME>"
ADAFRUIT_AIO_KEY = "<AIO KEY>"
FEED1 = "temperature"
API_key = "<API金鑰>"
city = "Taipei"
country = "TW"

def get_temperature():
    url  = "https://api.openweathermap.org/data/2.5/weather?"
    url += "q=" + city + "," + country   # 城市與國別
    url += "&units=metric&lang=zh_tw&"   # 單位
    url += "appid=" + API_key
    try:
        response = urequests.get(url)
        data = ujson.loads(response.text)
        main = data["main"]
        return main["temp"]
    except:
        return 0

while True:
    temp = get_temperature()
    print("儲存溫度資料: ", temp)
    url = "https://io.adafruit.com/api/v2/" + ADAFRUIT_AIO_USERNAME
    url+= "/feeds/"+ FEED1 + "/data?X-AIO-Key=" + ADAFRUIT_AIO_KEY
    print('url1=', url)
    data1 = {"value": temp}
    xtools.webhook_post(url, data1)
    utime.sleep(30) 
