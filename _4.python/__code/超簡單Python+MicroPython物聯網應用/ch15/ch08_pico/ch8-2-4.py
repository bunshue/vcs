from machine import Pin 

led = Pin(25, Pin.OUT)  # Pico 內建LED是GPIO25, Pico W 是"LED"
led.value(1)
v = led.value()
print("狀態值", v)
led.value(0)
v = led.value()
print("狀態值", v)
