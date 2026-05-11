from xtools import connect_wifi_led, webhook_get
from utime import sleep
from machine import ADC

# 連接WiFi
connect_wifi_led()

# ThingSpeak的WRITE API金鑰
WRITE_API_KEY = "RDLW---------PT75Y"

# 設定光敏電阻的ADC引腳（假設是A0）
adc = ADC(0)

while True:
    # 讀取光敏電阻值
    light_level = adc.read()
    print("光敏電阻值: ", light_level)
    
    # 建立ThingSpeak的URL
    url = "http://api.thingspeak.com/update?"
    url += "api_key=" + WRITE_API_KEY
    url += "&field1=" + str(light_level)
    print(url)
    
    # 發送HTTP請求
    webhook_get(url)
    
    # 等待15秒
    sleep(15)
