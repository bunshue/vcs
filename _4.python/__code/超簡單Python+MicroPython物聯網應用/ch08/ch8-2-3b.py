import utime 
from machine import Pin

led = Pin(2, Pin.OUT)
while True:
    led.value(0)
    utime.sleep(1)
    led.value(1)
    #utime.sleep(1)
    