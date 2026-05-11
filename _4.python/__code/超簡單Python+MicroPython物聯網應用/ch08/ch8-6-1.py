from machine import Pin
import utime 

for i in range(10):
    led = Pin(15, Pin.OUT)
    led.value(1)
    utime.sleep(0.3)
    led.value(0)
    led = Pin(13, Pin.OUT)
    led.value(1)
    utime.sleep(0.3)
    led.value(0) 
    led = Pin(12, Pin.OUT)
    led.value(1)
    utime.sleep(0.3)
    led.value(0)
    