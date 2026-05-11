from machine import Pin
import utime 

pin15 = Pin(15, Pin.OUT)
pin13 = Pin(13, Pin.OUT)
pin12 = Pin(12, Pin.OUT)
leds = [pin15, pin13, pin12]

for i in range(10):
    for led in leds:
        led.value(1)
        utime.sleep(0.3)
        led.value(0)        
        