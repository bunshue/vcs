import utime 
from machine import Pin

led = Pin(25, Pin.OUT)  # Pico 內建LED是GPIO25, Pico W 是"LED"
while True:
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)
    