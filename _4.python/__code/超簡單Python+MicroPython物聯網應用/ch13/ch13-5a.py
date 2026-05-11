from machine import Pin, Timer

def blink(t):
    led2.value(not led2.value())
    
led2 = Pin(2, Pin.OUT)
led2.value(0)
    
t = Timer(0)
t.init(period=1000, mode=Timer.PERIODIC, callback=blink)
