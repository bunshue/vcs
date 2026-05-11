from machine import Pin
import dht
import xtools, utime

xtools.connect_wifi_led()
sensor = dht.DHT11(Pin(22))

WRITE_API_KEY = "<WRITE API金鑰>"

while True:
    print("儲存溫度和濕度資料!")
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print(temp, hum)
    url = "http://api.thingspeak.com/update?"
    url += "api_key=" + WRITE_API_KEY
    url += "&field1=" + str(temp)
    url += "&field2=" + str(hum)
    print(url)
    xtools.webhook_get(url)
    utime.sleep(15)
