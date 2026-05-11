from machine import Pin 

led = Pin(2, Pin.OUT)               
button = Pin(4, Pin.IN)
led.value(1)
while True:
    value = button.value()
    if value:
        print(value)
        led.value(1)     # 熄  
    else:
        print(value)
        led.value(0)     # 亮
        