from machine import Pin 

led = Pin(2, Pin.OUT)
led.value(0)
v = led.value()
print("狀態值", v)
led.value(1)
v = led.value()
print("狀態值", v)
