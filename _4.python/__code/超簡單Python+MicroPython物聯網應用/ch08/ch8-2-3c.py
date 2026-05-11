import utime 
from machine import Pin

led = Pin(2, Pin.OUT)
while True:
    led.off()
    utime.sleep(1)
    led.on()
    utime.sleep(1)
    