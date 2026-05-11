import utime 
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(1)
while True:
    v = not led.value()
    print("狀態值", v)
    led.value(v)
    utime.sleep(1)
