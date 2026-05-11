import network

def connect_wifi(ssid, passwd):
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    if not sta.isconnected():
       print("Connecting to network...")
       sta.connect(ssid, passwd)
       while not sta.isconnected():
          pass
    print("network config:", sta.ifconfig())

SSID = "<WiFi名稱>"        # WiFi名稱
PASSWORD = "<WiFi密碼>"    # WiFi密碼
connect_wifi(SSID, PASSWORD)

import urequests, ujson

r = urequests.get("https://fchart.github.io/books.json")
if r.status_code == 200:
    j = ujson.loads(r.text)
    for book in j:
        print(book["title"])
        print(book["author"])
        print(book["id"])
             
        
        