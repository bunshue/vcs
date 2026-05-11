import utime
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(0)
utime.sleep(5)
led.value(1)
