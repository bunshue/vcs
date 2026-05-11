import utime 
from machine import Pin

led = Pin(25, Pin.OUT)  # Pico 內建LED是GPIO25, Pico W 是"LED"
while True:
    led.on()
    utime.sleep(1)
    led.off()
    utime.sleep(1)
    