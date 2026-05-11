import network

ap = network.WLAN(network.AP_IF)
if not ap.active():
    print("WiFi基地台尚未啟用, 啟用中…")
    ap.active(True)

print("WiFi基地台已經啟用...")
