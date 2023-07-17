import network

SSID='自己的SSID'
PASSWORD='自己的密碼'
sta = network.WLAN(network.STA_IF)

if not sta.isconnected():
    print('正在連線中...')
    sta.active(True) #啟用 STA 模式
    sta.connect(SSID, PASSWORD) #連線基地台
    # 等侯連線
    while not sta.isconnected():
        pass
print('連線成功!')
print(sta.ifconfig()) # 顯示網址、網路遮罩、閘道器和 DNS