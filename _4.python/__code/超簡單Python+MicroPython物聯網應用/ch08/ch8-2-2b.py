import time
from machine import Pin

led = Pin(2, Pin.OUT)
led.value(0)
time.sleep(5)
led.value(1)
