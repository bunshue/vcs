from machine import Pin 

led = Pin(25, Pin.OUT)  # Pico 內建LED是GPIO25, Pico W 是"LED"               
button = Pin(4, Pin.IN)
led.value(0)
while True:
    value = button.value()
    if value:
        print(value)
        led.value(0)     # 熄  
    else:
        print(value)
        led.value(1)     # 亮
        