import xtools, utime

xtools.connect_wifi_led()

WRITE_API_KEY = "<WRITE API金鑰>"

while True:
    temp = xtools.random_in_range(10, 35)
    hum = xtools.random_in_range(60, 90)
    print("儲存溫度和濕度資料: ", temp, hum)
    url = "http://api.thingspeak.com/update?"
    url += "api_key=" + WRITE_API_KEY
    url += "&field1=" + str(temp)
    url += "&field2=" + str(hum)
    print(url)
    xtools.webhook_get(url)
    utime.sleep(15) 
