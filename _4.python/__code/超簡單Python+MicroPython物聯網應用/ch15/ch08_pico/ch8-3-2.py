from machine import Pin 

button = Pin(4, Pin.IN, Pin.PULL_UP)
print(button.value())
