import utime
from machine import Pin 

button = Pin(4, Pin.IN)
while True:
    print(button.value())
    utime.sleep(0.5)
        