import network
import ubinascii

sta = network.WLAN(network.STA_IF)
sta.active(True)
print(sta.isconnected())
aps = sta.scan()
for ap in aps:
    ssid = ap[0].decode()
    mac = ubinascii.hexlify(ap[1], ":").decode()
    print(ssid, mac)
    