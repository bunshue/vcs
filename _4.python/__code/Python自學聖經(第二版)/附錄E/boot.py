# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc

import network
# 連線基地台
SSID='自已的SSID'
PASSWORD='自已的密碼'
def do_connect():
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
    #print(sta.ifconfig()) # 顯示網址、網路遮罩、閘道器和 DNS

#import webrepl
#webrepl.start()
gc.collect()
do_connect() #連線基地台