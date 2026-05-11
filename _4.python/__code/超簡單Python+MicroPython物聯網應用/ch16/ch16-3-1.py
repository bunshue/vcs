from machine import Pin
import utime
import dht 

sensor = dht.DHT11(Pin(22))

while True:
    try:
        utime.sleep(2)
        sensor.measure()
        print("溫度: ", sensor.temperature())
        print("溼度: ", sensor.humidity())
        print("------------")
    except OSError as e:
        print("DHT11溫溼度感測器讀取錯誤...")