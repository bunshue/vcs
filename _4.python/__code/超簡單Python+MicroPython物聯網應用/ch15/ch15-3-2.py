from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)
while True:
    if button.value() == 0:
        led.value(1)
        time.sleep(0.2)
    else:
        led.value(0)
