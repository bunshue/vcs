import xtools
import utime
from machine import Pin, ADC
import urequests

# 連接WiFi
xtools.connect_wifi_led()

# Adafruit IO 賬戶設定
ADAFRUIT_AIO_USERNAME = "hueyanchen2014"
ADAFRUIT_AIO_KEY = "aio_mHuM------------------4OkiJ4"
FEED = "distance"

# 設定光敏電阻接腳
adc = ADC(Pin(0))

while True:
    # 讀取光敏電阻值
    light_value = adc.read()
    print("光敏電阻值: ", light_value)
    
    # 構建 Adafruit IO 的 URL
    url = "https://io.adafruit.com/api/v2/" + ADAFRUIT_AIO_USERNAME
    url += "/feeds/" + FEED + "/data?X-AIO-Key=" + ADAFRUIT_AIO_KEY
    print('url=', url)
    
    # 上傳數據到 Adafruit IO
    data = {"value": light_value}
    response = urequests.post(url, json=data)
    response.close()
    
    # 等待 5 秒
    utime.sleep(5)
