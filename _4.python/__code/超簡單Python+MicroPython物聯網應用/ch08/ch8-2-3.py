import utime
from machine import Pin

led = Pin(2, Pin.OUT)
for i in range(10):
    led.value(0)
    utime.sleep(1)
    led.value(1)
    utime.sleep(1)
    