import urequests as req
import network
import json

SSID = "自己的SSID"
PASSWORD = "自己的密碼"


def do_connect():
    sta = network.WLAN(network.STA_IF)  # Station
    if not sta.isconnected():
        print("正在連線中...")
        sta.active(True)  # 啟用 STA 模式
        sta.connect(SSID, PASSWORD)  # 連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print("連線成功!")


do_connect()  # Connect to network

host = "https://api.thingspeak.com"
api_key = "L2GT60TEPN8MGMOO"  # Read Key (光線感測器)
ChannelID = "923788"
records = 3  # 讀取最後 3 筆

apiURL = "%s/channels/%s/feeds.json?api_key=%s&results=%d" % (
    host,
    ChannelID,
    api_key,
    records,
)
print(apiURL)

r = req.get(apiURL)
if r.status_code == 200:
    print("最後 3 筆資料讀取成功!")
    print(r.text)

    jsondata = json.loads(r.text)
    data = jsondata["feeds"]
    print("\n", data)
else:
    print("資料讀取錯誤!")
