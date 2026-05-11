from machine import Pin
import utime 

leds = [15, 13, 12]

for i in range(10):
    for num in leds:
        led = Pin(num, Pin.OUT)
        led.value(1)
        utime.sleep(0.3)
        led.value(0)
    for num in reversed(leds):
        led = Pin(num, Pin.OUT)
        led.value(1)
        utime.sleep(0.3)
        led.value(0)
        