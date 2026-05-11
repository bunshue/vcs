import network

sta = network.WLAN(network.STA_IF)
sta.active(True)
if not sta.isconnected():
    print("Connecting to network...")
    sta.connect('<WiFi名稱>', '<WiFi密碼>')
    while not sta.isconnected():
        pass

print("network config:", sta.ifconfig())
sta.disconnect()
print(sta.isconnected())
