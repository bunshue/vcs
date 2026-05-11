import network
import ubinascii

mac = network.WLAN().config('mac')
print("MAC地址: ", mac)
mac=ubinascii.hexlify(mac).decode()
print("MAC地址: ", mac)
