from machine import Pin,Timer
import time 

led = Pin(2, Pin.OUT) # DPIO2(D4)內建Led

def show(t):
    toggle=not led.value()    
    led.value(toggle)   #燈閃爍           

timer = Timer(1)
timer.init(period=500, mode=Timer.PERIODIC, callback=show)

try:
    while True:
        for n in range(100):
            print(n)
            time.sleep(0.1)
except:
    timer.deinit()
    print('stopped')