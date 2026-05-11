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

url = "https://www.googleapis.com/books/v1/volumes?maxResults=2&q=MicroPython&projection=lite"
r = urequests.get(url)
if r.status_code == 200:
    print("下載: ", len(r.text), "字元")
    info = ujson.loads(r.text)
    print("--------------------------")
    for item in info["items"]:
        book = item["volumeInfo"]        
        print("圖書名: " , book["title"])
        if "publisher" in book.keys():
            print("出版商: ", book["publisher"])
        print("出版日: ", book["publishedDate"])
        print("--------------------------")       
else:
    print("沒有圖書資料")
    